-- q5
alter table player_bios
add column position text;

update player_bios
set position = new_table.position
from new_table
where player_bios.id = new_table.player;

select firstname, lastname, position from player_bios order by id limit 5;