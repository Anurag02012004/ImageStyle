import os
import json
import logging
from flask import Flask, request, jsonify

app = Flask(__name__)

# Configure logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

@app.route('/v1/models/style_transfer', methods=['GET'])
def health_check():
    """
    Mimic TF Serving Status/Health endpoint
    """
    return jsonify({
        "model_version_status": [
            {
                "version": "1",
                "state": "AVAILABLE",
                "status": {
                    "error_code": "OK",
                    "error_message": ""
                }
            }
        ]
    })

@app.route('/v1/models/style_transfer:predict', methods=['POST'])
def predict():
    """
    Mimic TF Serving Prediction endpoint.
    Simply returns the content image (placeholder) as the output.
    """
    try:
        data = request.get_json()
        
        # Extract the content image from the input
        # Structure is {"inputs": {"placeholder": [...], "placeholder_1": [...]}}
        if 'inputs' in data and 'placeholder' in data['inputs']:
            content_image = data['inputs']['placeholder']
            logger.info("Received prediction request. Returning content image as style transfer result.")
            
            # Return it in the format TF Serving would: {"outputs": [...]}
            return jsonify({
                "outputs": content_image
            })
        else:
            logger.warning("Invalid input format")
            return jsonify({"error": "Invalid input format"}), 400
            
    except Exception as e:
        logger.error(f"Error in mock prediction: {e}")
        return jsonify({"error": str(e)}), 500

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 8501))
    logger.info(f"Starting Mock Model Server on port {port}")
    app.run(host='0.0.0.0', port=port)
