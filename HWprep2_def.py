def create_table():
    import os
    import sqlite3

    if os.path.exists("prep2.db"):
        os.remove("prep2.db")
    else:
        print("The file does not exist")
    conn = sqlite3.connect('prep2.db')
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    cursor.execute('''CREATE TABLE lecturers (
    lecturer_id INTEGER PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    email TEXT NOT NULL
    );''')
    cursor.execute('''CREATE TABLE courses (
    course_id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_name TEXT NOT NULL,
    lecturer_id INTEGER,
    FOREIGN KEY (lecturer_id) REFERENCES lecturers(lecturer_id)
    );''')
    cursor.execute('''INSERT INTO lecturers (first_name, last_name, email) VALUES
    ('John', 'Doe', 'john.doe@example.com'),
    ('Jane', 'Smith', 'jane.smith@example.com'),
    ('Mary', 'Johnson', 'mary.johnson@example.com'),
    ('James', 'Williams', 'james.williams@example.com'),
    ('Patricia', 'Brown', 'patricia.brown@example.com'),
    ('Robert', 'Jones', 'robert.jones@example.com'),
    ('Michael', 'Garcia', 'michael.garcia@example.com'),
    ('Linda', 'Martinez', 'linda.martinez@example.com'),
    ('Barbara', 'Rodriguez', 'barbara.rodriguez@example.com'),
    ('David', 'Hernandez', 'david.hernandez@example.com'),
    ('Susan', 'Lopez', 'susan.lopez@example.com'),
    ('Joseph', 'Gonzalez', 'joseph.gonzalez@example.com'),
    ('Thomas', 'Wilson', 'thomas.wilson@example.com'),
    ('Sarah', 'Anderson', 'sarah.anderson@example.com'),
    ('Daniel', 'Thomas', 'daniel.thomas@example.com'),
    ('Jessica', 'Taylor', 'jessica.taylor@example.com'),
    ('Mark', 'Moore', 'mark.moore@example.com'),
    ('Nancy', 'Jackson', 'nancy.jackson@example.com'),
    ('Lisa', 'Martin', 'lisa.martin@example.com'),
    ('Paul', 'Lee', 'paul.lee@example.com'),
    ('Steven', 'Perez', 'steven.perez@example.com'),
    ('Carol', 'Thompson', 'carol.thompson@example.com'),
    ('Andrew', 'White', 'andrew.white@example.com'),
    ('Kevin', 'Harris', 'kevin.harris@example.com'),
    ('Emily', 'Sanchez', 'emily.sanchez@example.com'),
    ('George', 'Clark', 'george.clark@example.com'),
    ('Laura', 'Ramirez', 'laura.ramirez@example.com'),
    ('Brian', 'Lewis', 'brian.lewis@example.com'),
    ('Christine', 'Walker', 'christine.walker@example.com'),
    ('Edward', 'Hall', 'edward.hall@example.com'),
    ('Karen', 'Young', 'karen.young@example.com'),
    ('Jason', 'Allen', 'jason.allen@example.com'),
    ('Kimberly', 'King', 'kimberly.king@example.com'),
    ('Charles', 'Wright', 'charles.wright@example.com'),
    ('Donna', 'Scott', 'donna.scott@example.com'),
    ('Matthew', 'Torres', 'matthew.torres@example.com'),
    ('Ashley', 'Nguyen', 'ashley.nguyen@example.com'),
    ('Patrick', 'Hill', 'patrick.hill@example.com'),
    ('Amanda', 'Flores', 'amanda.flores@example.com'),
    ('Justin', 'Green', 'justin.green@example.com'),
    ('Eric', 'Adams', 'eric.adams@example.com'),
    ('Michelle', 'Nelson', 'michelle.nelson@example.com'),
    ('Scott', 'Baker', 'scott.baker@example.com'),
    ('Rachel', 'Gonzales', 'rachel.gonzales@example.com'),
    ('Benjamin', 'Mitchell', 'benjamin.mitchell@example.com'),
    ('Joshua', 'Carter', 'joshua.carter@example.com'),
    ('Deborah', 'Phillips', 'deborah.phillips@example.com'),
    ('Rebecca', 'Evans', 'rebecca.evans@example.com'),
    ('Samuel', 'Edwards', 'samuel.edwards@example.com'),
    ('Kim', 'Collins', 'kim.collins@example.com');
    ''')
    cursor.execute('''INSERT INTO courses (course_name, lecturer_id) VALUES
    ('Mathematics 101', 1),
    ('Physics 101', 2),
    ('Chemistry 101', 3),
    ('Biology 101', 4),
    ('History 101', 5),
    ('Philosophy 101', NULL),
    ('Art History 101', 7),
    ('Music Theory 101', 8),
    ('Computer Science 101', NULL),
    ('Programming 101', 10),
    ('Data Science 101', 11),
    ('Machine Learning 101', NULL),
    ('Artificial Intelligence 101', 13),
    ('Economics 101', 14),
    ('Business 101', NULL),
    ('Accounting 101', 16),
    ('Finance 101', 17),
    ('Marketing 101', NULL),
    ('Sociology 101', 19),
    ('Psychology 101', 20),
    ('Political Science 101', NULL),
    ('Anthropology 101', 22),
    ('English Literature 101', 23),
    ('French Language 101', NULL),
    ('German Language 101', 25),
    ('Spanish Language 101', 26),
    ('Chinese Language 101', NULL),
    ('Japanese Language 101', 28),
    ('Engineering 101', 29),
    ('Mechanical Engineering 101', 30),
    ('Electrical Engineering 101', NULL),
    ('Civil Engineering 101', 32),
    ('Law 101', 33),
    ('Criminal Justice 101', NULL),
    ('Nursing 101', 35),
    ('Medicine 101', 36),
    ('Dentistry 101', NULL),
    ('Pharmacy 101', 38),
    ('Veterinary Science 101', 39),
    ('Architecture 101', NULL),
    ('Design 101', 41),
    ('Interior Design 101', 42),
    ('Fashion Design 101', NULL),
    ('Journalism 101', 44),
    ('Media Studies 101', 45),
    ('Film Studies 101', NULL),
    ('Photography 101', 47),
    ('Graphic Design 101', 48),
    ('Animation 101', NULL),
    ('Theatre Arts 101', 50);''')
    conn.commit()
    conn.close()
