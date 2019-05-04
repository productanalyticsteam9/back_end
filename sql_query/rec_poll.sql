CREATE TABLE IF NOT EXISTS "appdata.rec_poll" 
(
  
  uuid VARCHAR(100) 
  , recommend_polls VARCHAR [] NOT NULL
  , PRIMARY KEY (uuid)
);

commit;