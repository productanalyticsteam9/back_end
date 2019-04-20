
insert into "appdata.user" (uuid, email, password, name, age, gender, city,
  country, browser, is_developer, created_on,last_login) values
(DEFAULT, 'neha@gmail.com', '1234&', 'neha', '20', 'f', 'delhi', 'india', 'chrome', 
'true', '2019-03-30','2019-03-30'),
(DEFAULT, 'shivee@gmail.com', '456*7', 'shivee', '25', 'f', 'mumbai', 'india', 'firefox', 
'true', '2019-03-31','2019-03-31'),
(DEFAULT, 'anurag@gmail.com', '433ab4', 'anurag', '29', 'm', 'kolkata', 'india', 
'chrome', 'true', '2019-03-30','2019-03-30');


insert into "appdata.poll" (poll_uuid, uuid, image_id, image_path, vote_cnt, post_date, user_tag, model_tag, poll_text) values
(1, '363947ad-77cb-405d-bb52-e640a062735e', ARRAY[1, 2], ARRAY['path_a', 'path_b'], ARRAY[2, 3], '2019-03-30', 'car', 'red car', 'which is better'),
(2, '6a8cd336-0c06-426c-a781-05ffbe6e1f07', ARRAY[1, 2], ARRAY['path_a2', 'path_b2'], ARRAY[21, 13], '2019-03-31', 'dogs', ' golden retriver', 'which is better'),
(3, '6a8cd336-0c06-426c-a781-05ffbe6e1f07', ARRAY[1, 2], ARRAY['path_a3', 'path_b3'], ARRAY[22, 33], '2019-03-31', 'hairband', 'coolbands!', 'which looks better'),
(4, '6a8cd336-0c06-426c-a781-05ffbe6e1f07', ARRAY[1, 2], ARRAY['path_a4', 'path_b4'], ARRAY[27, 37], '2019-03-31', 'dress', 'straight-fit, regular', 'which do you like'),
(5, '6a8cd336-0c06-426c-a781-05ffbe6e1f07', ARRAY[1, 2], ARRAY['path_a5', 'path_b5'], ARRAY[22, 13], '2019-03-31', 'specs', 'black, white', 'which is better');


insert into "appdata.vote" (uuid, voter_poll_id, poll_date) values
('363947ad-77cb-405d-bb52-e640a062735e', 3, '2019-04-01'),
('6a8cd336-0c06-426c-a781-05ffbe6e1f07', 4, '2019-04-01'),
('6a8cd336-0c06-426c-a781-05ffbe6e1f07', 1, '2019-04-01'),
('6a8cd336-0c06-426c-a781-05ffbe6e1f07', 2, '2019-04-01');

commit;




