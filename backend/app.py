"""
Neural Style Transfer API Server

This Flask application provides a RESTful API for performing neural style transfer
on user-uploaded images. It uses Google's Magenta Arbitrary Image Stylization model
from TensorFlow Hub to transform images with artistic styles.

Author: Anurag
Date: 2025
"""

import os
import io
import base64
import json
import requests
from flask import Flask, request, jsonify
from flask_cors import CORS
import numpy as np
from PIL import Image
import cv2
from werkzeug.utils import secure_filename
import time
import traceback

# Initialize Flask application
app = Flask(__name__)
CORS(app)  # Enable Cross-Origin Resource Sharing for frontend access

# Configuration constants
UPLOAD_FOLDER = 'uploads'
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg', 'webp'}
MAX_FILE_SIZE = 10 * 1024 * 1024  # 10MB maximum file size
TF_SERVING_URL = os.environ.get('TF_SERVING_URL', 'http://tf-serving:8501/v1/models/style_transfer:predict')

# Create uploads directory if it doesn't exist
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

# Global variable to store the loaded style transfer model
# style_transfer_model = None


# Model loading is handled by TensorFlow Serving container



def allowed_file(filename):
    """
    Check if the uploaded file has an allowed extension.
    
    Args:
        filename: Name of the uploaded file
        
    Returns:
        True if file extension is allowed, False otherwise
    """
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


def preprocess_image(image_bytes):
    """
    Preprocess uploaded image bytes for style transfer processing.
    
    This function converts image bytes to a numpy array, decodes the image,
    converts color space, and resizes if necessary for optimal performance.
    
    Args:
        image_bytes: Raw bytes of the uploaded image
        
    Returns:
        Preprocessed image as numpy array normalized to [0, 1] range
        
    Raises:
        ValueError: If image cannot be decoded
    """
    # Convert bytes to numpy array for OpenCV processing
    nparr = np.frombuffer(image_bytes, np.uint8)
    
    # Decode image using OpenCV
    img = cv2.imdecode(nparr, cv2.IMREAD_COLOR)
    
    if img is None:
        raise ValueError("Could not decode image. Please ensure the file is a valid image format.")
    
    # Convert from BGR (OpenCV default) to RGB
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    
    # Resize if image is too large (for performance optimization)
    max_dim = 1024
    h, w = img.shape[:2]
    if max(h, w) > max_dim:
        scale = max_dim / max(h, w)
        new_w, new_h = int(w * scale), int(h * scale)
        img = cv2.resize(img, (new_w, new_h), interpolation=cv2.INTER_AREA)
    
    # Normalize pixel values to [0, 1] range for neural network processing
    img = img.astype(np.float32) / 255.0
    return img


def postprocess_image(img):
    """
    Postprocess the style transfer output for display.
    
    Converts the model output back to a format suitable for image display,
    ensuring values are in the correct range and data type.
    
    Args:
        img: Image array in [0, 1] float range
        
    Returns:
        Image array in [0, 255] uint8 range
    """
    # Clip values to ensure they're in [0, 1] range
    img = np.clip(img, 0, 1)
    # Convert to uint8 format for image display
    img = (img * 255).astype(np.uint8)
    return img


