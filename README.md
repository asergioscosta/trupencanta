# TrupEncanta

### Index

- [Description](#description)
- [Requirements](#requirements)
- [Features](#features)
- [Techniques and Technologies Used](#techniques-and-technologies-used)
- [Accessing the Project](#accessing-the-project)
- [Opening and Running the Project](#opening-and-running-the-project)
- [Developers](#developers)

## Description

This system aims to centralize the management of information related to the activities of the TrupEncanta NGO. This includes publishing news related to events and daily activities, presenting the team that makes up TrupEncanta, details about ongoing projects and workshops, established partnerships, a photo gallery telling the organization's timeline, etc. Additionally, the system seeks to enable user interaction, allowing comments, sending emails to the institution, and easy access to important documents of the NGO.

## Requirements

### System Functional Requirements

**`Administrator:`**
- The system must allow logging in.
- The system must allow registering Workshops, News, Teachers, Projects, and Documents.
- The system must allow editing Workshops, News, Teachers, Projects, and Documents.
- The system must allow deleting Workshops, News, Teachers, Projects, and Documents.
- The system must allow storing photos and videos.

**`Administrator and User:`**
- The system must allow commenting on publications.

### Non-functional System Requirements:

- The user interface must be intuitive and easy to use to ensure a good user experience.
- The system must offer an intuitive administration panel so that administrators can easily manage the content and settings of the system.
- The system must be compatible with mobile devices.
- The system must be compatible with major web browsers.
- System data must be stored in compliance with data protection laws.

## Features

1. **Registering News:**
   - The administrator accesses the system through login to register news.
   - The system requests essential information, such as title, description, and relevant dates.
   - After validation, the news is registered in the system.

2. **Editing News:**
   - The administrator accesses the system through login and goes to the desired news.
   - Makes necessary changes and saves the updates.

3. **Deleting News:**
   - The administrator accesses the system through login and goes to the desired news.
   - Selects the news to be removed and confirms deletion.
   - The system updates the database to reflect the removal.

4. **Registering Workshops:**
   - The administrator accesses the system through login and registers new workshops.
   - Includes information such as title, description, and event dates.
   - After validation, the workshop is registered in the system.

5. **Editing Workshops:**
   - The administrator accesses the system through login and goes to the desired workshop.
   - Makes necessary changes and saves the updates.

6. **Deleting Workshops:**
   - The administrator accesses the system through login and goes to the desired workshop.
   - Selects the workshop to be removed and confirms deletion.
   - The system updates the database to reflect the removal.

7. **Registering Teachers:**
   - The administrator accesses the system through login and registers new teachers.
   - Includes information such as name, area of expertise, and contact information.
   - After validation, the teacher is registered in the system.

8. **Editing Teachers:**
   - The administrator accesses the system through login and goes to the profile of the desired teacher.
   - Makes necessary changes and saves the updates.

9. **Deleting Teachers:**
   - The administrator accesses the system through login and goes to the profile of the desired teacher.
   - Selects the teacher to be removed and confirms deletion.
   - The system updates the database to reflect the removal.

10. **Registering Documents:**
    - The administrator accesses the system through login and registers new documents.
    - Includes information such as title, description, and attached file.
    - After validation, the document is registered in the system.

11. **Editing Documents:**
    - The administrator accesses the system through login and goes to the desired document.
    - Makes necessary changes and saves the updates.

12. **Deleting Documents:**
    - The administrator accesses the system through login and goes to the desired document.
    - Selects the document to be removed and confirms deletion.
    - The system updates the database to reflect the removal.

13. **Registering Projects:**
   - The administrator accesses the system through login to register new projects.
   - The system requests essential information, such as title, description, and relevant dates.
   - After validation, the project is registered in the system.

14. **Editing Projects:**
   - The administrator accesses the system through login and goes to the desired project.
   - Makes necessary changes and saves the updates.

15. **Deleting Projects:**
   - The administrator accesses the system through login and goes to the desired project.
   - Selects the project to be removed and confirms deletion.
   - The system updates the database to reflect the removal.

16. **Comments:**
    - The administrator, student, teacher, visitor, and partnership can leave comments on news.
    - Comments are directly associated with the news and can be viewed by all users.

## Techniques and Technologies Used

- **Programming Languages:** ``HTML5``, ``CSS``, ``JavaScript``, ``Python``
- **Development Environment:** ``Visual Studio Code``
- **Framework:** ``Django``
- **Database:** ``PostgreSQL`` (managed with PgAdmin)
- **Version Control Tools:** ``Git`` and ``GitHub``

## Accessing the Project

You can access the project files [by clicking here](https://github.com/asergioscosta/trupencanta/tree/main/trupencanta) or [download it as a zip file](https://github.com/asergioscosta/trupencanta/archive/refs/heads/main.zip).

## Opening and Running the Project

1. Choose or create a folder on your computer where you want to store the project.
2. Create a repository on GitHub or use an existing one.
3. Clone the repository to your local machine using the command `git clone <repository_URL>` in your terminal or Git Bash.
4. Make sure you have Visual Studio Code installed on your computer. If you don't have it, you can download it [here](https://code.visualstudio.com/).
5. Open Visual Studio Code.
6. In the main menu, select "File" -> "Open Folder" and navigate to the directory where you cloned the project.
7. Select the project folder and click "Open".
8. Now you have access to the project files in your development environment.
9. Now, activate the Visual Studio Code terminal. In the top menu, click on `View`.
10. Select `Terminal`.
11. Next to the "+" arrow, choose the option "Command Prompt".
12. With the terminal already open and configured, create a virtual environment using the command `python -m venv venv`.
13. Activate the virtual environment:
    - On Windows: `venv\Scripts\Activate`.
    - On Linux/Mac: `source venv/bin/activate`.
14. Install project dependencies:
    - Django: `pip install django`.
    - psycopg2 (to connect to PostgreSQL): `pip install psycopg2`.
    - django-bootstrap-v5: `pip install django-bootstrap-v5`.
    - Django REST Framework: `pip install djangorestframework`.
15. Check the Django version with the command `python -m django --version`.
16. Check the Python version with the command `python --version`.
17. Start a new Django project with the command `django-admin startproject project-name`.
18. Enter the project directory using the command `cd project-name`.
19. Run initial database migrations with the command `python manage.py makemigrations` and then execute the command `python manage.py migrate`.
20. Create a superuser with the command `python manage.py createsuperuser`.
21. Create a Django application with the command `python manage.py startapp app-name`.
22. Configure the project's `urls.py` file to include the `urls.py` of the application.
23. Create the `templates` directory within the application directory to store the application's HTML templates.
24. Create the `index.html` file within the `templates` directory. This will be the application's home page.
25. Configure the application's `views.py` file to render `index.html`.
26. Create a database named `trupencanta` in PostgreSQL.
27. Configure the `settings.py` file to connect to PostgreSQL, including the database credentials.

Make sure all necessary dependencies are installed and properly configured in your development environment.

## Developers

[<img loading="lazy" src="https://avatars.githubusercontent.com/u/102989796?v=4" width=115>](https://github.com/asergioscosta)