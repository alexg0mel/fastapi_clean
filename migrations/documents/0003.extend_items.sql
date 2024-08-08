create table transaction
(
    id                   int                 not null,
    product_id           int                 not null,
    product_variant_id   int                 not null,
    product_variant_name varchar(256)        not null,
    localization         varchar(40)     default null,
    chip                 varchar(40)     default null,
    quality              varchar(40)     default null,
    supplier_id          int                 not null,
    customer_id          int                 not null,
    constraint pk_transaction primary key (id)
);

create table box
(
    uuid        uuid                         not null,
    number      varchar(7)                   not null,
    constraint pk_box primary key (uuid)
);


alter table item
    add column transaction_id int NOT NULL,
    drop column product_id,
    drop column product_variant_id,
    drop column product_variant_name,
    drop column localization,
    drop column chip,
    drop column quality,
    add constraint fk_item_transaction foreign key (transaction_id) references transaction (id) on delete cascade;

create table imei
(
    code                 varchar(21)         not null,
    transaction_id       int                 not null,
    box_uuid             uuid                not null,
    constraint pk_imei primary key (code, transaction_id),
    constraint fk_imei_box_uuid foreign key (box_uuid) references box (uuid) ON DELETE CASCADE
);
