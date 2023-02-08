
-- Create User table
CREATE TABLE User_ (
    user_id SERIAL       NOT NULL,
    name    VARCHAR(255) NOT NULL,
    email VARCHAR(255) NOT NULL,
    user_password VARCHAR(255) NOT NULL,
	account_created TIMESTAMP NOT NULL,
    authenticated BOOLEAN NOT NULL,
    PRIMARY KEY (user_id),
	UNIQUE (email)
);


