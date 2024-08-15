create table transaction
(
    id                   int                 not null,
    session_id           int                 not null,
    product_id           int                 not null,
    product_variant_id   int                 not null,
    product_variant_name varchar(256)        not null,
    localization         varchar(40)     default null,
    chip                 varchar(40)     default null,
    quality              varchar(40)     default null,
    supplier_id          int                 not null,
    customer_id          int                 not null,
    confirmed_qty        int                 not null,
    accepted             boolean             not null,
    constraint pk_transaction primary key (id)
);

create index idx_transaction_session_id
    on transaction (session_id);

create table box
(
    uuid            uuid                         not null,
    number          varchar(7)                   not null,
    document_uuid   uuid                         not null,
    constraint pk_box primary key (uuid),
    constraint fk_box_document_uuid foreign key (document_uuid) references document (uuid) ON DELETE CASCADE
);

create index idx_box_document_uuid
    on box (document_uuid);

create table imei
(
    code                 varchar(21)         not null,
    transaction_id       int                 not null,
    box_uuid             uuid                not null,
    from_document_uuid   uuid                not null,
    constraint pk_imei primary key (code, transaction_id),
    constraint fk_imei_box_uuid foreign key (box_uuid) references box (uuid) ON DELETE CASCADE
);

create index idx_imei_from_document_uuid
    on imei (from_document_uuid);

create table transaction_to_item
(
    transaction_id  int    not null,
    base_item_uuid  uuid   not null,
    constraint pk_transaction_to_item primary key (transaction_id, base_item_uuid)
);
