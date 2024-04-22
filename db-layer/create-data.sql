CREATE TABLE cats (
    id SERIAL PRIMARY KEY,
    name VARCHAR(50),
    age INT,
    breed VARCHAR(50)
);

INSERT INTO cats (name, age, breed) VALUES
('Whiskers', 5, 'Siamese'),
('Fluffy', 2, 'Maine Coon'),
('Sassy', 3, 'Persian'),
('Bob', 4, 'Bengal'),
('Luna', 1, 'Sphynx'),
('Bella', 2, 'Ragdoll'),
('Lucy', 3, 'British Shorthair'),
('Simba', 4, 'Scottish Fold'),
('Chloe', 5, 'Abyssinian'),
('Oliver', 1, 'Russian Blue'),
('Leo', 2, 'Norwegian Forest');