🌐 Portfolio WebsiteProject Overview.
 This is a professional, dynamic portfolio website built using the Django framework to manage content (projects, skills, services) via an admin interface and styled with a responsive Bootstrap template for a modern, clean look.It serves as a single source of truth for all professional work, allowing easy updates without touching the front-end code.
[<img width="2561" height="1399" alt="portfolio" src="https://github.com/user-attachments/assets/d8f82171-091a-44e7-99ae-73abe9daad59" />](https://nailabashir.pythonanywhere.com/)

# ✨ Features
Dynamic Content Management: All portfolio items (projects, skills, services) are managed through the Django Admin Panel.
Fully Responsive Design: Uses a Bootstrap template to ensure optimal viewing on desktop, tablet, and mobile devices.
Contact Form: Integrated Django forms for receiving inquiries directly to the site administrator's email.
Templating: Uses Django Template Language (DTL) for rendering data pulled from the database.
# ⚙️ Tech Stack
Backend Framework: Django (Python)Frontend Styling: Bootstrap (CSS/JS Framework)Database: SQLite (default for development), extensible to PostgreSQL/MySQL for production.
Deployment: Designed to be easily deployable on services like Heroku, AWS, or DigitalOcean.
# 🚀 Installation and Local Setup
Follow these steps to get a copy of the project running on your local machine for development and testing.
Prerequisites
Python 3.8+pip (Python package installer)
# Steps
Clone the Repositorygit clone [https://github.com/your-username/your-portfolio-repo.git](https://github.com/your-username/your-portfolio-repo.git)
cd your-portfolio-repo
Create and Activate Virtual EnvironmentIt's highly recommended to use a virtual environment to manage dependencies.
# Create the environment (Linux/macOS)
python3 -m venv venv
source venv/bin/activate

# Create the environment (Windows)
 python -m venv venv
venv\Scripts\activate
Install Dependencies
Database Migrations
Set up the initial database structure:
python manage.py makemigrations
python manage.py migrate
Create a SuperuserCreate an admin user to access the dynamic content management system (Django Admin).python manage.py createsuperuser
# Follow the prompts to set username, email, and password
Run the Development ServerStart the local server:python manage.py runserver
The site will be accessible at: http://127.0.0.1:8000/
# 👨‍💻 Content Management 
(Django Admin)To add projects, update skills, or change services:
Navigate to the Django Admin interface: http://127.0.0.1:8000/admin/Log in using the superuser credentials you created.
You will find models (e.g., Projects, Skills, services) listed where you can add, edit, or delete portfolio entries.
# 🤝 Contributing
This is primarily a personal portfolio project, but if you notice any issues or have suggestions for improvements, feel free to open an issue or submit a pull request!.
