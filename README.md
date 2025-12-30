#  Neural Style Transfer Web Application

A sophisticated, production-ready web application that transforms ordinary photographs into stunning artistic masterpieces using advanced neural style transfer technology. Built with cutting-edge machine learning models and modern web technologies.

##  Features

- ** Real-Time Style Transfer**: Transform images with artistic styles using state-of-the-art neural networks
- ** Drag & Drop Interface**: Intuitive image upload with instant preview
- ** High Performance**: Optimized processing with automatic image resizing
- ** Multiple Formats**: Support for PNG, JPG, JPEG, and WEBP formats
- ** Fast Processing**: Efficient TensorFlow model execution
- ** Docker Ready**: Complete containerization for easy deployment
- ** Responsive Design**: Beautiful, modern UI that works on all devices

## Technology Stack

### Backend
- **Python 3.11+**: Core backend language
- **Flask**: Lightweight, powerful web framework
- **TensorFlow 2.20**: Deep learning framework
- **TensorFlow Hub**: Pre-trained model repository
- **OpenCV**: Advanced image processing
- **Pillow**: Image manipulation and conversion
- **Gunicorn**: Production WSGI server

### Frontend
- **React 18**: Modern, component-based UI library
- **Axios**: HTTP client for API communication
- **React Dropzone**: Drag-and-drop file upload
- **CSS3**: Modern styling with gradients and animations

### Deployment
- **Docker**: Containerization
- **Docker Compose**: Multi-container orchestration
- **Nginx**: Production web server (frontend)

##  Quick Start

### Prerequisites

- Python 3.11 or higher
- Node.js 16 or higher
- npm or yarn
- Docker (optional, for containerized deployment)

### Local Development Setup

#### 1. Clone the Repository

```bash
git clone https://github.com/Anurag02012004/ImageStyle.git
cd ImageStyle
```

#### 2. Backend Setup

```bash
# Navigate to backend directory
cd backend

# Create virtual environment
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Run the server
python app.py
```

The backend will start on `http://localhost:8000`

#### 3. Frontend Setup

```bash
# Navigate to frontend directory (from project root)
cd frontend

# Install dependencies
npm install

# Start development server
npm start
```

The frontend will open automatically at `http://localhost:3000`

##  Docker Deployment

### Using Docker Compose (Recommended)

```bash
# Build and start all services
docker-compose up --build

# Run in background
docker-compose up -d

# View logs
docker-compose logs -f

# Stop services
docker-compose down
```

### Individual Container Builds

**Backend:**
```bash
cd backend
docker build -t style-transfer-backend .
docker run -p 8000:8000 style-transfer-backend
```

**Frontend:**
```bash
cd frontend
docker build -t style-transfer-frontend .
docker run -p 3000:3000 style-transfer-frontend
```

##  Live Demo

Visit the live application: [Demo URL will be added after deployment]

##  Usage Guide

1. **Upload Content Image**: Select or drag-and-drop the image you want to stylize
2. **Upload Style Image**: Choose an artistic style image (paintings, textures, etc.)
3. **Transfer Style**: Click the "Transfer Style" button
4. **Download Result**: Save your stylized masterpiece!

### Best Practices

- **Content Images**: Use clear, high-resolution photographs (500x500 to 2000x2000 pixels)
- **Style Images**: Bold, distinctive artistic styles work best (famous paintings, abstract art)
- **File Formats**: PNG for best quality, JPG for smaller file sizes
- **Image Size**: Maximum 10MB per image (automatically resized if larger)

##  Project Structure

```
ImageStyle/
├── backend/
│   ├── app.py              # Flask API server
│   ├── requirements.txt    # Python dependencies
│   ├── Dockerfile         # Backend container config
│   └── uploads/           # Uploaded images (created at runtime)
├── frontend/
│   ├── public/            # Static files
│   ├── src/
│   │   ├── components/    # React components
│   │   ├── App.js         # Main application component
│   │   └── index.js       # Application entry point
│   ├── package.json       # Node dependencies
│   ├── Dockerfile         # Frontend container config
│   └── nginx.conf         # Nginx configuration
├── example_images/        # Sample images for testing
├── docker-compose.yml     # Docker Compose configuration
└── README.md             # This file
```

