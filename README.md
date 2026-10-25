# OrbitHub

**Secure document sharing platform by Cyberhub Solutions and Systems Ltd**

OrbitHub is a web application designed for professional and secure exchange of company documents — including profiles, EHS plans, compliance policies, and proposals — with clients.

---

## Overview

OrbitHub provides a clean, modern interface for organizations to share sensitive business documents in a controlled and professional manner. Built with simplicity and reliability in mind, it currently serves as the company web presence and is being expanded into a full document management and sharing platform.

**Company:** Cyberhub Solutions and Systems Ltd  
**Registration:** RC 8221971 (Nigeria)

---

## Current Features

- Responsive company website (Home, About Us, Contact)
- Clean, professional branding with OrbitHub logo
- Lightweight and fast Flask-based architecture
- Easy to extend for future document-sharing capabilities

## Planned Features

- Secure user authentication
- Document upload and organized storage
- Controlled sharing links with access control
- Client-specific document portals
- Audit trail and activity logs
- Role-based access (Admin / Client)

---

## Tech Stack

| Layer       | Technology          |
|-------------|---------------------|
| Backend     | Python, Flask       |
| Frontend    | HTML, CSS, Jinja2   |
| Structure   | Templates + Static  |

---

## Project Structure
OrbitHub/
├── app.py                 # Main Flask application
├── templates/
│   ├── base.html          # Base layout
│   ├── index.html         # Home page
│   ├── about_us.html      # About page
│   └── contact_us.html    # Contact page
├── static/
│   └── images/
│       └── logo2.jpg      # OrbitHub logo
├── .gitignore
└── README.md


---

## Getting Started

### Prerequisites
- Python 3.8 or higher
- pip

### Installation

1. Clone the repository:
```bash
git clone https://github.com/sammylofy/OrbitHub.git
cd OrbitHub


---

## Getting Started

### Prerequisites
- Python 3.8 or higher
- pip

### Installation

1. Clone the repository:
```bash
git clone https://github.com/sammylofy/OrbitHub.git
cd OrbitHub

2. (Recommended) Create and activate a virtual environment:

python -m venv venv
# Windows
venv\Scripts\activate
# macOS / Linux
source venv/bin/activate

3. Install dependencies:

pip install flask

4. Run the application:

python app.py

Open your browser and visit:

Available Routes
Route,Description
/,Home page
/about,About Us page
/contact,Contact page

Contributing
This is currently a private company project. For internal contributions or feature suggestions, please contact the development team.

License
Proprietary — All rights reserved.

© 2025 Cyberhub Solutions and Systems Ltd

Contact
Cyberhub Solutions and Systems Ltd

For inquiries related to OrbitHub or business proposals, please use the Contact page on the application.