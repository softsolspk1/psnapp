import os
import base64
import re

# Create default avatar image as a data URL
default_avatar = '''
<svg width="40" height="40" viewBox="0 0 40 40" fill="none" xmlns="http://www.w3.org/2000/svg">
    <circle cx="20" cy="20" r="20" fill="#E9ECEF"/>
    <path d="M20 10C22.2091 10 24 11.7909 24 14C24 16.2091 22.2091 18 20 18C17.7909 18 16 16.2091 16 14C16 11.7909 17.7909 10 20 10Z" fill="#ADB5BD"/>
    <path d="M28 30H12C12 25.5817 15.5817 22 20 22C24.4183 22 28 25.5817 28 30Z" fill="#ADB5BD"/>
</svg>
'''

# Convert SVG to base64 data URL
default_avatar_base64 = base64.b64encode(default_avatar.encode()).decode()
default_avatar_data_url = f"data:image/svg+xml;base64,{default_avatar_base64}"

# Save the default avatar as an SVG file
with open('assets/images/avatars/default.svg', 'w') as f:
    f.write(default_avatar)

# Update forum.html to use the new avatar
with open('forum.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace all instances of missing avatar images with the default avatar
content = re.sub(
    r'src="assets/images/avatars/default\.jpg"',
    'src="assets/images/avatars/default.svg"',
    content
)

# Save the updated forum.html
with open('forum.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Forum avatars have been fixed successfully!") 