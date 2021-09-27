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
weapon_outcomes = ((True,       False,      overlay_flip_flop,  'energy',   -10,    null_img),
                   (True,       False,      overlay_spray,      'hunger',   -5,     null_img),
                   (True,       False,      overlay_bleach,     'waste',    -50,    null_img),
                   (True,       False,      overlay_freeze,     'energy',   -10,    null_img),
                   (True,       False,      overlay_cat,        'power',    10,     null_img),
                   (True,       False,      overlay_ignite,     'hunger',   -5,     null_img),
                   (False,      True,       null_img,           'energy',   10,     underlay_electr_chair),
                   (True,       False,      overlay_boil,       'hunger',   -5,     null_img),
                   (True,       False,      overlay_bomb,       'energy',   10,     null_img),
                   (False,      True,       null_img,           'power',    10,     underlay_crucify),
                   (True,       False,      overlay_exist,      'energy',   10,     null_img,   overlay_tear), # anim
                   (True,       False,      overlay_heartbreak, 'energy',   10,     null_img,   overlay_tear), # anim
                   (True,       False,      overlay_smoking,    'energy',   10,     null_img),
                   (True,       False,      overlay_vaccine,    'energy',   10,     null_img),
                   (True,       False,      overlay_burger,     'energy',   10,     null_img),
                   (True,       False,      overlay_roll20,     'energy',   10,     null_img),
                   (True,       False,      overlay_flip_flop,  'energy',   -10,    null_img),
                   (True,       False,      overlay_flip_flop,  'energy',   -10,    null_img),
                   (True,       False,      overlay_flip_flop,  'energy',   -10,    null_img),
                   (True,       False,      overlay_flip_flop,  'energy',   -10,    null_img),
                   (True,       False,      overlay_flip_flop,  'energy',   -10,    null_img),
                   (True,       False,      overlay_flip_flop,  'energy',   -10,    null_img),
                   (True,       False,      overlay_flip_flop,  'energy',   -10,    null_img),
                   (True,       False,      overlay_flip_flop,  'energy',   -10,    null_img)
                   )


def trigger_weapon(sel_colid, sel_rowid, pet):
    using_weapon = True
    wid = (sel_colid - 4) + (3 * sel_rowid)
    overlay_img = weapon_outcomes[wid][OL_IMAGE]
    underlay_img = weapon_outcomes[wid][UL_IMAGE]
    overlay_img2 = weapon_outcomes[wid][OL_IMAGE2]
    has_overlay = weapon_outcomes[wid][OVERLAY]
    has_underlay = weapon_outcomes[wid][UNDERLAY]
    pet[weapon_outcomes[wid][STATS]] += weapon_outcomes[wid][POINTS]
    return overlay_img, overlay_img2, underlay_img, using_weapon, has_overlay, has_underlay