import os
import requests
from pathlib import Path
import shutil

def create_directory(path):
    Path(path).mkdir(parents=True, exist_ok=True)

def download_image(url, save_path):
    try:
        response = requests.get(url, stream=True)
        response.raise_for_status()
        with open(save_path, 'wb') as f:
            shutil.copyfileobj(response.raw, f)
        print(f"Downloaded: {save_path}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

# Create required directories
base_dir = "assets/images"
directories = [
    "slider",
    "news",
    "team",
    "projects",
    "articles",
    "events",
    "gallery",
    "gallery/conferences",
    "gallery/workshops",
    "gallery/events",
    "gallery/meetings",
    "journal"
]

for dir_name in directories:
    create_directory(os.path.join(base_dir, dir_name))

# Define image URLs using Picsum for placeholders
images = {
    # Gallery - Conference Images
    "gallery/conferences/conference1.jpg": "https://picsum.photos/800/600?random=1",
    "gallery/conferences/conference2.jpg": "https://picsum.photos/800/600?random=2",
    
    # Gallery - Workshop Images
    "gallery/workshops/workshop1.jpg": "https://picsum.photos/800/600?random=3",
    "gallery/workshops/workshop2.jpg": "https://picsum.photos/800/600?random=4",
    
    # Gallery - Event Images
    "gallery/events/event1.jpg": "https://picsum.photos/800/600?random=5",
    "gallery/events/event2.jpg": "https://picsum.photos/800/600?random=6",
    
    # Gallery - Meeting Images
    "gallery/meetings/meeting1.jpg": "https://picsum.photos/800/600?random=7",
    "gallery/meetings/meeting2.jpg": "https://picsum.photos/800/600?random=8",
    
    # Journal Images
    "journal/latest-issue.jpg": "https://picsum.photos/400/600?random=9",
    
    # Team Images
    "team/naila-shahbaz.png": "https://picsum.photos/400/400?random=10",
    
    # Slider Images
    "slider/slide1.jpg": "https://picsum.photos/1920/600?random=11",
    "slider/slide2.jpg": "https://picsum.photos/1920/600?random=12",
    "slider/slide3.jpg": "https://picsum.photos/1920/600?random=13"
}

# Download images
for path, url in images.items():
    save_path = os.path.join(base_dir, path)
    download_image(url, save_path)

print("Image download complete. Please check the assets/images directory.") 