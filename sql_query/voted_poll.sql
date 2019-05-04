CREATE TABLE IF NOT EXISTS "appdata.voted_poll"
(
  uuid VARCHAR(100)
  , voted_polls VARCHAR [] NOT NULL
  , PRIMARY KEY (uuid)
);

commit;
