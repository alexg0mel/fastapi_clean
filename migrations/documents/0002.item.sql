create table base_item
(
    uuid                 uuid                not null,
    document_base_uuid   uuid                not null,
    qty0                 int                 not null,
    price0               int                 not null,
    user_price0          int                 not null,
    delivery_date0       timestamp with time zone not null,
    constraint pk_base_item PRIMARY KEY (uuid),
    constraint fk_base_item_document_base_uuid foreign key (document_base_uuid) references base_document (base_uuid) ON DELETE CASCADE
);

create index idx_base_item_document_base_uuid
    on base_item (document_base_uuid);


create table item
(
    base_item_uuid     uuid                not null,
    document_uuid      uuid                not null,
    qty                int                 not null,
    price              int                 not null,
    user_price         int                 not null,
    delivery_date      timestamp with time zone not null,
    constraint pk_item PRIMARY KEY (base_item_uuid, document_uuid),
    constraint fk_item_document_uuid foreign key (document_uuid) references document (uuid) ON DELETE CASCADE
);

create index idx_item_document_uuid
    on item (document_uuid);