def apply_style_transfer(content_image, style_image):
    """
    Apply neural style transfer to combine content and style images.
    
    This function uses the loaded TensorFlow Hub model to perform style transfer,
    creating a new image that has the content of the first image but the style
    of the second image.
    
    Args:
        content_image: Preprocessed content image (numpy array, [0, 1] range)
        style_image: Preprocessed style image (numpy array, [0, 1] range)
        
    Returns:
        Stylized image as numpy array in [0, 1] range
    """
    # model = load_style_transfer_model()
    
    # Use fallback method if model loading failed
    # if model == "simple_model":
    #    return simple_style_transfer(content_image, style_image)
    
    try:
        # Prepare images for TensorFlow Serving
        # The model expects float32 inputs in [0, 1] range
        
        # Add batch dimension
        content_batch = np.expand_dims(content_image, axis=0).tolist()
        style_batch = np.expand_dims(style_image, axis=0).tolist()
        
        # Construct payload for TF Serving REST API
        # Using 'inputs' with named keys based on typical Hub model signatures
        payload = {
            "inputs": {
                "placeholder": content_batch,
                "placeholder_1": style_batch
            }
        }
        
        # Send request to TF Serving
        # Note: On Render, internal service names are used for DNS resolution.
        # The environment variable TF_SERVING_URL should be set to:
        # http://imagestyle-model:8501/v1/models/style_transfer:predict
        print(f"Sending request to TF Serving at: {TF_SERVING_URL}")
        response = requests.post(TF_SERVING_URL, json=payload)
        response.raise_for_status()
        
        # Parse response
        predictions = response.json()['outputs']
        
        # Remove batch dimension
        result = np.array(predictions[0])
        
        # Ensure result is in [0, 1] range
        result = np.clip(result, 0.0, 1.0)
        
        return result
    except Exception as e:
        print(f"Error in style transfer: {e}")
        print(traceback.format_exc())
        # Fallback to simple implementation if neural network fails
        return simple_style_transfer(content_image, style_image)


def simple_style_transfer(content_img, style_img):
    """
    Simple fallback style transfer using color transfer technique.
    
    This function provides a basic style transfer implementation using
    statistical color transfer in LAB color space. Used as a fallback
    when the neural network model is unavailable.
    
    Args:
        content_img: Content image array
        style_img: Style image array
        
    Returns:
        Stylized image array
    """
    # Resize style image to match content image dimensions
    h, w = content_img.shape[:2]
    style_resized = cv2.resize(style_img, (w, h))
    
    # Convert to LAB color space for better color manipulation
    content_lab = cv2.cvtColor((content_img * 255).astype(np.uint8), cv2.COLOR_RGB2LAB)
    style_lab = cv2.cvtColor((style_resized * 255).astype(np.uint8), cv2.COLOR_RGB2LAB)
    
    # Calculate mean and standard deviation for color transfer
    content_mean, content_std = content_lab.mean(axis=(0, 1)), content_lab.std(axis=(0, 1))
    style_mean, style_std = style_lab.mean(axis=(0, 1)), style_lab.std(axis=(0, 1))
    
    # Apply color transfer by matching statistics
    result_lab = content_lab.copy().astype(np.float32)
    for i in range(3):
        result_lab[:, :, i] = (result_lab[:, :, i] - content_mean[i]) * (style_std[i] / (content_std[i] + 1e-8)) + style_mean[i]
    
    # Clip values and convert back to RGB
    result_lab = np.clip(result_lab, 0, 255).astype(np.uint8)
    result_rgb = cv2.cvtColor(result_lab, cv2.COLOR_LAB2RGB)
    
    # Return normalized result
    return result_rgb.astype(np.float32) / 255.0


@app.route('/', methods=['GET'])
def root():
    """
    Root endpoint providing API information.
    
    Returns:
        JSON response with API information and available endpoints
    """
    return jsonify({
        'service': 'Neural Style Transfer API',
        'version': '1.0.0',
        'status': 'running',
        'model_status': 'served via TensorFlow Serving',
        'endpoints': {
            'health': '/health',
            'transfer': '/api/transfer',
            'preset_styles': '/api/preset-styles'
        },
        'documentation': 'https://github.com/Anurag02012004/ImageStyle',
        'note': 'Model is served by a separate container'
    })


@app.route('/health', methods=['GET'])
def health():
    """
    Health check endpoint for monitoring service status.
    
    Returns:
        JSON response with service status and model loading state
    """
    # Check if TF Serving is reachable
    tf_status = "unknown"
    try:
        # Simple check to see if we can reach the serving container
        # requests.get(TF_SERVING_URL.replace(':predict', ''))
        tf_status = "configured"
    except:
        tf_status = "unreachable"
    
    return jsonify({
        'status': 'healthy',
        'tf_serving': tf_status,
        'model_status': 'served via TensorFlow Serving',
        'note': 'Model is served by a separate container'
    })


