import os
import re

# List of pages to update (all pages except login.html and index.html)
pages_to_update = [
    'dashboard.html', 'about.html', 'mission.html', 'leadership.html', 'committees.html',
    'news.html', 'events.html', 'projects.html', 'articles.html',
    'forum.html', 'guidelines.html', 'research.html', 'chat.html',
    'contact.html', 'resources.html', 'gallery.html', 'pjns.html',
    'publications.html'
]

def add_members_link(content):
    # Find the navigation items
    nav_pattern = r'(<li class="nav-item"><a class="nav-link" href="articles\.html">Articles</a></li>)'
    
    # Add Members link after Articles
    members_link = r'\1\n                        <li class="nav-item"><a class="nav-link" href="members.html">Members</a></li>'
    
    # Replace in content
    updated_content = re.sub(nav_pattern, members_link, content)
    
    return updated_content

def update_navigation():
    for page in pages_to_update:
        try:
            # Read the file
            with open(page, 'r', encoding='utf-8') as f:
                content = f.read()
            
            # Add Members link
            updated_content = add_members_link(content)
            
            # Save the file
            with open(page, 'w', encoding='utf-8') as f:
                f.write(updated_content)
                
            print(f"Updated navigation in {page}")
            
        except Exception as e:
            print(f"Error updating {page}: {str(e)}")

if __name__ == "__main__":
    update_navigation() 