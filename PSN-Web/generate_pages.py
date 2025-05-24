import os
from pathlib import Path

def read_template():
    with open('template.html', 'r', encoding='utf-8') as f:
        return f.read()

def create_page(template, output_path, title, breadcrumb_items, content):
    # Create directory if it doesn't exist
    directory = os.path.dirname(output_path)
    if directory:  # Only create directory if path has a directory component
        os.makedirs(directory, exist_ok=True)
    
    # Replace placeholders
    page_content = template.replace('{{PAGE_TITLE}}', title)
    page_content = page_content.replace('{{BREADCRUMB_ITEMS}}', breadcrumb_items)
    page_content = page_content.replace('{{MAIN_CONTENT}}', content)
    
    # Fix relative paths based on directory depth
    depth = len(Path(output_path).parent.parts)
    if depth > 0:
        prefix = '../' * depth
        page_content = page_content.replace('href="assets/', f'href="{prefix}assets/')
        page_content = page_content.replace('src="assets/', f'src="{prefix}assets/')
    
    # Write the file
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(page_content)
    print(f"Created {output_path}")

def main():
    template = read_template()
    
    pages = [
        # Main Pages
        {
            'path': 'about.html',
            'title': 'About PSN',
            'breadcrumb': '<li class="breadcrumb-item active">About PSN</li>',
            'content': '<!-- About PSN content -->'
        },
        {
            'path': 'mission.html',
            'title': 'Mission & Vision',
            'breadcrumb': '<li class="breadcrumb-item active">Mission & Vision</li>',
            'content': '<!-- Mission & Vision content -->'
        },
        {
            'path': 'office-bearers/current.html',
            'title': 'Current Office Bearers',
            'breadcrumb': '<li class="breadcrumb-item">Office Bearers</li><li class="breadcrumb-item active">Current Office Bearers</li>',
            'content': '<!-- Current Office Bearers content -->'
        },
        {
            'path': 'office-bearers/past-presidents.html',
            'title': 'Past Presidents',
            'breadcrumb': '<li class="breadcrumb-item">Office Bearers</li><li class="breadcrumb-item active">Past Presidents</li>',
            'content': '<!-- Past Presidents content -->'
        },
        # Education & Training
        {
            'path': 'education/research-workshops.html',
            'title': 'Research Workshops',
            'breadcrumb': '<li class="breadcrumb-item">Education & Training</li><li class="breadcrumb-item active">Research Workshops</li>',
            'content': '<!-- Research Workshops content -->'
        },
        {
            'path': 'education/conferences.html',
            'title': 'Conferences',
            'breadcrumb': '<li class="breadcrumb-item">Education & Training</li><li class="breadcrumb-item active">Conferences</li>',
            'content': '<!-- Conferences content -->'
        },
        {
            'path': 'education/neurological-emergencies.html',
            'title': 'Neurological Emergencies',
            'breadcrumb': '<li class="breadcrumb-item">Education & Training</li><li class="breadcrumb-item active">Neurological Emergencies</li>',
            'content': '<!-- Neurological Emergencies content -->'
        },
        {
            'path': 'education/future-conference.html',
            'title': 'Future Conference',
            'breadcrumb': '<li class="breadcrumb-item">Education & Training</li><li class="breadcrumb-item active">Future Conference</li>',
            'content': '<!-- Future Conference content -->'
        },
        # Guidelines
        {
            'path': 'guidelines/epilepsy.html',
            'title': 'Epilepsy Guidelines',
            'breadcrumb': '<li class="breadcrumb-item">Guidelines</li><li class="breadcrumb-item active">Epilepsy</li>',
            'content': '<!-- Epilepsy Guidelines content -->'
        },
        {
            'path': 'guidelines/stroke.html',
            'title': 'Stroke Guidelines',
            'breadcrumb': '<li class="breadcrumb-item">Guidelines</li><li class="breadcrumb-item active">Stroke</li>',
            'content': '<!-- Stroke Guidelines content -->'
        },
        {
            'path': 'guidelines/alzheimers.html',
            'title': "Alzheimer's Guidelines",
            'breadcrumb': '<li class="breadcrumb-item">Guidelines</li><li class="breadcrumb-item active">Alzheimer\'s</li>',
            'content': '<!-- Alzheimer\'s Guidelines content -->'
        },
        {
            'path': 'guidelines/parkinsons.html',
            'title': "Parkinson's Guidelines",
            'breadcrumb': '<li class="breadcrumb-item">Guidelines</li><li class="breadcrumb-item active">Parkinson\'s</li>',
            'content': '<!-- Parkinson\'s Guidelines content -->'
        },
        # Other Pages
        {
            'path': 'pjns.html',
            'title': 'PJNS',
            'breadcrumb': '<li class="breadcrumb-item active">PJNS</li>',
            'content': '<!-- PJNS content -->'
        },
        {
            'path': 'gallery.html',
            'title': 'Gallery',
            'breadcrumb': '<li class="breadcrumb-item active">Gallery</li>',
            'content': '<!-- Gallery content -->'
        },
        {
            'path': 'resources.html',
            'title': 'Resources',
            'breadcrumb': '<li class="breadcrumb-item active">Resources</li>',
            'content': '<!-- Resources content -->'
        },
        {
            'path': 'events.html',
            'title': 'Events',
            'breadcrumb': '<li class="breadcrumb-item active">Events</li>',
            'content': '<!-- Events content -->'
        },
        {
            'path': 'contact.html',
            'title': 'Contact Us',
            'breadcrumb': '<li class="breadcrumb-item active">Contact Us</li>',
            'content': '<!-- Contact Us content -->'
        }
    ]
    
    # Create each page
    for page in pages:
        create_page(
            template,
            page['path'],
            page['title'],
            page['breadcrumb'],
            page['content']
        )

if __name__ == '__main__':
    main()