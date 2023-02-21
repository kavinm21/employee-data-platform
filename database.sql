use employee_db;

CREATE TABLE `employee_db`.`department` (
    department_id INT NOT NULL,
    department_name VARCHAR(45) NULL,
    employee_salary DOUBLE NULL,
    PRIMARY KEY(department_id)
);

CREATE TABLE `employee_db`.`employee` (
    id INT NOT NULL,
    first_name VARCHAR(45) NULL,
    last_name VARCHAR(45) NULL,
    date_of_birth DATE NULL,
    gender CHAR(100) NULL,
    d_id INT NULL,
    employee_role VARCHAR(45) NULL,
    PRIMARY KEY (id),
    FOREIGN KEY (d_id) REFERENCES `employee_db`.`department` (department_id) ON DELETE NO ACTION ON UPDATE NO ACTION
);

CREATE TABLE `employee_db`.`address` (
    e_id INT NOT NULL,
    house_no INT NULL,
    street_name VARCHAR(45) NULL,
    city VARCHAR(45) NULL,
    state VARCHAR(45) NULL,
    country VARCHAR(45) NULL,
    pincode BIGINT(20) NULL,
    FOREIGN KEY (e_id) REFERENCES `employee_db`.`employee` (id)
);

INSERT INTO
    department (department_id, department_name, employee_salary)
VALUES
(100001, 'Technical', 15000);

INSERT INTO
    department (department_id, department_name, employee_salary)
VALUES
(123456, 'Execution', 10000);

select
    *
from
    department;

INSERT INTO
    employee (
        id,
        first_name,
        last_name,
        date_of_birth,
        gender,
        d_id,
        employee_role
    )
VALUES
(
        105,
        'Kavin',
        'M',
        '2001-10-12 00:00:00',
        'Male',
        100001,
        'Software1'
    );

INSERT INTO
    employee (
        id,
        first_name,
        last_name,
        date_of_birth,
        gender,
        d_id,
        employee_role
    )
VALUES
(
        106,
        'Shreya',
        'Ganeshe',
        '2002-12-12 00:00:00',
        'Female',
        100001,
        'Software2'
    );

INSERT INTO
    employee (
        id,
        first_name,
        last_name,
        date_of_birth,
        gender,
        d_id,
        employee_role
    )
VALUES
(
        107,
        'Abinaya',
        'Uday',
        '2001-03-23 00:00:00',
        'Female',
        123456,
        'JA1'
    );

INSERT INTO
    employee (
        id,
        first_name,
        last_name,
        date_of_birth,
        gender,
        d_id,
        employee_role
    )
VALUES
(
        108,
        'Dhikshitha',
        'Arulkumar',
        '2001-04-29 00:00:00',
        'Female',
        123456,
        'JA2'
    );

INSERT INTO
    employee (
        id,
        first_name,
        last_name,
        date_of_birth,
        gender,
        d_id,
        employee_role
    )
VALUES
(
        109,
        'Swathi',
        'Prathaa',
        '2001-04-13 00:00:00',
        'Female',
        123456,
        'JA1'
    );

select
    *
from
    employee;

INSERT INTO
    address (
        e_id,
        house_no,
        street_name,
        city,
        state,
        country,
        pincode
    )
VALUES
(
        105,
        1,
        'Srinagar',
        'Chennai',
        'TN',
        'India',
        641001
    );

INSERT INTO
    address (
        e_id,
        house_no,
        street_name,
        city,
        state,
        country,
        pincode
    )
VALUES
(106, 2, 'Powai', 'Mumbai', 'TN', 'India', 641101);

INSERT INTO
    address (
        e_id,
        house_no,
        street_name,
        city,
        state,
        country,
        pincode
    )
VALUES
(
        107,
        3,
        'Managr',
        'Chennai',
        'TN',
        'India',
        641201
    );

INSERT INTO
    address (
        e_id,
        house_no,
        street_name,
        city,
        state,
        country,
        pincode
    )
VALUES
(
        108,
        4,
        'Tatabad',
        'Coimbatore',
        'TN',
        'India',
        641401
    );

INSERT INTO
    address (
        e_id,
        house_no,
        street_name,
        city,
        state,
        country,
        pincode
    )
VALUES
(
        109,
        5,
        'CheranManagar',
        'Coimbatore',
        'TN',
        'India',
        641501
    );

select
    *
from
    address;