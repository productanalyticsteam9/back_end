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
  , current_login TIMESTAMP WITHOUT TIME ZONE NOT NULL
  , authenticated BOOLEAN
  , PRIMARY KEY (uuid, username)
 );


-- CREATE SEQUENCE if not exists poll_image_id_seq;

CREATE TABLE IF NOT EXISTS "appdata.poll" 
(
  poll_uuid VARCHAR(100) NOT NULL
  , uuid VARCHAR(100) 
  , image_id JSON NOT NULL  
  , image_path VARCHAR [] NOT NULL
  , vote_cnt BIGINT []
  , post_date TIMESTAMP WITHOUT TIME ZONE
  , user_tag TEXT
  , model_tag TEXT
  , poll_text VARCHAR(200)
  , PRIMARY KEY (poll_uuid)
);


CREATE TABLE IF NOT EXISTS "appdata.vote_history" 
(
  uuid VARCHAR(100) 
  , poll_uuid VARCHAR(100) NOT NULL
  , vote_date TIMESTAMP WITHOUT TIME ZONE
);

commit;
