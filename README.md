*  Overview
    Django’s default admin interface is powerful but visually basic. By customizing the admin templates and applying Bootstrap 5 styling, you can:
      *** Enhance the UI/UX with a modern design.
      *** Make the admin interface responsive for various devices.
      *** Customize forms, buttons, and layout using Bootstrap utilities.
      *** Maintain full Django admin functionality while improving aesthetics.

*  Features
    *** Custom base admin template extending admin/base_site.html.
    *** Usage of Bootstrap 5 CSS classes for buttons, forms, navigation, and layout.
    *** Customized list views and form views with Bootstrap styling.
    *** Responsive admin interface adjustments.
    *** Example snippets of template overrides for login, dashboard, change list, and change form pages.

*  Getting Started

  **  Prerequisites
    *** Python 3.x
    *** Django 3.x or 4.x
    *** Bootstrap 5 (included via CDN or locally)

*  Installation
  1) Clone this repository:
  
     git clone https://github.com/your-username/django-admin-bootstrap5.git
     cd django-admin-bootstrap5
  
  2) Create and activate a virtual environment (optional but recommended):

     python -m venv venv
     source venv/bin/activate  # Linux/macOS
     venv\Scripts\activate     # Windows
  
  3) Install dependencies:

      pip install -r requirements.txt
  
  4) Run migrations and start the server:
    
      python manage.py migrate
      python manage.py createsuperuser  # create admin user
      python manage.py runserver
  
  5) Access the admin panel at:

      http://localhost:8000/admin/

*  Usage

  *** The Bootstrap 5 CSS is linked in the overridden admin/base_site.html.
  *** Custom templates reside in your project’s templates/admin/ directory.
  *** Override specific admin templates as needed (e.g., change_list.html, change_form.html, login.html).
  *** Apply Bootstrap 5 classes to buttons, forms, tables, and navigation elements in the template files.
