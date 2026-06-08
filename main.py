import mysql.connector as m
import datetime
import time
import os
import sys

# Connect to MySQL server
mydb = m.connect(host='localhost', user='root', passwd='root')
c = mydb.cursor()

# Create the EMP_RECRUIT database
c.execute("CREATE DATABASE IF NOT EXISTS EMP_RECRUIT")
mydb.close()

# Connect to the EMP_RECRUIT database
d = m.connect(host='localhost', user='root', passwd='root', database='EMP_RECRUIT')
C = d.cursor()

# Create LOGIN/SIGNUP Table for Admin
C.execute("""CREATE TABLE IF NOT EXISTS loginad (
    adminid INT PRIMARY KEY,
    pass VARCHAR(255) NOT NULL)""")

# Create LOGIN/SIGNUP Table for Candidate
C.execute("""CREATE TABLE IF NOT EXISTS logincd (
    candid INT PRIMARY KEY,
    pass VARCHAR(255) NOT NULL)""")
# Create the vacancies table
C.execute("""CREATE TABLE IF NOT EXISTS vacancies(
    vacid INT PRIMARY KEY,
    org_name VARCHAR(30),
    post VARCHAR(30),
    min_exp INT,
    max_salary DECIMAL(10,2))""")
# Create the candidate table with a foreign key referencing the vacancies table
C.execute("""CREATE TABLE IF NOT EXISTS candidate (
 candid INT PRIMARY KEY,
    candname VARCHAR(30),
    gender VARCHAR(30),
    birthdate DATE,
    state VARCHAR(30),
    university VARCHAR(100),
    branch VARCHAR(50),
    degree VARCHAR(50),
    experience INT,
    status VARCHAR(100),
    vacid INT,
    idate DATE,
    iloc VARCHAR(100),
    FOREIGN KEY(vacid)
    REFERENCES vacancies(vacid))""")
d.close()
# Establishing the connection
d = m.connect(host='localhost', user='root', passwd='root', database='EMP_RECRUIT')
C = d.cursor()

# Clear screen function
def clear_screen():
    time.sleep(2)  # Pause for 3 seconds before clearing the screen
    os.system('cls' if os.name == 'nt' else 'clear')

# LOGIN Functions
def admin_login(C, d):
    adminid = input("Enter Admin ID: ")
    password = input("Enter Password: ")
    query1 = "SELECT * FROM loginad WHERE adminid = %s AND pass = %s"
    C.execute(query1, (adminid, password))
    result = C.fetchone()
    if result:
        print("Admin login successful!")
        clear_screen()
        admin(C, d)
    else:
        print("Login failed. Invalid Admin ID or Password.")
        yn = input("Do you want to sign up with these credentials? (YES/NO): ")
        if yn.lower() == "yes":
            query2 = "INSERT INTO loginad (adminid, pass) VALUES (%s, %s)"
            C.execute(query2, (adminid, password))
            d.commit()
            print("You have successfully signed up. Please login again.")
            clear_screen()
            admin_login(C, d)
        else:
            clear_screen()
            main_program()

def candidate_login(C, d):
    candid = input("Enter Candidate ID: ")
    password = input("Enter Password: ")

    query3 = "SELECT * FROM logincd WHERE candid = %s AND pass = %s"
    C.execute(query3, (candid, password))
    result = C.fetchone()

    if result:
        print("Candidate login successful!")
        clear_screen()
        candidate(C, d, candid)
    else:
        print("Login failed. Invalid Candidate ID or Password.")
        yn = input("Do you want to sign up with these credentials? (YES/NO): ")
        if yn.lower() == "yes":
            query4 = "INSERT INTO logincd (candid, pass) VALUES (%s, %s)"
            C.execute(query4, (candid, password))
            d.commit()
            print("You have successfully signed up. Please login again.")
            clear_screen()
            candidate_login(C, d)
        else:
            clear_screen()
            main_program()
    # Admin Function
def admin(C, d):
    print("{:>60}".format("-->>ADMIN PAGE<<--"))
    while True:
        x = int(input("""Choose the following options:
1. Add Vacancy Details
2. Check List of Candidates
3. Back
4. Exit
Enter your option (1/2/3/4): """))
        print(f"User selected option: {x}")
        if x == 1:
            vacancy_details(C, d)
        elif x == 2:
            loc_details(C, d)
        elif x == 3:
            clear_screen()
            main_program()
        elif x == 4:
            print("Thank You for Using Employee Recruitment System!!!")
            d.close()  
            time.sleep(3)
            sys.exit()
        else:
            print("Invalid Entry. Please Try Again")
            clear_screen()
