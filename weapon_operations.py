from graphics import *

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
                   (True,       False,      overlay_spray,      'hunger',   -5,     null_img),
                   (True,       False,      overlay_bleach,     'waste',    -10,    null_img),
                   (True,       False,      overlay_freeze,     'energy',   -1,     null_img),
                   (True,       False,      overlay_cat,        'power',    5,      null_img),
                   (True,       False,      overlay_ignite,     'hunger',   -5,     null_img),
                   (False,      True,       null_img,           'energy',   10,     underlay_electr_chair),
                   (True,       False,      overlay_boil,       'hunger',   2,      null_img),
                   (True,       False,      overlay_heartbreak, 'happy',    -5,     null_img,   overlay_tear),  # anim
                   (True,       False,      overlay_vaccine,    'power',    5,      null_img),
                   (True,       False,      overlay_exist,      'happy',    -10,    null_img,   overlay_tear),  # anim
                   (True,       False,      overlay_smoking,    'hunger',   -5,     null_img),
                   (False,      True,       null_img,           'power',    10,     underlay_crucify),
                   (True,       False,      overlay_burger,     'waste',    10,     null_img),
                   (True,       False,      overlay_bomb,       'energy',   20,     null_img),
                   (True,       False,      overlay_roll20,     'energy',   -10,    null_img),  # TODO
                   (True,       False,      overlay_flip_flop,  'energy',   -10,    null_img),
                   (True,       False,      overlay_flip_flop,  'energy',   -10,    null_img),
                   (True,       False,      overlay_flip_flop,  'energy',   -10,    null_img),
                   (True,       False,      overlay_flip_flop,  'energy',   -10,    null_img),
                   (True,       False,      overlay_flip_flop,  'energy',   -10,    null_img),
                   (True,       False,      overlay_flip_flop,  'energy',   -10,    null_img),
                   (True,       False,      overlay_flip_flop,  'energy',   -10,    null_img),
                   (True,       False,      overlay_flip_flop,  'energy',   -10,    null_img)
                   )


baby_weapons =          [smash_img,     spray_img,  bleach_img  ]
adult_weapons =         [freeze_img,    cat_img,    ignite_img  ]
evil_weapons =          [electr_img,    boil_img,   heartbrk_img]
superevil_weapons =     [vaxx_img,      exist_img,  smoke_img   ]
megaevil_weapons =      [cruc_img,      eat_img,    bomb_img    ]
ultraevil_weapons =     [roll_img,      smash_img,  smash_img   ]
zettaevil_weapons =     [smash_img,     smash_img,  smash_img   ]
insect_demon_weapons =  [smash_img,     smash_img,  smash_img   ]
all_weapons = [baby_weapons, adult_weapons, evil_weapons, superevil_weapons, megaevil_weapons,
               ultraevil_weapons, zettaevil_weapons, insect_demon_weapons]


def trigger_weapon(sel_colid, sel_rowid, pet):
    using_weapon = True
    wid = (sel_colid - 4) + (3 * sel_rowid)
    overlay_img = weapon_outcomes[wid][OL_IMAGE]
    underlay_img = weapon_outcomes[wid][UL_IMAGE]
    overlay_img2 = weapon_outcomes[wid][OL_IMAGE2]
    has_overlay = weapon_outcomes[wid][OVERLAY]
    has_underlay = weapon_outcomes[wid][UNDERLAY]
    pet[weapon_outcomes[wid][STATS]] += weapon_outcomes[wid][POINTS]
    return overlay_img, overlay_img2, underlay_img, using_weapon, has_overlay, has_underlay, wid
