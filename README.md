# Django-MicroBlog

[![Python Version](https://img.shields.io/badge/python-v3.8-brightgreen.svg)](https://python.org)
[![Django Version](https://img.shields.io/badge/django-3.1-blue.svg)](https://djangoproject.com)
[![Bootstrap Version](https://img.shields.io/badge/bootstrap-4.5-blueviolet.svg)](https://getbootstrap.com/)
[![Ckeditor Version](https://img.shields.io/badge/ckeditor-6-red.svg)](https://ckeditor.com/)

## Description: 
Simple Blog application created using Django Framework.

## Installation
1. To run the website you will have to [install django](https://docs.djangoproject.com/en/3.1/topics/install/).After installing django, I recommend to create a virtual environment for your project, and activate it using this command.
```bash
   $ python3 -m venv _virtual_enviroment_name_
   $ source _virtual_enviroment_name_/bin/activate
   (_virtual_enviroment_name_) $ your_directory 
   ```
2. After creating virtual environments, install all package requirements from **_requirements.txt_**
 ```bash
   $ pip install -r requirements.txt
   ``` 
3. Clone the project in your personal directory, and change directory to website folder.
4. Project contains 2 applications accounts, posts so in case any database errors run migrations on them, using these commands.
```bash
   $ python manage.py makemigrations accounts
   $ python manage.py makemigrations posts
   ```
5. Run the project using following django command.
```bash
   $ python manage.py runserver
   $ Watching for file changes with StatReloader
     Performing system checks...
     System check identified no issues (0 silenced).
     October 01, 2020 - 00:06:54
     Django version 3.1.1, using settings 'microblog.settings'
     Starting development server at http://127.0.0.1:8000/
     Quit the server with CONTROL-C.
```
6. The project will be available at **127.0.0.1:8000** in your browser.

## Credits:
   * The website can be found live at http://microblog76.pythonanywhere.com/

## License: 
   * [![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
   
   
   
   
   
   
   
   
