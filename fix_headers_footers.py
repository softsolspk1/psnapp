import re
import os

# Pages to update
pages_to_update = [
    'projects.html',
    'research.html',
    'articles.html'
]

def get_dashboard_header_footer():
    with open('dashboard.html', 'r', encoding='utf-8') as f:
        dashboard_content = f.read()
        
    # Extract header (from DOCTYPE to end of nav)
    header_pattern = r'<!DOCTYPE html>.*?</nav>'
    header = re.search(header_pattern, dashboard_content, re.DOTALL).group(0)
    
    # Extract footer (from footer tag to end of body)
    footer_pattern = r'<footer.*?</body>\s*</html>'
    footer = re.search(footer_pattern, dashboard_content, re.DOTALL).group(0)
    
    return header, footer

def create_publications_page(header, footer):
    publications_content = f'''{header}
    
    <!-- Main Content -->
    <main class="py-5">
        <div class="container">
            <!-- Page Title -->
            <div class="row mb-5">
                <div class="col-12 text-center">
                    <h1 class="display-4 mb-3">Publications</h1>
                    <p class="lead">Scientific publications and research papers from PSN members</p>
                </div>
            </div>

            <!-- Publications Categories -->
            <div class="row mb-4">
                <div class="col-md-4 mb-4">
                    <div class="card h-100">
                        <div class="card-body">
                            <h5 class="card-title">Journal Articles</h5>
                            <p class="card-text">Peer-reviewed research papers published in medical journals.</p>
                            <a href="#journalArticles" class="btn btn-primary">View Articles</a>
                        </div>
                    </div>
                </div>
                <div class="col-md-4 mb-4">
                    <div class="card h-100">
                        <div class="card-body">
                            <h5 class="card-title">Conference Papers</h5>
                            <p class="card-text">Papers presented at national and international conferences.</p>
                            <a href="#conferencePapers" class="btn btn-primary">View Papers</a>
                        </div>
                    </div>
                </div>
                <div class="col-md-4 mb-4">
                    <div class="card h-100">
                        <div class="card-body">
                            <h5 class="card-title">Books & Chapters</h5>
                            <p class="card-text">Published books and book chapters by PSN members.</p>
                            <a href="#books" class="btn btn-primary">View Books</a>
                        </div>
                    </div>
                </div>
            </div>

            <!-- Recent Publications -->
            <div class="row mb-5">
                <div class="col-12">
                    <h2 class="h3 mb-4">Recent Publications</h2>
                    <div class="table-responsive">
                        <table class="table table-hover">
                            <thead>
                                <tr>
                                    <th>Title</th>
                                    <th>Authors</th>
                                    <th>Journal/Publisher</th>
                                    <th>Year</th>
                                    <th>Actions</th>
                                </tr>
                            </thead>
                            <tbody>
                                <tr>
                                    <td>
                                        <a href="#" class="text-primary">Neurological Manifestations of COVID-19 in Pakistan</a>
                                    </td>
                                    <td>Khan M, et al.</td>
                                    <td>Pakistan Journal of Neurology</td>
                                    <td>2024</td>
                                    <td>
                                        <button class="btn btn-sm btn-outline-primary">View PDF</button>
                                    </td>
                                </tr>
                                <tr>
                                    <td>
                                        <a href="#" class="text-primary">Stroke Management Guidelines: A Pakistani Perspective</a>
                                    </td>
                                    <td>Ahmed S, et al.</td>
                                    <td>International Neurology Journal</td>
                                    <td>2024</td>
                                    <td>
                                        <button class="btn btn-sm btn-outline-primary">View PDF</button>
                                    </td>
                                </tr>
                            </tbody>
                        </table>
                    </div>
                </div>
            </div>

            <!-- Submit Publication -->
            <div class="row">
                <div class="col-12">
                    <div class="card bg-light">
                        <div class="card-body">
                            <div class="row align-items-center">
                                <div class="col-md-8">
                                    <h2 class="h4">Submit Your Publication</h2>
                                    <p>Share your research publications with the neurology community.</p>
                                    <button class="btn btn-primary" data-bs-toggle="modal" data-bs-target="#submitPublicationModal">
                                        Submit Publication
                                    </button>
                                </div>
                                <div class="col-md-4 text-center">
                                    <img src="assets/images/publications/submit-publication.png" alt="Submit Publication" class="img-fluid">
                                </div>
                            </div>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </main>

    <!-- Submit Publication Modal -->
    <div class="modal fade" id="submitPublicationModal" tabindex="-1">
        <div class="modal-dialog modal-lg">
            <div class="modal-content">
                <div class="modal-header">
                    <h5 class="modal-title">Submit Publication</h5>
                    <button type="button" class="btn-close" data-bs-dismiss="modal"></button>
                </div>
                <div class="modal-body">
                    <form>
                        <div class="mb-3">
                            <label class="form-label">Publication Title</label>
                            <input type="text" class="form-control" required>
                        </div>
                        <div class="mb-3">
                            <label class="form-label">Authors</label>
                            <input type="text" class="form-control" placeholder="Separate multiple authors with commas" required>
                        </div>
                        <div class="row mb-3">
                            <div class="col-md-6">
                                <label class="form-label">Publication Type</label>
                                <select class="form-select" required>
                                    <option value="">Select Type</option>
                                    <option>Journal Article</option>
                                    <option>Conference Paper</option>
                                    <option>Book Chapter</option>
                                    <option>Book</option>
                                </select>
                            </div>
                            <div class="col-md-6">
                                <label class="form-label">Publication Year</label>
                                <input type="number" class="form-control" required>
                            </div>
                        </div>
                        <div class="mb-3">
                            <label class="form-label">Journal/Publisher</label>
                            <input type="text" class="form-control" required>
                        </div>
                        <div class="mb-3">
                            <label class="form-label">Abstract</label>
                            <textarea class="form-control" rows="4" required></textarea>
                        </div>
                        <div class="mb-3">
                            <label class="form-label">Upload PDF</label>
                            <input type="file" class="form-control" accept=".pdf" required>
                        </div>
                    </form>
                </div>
                <div class="modal-footer">
                    <button type="button" class="btn btn-secondary" data-bs-dismiss="modal">Cancel</button>
                    <button type="submit" class="btn btn-primary">Submit Publication</button>
                </div>
            </div>
        </div>
    </div>
    {footer}'''

    with open('publications.html', 'w', encoding='utf-8') as f:
        f.write(publications_content)
    print("Created publications.html successfully")

