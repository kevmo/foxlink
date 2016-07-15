CREATE TABLE polls (
    created_at              timestamp default current_timestamp,
    updated_at              timestamp,

    url_identifier          varchar(32) primary key,
    secret                  varchar(32)
);

CREATE TABLE results (
    poll                    varchar(32) REFERENCES polls (url_identifier),
    data                    json
)