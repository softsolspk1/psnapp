import os
import base64

# Create default avatar SVG
default_avatar = '''
<svg width="200" height="200" viewBox="0 0 200 200" fill="none" xmlns="http://www.w3.org/2000/svg">
    <circle cx="100" cy="100" r="100" fill="#E9ECEF"/>
    <path d="M100 50C111.046 50 120 58.9543 120 70C120 81.0457 111.046 90 100 90C88.9543 90 80 81.0457 80 70C80 58.9543 88.9543 50 100 50Z" fill="#ADB5BD"/>
    <path d="M140 150H60C60 127.909 77.9086 110 100 110C122.091 110 140 127.909 140 150Z" fill="#ADB5BD"/>
</svg>
'''

# Create CSS for chat interface
chat_css = '''
/* Chat Styles */
.chat-container {
    height: calc(100vh - 200px);
    background: #f8f9fa;
    margin-top: -30px;
}

.contacts-header {
    padding: 20px;
    border-bottom: 1px solid #dee2e6;
    background: #fff;
}

.contacts-list {
    height: calc(100vh - 350px);
    overflow-y: auto;
}

.contact-item {
    padding: 15px 20px;
    border-bottom: 1px solid #dee2e6;
    cursor: pointer;
    background: #fff;
    transition: all 0.3s ease;
}

.contact-item:hover {
    background: #f8f9fa;
}

.contact-item.active {
    background: #e9ecef;
}

.chat-header {
    padding: 20px;
    background: #fff;
    border-bottom: 1px solid #dee2e6;
}

.chat-messages {
    height: calc(100vh - 400px);
    overflow-y: auto;
    padding: 20px;
}

.message {
    display: flex;
    align-items: flex-start;
    margin-bottom: 20px;
}

.message.sent {
    flex-direction: row-reverse;
}

.message-avatar {
    width: 40px;
    height: 40px;
    border-radius: 50%;
    margin: 0 10px;
}

.message-content {
    max-width: 70%;
    padding: 10px 15px;
    border-radius: 15px;
    background: #fff;
    box-shadow: 0 1px 2px rgba(0,0,0,0.1);
}

.message.sent .message-content {
    background: #007bff;
    color: #fff;
}

.message.sent .message-content .text-muted {
    color: rgba(255,255,255,0.7) !important;
}

.chat-input {
    padding: 20px;
    background: #fff;
    border-top: 1px solid #dee2e6;
}

.typing-indicator {
    display: none;
    padding: 10px 20px;
}

.typing-dot {
    display: inline-block;
    width: 8px;
    height: 8px;
    margin-right: 4px;
    background: #6c757d;
    border-radius: 50%;
    animation: typing 1s infinite;
}

.typing-dot:nth-child(2) { animation-delay: 0.2s; }
.typing-dot:nth-child(3) { animation-delay: 0.4s; }

@keyframes typing {
    0%, 100% { transform: translateY(0); }
    50% { transform: translateY(-5px); }
}

.online-indicator {
    display: inline-block;
    width: 8px;
    height: 8px;
    background: #28a745;
    border-radius: 50%;
    margin-right: 5px;
}

/* Video Call Styles */
.video-call-container {
    position: relative;
    width: 100%;
    height: 70vh;
    background: #000;
}

.main-video {
    width: 100%;
    height: 100%;
}

.self-video {
    position: absolute;
    top: 20px;
    right: 20px;
    width: 150px;
    height: 150px;
    border-radius: 10px;
    overflow: hidden;
    border: 2px solid #fff;
}

.call-controls {
    position: absolute;
    bottom: 20px;
    left: 50%;
    transform: translateX(-50%);
    display: flex;
    gap: 20px;
}

.call-controls .btn {
    width: 50px;
    height: 50px;
    padding: 0;
    display: flex;
    align-items: center;
    justify-content: center;
}
'''

# Save default avatar for team members
team_members = ['naila-shahbaz', 'muhammad-wasay', 'bashir-soomro', 'khalid-sher', 'sarwar-siddiqui']
for member in team_members:
    with open(f'assets/images/team/{member}.svg', 'w') as f:
        f.write(default_avatar)

# Save default avatar
with open('assets/images/team/default-avatar.svg', 'w') as f:
    f.write(default_avatar)

# Create or update custom.css
with open('assets/css/custom.css', 'a') as f:
    f.write(chat_css)

# Update chat.html to initialize modals properly
with open('chat.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Add modal initialization script
modal_init = '''
    <!-- Initialize Bootstrap modals -->
    <script>
        document.addEventListener('DOMContentLoaded', function() {
            var modals = [].slice.call(document.querySelectorAll('.modal'))
            var modalInstances = modals.map(function(modal) {
                return new bootstrap.Modal(modal)
            })
        })
    </script>
'''

# Insert modal initialization before closing body tag
content = content.replace('</body>', f'{modal_init}\n</body>')

# Save updated chat.html
with open('chat.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("Chat page has been fixed successfully!") 