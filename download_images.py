import os
import requests
from pathlib import Path
import random

def create_directory(path):
    Path(path).mkdir(parents=True, exist_ok=True)

def download_image(url, save_path):
    try:
        response = requests.get(url)
        response.raise_for_status()
        with open(save_path, 'wb') as f:
            f.write(response.content)
        print(f"Downloaded: {save_path}")
    except Exception as e:
        print(f"Error downloading {url}: {e}")

# Create required directories
base_dir = "assets/images"
directories = ["slider", "news", "team", "projects", "articles", "events", "gallery"]
for dir_name in directories:
    create_directory(os.path.join(base_dir, dir_name))

# Define image URLs and their save paths
images = {
    # Slider images
    "https://picsum.photos/1920/600": f"{base_dir}/slider/conference.jpg",
    "https://picsum.photos/1920/600": f"{base_dir}/slider/research.jpg",
    "https://picsum.photos/1920/600": f"{base_dir}/slider/education.jpg",
    
    # News images
    "https://picsum.photos/800/600": f"{base_dir}/news/conference-announcement.jpg",
    "https://picsum.photos/800/600": f"{base_dir}/news/research-collab.jpg",
    "https://picsum.photos/800/600": f"{base_dir}/news/cme-workshop.jpg",
    
    # Team images
    "https://picsum.photos/400/400": f"{base_dir}/team/naila-shahbaz.jpg",
    "https://picsum.photos/400/400": f"{base_dir}/team/member1.jpg",
    "https://picsum.photos/400/400": f"{base_dir}/team/member2.jpg",
    "https://picsum.photos/400/400": f"{base_dir}/team/member3.jpg",
    
    # Project images
    "https://picsum.photos/800/600": f"{base_dir}/projects/stroke-registry.jpg",
    "https://picsum.photos/800/600": f"{base_dir}/projects/epilepsy-research.jpg",
    "https://picsum.photos/800/600": f"{base_dir}/projects/neurology-awareness.jpg",
    
    # Article images
    "https://picsum.photos/800/600": f"{base_dir}/articles/latest-research.jpg",
    "https://picsum.photos/800/600": f"{base_dir}/articles/clinical-study.jpg",
    "https://picsum.photos/800/600": f"{base_dir}/articles/medical-guidelines.jpg",
    
    # Event images
    "https://picsum.photos/800/600": f"{base_dir}/events/annual-conference.jpg",
    "https://picsum.photos/800/600": f"{base_dir}/events/workshop.jpg",
    "https://picsum.photos/800/600": f"{base_dir}/events/seminar.jpg",
    
    # Gallery images
    "https://picsum.photos/800/600": f"{base_dir}/gallery/team1.jpg",
    "https://picsum.photos/800/600": f"{base_dir}/gallery/event1.jpg",
    "https://picsum.photos/800/600": f"{base_dir}/gallery/conference1.jpg",
    "https://picsum.photos/800/600": f"{base_dir}/gallery/award1.jpg"
}

# Add random parameter to each URL to get different images
images = {f"{url}?random={random.randint(1, 1000)}": path for url, path in images.items()}

# Download all images
for url, save_path in images.items():
    download_image(url, save_path)

print("Image download complete. Please check the assets/images directory.")