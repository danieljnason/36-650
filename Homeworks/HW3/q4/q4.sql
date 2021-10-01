-- q4
create table new_table(
	player integer references more_player_stats,
	pr1 numeric,
	position text
);

insert into new_table (player, pr1) (select id, round(per - 67*va/(gp*minutes), 1) from more_player_stats);

update new_table
set position = 'PF'
where pr1 >= 11.3;

update new_table
set position = 'PG'
where pr1 >= 10.8 and pr1 < 11.3;

update new_table
set position = 'C'
where pr1 >= 10.6 and pr1 < 10.8;

update new_table
set position = 'SG/SF'
where pr1 >= 0 and pr1 < 10.6;
	 
select * from new_table limit 10;