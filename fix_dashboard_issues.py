import re

def fix_dashboard_issues(content):
    # 1. Fix slider structure
    slider_pattern = r'<section class="hero-section">.*?</section>'
    fixed_slider = '''<section class="hero-section">
        <div class="owl-carousel hero-slider">
            <div class="item">
                <img src="assets/images/slider/research.jpg" alt="PSN Research">
                <div class="carousel-caption">
                    <h2>Advancing Neurological Research</h2>
                    <p>Leading the way in neurological research and innovation</p>
                    <a href="#" class="btn">Explore Research</a>
                </div>
            </div>
            <div class="item">
                <img src="assets/images/slider/education.jpg" alt="PSN Education">
                <div class="carousel-caption">
                    <h2>Education & Training Programs</h2>
                    <p>Empowering the next generation of neurologists</p>
                    <a href="#" class="btn">View Programs</a>
                </div>
            </div>
        </div>
    </section>'''
    content = re.sub(slider_pattern, fixed_slider, content, flags=re.DOTALL)

    # 2. Fix Home menu link
    content = re.sub(
        r'<a class="nav-link active" href="[^"]*">Home</a>',
        '<a class="nav-link active" href="dashboard.html">Home</a>',
        content
    )

    # 3. Remove Pak Neurology Network name from header
    content = re.sub(
        r'<div class="brand-text">\s*<h1[^>]*>Pak Neurology Network</h1>\s*</div>',
        '',
        content
    )

    return content

try:
    # Read dashboard.html
    with open('dashboard.html', 'r', encoding='utf-8') as f:
        content = f.read()
    
    # Apply fixes
    updated_content = fix_dashboard_issues(content)
    
    # Write back to file
    with open('dashboard.html', 'w', encoding='utf-8') as f:
        f.write(updated_content)
        
    print("Successfully updated dashboard.html")
    
except Exception as e:
    print(f"Error updating dashboard.html: {str(e)}") 