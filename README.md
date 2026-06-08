# Employee-Recruitment-System
The Employee Recruitment System is a command-line interface (CLI) application developed in Python, designed to streamline and automate the recruitment process for both employers (admins) and job candidates.

The Employee Recruitment System is a Python-based application that facilitates the recruitment process for both employers (admins) and candidates. It leverages MySQL as the backend database to store and manage various recruitment-related data, including candidate details, vacancy postings, and interview scheduling. The system is designed to be used through a command-line interface (CLI), providing a straightforward and efficient way to manage recruitment activities.
Key Features
Admin (Employer) Functions:
Add Vacancy Details: Admins can create new job postings by entering details such as the vacancy ID, organization name, required experience, and offered salary. This information is stored in the database and can be retrieved for future reference.
Check List of Candidates: Admins can search for candidates based on specific criteria such as branch, degree, and experience. The system displays a list of candidates that match the search criteria.
Schedule Interviews: Admins can schedule interviews for selected candidates by updating their status and setting an interview date in the system.

Candidate Functions:
Add Candidate Details: Candidates can register their details in the system, including their name, gender, date of birth, educational qualifications, and work experience. The system checks for duplicate candidate IDs to prevent multiple registrations.
Update Details: Candidates can update specific details such as their state, university, branch, degree, and experience. The system ensures that only valid fields are updated.
View Vacancies: Candidates can search for job vacancies that match their qualifications and experience. The system retrieves and displays relevant job postings from the database.
Check Interview Status: Candidates can check the status of their application to see if they have been selected for an interview. If selected, the system displays the interview date.

Implementation Details
Database Connection:
The application uses the mysql.connector library to connect to a MySQL database. The connection is established at the beginning of the script, and a cursor is created to execute SQL queries.

 2. Functions and Logic:
The application is modular, with separate functions handling specific tasks such as adding candidate details, updating records, viewing vacancies, and scheduling interviews.
Input validation is performed to ensure that only valid data is entered into the system, such as correct date formats and appropriate field values.
The application uses SQL queries to interact with the database, retrieving and updating records as needed.
      3. User Interaction:
The user interacts with the system through a series of prompts in the command-line interface. Depending on the role (Admin or Candidate), the user is presented with different options to perform specific tasks.
The system provides feedback to the user, confirming successful operations or alerting them to errors, such as invalid inputs or non-existent records.