# Candidate Function
def candidate(C, d, candid):
    print("{:>60}".format("-->>CANDIDATE PAGE<<--"))
    while True:
        x = int(input("""Choose the following options:
1. Add Candidate Details
2. Update Details
3. View Vacancies
4. Check Interview Status
5. Back
6. Exit
Enter your option (1/2/3/4/5/6): """))
        if x == 1:
            cand_details(C, d, candid)
        elif x == 2:
            update_details(C, d, candid)
        elif x == 3:

            post = input("Enter desired post: ")
            exp = int(input("Enter your experience (years): "))

            query = """
            SELECT *
            FROM vacancies
            WHERE post = %s
            AND min_exp <= %s
            """

            C.execute(query, (post, exp))

            result = C.fetchall()

            if not result:
                print("No vacancies available.")

            else:
                for row in result:
                    print("\nVacancy ID:", row[0])
                    print("Organization:", row[1])
                    print("Post:", row[2])
                    print("Minimum Experience:", row[3])
                    print("Maximum Salary:", row[4])

            input("\nPress Enter to continue...")
        elif x == 4:
            query6 = "SELECT status, idate, vacid, iloc FROM candidate WHERE candid = %s"
            C.execute(query6, (candid,))
            result = C.fetchone()
            if result and result[0] == "Chosen for Interview":
                print("Congratulations! You are selected for the Interview")
                print(f"Your interview is on {result[1]}")
                print(f"Interview Location is at {result[3]}")
                query7 = "SELECT * FROM vacancies WHERE vacid = %s"
                C.execute(query7, (result[2],))
                vac_info = C.fetchone()
                vacid, org, post, minexp, maxsal = vac_info
                print("Interview for post:")
                print("Vacancy ID:", vacid)
                print("Name of Organization/Company:", org)
                print("Post:", post)
                print("Minimum Experience Required:", minexp)
                print("Maximum Salary:", maxsal)
                print("\n")
                time.sleep(4)
                clear_screen()
            else:
                print("You are not yet chosen for an interview.")
                clear_screen()
        elif x == 5:
            clear_screen()
            main_program()
        elif x == 6:
            print("Thank You for Using Employee Recruitment System!!!")
            d.close()  
            time.sleep(3)
            sys.exit()
        else:
            print("Invalid Choice")
            clear_screen()
# Function to check if DATE format is valid
def parse_date(date_str):
    try:
        return datetime.date.fromisoformat(date_str)
    except ValueError:
        print("Incorrect format for date. Please enter in this format (YYYY-MM-DD)")
        new_date = input("Enter Date: ")
        return parse_date(new_date)

# Function to check if Candidate ID exists
def candid_check(C, candid):
    C.execute("SELECT * FROM candidate WHERE candid = %s", (candid,))
    if C.fetchone():
        return True
    return False
# Function to check if Vacancy ID exists
def vacid_check(C, vacid):
    C.execute("SELECT * FROM vacancies WHERE vacid = %s", (vacid,))
    if C.fetchone():
        return True
    return False
# Function to add candidate details
def cand_details(C, d, candid):
    print("{:>60}".format("-->>Candidate Details<<--"))
    if candid_check(C, candid):
        print("Candidate Id already exists. You can only update your details.")
        x = input("Do you want to update your details? YES/NO: ")
        if x.lower() == "yes":
            update_details(C, d, candid)
        else:
            clear_screen()
            candidate(C, d, candid)
    else:
        p = input("Enter Candidate Name: ")
        g = input("Enter Gender: ")
        while g.lower() not in ["male", "female"]:
            print("Invalid Gender")
            g = input("Enter Gender: ")

        bd = input("Enter Date of Birth: ")
        bd = parse_date(bd)
        s = input("Enter State: ")
        u = input("Enter University of Highest Degree: ")
        br = input("Enter Branch: ")
        dg = input("Enter the highest degree you achieved: ")
        exp = int(input("Enter Years of Experience: "))

        query8 = """INSERT INTO candidate 
(candid, candname, gender, birthdate, state, university, branch, degree, experience, status) 
 VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, 'Applied')"""
        C.execute(query8, (candid, p, g, bd, s, u, br, dg, exp))
        d.commit()
        print("Details added successfully.")
        clear_screen()
        return
