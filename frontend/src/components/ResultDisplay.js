import React from 'react';
import './ResultDisplay.css';

const ResultDisplay = ({ resultImage, loading }) => {
  if (!resultImage && !loading) {
    return null;
  }

  return (
    <div className="result-display">
      <h2> Stylized Result</h2>
      <div className="result-container">
        {loading ? (
          <div className="loading-spinner">
            <div className="spinner"></div>
            <p>Applying artistic style... This may take a moment</p>
          </div>
        ) : (
          <div className="result-image-wrapper">
            <img src={resultImage} alt="Stylized result" />
            <div className="download-overlay">
              <a
                href={resultImage}
                download="stylized-image.png"
                className="download-button"
              >
                 Download
              </a>
            </div>
          </div>
        )}
      </div>
    </div>
  );
};

export default ResultDisplay;

