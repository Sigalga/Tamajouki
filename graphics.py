import pygame
from params import DISPLAY_SIZE, SELECTOR_SIZE

def render_image(file, size):
    image = pygame.image.load(file)
    image = pygame.transform.scale(image, size)
    return image

bg_img = render_image('graphics/background.png', DISPLAY_SIZE)
selector_img = render_image('graphics/selector.png', SELECTOR_SIZE)

# life phases
egg_img = render_image('graphics/egg.png', DISPLAY_SIZE)
baby_img = render_image('graphics/baby_happy_d.png', DISPLAY_SIZE)
adult_img = render_image('graphics/adult_happy.png', DISPLAY_SIZE)
evil_img = render_image('graphics/evil.png', DISPLAY_SIZE)
superevil_img = render_image('graphics/superevil_u.png', DISPLAY_SIZE)
megaevil_img = render_image('graphics/megaevil_u.png', DISPLAY_SIZE)
ultraevil_img = render_image('graphics/ultraevil.png', DISPLAY_SIZE)
zettaevil_img = render_image('graphics/zettaevil.png', DISPLAY_SIZE)
insect_demon_img = render_image('graphics/zettaevil.png', DISPLAY_SIZE)
sewage_devil_img = render_image('graphics/sewage_devil.png', DISPLAY_SIZE)
pet_images = (egg_img, baby_img, adult_img, evil_img, superevil_img, megaevil_img,
              ultraevil_img, zettaevil_img, insect_demon_img, sewage_devil_img)
dead_img = render_image('graphics/dead.png', DISPLAY_SIZE)

# stats
stat_bg_img = render_image('graphics/stats/background.png', DISPLAY_SIZE)
hunger_img = render_image('graphics/stats/stat_hunger.png', DISPLAY_SIZE)
age_img = render_image('graphics/stats/stat_age.png', DISPLAY_SIZE)
waste_img = render_image('graphics/stats/stat_waste.png', DISPLAY_SIZE)
energy_img = render_image('graphics/stats/stat_energy.png', DISPLAY_SIZE)
happiness_img = render_image('graphics/stats/stat_happy.png', DISPLAY_SIZE)

bar_img = (render_image('graphics/stats/bar_0.png', DISPLAY_SIZE),
            render_image('graphics/stats/bar_1.png', DISPLAY_SIZE),
            render_image('graphics/stats/bar_2.png', DISPLAY_SIZE),
            render_image('graphics/stats/bar_3.png', DISPLAY_SIZE),
            render_image('graphics/stats/bar_4.png', DISPLAY_SIZE),
            render_image('graphics/stats/bar_5.png', DISPLAY_SIZE),
            render_image('graphics/stats/bar_6.png', DISPLAY_SIZE),
            render_image('graphics/stats/bar_7.png', DISPLAY_SIZE),
            render_image('graphics/stats/bar_8.png', DISPLAY_SIZE),
            render_image('graphics/stats/bar_9.png', DISPLAY_SIZE),
            render_image('graphics/stats/bar_10.png', DISPLAY_SIZE),
            render_image('graphics/stats/bar_11.png', DISPLAY_SIZE),
            render_image('graphics/stats/bar_12.png', DISPLAY_SIZE),
            render_image('graphics/stats/bar_13.png', DISPLAY_SIZE))

stat_labels = ('HUNGER', 'AGE', 'WASTE', 'ENERGY', 'HAPPINESS')
stat_keys = ('hunger', 'age', 'waste', 'energy', 'happiness')
stat_images = (hunger_img, age_img, waste_img, energy_img, happiness_img)

# options
sleep_img = render_image('graphics/option_buttons/o_sleep.png', SELECTOR_SIZE)
flush_img = render_image('graphics/option_buttons/o_clean.png', SELECTOR_SIZE)
feed_img = render_image('graphics/option_buttons/o_feed.png', SELECTOR_SIZE)
health_img = render_image('graphics/option_buttons/o_stats.png', SELECTOR_SIZE)
option_images = [feed_img, flush_img, health_img, sleep_img]

# options overlay
egg_bounce_img = render_image('graphics/egg_bounce.png', DISPLAY_SIZE)
sleep_baby_img = render_image('graphics/baby_sleep.png', DISPLAY_SIZE)
sleep_adult_img = render_image('graphics/adult_sleep.png', DISPLAY_SIZE)
sleep_evil_img = sleep_adult_img
sleep_superevil_img = render_image('graphics/superevil_sleep.png', DISPLAY_SIZE)
sleep_megaevil_img = render_image('graphics/megaevil_sleep.png', DISPLAY_SIZE)
sleep_ultraevil_img = render_image('graphics/ultraevil_sleep.png', DISPLAY_SIZE)
sleep_zettaevil_img = render_image('graphics/zettaevil_sleep.png', DISPLAY_SIZE)
sleep_insect_demon_img = render_image('graphics/insect_demon_sleep.png', DISPLAY_SIZE)
sleep_pet_images = (sleep_baby_img, sleep_adult_img, sleep_evil_img, sleep_superevil_img, sleep_megaevil_img,
                    sleep_ultraevil_img, sleep_zettaevil_img, sleep_insect_demon_img, sewage_devil_img)

