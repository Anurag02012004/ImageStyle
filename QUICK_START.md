# 🚀 Quick Start Guide - Style Transfer

## What Images Should I Upload?

### Content Image (Left Side)
**This is the image you want to transform/stylize.**

Good examples:
- 📸 A photo of yourself or a person
- 🏔️ A landscape or nature scene
- 🏛️ A building or architecture photo
- 🐱 A pet or animal photo
- 🎭 Any clear, detailed photograph

### Style Image (Right Side)
**This is the artistic style you want to apply.**

Good examples:
- 🎨 Famous paintings (Van Gogh, Picasso, Monet)
- 🌊 The Great Wave by Hokusai
- ⭐ The Starry Night by Van Gogh
- 🖼️ Any artistic painting or texture
- 🎨 Abstract art or patterns

## 📥 Ready-to-Use Example Images

I've downloaded some example images for you! They're in:

```
example_images/
├── content/          (images to stylize)
│   ├── portrait.jpg
│   └── landscape.jpg
└── style/            (artistic styles)
    ├── starry_night.jpg
    └── great_wave.jpg
```

## 🎯 Best Test Combinations

### Combination 1: Portrait + Starry Night
- Content: `example_images/content/portrait.jpg`
- Style: `example_images/style/starry_night.jpg`
- **Result:** Portrait with Van Gogh's swirling brushstrokes!

### Combination 2: Landscape + Great Wave
- Content: `example_images/content/landscape.jpg`
- Style: `example_images/style/great_wave.jpg`
- **Result:** Landscape with wave-like patterns!

## 🖼️ Where to Find More Images

### For Content Images (Photos):
1. **Unsplash** - https://unsplash.com (free, high-quality photos)
2. **Pexels** - https://pexels.com (free stock photos)
3. Use your own photos from your phone/computer!

### For Style Images (Art):
1. **Wikimedia Commons** - https://commons.wikimedia.org (public domain art)
2. **Artvee** - https://artvee.com (public domain artwork)
3. Search Google Images for "famous paintings" and use images marked as "reusable"

## 💡 Pro Tips

1. **Start Simple:** Try a portrait with Starry Night first - it's very recognizable!
2. **Use High-Quality Images:** Clear, detailed images work best
3. **Be Creative:** Try different combinations - you might be surprised!
4. **Image Size:** The app handles images up to 10MB, automatically resizing large ones

## 🎨 Quick Test Right Now

1. Open http://localhost:3000 in your browser
2. Upload `example_images/content/portrait.jpg` as Content Image
3. Upload `example_images/style/starry_night.jpg` as Style Image
4. Click "✨ Transfer Style"
5. Wait a few seconds...
6. See your masterpiece! 🎉

## 📸 Need More Examples?

Run this command to download more example images:
```bash
./download_examples.sh
```

Or visit the links in `EXAMPLE_IMAGES.md` for direct image URLs!

