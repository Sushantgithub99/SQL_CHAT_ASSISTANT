import sqlite3

# Database file
DATABASE_FILE = "D://Saffer//Data Science//Machine Learning Projects//Chat assistant//Chat_Assistant_DeepseekAPI//Database//company.db"

def create_database():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    
    # Create Employees table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Employees (
            ID INTEGER PRIMARY KEY,
            Name TEXT NOT NULL,
            Department TEXT NOT NULL,
            Salary INTEGER NOT NULL,
            Hire_Date TEXT NOT NULL
        )
    ''')
    
    # Create Departments table
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS Departments (
            ID INTEGER PRIMARY KEY,
            Name TEXT NOT NULL,
            Manager TEXT NOT NULL
        )
    ''')
    
    conn.commit()
    conn.close()

def insert_data():
    conn = sqlite3.connect(DATABASE_FILE)
    cursor = conn.cursor()
    
    # Insert data into Departments
    departments = [
        (1, 'HR', 'Alice Johnson'),
        (2, 'Finance', 'Bob Smith'),
        (3, 'IT', 'Charlie Brown'),
        (4, 'Marketing', 'David White'),
        (5, 'Sales', 'Emily Green')
    ]
    cursor.executemany("INSERT OR IGNORE INTO Departments VALUES (?, ?, ?)", departments)
    
    # Insert data into Employees
    employees = [
        (1, 'John Doe', 'HR', 50000, '2020-01-15'),
        (2, 'Jane Smith', 'Finance', 60000, '2019-03-22'),
        (3, 'Mike Brown', 'IT', 70000, '2021-06-10'),
        (4, 'Emma Wilson', 'Marketing', 55000, '2018-07-19'),
        (5, 'Chris Evans', 'Sales', 65000, '2017-11-25'),
        (6, 'Sophia Miller', 'HR', 52000, '2020-05-03'),
        (7, 'Daniel Martinez', 'Finance', 62000, '2019-09-12'),
        (8, 'Olivia Taylor', 'IT', 71000, '2021-02-28'),
        (9, 'James Anderson', 'Marketing', 53000, '2016-08-07'),
        (10, 'Mia Thomas', 'Sales', 67000, '2015-10-30'),
        (11, 'Lucas White', 'HR', 51000, '2022-01-20'),
        (12, 'Liam Harris', 'Finance', 63000, '2020-04-17'),
        (13, 'Ava King', 'IT', 72000, '2019-12-05'),
        (14, 'Ethan Scott', 'Marketing', 56000, '2021-07-21'),
        (15, 'Charlotte Lewis', 'Sales', 68000, '2018-03-11')
    ]
    cursor.executemany("INSERT OR IGNORE INTO Employees VALUES (?, ?, ?, ?, ?)", employees)
    
    conn.commit()
    conn.close()

if __name__ == "__main__":
    create_database()
    insert_data()
    print("Database and tables created with sample data.")
