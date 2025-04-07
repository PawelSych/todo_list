-- Tworzenie tabel
CREATE TABLE users (
    id BIGSERIAL PRIMARY KEY,
    username VARCHAR(50) NOT NULL UNIQUE,
    email VARCHAR(100) NOT NULL UNIQUE,
    password VARCHAR(255) NOT NULL,
    created_at TIMESTAMP NOT NULL
);

CREATE TABLE tasks (
    id BIGSERIAL PRIMARY KEY,
    user_id BIGINT NOT NULL REFERENCES users(id),
    title VARCHAR(255),
    priority INTEGER NOT NULL,
    completed BOOLEAN NOT NULL DEFAULT FALSE,
    created_at TIMESTAMP NOT NULL,
    updated_at TIMESTAMP NOT NULL
);

CREATE TABLE sessions (
    id BIGSERIAL PRIMARY KEY,
    user_id BIGINT NOT NULL REFERENCES users(id),
    token VARCHAR(255) NOT NULL,
    created_at TIMESTAMP NOT NULL,
    expires_at TIMESTAMP
);

-- Przykładowi użytkownicy
INSERT INTO users (username, email, password, created_at)
VALUES 
    ('pawel', 'pawel@dev.pl', 'tajnehaslo', CURRENT_TIMESTAMP),
    ('kasia', 'kasia@example.com', '1234', CURRENT_TIMESTAMP),
    ('arek', 'arek@example.com', 'haslo', CURRENT_TIMESTAMP);

-- Przykładowe zadania
INSERT INTO tasks (user_id, title, priority, completed, created_at, updated_at)
VALUES 
    (1, 'Kup mleko', 2, false, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
    (1, 'Zrób zadanie domowe', 3, false, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP),
    (2, 'Zaplanuj wakacje', 1, true, CURRENT_TIMESTAMP, CURRENT_TIMESTAMP);

-- Przykładowe sesje
INSERT INTO sessions (user_id, token, created_at, expires_at)
VALUES 
    (1, '1111-aaaa-xxxx-yyyy', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP + INTERVAL '1 hour'),
    (2, '2222-bbbb-yyyy-zzzz', CURRENT_TIMESTAMP, CURRENT_TIMESTAMP + INTERVAL '2 hours');
