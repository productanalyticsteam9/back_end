CREATE TABLE IF NOT EXISTS "appdata.vote_history" 
(
  uuid VARCHAR(100) 
  , poll_uuid VARCHAR(100) NOT NULL
  , vote_date TIMESTAMP WITHOUT TIME ZONE
);

commit;