#importing packages
import sqlite3

#connecting to database
conn = sqlite3.connect('school.db')

#creating cursors
c = conn.cursor()

#creating tables (will be commented out after successful completion)

#student table
c.execute("""CREATE TABLE students(
    f_name text,
    l_name text,
    phone integer,
    Class integer,
    address text
)""")

#teacher table
c.execute("""CREATE TABLE teachers(
    f_name text,
    l_name text,
    phone integer,
    email text
)""")

#staff table
c.execute("""CREATE TABLE staffs(
    f_name text,
    l_name text,
    phone integer,
    email text
)""")

#to continiously run the loop.
while True:

    print("Welcome to automated School management system by Miden Topno, class 12 'Science'.")
    print('\n')


    #inputting student data
    #while loop
    i = 1
    while i == 1:
        q1 = str(input("Do you want to input student data? (y/n) "))
        q1 = q1.capitalize()
        q1 = q1[0]
        if ord(q1) == 89:
            i = 1
            first_name = str(input("Enter first name: "))
            last_name = str(input("Enter last name: "))
            phone_number = int(input("Enter Phone Number: "))
            _class = int(input("Enter class: "))
            address = str(input("Enter Address: "))
            student_details = [first_name, last_name, phone_number, _class, address]
            c.execute("INSERT INTO students VALUES(?, ?, ?, ?, ?)", student_details)
            print("student added successfully.")
            print("\n")
        elif ord(q1) == 78:
            i = 0
            print("Okay, moving forward")
        else:
            i = 1
            print("wrong input.")


    #inputting teachers data
    i = 1
    while i == 1:
        q2 = str(input("Do you want to input Teacher data? (y/n) "))
        q2 = q2.capitalize()
        q2 = q2[0]
        if ord(q2) == 89:
            i = 1
            first_name = str(input("Enter first name: "))
            last_name = str(input("Enter last name: "))
            phone_number = int(input("Enter Phone Number: "))
            email = str(input("Enter Email ID: "))
            teacher_details = [first_name, last_name, phone_number, email]
            c.execute("INSERT INTO teachers VALUES(?,?,?,?)", teacher_details)
            print("Teacher added successfully.")
            print("\n")
        elif ord(q2) == 78:
            i = 0
            print("Okay, moving forward")
        else:
            i = 1
            print("wrong input.")


    #inputting staff data
    i = 1
    while i == 1:
        q3 = str(input("Do you want to input Staff data? (y/n) "))
        q3 = q3.capitalize()
        q3 = q3[0]
        if ord(q3) == 89:
            i=1
            first_name = str(input("Enter first name: "))
            last_name = str(input("Enter last name: "))
            phone_number = int(input("Enter Phone Number: "))
            email = str(input("Enter Email ID: "))
            staff_details = [first_name, last_name, phone_number, email]
            c.execute("INSERT INTO staffs VALUES(?,?,?,?)", staff_details)
            print("Staff added successfully.")
            print("\n")
        elif ord(q3) == 78:
            i=0
            print("Okay, moving forward")
        else:
            i=1
            print("wrong input.")

    #fetching student data
    q4 = str(input("Do you want to see student data? (y/n) "))
    q4 = q4.capitalize()
    q4 = q4[0]
    if ord(q4) == 89:
        c.execute("SELECT rowid, * FROM students")
        items = c.fetchall()

        for item in items:
            print(item)

    elif ord(q4) == 78:
        ("Okay, Moving forward")
    else:
        print('wrong input')

    #fetching teacher data
    q5 = str(input("Do you want to see teachers data? (y/n) "))
    q5 = q5.capitalize()
    q5 = q5[0]
    if ord(q5) == 89:
        c.execute("SELECT rowid, * FROM teachers")
        items = c.fetchall()

        for item in items:
            print(item)

    elif ord(q4) == 78:
        ("Okay, Moving forward")
    else:
        print('wrong input')


    #fetching staffs data
    q6 = str(input("Do you want to see staffs data? (y/n) "))
    q6 = q6.capitalize()
    q6 = q6[0]
    if ord(q6) == 89:
        c.execute("SELECT rowid, * FROM staffs")
        items = c.fetchall()

        for item in items:
            print(item)

    elif ord(q4) == 78:
        ("Okay, Thank you for using our automated system.")
    else:
        print('wrong input')

    #student deletation
    q = str(input("Do you want to delete any student record? (Y/N)"))
    q = q.capitalize()
    q = q[0]
    if ord(q) == 89:
        p_name = str(input("Enter the name of student: "))
        c.execute("""DELETE from students 
                    WHERE f_name = "p_name"
                """)
        print(p_name, "student successfully deleted.")

        conn.commit()

    elif ord(q) == 78:
        print("Okay, Thank you for using our automated system.")
    
    else:
        print("Wrong choice.")

    #class deletation
    _d = str(input("Do you want to delete any teacher's record? (Y/N)"))
    _d = _d.capitalize()
    _d = _d[0]
    if ord(_d) == 89:
        d_name = str(input("Enter the name of teacher: "))
        c.execute("""DELETE from students 
                    WHERE f_name = "d_name"
                """)
        print(d_name, "teacher successfully deleted.")
        conn.commit()


    elif ord(_d) == 78:
        print("Okay, Thank you for using our automated system.")
    
    else:
        print("Wrong choice.")

    #Staff deletation
    _s = str(input("Do you want to delete any staff record? (Y/N)"))
    _s = _s.capitalize()
    _s = _s[0]
    if ord(_s) == 89:
        s_name = str(input("Enter the name of staff: "))
        c.execute("""DELETE from students 
                    WHERE f_name = "s_name"
                """)
        print(s_name, "staff successfully deleted.")
        conn.commit()


    elif ord(_s) == 78:
        print("Okay, Thank you for using our automated system.")
    
    else:
        print("Wrong choice.")

    print('\n')
    print("Thank you for using our system. press ctrl+c to exit.")
    print('\n')


#commiting it to Database
conn.commit()

#closing our connection
#it's done by default, but it's best practise to do it explicitely
conn.close()