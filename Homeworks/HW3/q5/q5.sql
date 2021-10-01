-- q5
alter table player_bios
add column position text;

update player_bios
set position = new_table.position
from new_table
where player = id;

select firstname, lastname, position from player_bios limit 5;