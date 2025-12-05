# BK BOND MASTERS CONSTRUCTION LTD - Website Setup

## Logo Upload Instructions

To add your company logo to the website:

1. **Prepare Your Logo**
   - Ensure your logo is in PNG or JPG format
   - Recommended size: 200x200 pixels or larger
   - Transparent background is preferred (PNG)

2. **Upload the Logo**
   - Place your logo file in the `static/images/` folder
   - Name it exactly: `logo.png` (or `logo.jpg` if using JPG)

3. **Update File Reference (if needed)**
   - The templates are already configured to look for `logo.png`
   - If you use a different filename, update these files:
     - `templates/index.html` - Search for `images/logo.png`
     - `templates/projects.html` - Search for `images/logo.png`

## Installation & Running the Website

### Prerequisites
- Python 3.7 or higher installed

### Setup Steps

1. **Install Dependencies**
   ```
   pip install -r requirements.txt
   ```

2. **Run the Flask Application**
   ```
   python app.py
   ```

3. **Access the Website**
   - Open your browser and go to: `http://localhost:5000`
   - Homepage: `http://localhost:5000/`
   - Projects Page: `http://localhost:5000/projects`

## Project Structure

```
BK BOND MASTERS WEB/
├── app.py                 # Main Flask application
├── requirements.txt       # Python dependencies
├── templates/             # HTML templates
│   ├── index.html        # Homepage
│   └── projects.html     # Projects page
└── static/               # Static files
    ├── css/
    │   └── style.css     # Stylesheet
    └── images/
        └── logo.png      # Company logo (ADD YOUR LOGO HERE)
```

## Customization

You can easily customize the content:

1. **Homepage Content** - Edit `templates/index.html`
2. **Projects Content** - Edit `templates/projects.html`
3. **Styling** - Modify `static/css/style.css`
4. **Contact Information** - Update the contact section in `index.html`

## Features

✓ Responsive design (works on mobile, tablet, desktop)
✓ Modern gradient styling
✓ Navigation bar with sticky positioning
✓ Hero section with call-to-action button
✓ About section with company features
✓ Projects showcase with cards
✓ Statistics display
✓ Contact information section
✓ Professional footer

## Support

For any issues or modifications needed, ensure Flask is properly installed and the directory structure is maintained as shown above.
