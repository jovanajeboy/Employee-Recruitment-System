# Employee Recruitment System

## Overview

The Employee Recruitment System is a Python-based application that streamlines the recruitment process by connecting job candidates with recruiters through a MySQL database. The system provides separate interfaces for administrators and candidates, allowing efficient management of vacancies, candidate information, and interview scheduling.

This project demonstrates the use of Python programming, database management, CRUD operations, user authentication, and workflow automation.

---

## Features

### Administrator Features

* Admin login and signup
* Add and manage job vacancies
* View and filter candidate profiles
* Shortlist candidates based on qualifications and experience
* Schedule interviews
* Update candidate interview status

### Candidate Features

* Candidate login and signup
* Create and manage candidate profiles
* Update personal and educational information
* View available vacancies
* Check interview status and interview details

---

## Technologies Used

* Python
* MySQL
* MySQL Connector for Python
* SQL
* Command Line Interface (CLI)

---

## Database Structure

### Tables

#### loginad

Stores administrator login credentials.

| Column  | Type    |
| ------- | ------- |
| adminid | INT     |
| pass    | VARCHAR |

#### logincd

Stores candidate login credentials.

| Column | Type    |
| ------ | ------- |
| candid | INT     |
| pass   | VARCHAR |

#### vacancies

Stores vacancy information.

| Column     | Type    |
| ---------- | ------- |
| vacid      | INT     |
| org_name   | VARCHAR |
| post       | VARCHAR |
| min_exp    | INT     |
| max_salary | DECIMAL |

#### candidate

Stores candidate information and interview details.

| Column     | Type    |
| ---------- | ------- |
| candid     | INT     |
| candname   | VARCHAR |
| gender     | VARCHAR |
| birthdate  | DATE    |
| state      | VARCHAR |
| university | VARCHAR |
| branch     | VARCHAR |
| degree     | VARCHAR |
| experience | INT     |
| status     | VARCHAR |
| vacid      | INT     |
| idate      | DATE    |
| iloc       | VARCHAR |

---

## Installation

### Prerequisites

* Python 3.x
* MySQL Server
* mysql-connector-python package

### Install Dependency

```bash
pip install mysql-connector-python
```

### Configure MySQL

Update the connection details in the code if your MySQL credentials differ:

```python
host='localhost'
user='root'
passwd='root'
```

### Run the Program

```bash
python employee_recruitment_system.py
```

---

## Workflow

1. Start the application.
2. Choose Admin or Candidate mode.
3. Login or create an account.
4. Admins can add vacancies and schedule interviews.
5. Candidates can create profiles, update details, and view vacancies.
6. Selected candidates can view interview information through the system.

---

## Learning Outcomes

This project demonstrates:

* Python programming fundamentals
* Functions and modular programming
* MySQL database integration
* SQL queries and relational databases
* CRUD operations
* User authentication systems
* Input validation
* Recruitment workflow management

---

## Future Improvements

* Password hashing using bcrypt
* Graphical User Interface (GUI)
* Resume upload functionality
* Email notifications for interview scheduling
* Search and filtering enhancements
* Web-based implementation using Flask or Django
* Candidate ranking and recommendation system

---

## Author

Developed as an academic project to explore database-driven application development using Python and MySQL.
