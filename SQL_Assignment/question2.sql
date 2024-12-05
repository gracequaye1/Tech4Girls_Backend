-- Use the Tech4Girls_DB database
USE Tech4Girls_DB;

-- Create the Posts table
CREATE TABLE Posts (
    id INT AUTO_INCREMENT PRIMARY KEY,
    user_id INT NOT NULL,
    title VARCHAR(255) NOT NULL,
    content TEXT NOT NULL,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    FOREIGN KEY (user_id) REFERENCES Users(id)
);

-- Insert sample data into the Posts table
INSERT INTO Posts (user_id, title, content, created_at) VALUES
(1, 'Augustine\'s First Post', 'This is the content of Augustine\'s first post.', '2024-11-01 11:00:00'),
(2, 'Abena\'s Post', 'Abena shares her experience here.', '2024-11-02 13:00:00'),
(3, 'Betty\'s Thoughts', 'Betty writes about her journey.', '2024-11-03 15:00:00');