# Function to update candidate details
def update_details(C, d, candid):
    print("{:>60}".format("-->>Update Candidate Details<<--"))

    allowed_fields = [
        "state",
        "university",
        "branch",
        "degree",
        "experience"
    ]

    nd = int(input("Enter number of details to change: "))

    for _ in range(nd):

        field = input(
            "Enter field (state/university/branch/degree/experience): "
        ).lower()

        if field not in allowed_fields:
            print("Invalid field.")
            continue

        value = input("Enter new value: ")

        query = f"UPDATE candidate SET {field} = %s WHERE candid = %s"

        C.execute(query, (value, candid))

    d.commit()

    print("Successfully Updated.")
    clear_screen()
# Function to add vacancy details
def vacancy_details(C, d):
    print("{:>60}".format("-->>Add Vacancy Details<<--"))
    vacid = int(input("Enter Vacancy ID: "))
    if vacid_check(C, vacid):
        print("Vacancy ID already exists.")
    else:
        org_name = input("Enter Organization Name: ")
        post = input("Enter Post: ")
        min_exp = int(input("Enter Minimum Experience: "))
        max_salary = float(input("Enter Maximum Salary: "))
        query9 = """INSERT INTO vacancies (vacid, org_name, post, min_exp, max_salary) VALUES (%s, %s, %s, %s, %s)"""
        C.execute(query9, (vacid, org_name, post, min_exp, max_salary))
        d.commit()
        print("Vacancy details added successfully.")
    clear_screen()
    return
# Function to check candidate details
def loc_details(C, d):

    branch = input("Enter Branch: ")

    degree = input(
        "Enter Required Degree: "
    ).lower()

    exp = int(input("Enter Minimum Experience: "))

    degree_hierarchy = [
        "b.sc",
        "b.tech",
        "b.ba",
        "ba",
        "b.e",
        "m.ba",
        "ma",
        "m.sc",
        "m.tech",
        "m.e",
        "ph.d"
    ]

    if degree not in degree_hierarchy:
        print("Invalid Degree")
        return

    degree_index = degree_hierarchy.index(degree)

    higher_degrees = tuple(
        degree_hierarchy[degree_index:]
    )

    placeholders = ",".join(
        ["%s"] * len(higher_degrees)
    )

    query = f"""
    SELECT *
    FROM candidate
    WHERE branch = %s
    AND degree IN ({placeholders})
    AND experience >= %s
    """

    values = (branch, *higher_degrees, exp)

    C.execute(query, values)

    result = C.fetchall()

    if not result:
        print(
            "No candidates with those qualifications."
        )
        return

    count = 1

    for row in result:

        print("\nCandidate No:", count)
        print("Candidate ID:", row[0])
        print("Candidate Name:", row[1])
        print("State:", row[4])
        print("University:", row[5])
        print("Branch:", row[6])
        print("Degree:", row[7])
        print("Experience:", row[8])

        count += 1

    n = int(
        input(
            "\nHow many candidates are selected for interview? "
        )
    )

    for _ in range(n):

        cid = int(input("Candidate ID: "))
        vacid = int(input("Vacancy ID: "))

        idate = parse_date(
            input("Interview Date (YYYY-MM-DD): ")
        )

        iloc = input(
            "Interview Location: "
        )

        query = """
        UPDATE candidate
        SET status=%s,
            vacid=%s,
            idate=%s,
            iloc=%s
        WHERE candid=%s
        """

        C.execute(
            query,
            (
                "Chosen for Interview",
                vacid,
                idate,
                iloc,
                cid
            )
        )

    d.commit()

    print("Interview details updated successfully.")

    clear_screen()
    return
def main_program():
    print("{:>60}".format("-->>WELCOME TO EMPLOYEE RECRUITMENT SYSTEM<<--"))
    while True:
        role = input("Are you an Admin or Candidate? (admin/candidate): ").lower()
        if role == 'admin':
            admin_login(C, d)
        elif role == 'candidate':
            candidate_login(C, d)
        else:
            print("Invalid role. Please try again.")
            clear_screen()
# Start the program
main_program()
