create table item
(
    uuid                 uuid                not null,
    document_uuid        uuid                not null,
    product_id           int                 not null,
    product_variant_id   int                 not null,
    product_variant_name varchar(256)        not null,
    localization         varchar(40)     default null,
    chip                 varchar(40)     default null,
    quality              varchar(40)     default null,
    qty                  int                 not null,
    price                int                 not null,
    user_price           int                 not null,
    delivery_date        timestamp with time zone not null,
    constraint pk_item PRIMARY KEY (uuid),
    constraint fk_item_document_uuid foreign key (document_uuid) references document (uuid) ON DELETE CASCADE
);

create index idx_item_document_uuid
    on item (document_uuid);

create table item_pi
(
    uuid                 uuid                     not null,
    qty0                 int                      not null,
    user_price0          int                      not null,
    accepted             boolean default false    not null,
    constraint pk_item_pi PRIMARY KEY (uuid),
    constraint fk_item_pi_item_uuid foreign key (uuid) references item (uuid) ON DELETE CASCADE
);

create table item_in
(
    uuid                 uuid                     not null,
    qty0                 int                      not null,
    user_price0          int                      not null,
    constraint pk_item_in PRIMARY KEY (uuid),
    constraint fk_item_in_item_uuid foreign key (uuid) references item (uuid) ON DELETE CASCADE
);
