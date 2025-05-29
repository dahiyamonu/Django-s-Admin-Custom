*  Overview
      Django’s default admin interface is powerful but visually basic. By customizing the admin templates and applying Bootstrap 5 styling, you can:
      1) Enhance the UI/UX with a modern design.
      2) Make the admin interface responsive for various devices.
      3) Customize forms, buttons, and layout using Bootstrap utilities.
      4) Maintain full Django admin functionality while improving aesthetics.

*  Features
      !) Custom base admin template extending admin/base_site.html.
      2) Usage of Bootstrap 5 CSS classes for buttons, forms, navigation, and layout.
      3) Customized list views and form views with Bootstrap styling.
      4) Responsive admin interface adjustments.
      5) Example snippets of template overrides for login, dashboard, change list, and change form pages.

*  Getting Started

  *  Prerequisites
        1) Python 3.x
        2) Django 3.x or 4.x
        3) Bootstrap 5 (included via CDN or locally)

*  Installation
  1) Clone this repository:
  
     git clone https://github.com/dahiyamonu/Django-s-Admin-Custom.git
  
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

  1) The Bootstrap 5 CSS is linked in the overridden admin/base_site.html.
  2) Custom templates reside in your project’s templates/admin/ directory.
  3) Override specific admin templates as needed (e.g., change_list.html, change_form.html, login.html).
  4) Apply Bootstrap 5 classes to buttons, forms, tables, and navigation elements in the template files.
