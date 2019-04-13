
insert into appdata.user (user_id, email, password, name, age, gender, city,
  country, browser, is_developer, created_on,last_login) values
(DEFAULT, 'neha@gmail.com', '1234&', 'neha', '20', 'f', 'delhi', 'india', 'chrome', 
'true', '2019-03-30','2019-03-30'),
(DEFAULT, 'shivee@gmail.com', '456*7', 'shivee', '25', 'f', 'mumbai', 'india', 'firefox', 
'true', '2019-03-31','2019-03-31'),
(DEFAULT, 'anurag@gmail.com', '433ab4', 'anurag', '29', 'm', 'kolkata', 'india', 
'chrome', 'true', '2019-03-30','2019-03-30');


insert into appdata.poll (user_id, image_path_a,
image_path_b, vote_a_cnt, vote_b_cnt, post_date, user_tag, model_tag) values
(1, 'path_a', 'path_b', 2, 3, '2019-03-30', 'car', 'red car'),
(1, 'path_a2', 'path_b2', 21, 13, '2019-03-31', 'dogs', ' golden retriver'),
(2, 'path_a3', 'path_b3', 22, 33, '2019-03-31', 'hairband', 'coolbands!'),
(2, 'path_a4', 'path_b4', 27, 37, '2019-03-31', 'dress', 'straight-fit, regular'),
(2, 'path_a5', 'path_b5', 22, 13, '2019-03-31', 'specs', 'black, white');


insert into appdata.vote (user_id, voter_poll_id, poll_date) values
(1, 3, '2019-04-01'),
(1, 4, '2019-04-01'),
(2, 1, '2019-04-01'),
(2, 2, '2019-04-01');

commit;
