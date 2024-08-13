insert into base_document (base_uuid, location_key, number, date, session_id, user_id, type_user, currency, user_currency, is_partner, alpha_group) values ('a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11', 'TEST', '2S001', '2024-06-17 16:33:10.491000 +00:00', 1024, 172, 'seller', 'USD', 'RUB', false, '-');

insert into document (created, updated, created_by, updated_by, uuid, base_uuid, stage, status, next_uuid) values ('2024-06-17 13:33:34.374893 +00:00', '2024-06-20 05:00:18.924696 +00:00', '', null, 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11', 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11', 'TO', 'active', '2a53b5c9-129f-406f-bf7b-08d73ab337e2');
insert into document (created, updated, created_by, updated_by, uuid, base_uuid, stage, status, next_uuid) values ('2024-06-17 13:33:34.374893 +00:00', '2024-06-20 05:04:01.697323 +00:00', '', null, '2a53b5c9-129f-406f-bf7b-08d73ab337e2', 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11', 'PI', 'active', '4235d217-991a-44e4-ab39-fcde13165b95');
insert into document (created, updated, created_by, updated_by, uuid, base_uuid, stage, status, next_uuid) values ('2024-06-17 13:33:34.374893 +00:00', '2024-06-20 05:02:12.026374 +00:00', '', null, '4235d217-991a-44e4-ab39-fcde13165b95', 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11', 'IN', 'draft', null);

insert into transaction (id, session_id, product_id, product_variant_id, product_variant_name, localization, chip, quality, supplier_id, customer_id, confirmed_qty, accepted) values (1, 1024, 280, 2122, 'Apple iPhone 11 Dual 128Gb (Purple)', 'RU', null, null, 172, 162, 3, true);
insert into transaction (id, session_id, product_id, product_variant_id, product_variant_name, localization, chip, quality, supplier_id, customer_id, confirmed_qty, accepted) values (2, 1024, 280, 2122, 'Apple iPhone 11 Dual 128Gb (Purple)', 'RU', null, null, 172, 162, 3, true);
insert into transaction (id, session_id, product_id, product_variant_id, product_variant_name, localization, chip, quality, supplier_id, customer_id, confirmed_qty, accepted) values (3, 1024, 280, 2122, 'Apple iPhone 11 Dual 128Gb (Purple)', 'RU', null, null, 172, 162, 2, true);
insert into transaction (id, session_id, product_id, product_variant_id, product_variant_name, localization, chip, quality, supplier_id, customer_id, confirmed_qty, accepted) values (4, 1024, 280, 2122, 'Apple iPhone 11 Dual 128Gb (Purple)', 'RU', null, null, 172, 162, 5, true);
insert into transaction (id, session_id, product_id, product_variant_id, product_variant_name, localization, chip, quality, supplier_id, customer_id, confirmed_qty, accepted) values (5, 1024, 280, 2122, 'Apple iPhone 11 Dual 128Gb (Purple)', 'RU', null, null, 172, 161, 4, true);

insert into base_item (uuid, document_base_uuid, qty0, price0, user_price0, delivery_date0) values ('f82a7e8a-6315-4d4a-8423-45b5c4d6cd3c', 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11', 10, 10000, 10000, '2024-06-21 14:34:47.667000 +00:00');
insert into base_item (uuid, document_base_uuid, qty0, price0, user_price0, delivery_date0) values ('9f8e48c2-b8d8-406d-bfe4-8c2492edbcf7', 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11', 9, 12000, 10000, '2024-06-21 14:34:47.667000 +00:00');

insert into item (base_item_uuid, document_uuid, qty, price, user_price, delivery_date) values ('f82a7e8a-6315-4d4a-8423-45b5c4d6cd3c', 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11', 10, 10000, 10000, '2024-06-21 14:34:47.667000 +00:00');
insert into item (base_item_uuid, document_uuid, qty, price, user_price, delivery_date) values ('9f8e48c2-b8d8-406d-bfe4-8c2492edbcf7', 'a0eebc99-9c0b-4ef8-bb6d-6bb9bd380a11', 9, 12000, 10000, '2024-06-21 14:34:47.667000 +00:00');

insert into item (base_item_uuid, document_uuid, qty, price, user_price, delivery_date) values ('f82a7e8a-6315-4d4a-8423-45b5c4d6cd3c', '2a53b5c9-129f-406f-bf7b-08d73ab337e2', 8, 10000, 10000, '2024-06-21 14:34:47.667000 +00:00');
insert into item (base_item_uuid, document_uuid, qty, price, user_price, delivery_date) values ('9f8e48c2-b8d8-406d-bfe4-8c2492edbcf7', '2a53b5c9-129f-406f-bf7b-08d73ab337e2', 9, 12000, 10000, '2024-06-21 14:34:47.667000 +00:00');

insert into item (base_item_uuid, document_uuid, qty, price, user_price, delivery_date) values ('f82a7e8a-6315-4d4a-8423-45b5c4d6cd3c', '4235d217-991a-44e4-ab39-fcde13165b95', 8, 10000, 10000, '2024-06-21 14:34:47.667000 +00:00');
insert into item (base_item_uuid, document_uuid, qty, price, user_price, delivery_date) values ('9f8e48c2-b8d8-406d-bfe4-8c2492edbcf7', '4235d217-991a-44e4-ab39-fcde13165b95', 9, 12000, 10000, '2024-06-21 14:34:47.667000 +00:00');


insert into transaction_to_item (transaction_id, base_item_uuid) values (1, 'f82a7e8a-6315-4d4a-8423-45b5c4d6cd3c');
insert into transaction_to_item (transaction_id, base_item_uuid) values (2, 'f82a7e8a-6315-4d4a-8423-45b5c4d6cd3c');
insert into transaction_to_item (transaction_id, base_item_uuid) values (3, 'f82a7e8a-6315-4d4a-8423-45b5c4d6cd3c');
insert into transaction_to_item (transaction_id, base_item_uuid) values (4, '9f8e48c2-b8d8-406d-bfe4-8c2492edbcf7');
insert into transaction_to_item (transaction_id, base_item_uuid) values (5, '9f8e48c2-b8d8-406d-bfe4-8c2492edbcf7');

insert into box (uuid, number, document_uuid) values ('07614902-26cc-4213-b190-4467420eac02', '0001', '4235d217-991a-44e4-ab39-fcde13165b95');
insert into box (uuid, number, document_uuid) values ('863f8ff2-6bf1-424a-9a37-d751eeb2bf9b', '0002', '4235d217-991a-44e4-ab39-fcde13165b95');

insert into imei (code, transaction_id, box_uuid) values ('12345678901', 1, '07614902-26cc-4213-b190-4467420eac02');
insert into imei (code, transaction_id, box_uuid) values ('12345678902', 1, '07614902-26cc-4213-b190-4467420eac02');
insert into imei (code, transaction_id, box_uuid) values ('12345678903', 1, '07614902-26cc-4213-b190-4467420eac02');
insert into imei (code, transaction_id, box_uuid) values ('12345678904', 2, '863f8ff2-6bf1-424a-9a37-d751eeb2bf9b');
insert into imei (code, transaction_id, box_uuid) values ('12345678905', 2, '863f8ff2-6bf1-424a-9a37-d751eeb2bf9b');
insert into imei (code, transaction_id, box_uuid) values ('12345678906', 2, '863f8ff2-6bf1-424a-9a37-d751eeb2bf9b');
