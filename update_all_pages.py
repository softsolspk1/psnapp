import os
import re

# List of pages to update (all pages except index.html and login.html)
pages_to_update = [
    'dashboard.html', 'about.html', 'mission.html', 'leadership.html', 'committees.html',
    'news.html', 'events.html', 'projects.html', 'articles.html',
    'forum.html', 'guidelines.html', 'research.html', 'chat.html',
    'contact.html', 'resources.html', 'gallery.html', 'pjns.html'
]

def update_page_content(content):
    # 1. Remove Pak Neurology Network name from header
    content = re.sub(
        r'<div class="brand-text">\s*<h1[^>]*>Pak Neurology Network</h1>\s*</div>',
        '',
        content,
        flags=re.DOTALL
    )

    # 2. Fix Home menu link in navigation
    content = re.sub(
        r'<a class="nav-link[^"]*" href="[^"]*">Home</a>',
        '<a class="nav-link" href="dashboard.html">Home</a>',
        content
    )

    # Make Home link active if this is dashboard.html
    if 'dashboard.html' in content[:1000]:  # Check in first 1000 chars to determine if it's dashboard
        content = re.sub(
            r'<a class="nav-link" href="dashboard.html">Home</a>',
            '<a class="nav-link active" href="dashboard.html">Home</a>',
            content
        )

    return content

# Process each file
for page in pages_to_update:
    if not os.path.exists(page):
        print(f"Skipping {page} - file not found")
        continue
        
    try:
        # Read the current file
        with open(page, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Update content
        updated_content = update_page_content(content)
        
        # Write the updated content back to the file
        with open(page, 'w', encoding='utf-8') as f:
            f.write(updated_content)
            
        print(f"Updated {page} successfully")
        
    except Exception as e:
        print(f"Error updating {page}: {str(e)}")

print("\nContent update complete!") 