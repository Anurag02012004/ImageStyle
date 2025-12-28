#  Deployment Guide

This guide provides step-by-step instructions for deploying the Neural Style Transfer application to various free hosting platforms.

##  Deployment Options

### Option 1: Render.com (Recommended - Easiest)

Render.com offers free hosting with automatic deployments from GitHub.

#### Backend Deployment

1. **Sign up** at [render.com](https://render.com) (free account)

2. **Create a New Web Service**:
   - Click "New +" → "Web Service"
   - Connect your GitHub repository: `Anurag02012004/ImageStyle`
   - Name: `imagestyle-backend`

3. **Configure Backend**:
   - **Build Command**: `cd backend && pip install -r requirements.txt`
   - **Start Command**: `cd backend && gunicorn --bind 0.0.0.0:$PORT --workers 2 --threads 4 --timeout 120 app:app`
   - **Environment**: Python 3
   - **Add Environment Variable**:
     - Key: `PORT`
     - Value: `8000`

4. **Deploy**: Click "Create Web Service"

5. **Note the Backend URL**: e.g., `https://imagestyle-backend.onrender.com`

#### Frontend Deployment

1. **Create a New Static Site**:
   - Click "New +" → "Static Site"
   - Connect your GitHub repository: `Anurag02012004/ImageStyle`
   - Name: `imagestyle-frontend`

2. **Configure Frontend**:
   - **Build Command**: `cd frontend && npm install && npm run build`
   - **Publish Directory**: `frontend/build`
   - **Add Environment Variable**:
     - Key: `REACT_APP_API_URL`
     - Value: `https://your-backend-url.onrender.com` (use your actual backend URL)

3. **Deploy**: Click "Create Static Site"

4. **Your app is live!**: Visit the provided URL

#### Using render.yaml (Alternative)

The repository includes a `render.yaml` file. To use it:

1. In Render dashboard, go to "New +" → "Blueprint"
2. Connect your GitHub repository
3. Render will automatically detect and use `render.yaml`
4. Both services will be deployed automatically

### Option 2: Railway.app

Railway offers free tier with automatic deployments.

1. **Sign up** at [railway.app](https://railway.app)

2. **Create New Project**:
   - Click "New Project"
   - Select "Deploy from GitHub repo"
   - Choose your repository

3. **Add Backend Service**:
   - Click "+ New" → "GitHub Repo"
   - Select your repository
   - Set Root Directory: `backend`
   - Add environment variable: `PORT=8000`
   - Railway will auto-detect Python and deploy

4. **Add Frontend Service**:
   - Click "+ New" → "GitHub Repo"
   - Select your repository
   - Set Root Directory: `frontend`
   - Add environment variable: `REACT_APP_API_URL=https://your-backend-url.up.railway.app`
   - Railway will auto-detect Node.js and deploy

### Option 3: Vercel (Frontend) + Render (Backend)

**Frontend on Vercel:**

1. **Sign up** at [vercel.com](https://vercel.com)

2. **Import Project**:
   - Click "New Project"
   - Import from GitHub: `Anurag02012004/ImageStyle`
   - Root Directory: `frontend`

3. **Configure**:
   - Framework Preset: Create React App
   - Build Command: `npm run build`
   - Output Directory: `build`
   - Add Environment Variable:
     - Key: `REACT_APP_API_URL`
     - Value: `https://your-backend-url.onrender.com`

4. **Deploy**: Click "Deploy"

**Backend on Render:** Follow Option 1 backend instructions above.

### Option 4: Fly.io

Fly.io offers free hosting with Docker support.

1. **Install Fly CLI**:
   ```bash
   curl -L https://fly.io/install.sh | sh
   ```

2. **Login**:
   ```bash
   fly auth login
   ```

3. **Deploy Backend**:
   ```bash
   cd backend
   fly launch
   # Follow prompts, select Python app
   fly deploy
   ```

4. **Deploy Frontend**:
   ```bash
   cd frontend
   fly launch
   # Follow prompts, select Node.js app
   fly deploy
   ```

##  Environment Variables

### Backend Environment Variables

- `PORT`: Port number (default: 8000)

### Frontend Environment Variables

- `REACT_APP_API_URL`: Backend API URL (e.g., `https://your-backend.onrender.com`)

##  Post-Deployment Steps

1. **Update CORS** (if needed):
   - If frontend is on a different domain, update CORS settings in `backend/app.py`

2. **Test the Deployment**:
   - Visit your frontend URL
   - Upload test images
   - Verify style transfer works

3. **Monitor Logs**:
   - Check backend logs for errors
   - Monitor API response times

##  Troubleshooting

### Backend Issues

- **Build Fails**: Check Python version (requires 3.11+)
- **Memory Errors**: Reduce image size limits in code
- **Timeout Errors**: Increase timeout in gunicorn command
- **Model Download Fails**: Ensure internet connectivity in deployment environment

### Frontend Issues

- **API Connection Fails**: Verify `REACT_APP_API_URL` environment variable
- **Build Fails**: Check Node.js version (requires 16+)
- **CORS Errors**: Update CORS settings in backend

##  Security Considerations

1. **Rate Limiting**: Consider adding rate limiting to prevent abuse
2. **File Size Limits**: Already implemented (10MB max)
3. **Input Validation**: Already implemented
4. **CORS**: Configured for frontend domain

##  Cost Estimates

All platforms mentioned offer **free tiers** that are sufficient for:
- Low to medium traffic
- Personal projects
- Demo applications
- Testing and development

For production use with high traffic, consider paid plans.

##  Additional Resources

- [Render Documentation](https://render.com/docs)
- [Railway Documentation](https://docs.railway.app)
- [Vercel Documentation](https://vercel.com/docs)
- [Fly.io Documentation](https://fly.io/docs)

---

**Need Help?** Open an issue on GitHub or check the troubleshooting section.

