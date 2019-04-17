
insert into "appdata.user" (uuid, email, password, name, age, gender, city,
  country, browser, is_developer, created_on,last_login) values
(DEFAULT, 'neha@gmail.com', '1234&', 'neha', '20', 'f', 'delhi', 'india', 'chrome', 
'true', '2019-03-30','2019-03-30'),
(DEFAULT, 'shivee@gmail.com', '456*7', 'shivee', '25', 'f', 'mumbai', 'india', 'firefox', 
'true', '2019-03-31','2019-03-31'),
(DEFAULT, 'anurag@gmail.com', '433ab4', 'anurag', '29', 'm', 'kolkata', 'india', 
'chrome', 'true', '2019-03-30','2019-03-30');


insert into "appdata.poll" (poll_id, uuid, image_id_a, image_id_b, image_path_a,
image_path_b, vote_a_cnt, vote_b_cnt, post_date, user_tag, model_tag) values
(1, '363947ad-77cb-405d-bb52-e640a062735e', 1, 2, 'path_a', 'path_b', 2, 3, '2019-03-30', 'car', 'red car'),
(2, '6a8cd336-0c06-426c-a781-05ffbe6e1f07', 3, 4, 'path_a2', 'path_b2', 21, 13, '2019-03-31', 'dogs', ' golden retriver'),
(3, '6a8cd336-0c06-426c-a781-05ffbe6e1f07', 5, 6, 'path_a3', 'path_b3', 22, 33, '2019-03-31', 'hairband', 'coolbands!'),
(4, '6a8cd336-0c06-426c-a781-05ffbe6e1f07', 7, 8, 'path_a4', 'path_b4', 27, 37, '2019-03-31', 'dress', 'straight-fit, regular'),
(5, '6a8cd336-0c06-426c-a781-05ffbe6e1f07', 9, 10, 'path_a5', 'path_b5', 22, 13, '2019-03-31', 'specs', 'black, white');


insert into "appdata.vote" (uuid, voter_poll_id, poll_date) values
('363947ad-77cb-405d-bb52-e640a062735e', 3, '2019-04-01'),
('6a8cd336-0c06-426c-a781-05ffbe6e1f07', 4, '2019-04-01'),
('6a8cd336-0c06-426c-a781-05ffbe6e1f07', 1, '2019-04-01'),
('6a8cd336-0c06-426c-a781-05ffbe6e1f07', 2, '2019-04-01');

commit;
