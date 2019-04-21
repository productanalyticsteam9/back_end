
insert into "appdata.user" (uuid, email, password, name, age, gender, city,
  country, browser, is_developer, created_on,last_login) values
(DEFAULT, 'neha@gmail.com', '1234&', 'neha', '20', 'f', 'delhi', 'india', 'chrome', 
'true', '2019-03-30','2019-03-30'),
(DEFAULT, 'shivee@gmail.com', '456*7', 'shivee', '25', 'f', 'mumbai', 'india', 'firefox', 
'true', '2019-03-31','2019-03-31'),
(DEFAULT, 'anurag@gmail.com', '433ab4', 'anurag', '29', 'm', 'kolkata', 'india', 
'chrome', 'true', '2019-03-30','2019-03-30');


insert into "appdata.poll" (poll_uuid, uuid, image_id, image_path, vote_cnt, post_date, user_tag, model_tag, poll_text) values
(1, '9e3e7950-317c-4707-aaba-207a4dbf501a', '{"1": "car1.png", "2": "car2.png"}', ARRAY['path_a', 'path_b'], ARRAY[2, 3], '2019-03-30', 'car', 'red car', 'which is better'),
(2, '97c112c6-386f-46ca-b686-d89558b0292f', '{"1": "car1.png", "2": "car2.png"}', ARRAY['path_a2', 'path_b2'], ARRAY[21, 13], '2019-03-31', 'dogs', ' golden retriver', 'which is better'),
(3, '895c43cc-27c4-4579-900f-5b1bf610587e', '{"1": "car1.png", "2": "car2.png"}', ARRAY['path_a3', 'path_b3'], ARRAY[22, 33], '2019-03-31', 'hairband', 'coolbands!', 'which looks better'),
(4, '13013da7-a5d5-4966-8587-54804a3bf535', '{"1": "car1.png", "2": "car2.png"}', ARRAY['path_a4', 'path_b4'], ARRAY[27, 37], '2019-03-31', 'dress', 'straight-fit, regular', 'which do you like'),
(5, '98a150a0-4391-4d3d-a864-d9a4ce9c2bd6', '{"1": "car1.png", "2": "car2.png"}', ARRAY['path_a5', 'path_b5'], ARRAY[22, 13], '2019-03-31', 'specs', 'black, white', 'which is better');


insert into "appdata.vote_history" (uuid, poll_uuid, vote_date) values
('363947ad-77cb-405d-bb52-e640a062735e', '9e3e7950-317c-4707-aaba-207a4dbf501a', '2019-04-01'),
('6a8cd336-0c06-426c-a781-05ffbe6e1f07', '97c112c6-386f-46ca-b686-d89558b0292f', '2019-04-01'),
('6a8cd336-0c06-426c-a781-05ffbe6e1f07', '895c43cc-27c4-4579-900f-5b1bf610587e', '2019-04-01'),
('6a8cd336-0c06-426c-a781-05ffbe6e1f07', '13013da7-a5d5-4966-8587-54804a3bf535', '2019-04-01');

commit;




