-- Use the Tech4Girls_DB database
USE Tech4Girls_DB;

-- Create the Courses table
CREATE TABLE Courses (
    id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(100) NOT NULL
);

-- Create the User_Courses table to establish the many-to-many relationship
CREATE TABLE User_Courses (
    user_id INT NOT NULL,
    course_id INT NOT NULL,
    PRIMARY KEY (user_id, course_id),
    FOREIGN KEY (user_id) REFERENCES Users(id),
    FOREIGN KEY (course_id) REFERENCES Courses(id)
);

-- Insert sample data into the Courses table
INSERT INTO Courses (course_name) VALUES
('Python Basics'),
('Web Development'),
('Data Analysis');

-- Insert sample data into the User_Courses table
INSERT INTO User_Courses (user_id, course_id) VALUES
(1, 1), -- Augustine enrolled in Python Basics
(1, 2), -- Ama enrolled in Web Development
(2, 3), -- Abena enrolled in Data Analysis
(3, 1), -- Betty enrolled in Python Basics
(3, 3); -- Betty enrolled in Data Analysis
