CREATE SCHEMA IF NOT EXISTS "appdata";

CREATE TABLE IF NOT EXISTS "appdata.user"
(
  uuid VARCHAR(100) NOT NULL
  , username VARCHAR(80) NOT NULL
  , email VARCHAR(100) UNIQUE NOT NULL
  , p_password VARCHAR NOT NULL
  , age SMALLINT
  , gender VARCHAR(3)
  , city VARCHAR(20)
  , country_code VARCHAR(20)
  , browser VARCHAR(10)
  , is_developer BOOLEAN
  , created_on TIMESTAMP WITHOUT TIME ZONE NOT NULL
  , last_login TIMESTAMP WITHOUT TIME ZONE NOT NULL
  , authenticated BOOLEAN
  , PRIMARY KEY (uuid, username)
 );


-- CREATE SEQUENCE if not exists poll_image_id_seq;

CREATE TABLE IF NOT EXISTS "appdata.poll" 
(
  poll_id BIGSERIAL NOT NULL
  , uuid VARCHAR(100) REFERENCES appdata.user(uuid) ON DELETE CASCADE
  , image_id_a BIGINT NOT NULL DEFAULT NEXTVAL('poll_image_id_seq')
  , image_id_b BIGINT NOT NULL DEFAULT NEXTVAL('poll_image_id_seq')
  , image_path_a VARCHAR(100) NOT NULL
  , image_path_b VARCHAR(100) NOT NULL
  , vote_a_cnt BIGINT
  , vote_b_cnt BIGINT
  , post_date TIMESTAMP WITHOUT TIME ZONE
  , user_tag TEXT
  , model_tag TEXT
  , PRIMARY KEY (poll_id)
);



CREATE TABLE IF NOT EXISTS "appdata.vote" 
(
  uuid BIGINT REFERENCES appdata.user(uuid) ON DELETE CASCADE
  , voter_poll_id BIGINT
  , poll_date TIMESTAMP WITHOUT TIME ZONE
);



commit;

