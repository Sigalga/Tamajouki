# stage indices:
# 0 - egg
# 1 - baby
# 2 - adult
# 3 - evil
# 4 - super-evil
# 5 - mega-evil
# 6 - ultra-evil
# 7 - zetta-evil
# 8 - insect demon
# 9 - sewage devil

AGE_HATCH = 6 #10 #128
AGE_MATURE = 18 #30 #796
AGE_OLD = 256
AGE_DEATHFROMNATURALCAUSES = 400000000000000000000 #8192

HUNGER_CANEAT = 2 #32
HUNGER_NEEDSTOEAT = 20 #128
HUNGER_SICKFROMNOTEATING = 40 #256
HUNGER_DEADFROMNOTEATING = 512

ENERGY_FULL = 256
ENERGY_CANSLEEP = 255
ENERGY_TIRED = 64
ENERGY_PASSOUT = 8

WASTE_EXPUNGE = 20 #256
WASTE_CANCLEAN = 1

stat_bar_limits = (HUNGER_DEADFROMNOTEATING, AGE_OLD, WASTE_EXPUNGE, ENERGY_FULL, 100)

EVIL_POWER = 10         # 60
SUPEREVIL_POWER = 15    # 80
MEGAEVIL_POWER = 20     # 100
ULTRAEVIL_POWER = 40
ZETTAEVIL_POWER = 60
DEMON_POWER = 80
DEVIL_POWER = 100
evil_powers = (EVIL_POWER, SUPEREVIL_POWER, MEGAEVIL_POWER, ULTRAEVIL_POWER, ZETTAEVIL_POWER, DEMON_POWER, DEVIL_POWER)

# bonus points to power
FOOD_BONUS = 5
WEAPON_BONUS = 1

# BG_COLOR = (102, 102, 255)          # darker sky blue
PIXEL_COLOR = (10, 12, 6)           # black
NONPIXEL_COLOR = (153, 153, 255)    # sky blue
TRANSPARENT_COLOR = (0, 0, 0, 0)
STAT_COLOR = (79, 194, 247)         # hot sky blue
BG_COLOR = STAT_COLOR               # hot sky blue
OPTION_COLOR = (222, 133, 210)      # soft pink
BTN_BORDER_COLOR = (255, 0, 127)    # hot pink
BTN_CENTER_COLOR = OPTION_COLOR     # soft pink
BTN_SHADOW_COLOR = PIXEL_COLOR      # black
BOMB_FILL_COLOR = (255, 255, 255)   # white

FPS = 30
SECOND = 1000
SCREEN_WIDTH = 500
SCREEN_HEIGHT_S = 360
SCREEN_HEIGHT_L = 450

DISPLAY_X = 42
DISPLAY_Y = 74
DISPLAY_WIDTH = 256
DISPLAY_SIZE = (DISPLAY_WIDTH, DISPLAY_WIDTH)
SELECTOR_X = 64
SELECTOR_Y = 16
SELECTOR_X_GAP: int = 64
SELECTOR_Y_GAP = 42
SELECTOR_SIZE = (32, 32)
STATS_X = 64
STATS_Y = 128
BTN_X = 42
BTN_Y = 350
BTN_GAP = 96
BTN_BORDER_SIZE = 64
BTN_CENTER_SIZE = 56


WEAPON_TIME = 1
CARE_TIME = 1

USING_KEYBOARD_BUTTONS = False
SERIAL_PORT = ""
