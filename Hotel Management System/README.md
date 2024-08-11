## Project Objective:
The Objective is to provide user with an easy system of a hotel through which he/she can attend guests and get information and also contains a restaurant billing system so they can manage hotel easily

## Project Description:
In this project user need to first login as the data security of guests are really important. Then he gets to choose between weather he needs to see information of guest check-in or check-out and finally exit when his shift ends.

## Project Tool and IDE:
The Project is written in Python and is developed on Python Integrated Development Environment “Vs code” and  we use “mysql” for the database connectivity

## Admin Login Info:
- Username: admin
- Password: admin

## Screenshots

![Alt text](https://github.com/MateenMureed/sms-school-management-system-/blob/main/Hotel%20Management%20System/Picture2.png))
![Alt text](https://github.com/MateenMureed/sms-school-management-system-/blob/main/Hotel%20Management%20System/Picture3.png))
![Alt text](https://github.com/MateenMureed/sms-school-management-system-/blob/main/Hotel%20Management%20System/Picture4.png))
![Alt text](https://github.com/MateenMureed/sms-school-management-system-/blob/main/Hotel%20Management%20System/Picture5.png))

## Database Setup for HOTEL

This section describes how to set up the database and create the necessary table.

### 1. Create the Database

```sql
CREATE DATABASE HOTEL;
USE HOTEL;
CREATE TABLE PI (
    NAME VARCHAR(32),
    GENDER VARCHAR(10),
    ADDRESS VARCHAR(40),
    AGE VARCHAR(40),
    CNIC VARCHAR(32),
    PHONE VARCHAR(11),
    ROOM_NO INT,
    RESERVATION_DATE DATE,
    HOW INT,
    AMOUNT INT,
    P_METHOD VARCHAR(30),
    CARD_NO VARCHAR(30),
    PRIMARY KEY (CNIC)
);


