/**
 * Neural Style Transfer - Main Application Component
 * 
 * This is the main React component for the Neural Style Transfer web application.
 * It provides a user interface for uploading content and style images, processing
 * them through the backend API, and displaying the stylized results.
 * 
 * @author Anurag
 * @date 2025
 */

import React, { useState } from 'react';
import './App.css';
import ImageUploader from './components/ImageUploader';
import ResultDisplay from './components/ResultDisplay';
import axios from 'axios';

/**
 * Main App Component
 * 
 * Manages the application state and handles style transfer operations.
 */
function App() {
  // State management for images and processing
  const [contentImage, setContentImage] = useState(null);
  const [styleImage, setStyleImage] = useState(null);
  const [resultImage, setResultImage] = useState(null);
  const [loading, setLoading] = useState(false);
  const [processingTime, setProcessingTime] = useState(null);
  const [error, setError] = useState(null);

  // API URL - uses environment variable or defaults to localhost
  const API_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000';

  /**
   * Handle style transfer request
   * 
   * Sends both content and style images to the backend API for processing
   * and updates the UI with the results.
   */
  const handleTransfer = async () => {
    // Validate that both images are selected
    if (!contentImage || !styleImage) {
      setError('Please upload both content and style images');
      return;
    }

    // Reset previous results and set loading state
    setLoading(true);
    setError(null);
    setResultImage(null);

    try {
      // Create form data for multipart file upload
      const formData = new FormData();
      formData.append('content_image', contentImage);
      formData.append('style_image', styleImage);

      // Send POST request to backend API
      const response = await axios.post(`${API_URL}/api/transfer`, formData, {
        headers: {
          'Content-Type': 'multipart/form-data',
        },
        timeout: 120000, // 2 minutes timeout for processing
      });

      // Handle successful response
      if (response.data.success) {
        setResultImage(response.data.result_image);
        setProcessingTime(response.data.processing_time);
      }
    } catch (err) {
      console.error('Error:', err);
      // Extract error message from response or use default
      setError(
        err.response?.data?.error || 
        'Failed to process images. Please try again.'
      );
    } finally {
      // Always clear loading state
      setLoading(false);
    }
  };

  /**
   * Reset all state to initial values
   * 
   * Clears all uploaded images, results, and errors.
   */
  const handleReset = () => {
    setContentImage(null);
    setStyleImage(null);
    setResultImage(null);
    setError(null);
    setProcessingTime(null);
  };

  return (
    <div className="App">
      <div className="container">
        {/* Application Header */}
        <header className="header">
          <h1> Neural Style Transfer</h1>
          <p className="subtitle">Transform your images with AI-powered artistic styles</p>
        </header>

        {/* Main Content Area */}
        <div className="main-content">
          {/* Image Upload Section */}
          <div className="upload-section">
            <div className="upload-column">
              <h2>Content Image</h2>
              <ImageUploader
                image={contentImage}
                setImage={setContentImage}
                label="Upload content image"
              />
            </div>

            <div className="upload-column">
              <h2>Style Image</h2>
              <ImageUploader
                image={styleImage}
                setImage={setStyleImage}
                label="Upload style image"
              />
            </div>
          </div>

          {/* Action Buttons */}
          <div className="action-section">
            <button
              className="transfer-button"
              onClick={handleTransfer}
              disabled={loading || !contentImage || !styleImage}
            >
              {loading ? ' Processing...' : ' Transfer Style'}
            </button>
            {(contentImage || styleImage || resultImage) && (
              <button className="reset-button" onClick={handleReset}>
                Reset
              </button>
            )}
          </div>

          {/* Error Message Display */}
          {error && (
            <div className="error-message">
              <span>⚠️ {error}</span>
            </div>
          )}

          {/* Processing Time Display */}
          {processingTime && (
            <div className="processing-info">
              Processed in {processingTime}s
            </div>
          )}

          {/* Result Display Component */}
          <ResultDisplay resultImage={resultImage} loading={loading} />
        </div>

        {/* Footer */}
        <footer className="footer">
          <p>Powered by TensorFlow & React</p>
        </footer>
      </div>
    </div>
  );
}

export default App;
