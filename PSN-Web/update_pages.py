import os
from bs4 import BeautifulSoup

def read_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        return file.read()

def write_file(file_path, content):
    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content)

def get_header_footer():
    index_content = read_file('index.html')
    soup = BeautifulSoup(index_content, 'html.parser')
    
    # Get everything from DOCTYPE to end of nav
    header = ''
    for element in soup.contents:
        if isinstance(element, str) and '<!DOCTYPE html>' in element:
            header = element.strip()
            break
    
    header += str(soup.html.head)
    header += '<body>\n'
    header += str(soup.find('div', class_='announcement-bar'))
    header += str(soup.find('header', class_='main-header'))
    header += str(soup.find('nav', class_='main-nav'))
    
    # Get footer
    footer = str(soup.find('footer'))
    
    # Get scripts
    scripts = ''
    for script in soup.find_all('script'):
        scripts += str(script) + '\n'
    
    footer += '\n' + scripts + '</body>\n</html>'
    
    return header, footer

def update_page(file_path, header, footer):
    content = read_file(file_path)
    soup = BeautifulSoup(content, 'html.parser')
    
    # Get the main content (everything between nav and footer)
    main_content = ''
    main_tag = soup.find('main')
    if main_tag:
        main_content = str(main_tag)
    else:
        # If no main tag, get content between nav and footer
        nav = soup.find('nav', class_='main-nav')
        footer_tag = soup.find('footer')
        if nav and footer_tag:
            current = nav.next_sibling
            while current and current != footer_tag:
                if hasattr(current, 'name'):
                    main_content += str(current)
                current = current.next_sibling
    
    # Create new page content
    new_content = header + '\n<main>\n' + main_content + '\n</main>\n' + footer
    
    # Update image paths
    new_content = new_content.replace('src="images/', 'src="assets/images/')
    
    write_file(file_path, new_content)

def main():
    # Get header and footer from index.html
    header, footer = get_header_footer()
    
    # List of pages to update
    pages = [
        # Main Pages
        'about.html',
        'mission.html',
        'contact.html',
        
        # Office Bearers
        'office-bearers/current.html',
        'office-bearers/past-presidents.html',
        
        # Education & Training
        'education/research-workshops.html',
        'education/conferences.html',
        'education/neurological-emergencies.html',
        'education/future-conference.html',
        
        # Guidelines
        'guidelines/epilepsy.html',
        'guidelines/stroke.html',
        'guidelines/alzheimers.html',
        'guidelines/parkinsons.html',
        
        # Other Pages
        'pjns.html',
        'gallery.html',
        'resources.html',
        'events.html',
        'news.html',
        'articles.html',
        'projects.html',
        'forum.html'
    ]
    
    # Update each page
    for page in pages:
        if os.path.exists(page):
            print(f"Updating {page}...")
            update_page(page, header, footer)
            print(f"Updated {page}")

if __name__ == "__main__":
    main() 