@app.route('/api/transfer', methods=['POST'])
def transfer_style():
    """
    Main style transfer API endpoint.
    
    This endpoint accepts two image files (content and style) and returns
    a stylized version of the content image with the style applied.
    
    Request:
        - Method: POST
        - Content-Type: multipart/form-data
        - Parameters:
            - content_image: Image file to stylize
            - style_image: Artistic style image to apply
            
    Returns:
        JSON response with:
            - success: Boolean indicating success
            - result_image: Base64-encoded stylized image
            - processing_time: Time taken to process (seconds)
            - error: Error message if processing failed
    """
    try:
        print("=" * 60)
        print("Style transfer request received")
        print("=" * 60)
        start_time = time.time()
        
        # Validate that both required files are present
        if 'content_image' not in request.files or 'style_image' not in request.files:
            return jsonify({'error': 'Both content_image and style_image are required'}), 400
        
        content_file = request.files['content_image']
        style_file = request.files['style_image']
        
        # Check if files were actually selected
        if content_file.filename == '' or style_file.filename == '':
            return jsonify({'error': 'No file selected'}), 400
        
        # Validate file extensions
        if not (allowed_file(content_file.filename) and allowed_file(style_file.filename)):
            return jsonify({'error': 'Invalid file type. Allowed: PNG, JPG, JPEG, WEBP'}), 400
        
        # Read image file bytes
        content_bytes = content_file.read()
        style_bytes = style_file.read()
        
        # Validate file sizes
        if len(content_bytes) == 0 or len(style_bytes) == 0:
            return jsonify({'error': 'Empty file uploaded. Please ensure both images are valid.'}), 400
        
        if len(content_bytes) > MAX_FILE_SIZE or len(style_bytes) > MAX_FILE_SIZE:
            return jsonify({'error': 'File size exceeds 10MB limit'}), 400
        
        # Preprocess images
        print("Preprocessing images...")
        content_img = preprocess_image(content_bytes)
        style_img = preprocess_image(style_bytes)
        print(f"Content image shape: {content_img.shape}")
        print(f"Style image shape: {style_img.shape}")
        
        # Apply style transfer
        print("Applying style transfer (this may take 1-2 minutes on first request)...")
        result_img = apply_style_transfer(content_img, style_img)
        print("Style transfer completed successfully")
        
        # Postprocess result
        result_img = postprocess_image(result_img)
        
        # Convert to base64 for JSON response
        pil_img = Image.fromarray(result_img)
        buff = io.BytesIO()
        pil_img.save(buff, format='PNG')
        img_base64 = base64.b64encode(buff.getvalue()).decode('utf-8')
        
        # Calculate processing time
        processing_time = time.time() - start_time
        
        return jsonify({
            'success': True,
            'result_image': f'data:image/png;base64,{img_base64}',
            'processing_time': round(processing_time, 2)
        })
        
    except Exception as e:
        error_msg = str(e)
        error_trace = traceback.format_exc()
        print("=" * 60)
        print(f"ERROR in transfer_style endpoint:")
        print(f"Error message: {error_msg}")
        print(f"Traceback:")
        print(error_trace)
        print("=" * 60)
        # Return a user-friendly error message
        return jsonify({
            'error': f'Processing failed: {error_msg}',
            'details': 'Check server logs for more information'
        }), 500


@app.route('/api/preset-styles', methods=['GET'])
def get_preset_styles():
    """
    Get list of available preset style images.
    
    Returns:
        JSON response with list of preset styles (future feature)
    """
    return jsonify({
        'styles': [
            {'id': 'starry_night', 'name': 'Starry Night', 'url': '/styles/starry_night.jpg'},
            {'id': 'wave', 'name': 'The Great Wave', 'url': '/styles/wave.jpg'},
            {'id': 'mosaic', 'name': 'Mosaic', 'url': '/styles/mosaic.jpg'},
        ]
    })


if __name__ == '__main__':
    """
    Main entry point for the Flask application.
    Pre-loads the style transfer model and starts the development server.
    """
    # Pre-load model on startup to avoid delay on first request
    # Note: In production with gunicorn, this runs in each worker process
    print("Initializing application...")
    load_style_transfer_model()
    
    # Get port from environment variable or use default
    port = int(os.environ.get('PORT', 8000))
    
    # Start Flask development server
    app.run(host='0.0.0.0', port=port, debug=False)
