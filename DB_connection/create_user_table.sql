CREATE SCHEMA IF NOT EXISTS "appdata";

CREATE TABLE IF NOT EXISTS "appdata.user"
(
  uuid VARCHAR(100) NOT NULL,
  username VARCHAR(80) NOT NULL,
  email VARCHAR(100) NOT NULL,
  p_password VARCHAR NOT NULL,
  age SMALLINT,
  gender VARCHAR(3),
  city VARCHAR(20),
  country_code VARCHAR(20),
  browser VARCHAR(10),
  is_developer BOOLEAN,
  created_on TIMESTAMP WITHOUT TIME ZONE,
  last_login TIMESTAMP WITHOUT TIME ZONE,
  current_login TIMESTAMP WITHOUT TIME ZONE,
  authenticated BOOLEAN,
  PRIMARY KEY (uuid, username)
);

