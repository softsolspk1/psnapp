import os
import re

# List of pages to update
pages_to_update = [
    'dashboard.html', 'about.html', 'mission.html', 'leadership.html', 'committees.html',
    'news.html', 'events.html', 'projects.html', 'articles.html',
    'forum.html', 'guidelines.html', 'research.html', 'chat.html',
    'contact.html', 'resources.html', 'gallery.html', 'pjns.html'
]

def update_page_content(content):
    # 1. Remove Donation, Join Now and Member Login Buttons
    content = re.sub(
        r'<a class="btn btn-donation"[^>]*>Donation</a>\s*' +
        r'<a class="btn btn-join"[^>]*>Join Now</a>\s*' +
        r'<a class="btn btn-login"[^>]*>Member Login</a>',
        '',
        content
    )

    # 2. Replace logo and text in header
    content = re.sub(
        r'<img src="PSN logo.jpg"[^>]*>.*?</div>',
        '<img src="logo.png" alt="Pak Neurology Network" class="img-fluid me-2" style="max-height: 60px;">' +
        '<div class="brand-text">' +
        '<h1 class="mb-0 fs-5">Pak Neurology Network</h1>' +
        '</div>',
        content,
        flags=re.DOTALL
    )

    # 3. Remove Conference Slide
    content = re.sub(
        r'<div class="item">\s*<img src="[^"]*conference[^"]*".*?</div>\s*</div>',
        '</div>',
        content,
        flags=re.DOTALL
    )

    # 4. Update statistics
    stats_updates = {
        r'<h3 class="counter">547</h3>\s*<p>Members</p>': '<h3 class="counter">314</h3><p>Members</p>',
        r'<h3 class="counter">52</h3>\s*<p>Annual Events</p>': '<h3 class="counter">04</h3><p>Annual Events</p>',
        r'<h3 class="counter">128</h3>\s*<p>Research Papers</p>': '<h3 class="counter">22</h3><p>Research Papers</p>',
        r'<h3 class="counter">34</h3>\s*<p>Partner Hospitals</p>': '<h3 class="counter">34</h3><p>Partner Hospitals</p>'
    }

    for old, new in stats_updates.items():
        content = re.sub(old, new, content)

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