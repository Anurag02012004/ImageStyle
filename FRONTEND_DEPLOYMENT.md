#  Frontend Deployment Instructions

Your backend is now **live** at: `https://imagestyle-backend.onrender.com`

## Quick Deployment Steps

### Step 1: Deploy Frontend on Render

1. Go to [Render Dashboard](https://dashboard.render.com)

2. Click **"New +"** → **"Static Site"**

3. **Connect Repository**:
   - GitHub: `Anurag02012004/ImageStyle`
   - Branch: `main`

4. **Configure Settings**:
   - **Name**: `imagestyle-frontend` (or any name you prefer)
   - **Root Directory**: Leave **EMPTY** (don't set this!)
   - **Build Command**: `cd frontend && npm install && npm run build`
     - ⚠️ **Important**: Make sure there are no extra spaces or characters
     - Copy exactly: `cd frontend && npm install && npm run build`
   - **Publish Directory**: `frontend/build`
     - ⚠️ **Important**: Make sure it's exactly `frontend/build` (no leading slash)

5. **Add Environment Variable**:
   - Click **"Advanced"** → **"Add Environment Variable"**
   - **Key**: `REACT_APP_API_URL`
   - **Value**: `https://imagestyle-backend.onrender.com`
   - ⚠️ **Important**: Make sure to include `https://` in the URL

6. Click **"Create Static Site"**

7. Wait for build to complete (2-5 minutes)

### Step 2: Verify Deployment

Once deployed, you'll get a URL like:
- `https://imagestyle-frontend.onrender.com`

Visit this URL to see your application!

## Testing

1. **Test Backend API**:
   - Visit: `https://imagestyle-backend.onrender.com/health`
   - Should show: `{"status":"healthy","model_loaded":true}`

2. **Test Frontend**:
   - Visit your frontend URL
   - Upload content and style images
   - Click "Transfer Style"
   - Should see stylized result!

## Troubleshooting

### Frontend shows connection error:
- Verify `REACT_APP_API_URL` environment variable is set correctly
- Make sure the URL starts with `https://`
- Check backend is running: `https://imagestyle-backend.onrender.com/health`

### CORS errors:
- The backend already has CORS enabled for all origins
- If issues persist, check backend logs

### Build fails:
- Check build logs in Render dashboard
- Ensure Node.js version is 16+
- Verify all dependencies in `package.json`

## Your Live URLs

After deployment:
- **Backend API**: `https://imagestyle-backend.onrender.com`
- **Frontend App**: `https://imagestyle-frontend.onrender.com` (or your custom URL)

## Cost

Both services are **FREE** on Render's free tier! 

---

**Need help?** Check the logs in Render dashboard or open an issue on GitHub.

