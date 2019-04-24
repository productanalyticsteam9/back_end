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

commit;