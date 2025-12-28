#!/bin/bash

# Download example images for style transfer testing

echo "📥 Downloading example images for Style Transfer..."

mkdir -p example_images/content
mkdir -p example_images/style

echo ""
echo "Downloading content images..."

# Portrait
curl -L "https://images.unsplash.com/photo-1507003211169-0a1dd7228f2d?w=800" -o example_images/content/portrait.jpg 2>/dev/null
echo "✅ Portrait image downloaded"

# Landscape
curl -L "https://images.unsplash.com/photo-1506905925346-21bda4d32df4?w=800" -o example_images/content/landscape.jpg 2>/dev/null
echo "✅ Landscape image downloaded"

echo ""
echo "Downloading style images..."

# Starry Night (Van Gogh)
curl -L "https://upload.wikimedia.org/wikipedia/commons/thumb/e/ea/Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg/800px-Van_Gogh_-_Starry_Night_-_Google_Art_Project.jpg" -o example_images/style/starry_night.jpg 2>/dev/null
echo "✅ Starry Night style downloaded"

# The Great Wave (Hokusai)
curl -L "https://upload.wikimedia.org/wikipedia/commons/thumb/a/a5/Tsunami_by_hokusai_19th_century.jpg/800px-Tsunami_by_hokusai_19th_century.jpg" -o example_images/style/great_wave.jpg 2>/dev/null
echo "✅ Great Wave style downloaded"

echo ""
echo "✨ Example images downloaded!"
echo ""
echo "Images saved to:"
echo "  Content: example_images/content/"
echo "  Style:   example_images/style/"
echo ""
echo "You can now upload these images in the Style Transfer app!"
