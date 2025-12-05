import os
import urllib.request
from urllib.error import URLError
import json

# Image URLs from free sources (Unsplash)
IMAGES = [
    {
        "name": "construction1.jpg",
        "url": "https://images.unsplash.com/photo-1504917595217-3404ee9c6e95?w=800&h=800&fit=crop",
        "description": "Commercial Project"
    },
    {
        "name": "construction2.jpg",
        "url": "https://images.unsplash.com/photo-1581092918056-0c4c3acd3789?w=800&h=800&fit=crop",
        "description": "Residential Development"
    },
    {
        "name": "construction3.jpg",
        "url": "https://images.unsplash.com/photo-1581092918056-0c4c3acd3789?w=800&h=800&fit=crop",
        "description": "Industrial Build"
    },
    {
        "name": "construction4.jpg",
        "url": "https://images.unsplash.com/photo-1562071503-3fc710c596a0?w=800&h=800&fit=crop",
        "description": "Infrastructure Work"
    }
]

def download_images():
    """Download construction images and save them to static/images folder"""
    
    # Create images directory if it doesn't exist
    images_dir = os.path.join(os.path.dirname(__file__), "static", "images")
    os.makedirs(images_dir, exist_ok=True)
    
    print("=" * 60)
    print("BK BOND MASTERS - Construction Images Downloader")
    print("=" * 60)
    print()
    
    successful = 0
    failed = 0
    
    for image_info in IMAGES:
        filename = image_info["name"]
        url = image_info["url"]
        filepath = os.path.join(images_dir, filename)
        
        # Skip if file already exists
        if os.path.exists(filepath):
            print(f"✓ {filename} - Already exists (skipped)")
            continue
        
        try:
            print(f"⏳ Downloading {filename}...", end=" ")
            urllib.request.urlretrieve(url, filepath)
            print(f"✓ Done ({image_info['description']})")
            successful += 1
        except URLError as e:
            print(f"✗ Failed - Network error")
            failed += 1
        except Exception as e:
            print(f"✗ Failed - {str(e)}")
            failed += 1
    
    print()
    print("=" * 60)
    print(f"Download Complete!")
    print(f"✓ Successful: {successful}")
    print(f"✗ Failed: {failed}")
    print(f"📁 Location: {images_dir}")
    print("=" * 60)
    print()
    print("You can now run your Flask app with: python app.py")
    print("Then visit: http://localhost:5000")

if __name__ == "__main__":
    download_images()
