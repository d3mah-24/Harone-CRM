# Harone

Harone CRM

## Table of Contents

- [Harone](#Harone)
  - [Table of Contents](#table-of-contents)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)

## Prerequisites

Before you begin, ensure that you have the following prerequisites installed on your system:

- Python 3.x: Make sure you have Python 3.x installed. You can download it from the official [Python website](https://www.python.org/downloads/).

## Installation

Follow these steps to set up the Django Installation Project on your local machine:

1. **Clone the Repository**:

   - Clone this repository to your local machine using the following command:

     ```bash
     git clone https://github.com/d3mah-24/Harone-CRM.git

     ```

2. **Navigate to the Project Directory**

   - Before you start working with Django, navigate to the project directory:

     ```bash
     cd Harone
     ```

3. **Creating a Virtual Environment**

   - On macOS and Linux

     ```bash
     python3 -m venv venv
     ```

   - On Windows

     ```bash
     python -m venv venv
     ```

4. **Activate the virtual environment**

   - On macOS and Linux

     ```bash
     source venv/bin/activate
     ```

   - On Windows

     ```bash
     .\venv\Scripts\activate.bat
     ```

5. **Install Requirements**

   - Install Django and other required packages for the project:

     ```bash
     pip install -r requirements.txt
     ```

6. **Setting Up the Database**

   - Create the database tables:

     ```bash
     python manage.py migrate
     ```

   - Create a superuser:

     ```bash
     python manage.py createsuperuser
     ```

7. **Usage**

   - Run the development server:

     ```bash
     python manage.py runserver
     ```
