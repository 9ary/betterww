
from collections import OrderedDict

OPTIONS = OrderedDict([
  (
    "custom_player_model",
    "Replaces Link's model with a custom player model.\nThese are loaded from the /models folder."
  ),
  (
    "player_in_casual_clothes",
    "Edit colors for second quest."
  ),
  (
    "disable_custom_player_voice",
    "If the chosen custom model comes with custom voice files, you can check this option to turn them off and simply use Link's normal voice instead."
  ),
  (
    "instant_text_boxes",
    "Text appears instantly and the B button will skip through text when held down."
  ),
  (
    "swift_sail",
    "Sailing speed is doubled and the direction of the wind is always at your back as long as the sail is out."
  ),
  (
    "increase_player_movement_speeds",
    "Change rolling so that it scales from 20.0 to 26.0 speed depending on the player's speed when they roll. Should fix idle rolls."
  ),
  (
    "increase_grapple_animation_speed",
    "Speeds up the grappling hook significantly to behave similarly to HD."
  ),
  (
    "increase_block_moving_animation",
    "Speeds up the rate in which blocks move when pushed/pulled."
  ),
  (
    "increase_misc_animations",
    "Speeds up crawling, climbing, sidle and the camera zoom when talking to an npc."
  ),
  (
    "tingle_chests_without_tuner",
    "Allows Tingle chests to be found with normal bombs, compass reveals location."
  ),
  (
    "invert_camera_x_axis",
    "Inverts the camera X-axis (left-right) like in HD."
  ),
  (
    "reveal_full_sea_chart",
    "Reveals the whole sea chart during file creation, does not apply to existing saves."
  ),
  (
    "KORL_control",
    "King of Red Lions will not stop you from veering off course, but will keep you within the map. Can cause sequence breaks."
  ),
  (
    "song_no_replay",
    "Remove song replays, where Link plays a fancy animation to conduct the song after the player plays it."
  ),
  (
    "swing_turn",
    "Allow turning while swinging on ropes and using the grappling hook."
  ),
  (
    "remove_title_and_ending_videos",
    "Remove the huge video files that play during the intro and ending."
  ),
  (
    "ballad",
    "Makes the cutscene shorter for Ballad of Gales transportation."
  ),
  (
    "titlelogo",
    "Change the title screen logo to gold."
  ),
  (
    "memorylogo",
    "Change the memory card logo to gold."
  ),
  (
    "brisk_sail",
    "1.5x faster Swift Sail, too fast. Cruising with R will be needed."
  ),
  (
    "brisk_sail2",
    "Sail texture will not be replaced, allowing a texture pack to replace it."
  ),
  (
    "swift_sail2",
    "Sail texture will not be replaced, allowing a texture pack to replace it."
  ),
  (
    "normal_sail",
    "Sail is not modified."
  ),
  (
    "normal_sail2",
    "Sail is the default speed but the wind is always at your back as long as the sail is out."
  ),
  (
    "disable_custom_player_voice",
    "If the chosen custom model comes with custom voice files, you can check this option to turn them off and simply use Link's normal voice instead."
  ),
  (
    "disable_custom_player_items",
    "If the chosen custom model comes with custom item models, you can check this option to turn them off and simply use Link's normal item models instead."
  ),
  (
    "randomize_enemy_palettes",
    "Gives all the enemies in the game random colors.",
  ),
])

NON_PERMALINK_OPTIONS = [
						
  "invert_camera_x_axis",
  "custom_player_model",
  # "player_in_casual_clothes",
  "disable_custom_player_voice",
  "disable_custom_player_items",
  # "disable_custom_boat",
  # "custom_color_preset",			
]
