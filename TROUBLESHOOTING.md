#  Troubleshooting Guide

## Common Issues and Solutions

### Issue 1: "Failed to process images" Error

**Symptoms:**
- Frontend shows "Failed to process images. Please try again."
- Backend logs show model is loading

**Possible Causes & Solutions:**

#### A. Model Still Loading (First Request)
- **Cause**: The TensorFlow model downloads on first use (takes 1-2 minutes)
- **Solution**: Wait for the first request to complete. Subsequent requests will be fast.
- **Check**: Look for "Loading style transfer model from TensorFlow Hub..." in logs

#### B. Request Timeout
- **Cause**: Request takes longer than frontend timeout (2 minutes)
- **Solution**: 
  - Check backend logs for completion
  - Increase timeout in frontend if needed
  - First request will always be slow due to model download

#### C. CORS Issues
- **Cause**: Frontend can't reach backend
- **Solution**: 
  - Verify `REACT_APP_API_URL` environment variable is set correctly
  - Should be: `https://imagestyle-backend.onrender.com`
  - Check browser console for CORS errors

#### D. Invalid Image Files
- **Cause**: Images are corrupted or wrong format
- **Solution**:
  - Use valid PNG, JPG, JPEG, or WEBP files
  - Ensure files are under 10MB
  - Try with different images

### Issue 2: Backend Shows "model_loaded: false"

**This is Normal!**
- Model loads lazily on first request
- Health check shows false until first style transfer request
- After first request, model stays loaded

### Issue 3: Frontend Can't Connect to Backend

**Symptoms:**
- Network errors in browser console
- "Failed to fetch" errors

**Solutions:**
1. Verify backend URL in environment variable
2. Check backend is running: `https://imagestyle-backend.onrender.com/health`
3. Check CORS is enabled (already configured in code)
4. Check browser console for specific error messages

### Issue 4: Build Fails on Render

**Frontend Build Fails:**
- Check build logs for specific errors
- Verify `package.json` is in `frontend/` directory
- Ensure Node.js version is 16+
- Try: Delete service and recreate with exact settings

**Backend Build Fails:**
- Check Python version (should be 3.11+)
- Verify `requirements.txt` exists
- Check build logs for dependency errors

### Issue 5: Model Download Takes Too Long

**This is Expected:**
- First model download: 1-2 minutes
- Model size: ~50-100MB
- Downloads from TensorFlow Hub
- Cached after first download

**To Speed Up:**
- Model is cached after first download
- Subsequent requests are fast
- Consider pre-warming by making a test request after deployment

## Debugging Steps

### 1. Check Backend Logs
```bash
# In Render Dashboard:
# Go to your backend service → Logs tab
# Look for:
# - "Style transfer request received"
# - "Preprocessing images..."
# - "Applying style transfer..."
# - Any error messages
```

### 2. Check Frontend Console
```javascript
// Open browser Developer Tools (F12)
// Check Console tab for errors
// Check Network tab for API requests
```

### 3. Test Backend Directly
```bash
# Test health endpoint
curl https://imagestyle-backend.onrender.com/health

# Should return:
# {"status":"healthy","model_loaded":true/false}
```

### 4. Verify Environment Variables

**Frontend:**
- `REACT_APP_API_URL` should be: `https://imagestyle-backend.onrender.com`
- No trailing slash
- Must include `https://`

**Backend:**
- `PORT` should be: `8000`
- `PYTHON_VERSION` should be: `3.11.0`

## Getting More Detailed Logs

The backend now includes detailed logging:
- Request received logs
- Image preprocessing logs
- Style transfer progress logs
- Detailed error messages with stack traces

Check Render dashboard logs for all output.

## Still Having Issues?

1. **Check Logs**: Both backend and frontend logs in Render
2. **Verify Configuration**: All settings match the guides
3. **Test Endpoints**: Use curl or Postman to test backend directly
4. **Check Browser Console**: Look for JavaScript errors
5. **Try Simple Test**: Use example images from `example_images/` folder

## Useful Test Commands

```bash
# Test backend health
curl https://imagestyle-backend.onrender.com/health

# Test backend root
curl https://imagestyle-backend.onrender.com/

# Test style transfer (with test images)
curl -X POST https://imagestyle-backend.onrender.com/api/transfer \
  -F "content_image=@example_images/content/portrait.jpg" \
  -F "style_image=@example_images/style/starry_night.jpg"
```

---

**Remember**: First style transfer request takes 1-2 minutes due to model download. This is normal and expected!

