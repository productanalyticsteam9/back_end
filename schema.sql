create schema if not exists appdata;

CREATE TABLE IF NOT EXISTS appdata.user
(
  user_id bigserial NOT NULL 
  , email varchar(50) UNIQUE NOT NULL
  , password varchar(10) NOT NULL
  , name varchar(30) NOT NULL
  , age smallint 
  , gender varchar(3)
  , city varchar(20)
  , country varchar(20)
  , browser varchar(10)
  , is_developer boolean
  , created_on timestamp without time zone NOT NULL
  , last_login timestamp without time zone NOT NULL
  , PRIMARY KEY (user_id)

 );


CREATE SEQUENCE if not exists poll_image_id_seq;

CREATE TABLE IF NOT EXISTS appdata.poll 
(
    poll_id bigserial NOT NULL
    , user_id bigint REFERENCES appdata.user(user_id) ON DELETE CASCADE
    , image_id_a bigint NOT NULL DEFAULT nextval('poll_image_id_seq')
    , image_id_b bigint NOT NULL DEFAULT nextval('poll_image_id_seq')
    , image_path_a varchar(100) NOT NULL
    , image_path_b varchar(100) NOT NULL
    , vote_a_cnt bigint
    , vote_b_cnt bigint
    , post_date timestamp without time zone
    , user_tag TEXT
    , model_tag TEXT
    , PRIMARY KEY (poll_id)
    
);



CREATE TABLE IF NOT EXISTS appdata.vote (
	user_id bigint REFERENCES appdata.user(user_id) ON DELETE CASCADE
	,voter_poll_id bigint
    ,poll_date timestamp without time zone
);



commit;

