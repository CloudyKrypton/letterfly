DROP SCHEMA IF EXISTS letterfly_schema CASCADE;
CREATE SCHEMA letterfly_schema;
SET search_path TO letterfly_schema;

CREATE TABLE LetterflyUser (
    username VARCHAR(100) PRIMARY KEY,
    pwd VARCHAR(100) NOT NULL,
    name VARCHAR(100) NOT NULL,
    reads_in VARCHAR(100)[] NOT NULL DEFAULT '{}',
    writes_in VARCHAR(100)[] NOT NULL DEFAULT '{}'
);

CREATE TABLE Letter (
    letter_id SERIAL PRIMARY KEY,
    content TEXT NOT NULL,
    language VARCHAR(100) NOT NULL,
    writer VARCHAR(100) NOT NULL REFERENCES LetterflyUser(username) ON DELETE CASCADE
);

CREATE TABLE SentTo (
    recipient VARCHAR(100) NOT NULL REFERENCES LetterflyUser(username) ON DELETE CASCADE,
    letter INT NOT NULL REFERENCES Letter(letter_id) ON DELETE CASCADE,
    time_sent TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
    status VARCHAR(100) NOT NULL,
    PRIMARY KEY (letter, recipient)
);

CREATE TABLE Friends (
    friend1 TEXT NOT NULL REFERENCES LetterflyUser(username) ON DELETE CASCADE,
    friend2 TEXT NOT NULL REFERENCES LetterflyUser(username) ON DELETE CASCADE,
    PRIMARY KEY (friend1, friend2),
    CHECK (friend1 <> friend2)
);
