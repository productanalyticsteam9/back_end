CREATE SEQUENCE IF NOT EXISTS poll_image_id_seq;

CREATE TABLE IF NOT EXISTS "appdata.poll"
(
    poll_id VARCHAR(100) NOT NULL
    , uuid VARCHAR(100) --REFERENCES "appdata.user"(uuid) --ON DELETE CASCADE
    , image_id_a BIGINT NOT NULL DEFAULT nextval('poll_image_id_seq')
    , image_id_b BIGINT NOT NULL DEFAULT nextval('poll_image_id_seq')
    , image_path_a VARCHAR(100) NOT NULL
    , image_path_b VARCHAR(100) NOT NULL
    , vote_a_cnt BIGINT
    , vote_b_cnt BIGINT
    , post_date timestamp without time zone
    , user_tag TEXT
    , model_tag TEXT
    , PRIMARY KEY (poll_id)
    
);
