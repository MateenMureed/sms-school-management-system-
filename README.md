# School Management System

## Description

School Management System is made by using TKINTER library which is Graphical User Interface library. The program is working by making modules . The  first window will appear for login after login main lobby window will open from which you can select student registration, staff registration ,student fee management and staff payroll system.

## School Management System has following features.
- Login System
- Student Registration
- Student Fee Management
- Staff Registration
- Staff Payroll Management

## OOP and Python Concept Used:
- Abstraction
- Single Inheritance
- Multilevel Inheritance
- Exception Handling
- Classes and objects
- For Loop
- If Else Conditions

## Fee Management System Features:
- Student data can be fetched from student record.
- Receipt will be generating and can be display in the tkinter window.
- Receipt will be saved as pdf in Fee Receipt folder(automatically will be create when you run the program).
- Previous Month dues will be added in the next month dues.
- Previous Month dues will be cleared if parent pay the fee.
- Fee data will be saved in database.
  
## Payroll Management System Features:
- Staff data will be fetched from staff record.
- There pays slip will generate.
- There is a loan and advance salary deduction system if staff get loan or advance salary.
- Receipt will be saved as pdf in Salary Receipt folder(auto create folder when program run)
- Pay slip data will be saved in data.

## Technologies Used
- **Languages:** Python
- **Libraries/Frameworks:** Tkinter
- **Tools/Platforms:** VS Code, MySQL Workbench
- **Databases:** MySQL

## Screenshots

Here are some screenshots of the School Management System:

### Main Interface
![Main Interface](https://github.com/MateenMureed/sms-school-management-system-/blob/main/Picture1.png)
![Student Records](https://github.com/MateenMureed/sms-school-management-system-/blob/main/Picture2.png)
![Fee Management](https://github.com/MateenMureed/sms-school-management-system-/blob/main/Picture3.png)
![Payroll Management](https://github.com/MateenMureed/sms-school-management-system-/blob/main/Picture4.png)

## Installation

To set up the School Management System locally, follow these steps:

1. Clone the repository:
    ```bash
    git clone https://github.com/yourusername/school-management-system.git](https://github.com/MateenMureed/sms-school-management-system-.git
    cd school-management-system
    ```

2. Install the required Python packages:
    ```bash
    pip install -r requirements.txt
    ```

3. Set up the MySQL database:
    - Create a MySQL database and write these querries
    - # School Management System Database Schema

## Table Definitions

### `MySQL Querries`
```sql
CREATE TABLE try_data (
    ID INT AUTO_INCREMENT,
    F_Name VARCHAR(20),
    L_Name VARCHAR(20),
    Email VARCHAR(32) UNIQUE CHECK (Email LIKE '%_@__%.__%'),
    Password VARCHAR(40),
    Phone VARCHAR(11),
    Gender VARCHAR(5),
    PRIMARY KEY (ID)
);

CREATE TABLE student_data (
    ID INT NOT NULL,
    Class VARCHAR(15),
    Std_Name VARCHAR(40),
    Father_Name VARCHAR(40),
    Gender VARCHAR(5) CHECK (Gender IN ('Male', 'Female', 'male', 'female')),
    DOB DATE,
    Email VARCHAR(32) UNIQUE CHECK (Email LIKE '%_@__%.__%'),
    Phone VARCHAR(11),
    Address VARCHAR(60),
    Image NVARCHAR(255),
    Fee VARCHAR(40),
    PRIMARY KEY (ID)
);


CREATE TABLE fee (
    ID INT REFERENCES student_data(ID),
    Receipt_No INT,
    Std_Name VARCHAR(32),
    Class VARCHAR(15),
    Fee_Month VARCHAR(20),
    Pay_Date DATE,
    Total VARCHAR(100),
    Paid VARCHAR(100),
    Balance VARCHAR(100),
    PRIMARY KEY (Receipt_No)
);

CREATE TABLE staff_registration (
    ID INT,
    Staff_Name VARCHAR(30),
    Role VARCHAR(20),
    DOB DATE,
    Joining_Date DATE,
    Gender VARCHAR(5) CHECK (Gender IN ('Male', 'Female', 'male', 'female')),
    Email VARCHAR(32) UNIQUE CHECK (Email LIKE '%_@__%.__%'),
    CNIC VARCHAR(19) CHECK (CNIC LIKE '_____-_______-_'),
    Address VARCHAR(60),
    Image NVARCHAR(255),
    UNIQUE (CNIC),
    Account_No VARCHAR(40) UNIQUE,
    Phone VARCHAR(11),
    PRIMARY KEY (ID)
);

CREATE TABLE payroll (
    Receipt_no INT NOT NULL AUTO_INCREMENT,
    ID INT REFERENCES staff_registration(ID),
    Staff_Name VARCHAR(30),
    Role VARCHAR(20),
    Joining_Date DATE,
    Account_No VARCHAR(40),
    Cur_Date DATE,
    Basic VARCHAR(250),
    Month VARCHAR(15) CHECK (Month != 'Month'),
    Medical VARCHAR(100),
    House VARCHAR(100),
    Conveyance VARCHAR(100),
    Tax VARCHAR(100),
    Loan VARCHAR(100),
    Add_Salary VARCHAR(100),
    Gross VARCHAR(100),
    Net VARCHAR(100),
    getloan VARCHAR(255),
    getadvance VARCHAR(255),
    PRIMARY KEY (Receipt_no)
);
'''