# weapon options
smash_img = render_image('graphics/option_buttons/wo_smsh.png', SELECTOR_SIZE)
spray_img = render_image('graphics/option_buttons/wo_spr.png', SELECTOR_SIZE)
bleach_img = render_image('graphics/option_buttons/wo_blch.png', SELECTOR_SIZE)
freeze_img = render_image('graphics/option_buttons/wo_frz.png', SELECTOR_SIZE)
cat_img = render_image('graphics/option_buttons/wo_ct.png', SELECTOR_SIZE)
ignite_img = render_image('graphics/option_buttons/wo_ign.png', SELECTOR_SIZE)
electr_img = render_image('graphics/option_buttons/wo_elec.png', SELECTOR_SIZE)
boil_img = render_image('graphics/option_buttons/wo_bl.png', SELECTOR_SIZE)
bomb_img = render_image('graphics/option_buttons/wo_bmb.png', SELECTOR_SIZE)
cruc_img = render_image('graphics/option_buttons/wo_crc.png', SELECTOR_SIZE)
exist_img = render_image('graphics/option_buttons/wo_crisis.png', SELECTOR_SIZE)
heartbrk_img = render_image('graphics/option_buttons/wo_hrtbrk.png', SELECTOR_SIZE)
smoke_img = render_image('graphics/option_buttons/wo_smok.png', SELECTOR_SIZE)
vaxx_img = render_image('graphics/option_buttons/wo_vaxx.png', SELECTOR_SIZE)


baby_weapons = [smash_img, spray_img, bleach_img]
adult_weapons = [freeze_img, cat_img, ignite_img]
evil_weapons = [electr_img, boil_img, bomb_img]
superevil_weapons = [cruc_img, exist_img, heartbrk_img]
megaevil_weapons = [smoke_img, vaxx_img, smash_img]
ultraevil_weapons = [smash_img, smash_img, smash_img]
zettaevil_weapons = [smash_img, smash_img, smash_img]
insect_demon_weapons = [smash_img, smash_img, smash_img]
all_weapons = [baby_weapons, adult_weapons, evil_weapons, superevil_weapons, megaevil_weapons,
               ultraevil_weapons, zettaevil_weapons, insect_demon_weapons]

# nurturing overlays
overlay_sleep = render_image('graphics/n_sleep.png', DISPLAY_SIZE)
overlay_eat = render_image('graphics/n_feed.png', DISPLAY_SIZE)
overlay_clean = render_image('graphics/n_clean.png', DISPLAY_SIZE)
overlay_stink = render_image('graphics/n_stink.png', DISPLAY_SIZE)
overlay_hungry = render_image('graphics/n_hungry.png', DISPLAY_SIZE)
overlay_starving = render_image('graphics/n_starving.png', DISPLAY_SIZE)

# weapon overlays
null_img = render_image('graphics/null_img.png', DISPLAY_SIZE)
overlay_flip_flop = render_image('graphics/w_flipflop.png', DISPLAY_SIZE)
overlay_spray = render_image('graphics/w_spray.png', DISPLAY_SIZE)
overlay_bleach = render_image('graphics/w_bleach.png', DISPLAY_SIZE)
overlay_freeze = render_image('graphics/w_freeze.png', DISPLAY_SIZE)
overlay_cat = render_image('graphics/w_cat.png', DISPLAY_SIZE)
overlay_ignite = render_image('graphics/w_ignite.png', DISPLAY_SIZE)
underlay_electr_chair = render_image('graphics/w_electric_chair.png', DISPLAY_SIZE)
overlay_boil = render_image('graphics/w_boil.png', DISPLAY_SIZE)
overlay_bomb = render_image('graphics/w_bomb.png', DISPLAY_SIZE)
overlay_crucify = render_image('graphics/w_cross.png', DISPLAY_SIZE)
overlay_exist = render_image('graphics/w_exist.png', DISPLAY_SIZE)
overlay_heartbreak = render_image('graphics/w_heartbreak.png', DISPLAY_SIZE)
overlay_smoking = render_image('graphics/w_smoking.png', DISPLAY_SIZE)
overlay_vaccine = render_image('graphics/w_smoking.png', DISPLAY_SIZE)

# layer indices
OVERLAY = 0
UNDERLAY = 1
IMAGE = 2
STATS = 3
POINTS = 4
#                   overlay     underlay    image                   stats       points
weapon_outcomes = ((True,       False,      overlay_flip_flop,      'energy',   -10),
                   (True,       False,      overlay_spray,          'hunger',   -5),
                   (True,       False,      overlay_bleach,         'waste',    -50),
                   (True,       False,      overlay_freeze,         'energy',   -10),
                   (True,       False,      overlay_cat,            'power',   10),
                   (True,       False,      overlay_ignite,         'hunger',   -5),
                   (False,      True,       underlay_electr_chair,  'energy',   10),
                   (True,       False,      overlay_boil,           'hunger',   -5),
                   (True,       False,      overlay_bomb,           'energy',   10),
                   (False,      True,       overlay_crucify,        'power',    10),
                   (True,       False,      overlay_exist,          'energy',   10),
                   (True,       False,      overlay_heartbreak,     'energy',   10),
                   (True,       False,      overlay_smoking,        'energy',   10),
                   (True,       False,      overlay_vaccine,        'energy',   10)
                   )
