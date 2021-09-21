drop table rdata;

create table rdata(
id serial primary key,
a varchar(5) unique not null,
b varchar(5) unique not null,
moment date default '2020-01-01',
x numeric(5,2) check (x > 0)
);