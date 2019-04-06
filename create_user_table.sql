CREATE SCHEMA IF NOT EXISTS appdata;

CREATE TABLE IF NOT EXISTS "appdata.user"
(
  uuid VARCHAR(100) UNIQUE NOT NULL,
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
  PRIMARY KEY(uuid, username)
);

CREATE SEQUENCE IF NOT exists poll_image_id_seq;

CREATE TABLE IF NOT EXISTS "appdata.poll" 
(
    poll_id VARCHAR(100) NOT NULL
    , uuid VARCHAR(100) REFERENCES "appdata.user"(uuid) 
    , image_id_a bigint NOT NULL DEFAULT nextval('poll_image_id_seq')
    , image_id_b bigint NOT NULL DEFAULT nextval('poll_image_id_seq')
    , image_path_a VARCHAR(200) NOT NULL
    , image_path_b VARCHAR(200) NOT NULL
    , vote_a_cnt bigint
    , vote_b_cnt bigint
    , post_date timestamp without time zone
    , user_tag TEXT
    , model_tag TEXT
    , PRIMARY KEY (poll_id)
    
);

