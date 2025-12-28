import React, { useCallback } from 'react';
import { useDropzone } from 'react-dropzone';
import './ImageUploader.css';

const ImageUploader = ({ image, setImage, label }) => {
  const onDrop = useCallback((acceptedFiles) => {
    if (acceptedFiles && acceptedFiles[0]) {
      setImage(acceptedFiles[0]);
    }
  }, [setImage]);

  const { getRootProps, getInputProps, isDragActive } = useDropzone({
    onDrop,
    accept: {
      'image/*': ['.png', '.jpg', '.jpeg', '.webp']
    },
    maxFiles: 1,
    maxSize: 10 * 1024 * 1024, // 10MB
  });

  const imagePreview = image ? URL.createObjectURL(image) : null;

  return (
    <div className="image-uploader">
      <div
        {...getRootProps()}
        className={`dropzone ${isDragActive ? 'active' : ''} ${imagePreview ? 'has-image' : ''}`}
      >
        <input {...getInputProps()} />
        {imagePreview ? (
          <div className="image-preview">
            <img src={imagePreview} alt="Preview" />
            <div className="image-overlay">
              <p>Click to change</p>
            </div>
          </div>
        ) : (
          <div className="dropzone-content">
            <div className="upload-icon">📤</div>
            <p className="dropzone-text">
              {isDragActive ? 'Drop image here' : label || 'Click or drag image here'}
            </p>
            <p className="dropzone-hint">PNG, JPG, JPEG, WEBP (max 10MB)</p>
          </div>
        )}
      </div>
      {image && (
        <div className="image-info">
          <span>{image.name}</span>
          <button
            className="remove-button"
            onClick={(e) => {
              e.stopPropagation();
              setImage(null);
            }}
          >
            ✕
          </button>
        </div>
      )}
    </div>
  );
};

export default ImageUploader;

