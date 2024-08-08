insert into document (created, updated, created_by, updated_by, uuid, base_uuid, stage, location_key, number, date, session_id, user_id, type_user, currency, user_currency, is_partner, status, alpha_group, next_uuid) values ('2024-06-17 13:33:34.374893 +00:00', '2024-06-20 05:00:18.924696 +00:00', '', null, 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11', 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11', 'TO', 'TEST', '2S001', '2024-06-17 16:33:10.491000 +00:00', 1024, 172, 'seller', 'USD', 'RUB', false, 'active', '-', '2a53b5c9-129f-406f-bf7b-08d73ab337e2');
insert into document (created, updated, created_by, updated_by, uuid, base_uuid, stage, location_key, number, date, session_id, user_id, type_user, currency, user_currency, is_partner, status, alpha_group, next_uuid) values ('2024-06-17 13:33:34.374893 +00:00', '2024-06-20 05:04:01.697323 +00:00', '', null, '2a53b5c9-129f-406f-bf7b-08d73ab337e2', 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11', 'PI', 'TEST', '2S001', '2024-06-17 16:33:10.491000 +00:00', 1024, 172, 'seller', 'USD', 'RUB', false, 'active', '-', '4235d217-991a-44e4-ab39-fcde13165b95');
insert into document (created, updated, created_by, updated_by, uuid, base_uuid, stage, location_key, number, date, session_id, user_id, type_user, currency, user_currency, is_partner, status, alpha_group, next_uuid) values ('2024-06-17 13:33:34.374893 +00:00', '2024-06-20 05:02:12.026374 +00:00', '', null, '4235d217-991a-44e4-ab39-fcde13165b95', 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11', 'IN', 'TEST', '2S001', '2024-06-17 16:33:10.491000 +00:00', 1024, 172, 'seller', 'USD', 'RUB', false, 'draft', '-', null);

insert into transaction (id, product_id, product_variant_id, product_variant_name, localization, chip, quality, supplier_id, customer_id) values (1, 280, 2122, 'Apple iPhone 11 Dual 128Gb (Purple)', 'RU', null, null, 172, 162);
insert into transaction (id, product_id, product_variant_id, product_variant_name, localization, chip, quality, supplier_id, customer_id) values (2, 280, 2122, 'Apple iPhone 11 Dual 128Gb (Purple)', 'RU', null, null, 172, 162);
insert into transaction (id, product_id, product_variant_id, product_variant_name, localization, chip, quality, supplier_id, customer_id) values (3, 280, 2122, 'Apple iPhone 11 Dual 128Gb (Purple)', 'RU', null, null, 172, 162);
insert into transaction (id, product_id, product_variant_id, product_variant_name, localization, chip, quality, supplier_id, customer_id) values (4, 280, 2122, 'Apple iPhone 11 Dual 128Gb (Purple)', 'RU', null, null, 172, 162);

insert into item (uuid, document_uuid, transaction_id, qty, price, user_price, delivery_date) values ('f82a7e8a-6315-4d4a-8423-45b5c4d6cd3c', '2a53b5c9-129f-406f-bf7b-08d73ab337e2', 1, 3, 10000, 10000, '2024-06-21 14:34:47.667000 +00:00');
insert into item (uuid, document_uuid, transaction_id, qty, price, user_price, delivery_date) values ('9f8e48c2-b8d8-406d-bfe4-8c2492edbcf7', 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11', 2, 3, 10000, 10000, '2024-06-21 14:34:47.667000 +00:00');
insert into item (uuid, document_uuid, transaction_id, qty, price, user_price, delivery_date) values ('0035d217-991a-44e4-ab39-fcde13165b95', '4235d217-991a-44e4-ab39-fcde13165b95', 3, 2, 10000, 10000, '2024-06-21 14:34:47.667000 +00:00');
insert into item (uuid, document_uuid, transaction_id, qty, price, user_price, delivery_date) values ('5432d217-991a-44e4-ab39-fcde13165b95', '2a53b5c9-129f-406f-bf7b-08d73ab337e2', 4, 6, 12000, 10000, '2024-06-21 14:34:47.667000 +00:00');


insert into item_pi (uuid, qty0, user_price0, accepted) values ('f82a7e8a-6315-4d4a-8423-45b5c4d6cd3c', 3, 10000, true);
insert into item_pi (uuid, qty0, user_price0, accepted) values ('5432d217-991a-44e4-ab39-fcde13165b95', 4, 12000, true);

insert into item_in (uuid, qty0, user_price0) values ('0035d217-991a-44e4-ab39-fcde13165b95', 3, 10000);

insert into box (uuid, number) values ('07614902-26cc-4213-b190-4467420eac02', '0001');
insert into box (uuid, number) values ('863f8ff2-6bf1-424a-9a37-d751eeb2bf9b', '0002');

insert into imei (code, transaction_id, box_uuid) values ('12345678901', 1, '07614902-26cc-4213-b190-4467420eac02');
insert into imei (code, transaction_id, box_uuid) values ('12345678902', 2, '07614902-26cc-4213-b190-4467420eac02');
insert into imei (code, transaction_id, box_uuid) values ('12345678903', 3, '07614902-26cc-4213-b190-4467420eac02');
insert into imei (code, transaction_id, box_uuid) values ('12345678904', 4, '863f8ff2-6bf1-424a-9a37-d751eeb2bf9b');
