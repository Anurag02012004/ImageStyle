# 🚀 Render.com Deployment Guide

## Important Note About render.yaml

Render's `render.yaml` does **not support static sites** directly. Therefore, we need to deploy the backend and frontend separately.

## Step-by-Step Deployment

### Step 1: Deploy Backend (Using Blueprint)

1. Go to [Render Dashboard](https://dashboard.render.com)
2. Click **"New +"** → **"Blueprint"**
3. Connect your GitHub repository: `Anurag02012004/ImageStyle`
4. Select branch: `main`
5. Render will detect `render.yaml` and deploy the backend service
6. **Note the backend URL** (e.g., `https://imagestyle-backend.onrender.com`)

### Step 2: Deploy Frontend (Manual - Static Site)

1. In Render Dashboard, click **"New +"** → **"Static Site"**
2. Connect your GitHub repository: `Anurag02012004/ImageStyle`
3. Configure:
   - **Name**: `imagestyle-frontend`
   - **Branch**: `main`
   - **Root Directory**: Leave empty (we'll specify in build command)
   - **Build Command**: `cd frontend && npm install && npm run build`
   - **Publish Directory**: `frontend/build`
4. Add Environment Variable:
   - **Key**: `REACT_APP_API_URL`
   - **Value**: `https://imagestyle-backend.onrender.com` (use your actual backend URL)
5. Click **"Create Static Site"**
6. Wait for deployment to complete

### Step 3: Update Frontend API URL (If Needed)

If you need to update the backend URL later:
1. Go to your frontend service in Render
2. Go to **"Environment"** tab
3. Update `REACT_APP_API_URL` to your backend URL
4. Save changes (auto-redeploys)

## Alternative: Deploy Both as Web Services

If you prefer to deploy both as web services:

### Backend (from render.yaml):
- Already configured ✅

### Frontend (manual web service):
1. **"New +"** → **"Web Service"**
2. Connect repository: `Anurag02012004/ImageStyle`
3. Configure:
   - **Name**: `imagestyle-frontend`
   - **Environment**: `Node`
   - **Root Directory**: `frontend`
   - **Build Command**: `npm install && npm run build`
   - **Start Command**: `npm start` or use a static file server like `npx serve -s build`
4. Add Environment Variable:
   - `REACT_APP_API_URL`: Your backend URL
5. **Plan**: Free

## Recommended Approach

**Use the Static Site method** (Step 2 above) - it's simpler and more appropriate for a React app that builds to static files.

## Troubleshooting

### Frontend can't connect to backend:
- Verify `REACT_APP_API_URL` is set correctly
- Check backend is running and accessible
- Check CORS settings in backend (already configured for all origins)

### Build fails:
- Check Node.js version (should be 16+)
- Verify all dependencies in `package.json`
- Check build logs in Render dashboard

### Backend fails to start:
- Check Python version (should be 3.11+)
- Verify all dependencies in `requirements.txt`
- Check startup logs in Render dashboard

## Cost

Both services are on the **free tier**:
- Backend: Free (with limitations)
- Frontend Static Site: Always free

---

**After deployment, your app will be live!** 🎉

