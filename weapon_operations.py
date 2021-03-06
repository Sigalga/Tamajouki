from graphics import *
from params import WEAPON_POWER_BONUS
import random

# layer indices
OVERLAY = 0
UNDERLAY = 1
OL_IMAGE = 2
STATS = 3
POINTS = 4
UL_IMAGE = 5
OL_IMAGE2 = 5
NEXT_FRAME_IMG = 6
#                   overlay     underlay    image               stats       points  2nd image
weapon_outcomes = ((True,       False,      overlay_flip_flop,  'energy',   -5,     null_img),
                   (True,       False,      overlay_spray,      'hunger',   -15,    null_img),
                   (True,       False,      overlay_bleach,     'waste',    -30,    null_img),
                   (True,       False,      overlay_freeze,     'energy',   -1,     null_img),
                   (True,       False,      overlay_cat,        'power',    5,      null_img),
                   (True,       False,      overlay_ignite,     'hunger',   -5,     null_img),
                   (False,      True,       null_img,           'energy',   10,     underlay_electr_chair),
                   (True,       False,      overlay_boil,       'hunger',   -2,     null_img),
                   (True,       False,      overlay_heartbreak, 'happy',    -5,     null_img,   overlay_tear),  # anim
                   (True,       False,      overlay_vaccine,    'power',    5,      null_img),
                   (True,       False,      overlay_exist,      'happy',    -10,    null_img,   overlay_tear),  # anim
                   (True,       False,      overlay_smoking,    'hunger',   -5,     null_img),
                   (False,      True,       null_img,           'power',    5,      underlay_crucify),
                   (True,       False,      overlay_burger,     'hunger',   -60,    null_img),
                   (True,       False,      overlay_bomb,       'energy',   20,     null_img),
                   (True,       False,      overlay_roll20,     'energy',    0,     null_img),
                   (True,       False,      overlay_sword,      'energy',   -5,     null_img),
                   (True,       True,       overlay_assassin,   'energy',   -10,     underlay_assassin),
                   (True,       False,      overlay_flip_flop,  'energy',   -10,    null_img),
                   (True,       False,      overlay_flip_flop,  'energy',   -10,    null_img),
                   (True,       False,      overlay_flip_flop,  'energy',   -10,    null_img),
                   (True,       False,      overlay_flip_flop,  'energy',   -10,    null_img),
                   (True,       False,      overlay_flip_flop,  'energy',   -10,    null_img),
                   (True,       False,      overlay_flip_flop,  'energy',   -10,    null_img)
                   )
# special weapons indices
SPRAY = 1
IGNITE = 5
BOIL = 7
SMOKE = 11
BURGER = 13
HRTBRK = 8
DICE = 15
SMASH = 0
SWORD = 16

baby_weapons =          [smash_img,     spray_img,  bleach_img  ]
adult_weapons =         [freeze_img,    cat_img,    ignite_img  ]
evil_weapons =          [electr_img,    boil_img,   heartbrk_img]
superevil_weapons =     [vaxx_img,      exist_img,  smoke_img   ]
megaevil_weapons =      [cruc_img,      eat_img,    bomb_img    ]
ultraevil_weapons =     [roll_img,      swrd_img,   asasin_img  ]
zettaevil_weapons =     [smash_img,     smash_img,  smash_img   ]
insect_demon_weapons =  [smash_img,     smash_img,  smash_img   ]
all_weapons = [baby_weapons, adult_weapons, evil_weapons, superevil_weapons, megaevil_weapons,
               ultraevil_weapons, zettaevil_weapons, insect_demon_weapons]

random.seed()

def trigger_weapon(sel_colid, sel_rowid, pet, dice_result):
    using_weapon = True
    wid = (sel_colid - 4) + (3 * sel_rowid)

    # graphics
    overlay_img = weapon_outcomes[wid][OL_IMAGE]
    underlay_img = weapon_outcomes[wid][UL_IMAGE]
    overlay_img2 = weapon_outcomes[wid][OL_IMAGE2]
    has_overlay = weapon_outcomes[wid][OVERLAY]
    has_underlay = weapon_outcomes[wid][UNDERLAY]

    # points
    if dice_result != -1 and wid != (SMASH or SWORD):
        dice_result = -1
    if wid == DICE:
        dice_result = random.randint(1, 20)
        pet[weapon_outcomes[wid][STATS]] -= dice_result
    else:
        pet[weapon_outcomes[wid][STATS]] += weapon_outcomes[wid][POINTS]
    if weapon_outcomes[wid][STATS] != 'power':
        pet['power'] += WEAPON_POWER_BONUS
    return overlay_img, overlay_img2, underlay_img, using_weapon, has_overlay, has_underlay, wid, dice_result
