-- q6
alter table player_bios
add column inches numeric;
	
update player_bios
set inches = 12*split_part(height,'-',1)::integer + split_part(height,'-',2)::integer;

alter table player_bios
drop column height;
	
alter table player_bios
rename column inches to height;

select firstname, lastname, height 
from player_bios
order by id
limit 5;