##  API Documentation

### Endpoints

#### Health Check
```
GET /health
```
Returns server status and model loading state.

**Response:**
```json
{
  "status": "healthy",
  "model_loaded": true
}
```

#### Style Transfer
```
POST /api/transfer
Content-Type: multipart/form-data
```

**Parameters:**
- `content_image` (file): The image to stylize
- `style_image` (file): The artistic style to apply

**Response:**
```json
{
  "success": true,
  "result_image": "data:image/png;base64,...",
  "processing_time": 2.45
}
```

##  Example Images

The repository includes example images in the `example_images/` directory:

- **Content Images**: `content/portrait.jpg`, `content/landscape.jpg`
- **Style Images**: `style/starry_night.jpg`, `style/great_wave.jpg`

Try combining these for your first style transfer!

##  Deployment Options

### Free Hosting Services

#### Option 1: Render.com (Recommended)

**Backend:**
1. Create a new Web Service
2. Connect your GitHub repository
3. Build command: `cd backend && pip install -r requirements.txt`
4. Start command: `cd backend && gunicorn --bind 0.0.0.0:$PORT app:app`
5. Add environment variable: `PORT=8000`

**Frontend:**
1. Create a new Static Site
2. Connect your GitHub repository
3. Build command: `cd frontend && npm install && npm run build`
4. Publish directory: `frontend/build`
5. Add environment variable: `REACT_APP_API_URL=https://your-backend-url.onrender.com`

#### Option 2: Railway.app

1. Connect your GitHub repository
2. Add two services (backend and frontend)
3. Configure build and start commands as above

#### Option 3: Vercel + Render

- Frontend: Deploy to Vercel (automatic with GitHub integration)
- Backend: Deploy to Render as described above

##  Testing

```bash
# Test backend API
curl http://localhost:8000/health

# Test style transfer (with test images)
curl -X POST http://localhost:8000/api/transfer \
  -F "content_image=@example_images/content/portrait.jpg" \
  -F "style_image=@example_images/style/starry_night.jpg"
```

##  Troubleshooting

**Backend Issues:**
- Ensure Python 3.11+ is installed
- Check virtual environment is activated
- Verify all dependencies are installed: `pip install -r requirements.txt`
- Check port 8000 is available (or set PORT environment variable)

**Frontend Issues:**
- Ensure Node.js 16+ is installed
- Delete `node_modules` and `package-lock.json`, then run `npm install`
- Verify backend URL in `.env` or `package.json` proxy setting

**Style Transfer Issues:**
- Ensure images are valid formats (PNG, JPG, JPEG, WEBP)
- Check image file sizes (max 10MB)
- Verify internet connection (required for first model download)

##  License

This project is open source and available under the MIT License.

##  Author

**Anurag**

- GitHub: [@Anurag02012004](https://github.com/Anurag02012004)
- Repository: [ImageStyle](https://github.com/Anurag02012004/ImageStyle)

##  Acknowledgments

- Google Magenta team for the Arbitrary Image Stylization model
- TensorFlow team for the excellent ML framework
- React community for amazing tools and libraries

##  Future Enhancements

- [ ] Multiple style presets
- [ ] Batch processing support
- [ ] Style intensity slider
- [ ] History of processed images
- [ ] Social sharing features
- [ ] Mobile app version

##  Contributing

Contributions, issues, and feature requests are welcome! Feel free to check the [issues page](https://github.com/Anurag02012004/ImageStyle/issues).

---

**Made with ❤️ using TensorFlow, Flask, and React**

*Transform your photos into artistic masterpieces!* 
