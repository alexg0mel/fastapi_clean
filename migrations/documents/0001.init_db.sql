create or replace function trigger_set_timestamp()
returns trigger as $$
begin
  new.updated = NOW();
  return new;
end;
$$ language plpgsql;

drop type if exists document_stage;
create type document_stage as ENUM('TO', 'PI', 'IN', 'CD');

drop type if exists document_status;
create type  document_status as ENUM('draft', 'active', 'forming');

drop type if exists type_user;
create type  type_user as ENUM('buyer', 'seller');

drop type if exists alpha_group;
create type alpha_group as ENUM('-', 'α', 'β', 'γ', 'δ', 'ε', 'ζ', 'η', 'θ', 'ι', 'κ');

create table audit_columns
(
    created    timestamp with time zone default now(),
    updated    timestamp with time zone default now(),
    created_by varchar(100),
    updated_by varchar(100)
);

create table document
(
    uuid           uuid                     not null,
    base_uuid      uuid                     not null,
    stage          document_stage           not null,
    location_key   varchar(10)              not null,
    number         varchar(8)               not null,
    date           timestamp with time zone not null,
    session_id     int                      not null,
    user_id        int                      not null,
    type_user      type_user                not null,
    currency       varchar(6)               not null,
    user_currency  varchar(6)               not null,
    is_partner     boolean default false    not null,
    status         document_status default 'forming' not null,
    alpha_group    alpha_group default '-'  not null,
    next_uuid      uuid,

    constraint pk_document PRIMARY KEY (uuid)
) inherits (audit_columns);


create index idx_document_base_uuid
    on document (base_uuid);

create trigger set_document_timestamp
    before update on document
    for each row
    execute procedure trigger_set_timestamp();
