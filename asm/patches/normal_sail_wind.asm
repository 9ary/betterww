
.open "files/rels/d_a_ship.rel"

; Make the wind always be at the players back as long as the sail is out.
.org 0xB9FC
  bl set_wind_dir_to_ship_dir

.close
