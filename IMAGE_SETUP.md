# BK BOND MASTERS - Image Setup Guide

## Logo
Your logo file is already referenced as:
- **Location:** `static/images/logo.jpeg`
- **Current status:** ✓ Ready to use

---

## Construction Images for Homepage Gallery

The homepage now has a beautiful "Our Work" gallery section that needs 4 construction images.

### Image Requirements:
- **Format:** JPG, PNG
- **Resolution:** 800x800px minimum (square aspect ratio)
- **File names:** 
  - `construction1.jpg`
  - `construction2.jpg`
  - `construction3.jpg`
  - `construction4.jpg`

### Image Placement:
Place all images in: `static/images/`

### Where to Find Construction Images:

**Free Resources:**
1. **Unsplash** (https://unsplash.com)
   - Search: "construction site", "building construction", "modern architecture"
   
2. **Pexels** (https://pexels.com)
   - Search: "construction work", "building project", "heavy machinery"
   
3. **Pixabay** (https://pixabay.com)
   - Search: "construction", "building", "crane"

4. **Freepik** (https://freepik.com)
   - Search: "construction site", "workers building"

### Recommended Images for Each Slot:

1. **construction1.jpg** - Commercial/Office building construction or modern skyscraper
2. **construction2.jpg** - Residential housing project or apartment complex
3. **construction3.jpg** - Industrial facility or warehouse construction
4. **construction4.jpg** - Infrastructure work, road, or bridge project

---

## Directory Structure

After adding your images, your `static/images/` folder should look like:

```
static/images/
├── logo.jpeg              ✓ Already have this
├── construction1.jpg      ← Add this
├── construction2.jpg      ← Add this
├── construction3.jpg      ← Add this
└── construction4.jpg      ← Add this
```

---

## Gallery Captions

The gallery items display these captions on hover:
1. "Commercial Project"
2. "Residential Development"
3. "Industrial Build"
4. "Infrastructure Work"

You can change these captions by editing `templates/index.html` in the gallery section.

---

## Testing

After adding your images:
1. Run `python app.py`
2. Go to `http://localhost:5000`
3. Your images should appear in the "Our Work" section with hover effects

---

## Tips

- Use square or near-square images for best results
- Ensure images are high quality and well-lit
- Professional/professional-looking images work best
- The overlay will darken images slightly, so use well-lit photos
- Consider before/after shots or different project types for variety