def update_page(page_path, header, footer):
    try:
        with open(page_path, 'r', encoding='utf-8') as f:
            content = f.read()
        
        # Replace header
        content = re.sub(r'<!DOCTYPE html>.*?</nav>', header, content, flags=re.DOTALL)
        
        # Replace footer
        content = re.sub(r'<footer.*?</body>\s*</html>', footer, content, flags=re.DOTALL)
        
        # Fix missing images in articles.html
        if page_path == 'articles.html':
            content = content.replace('src="missing-image.jpg"', 'src="assets/images/articles/article-placeholder.jpg"')
            content = content.replace('src=""', 'src="assets/images/articles/article-placeholder.jpg"')
            content = content.replace('src="assets/images/submit-article.png"', 'src="assets/images/articles/submit-article.png"')
        
        with open(page_path, 'w', encoding='utf-8') as f:
            f.write(content)
            
        print(f"Updated {page_path} successfully")
        
    except Exception as e:
        print(f"Error updating {page_path}: {str(e)}")

def main():
    # Get header and footer from dashboard
    header, footer = get_dashboard_header_footer()
    
    # Create publications page
    create_publications_page(header, footer)
    
    # Update each page
    for page in pages_to_update:
        update_page(page, header, footer)

if __name__ == "__main__":
    main() 