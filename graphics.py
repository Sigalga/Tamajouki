import pygame
from params import DISPLAY_SIZE, SELECTOR_SIZE


def render_image(file, size):
    image = pygame.image.load(file)
    image = pygame.transform.scale(image, size)
    return image


bg_img =            render_image('graphics/background.png', DISPLAY_SIZE)
selector_img =      render_image('graphics/selector.png', SELECTOR_SIZE)
null_img =          render_image('graphics/null_img.png', DISPLAY_SIZE)

# life phases
egg_img =           render_image('graphics/life_phases/egg.png', DISPLAY_SIZE)
baby_img =          render_image('graphics/life_phases/baby.png', DISPLAY_SIZE)
adult_img =         render_image('graphics/life_phases/adult.png', DISPLAY_SIZE)
evil_img =          render_image('graphics/life_phases/evil.png', DISPLAY_SIZE)
superevil_img =     render_image('graphics/life_phases/superevil.png', DISPLAY_SIZE)
megaevil_img =      render_image('graphics/life_phases/megaevil.png', DISPLAY_SIZE)
ultraevil_img =     render_image('graphics/life_phases/ultraevil.png', DISPLAY_SIZE)
zettaevil_img =     render_image('graphics/life_phases/zettaevil.png', DISPLAY_SIZE)
insect_demon_img =  render_image('graphics/life_phases/insect_demon.png', DISPLAY_SIZE)
sewage_devil_img =  render_image('graphics/life_phases/sewage_devil.png', DISPLAY_SIZE)
dead_img =          render_image('graphics/life_phases/dead.png', DISPLAY_SIZE)
pet_images = (egg_img, baby_img, adult_img, evil_img, superevil_img, megaevil_img,
              ultraevil_img, zettaevil_img, insect_demon_img, sewage_devil_img)

# life phases sleep option
egg_bounce_img =            render_image('graphics/life_phases/egg_bounce.png', DISPLAY_SIZE)
sleep_baby_img =            render_image('graphics/life_phases/baby_sleep.png', DISPLAY_SIZE)
sleep_adult_img =           render_image('graphics/life_phases/adult_sleep.png', DISPLAY_SIZE)
sleep_evil_img =            sleep_adult_img
sleep_superevil_img =       render_image('graphics/life_phases/superevil_sleep.png', DISPLAY_SIZE)
sleep_megaevil_img =        render_image('graphics/life_phases/megaevil_sleep.png', DISPLAY_SIZE)
sleep_ultraevil_img =       render_image('graphics/life_phases/ultraevil_sleep.png', DISPLAY_SIZE)
sleep_zettaevil_img =       render_image('graphics/life_phases/zettaevil_sleep.png', DISPLAY_SIZE)
sleep_insect_demon_img =    render_image('graphics/life_phases/insect_demon_sleep.png', DISPLAY_SIZE)
sleep_sewage_devil_img =    render_image('graphics/life_phases/sewage_devil_sleep.png', DISPLAY_SIZE)
sleep_pet_images = (egg_bounce_img, sleep_baby_img, sleep_adult_img, sleep_evil_img, sleep_superevil_img, sleep_megaevil_img,
                    sleep_ultraevil_img, sleep_zettaevil_img, sleep_insect_demon_img, sleep_sewage_devil_img)

# stats
stat_bg_img =       render_image('graphics/stats/background.png', DISPLAY_SIZE)
hunger_img =        render_image('graphics/stats/stat_hunger.png', DISPLAY_SIZE)
age_img =           render_image('graphics/stats/stat_age.png', DISPLAY_SIZE)
waste_img =         render_image('graphics/stats/stat_waste.png', DISPLAY_SIZE)
energy_img =        render_image('graphics/stats/stat_energy.png', DISPLAY_SIZE)
happiness_img =     render_image('graphics/stats/stat_happy.png', DISPLAY_SIZE)
stat_images =   (hunger_img, age_img, waste_img, energy_img, happiness_img)
stat_labels =   ('HUNGER', 'AGE', 'WASTE', 'ENERGY', 'HAPPINESS')
stat_keys =     ('hunger', 'age', 'waste', 'energy', 'happy')

# stat bar
bar_img =  (render_image('graphics/stats/bar_0.png', DISPLAY_SIZE),
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

# nurturing options
sleep_img =     render_image('graphics/option_buttons/o_sleep.png', SELECTOR_SIZE)
flush_img =     render_image('graphics/option_buttons/o_clean.png', SELECTOR_SIZE)
feed_img =      render_image('graphics/option_buttons/o_feed.png', SELECTOR_SIZE)
health_img =    render_image('graphics/option_buttons/o_stats.png', SELECTOR_SIZE)
option_images = [feed_img, flush_img, health_img, sleep_img]

# nurturing overlays
overlay_sleep =     render_image('graphics/n_sleep.png', DISPLAY_SIZE)
overlay_feed =       render_image('graphics/n_feed.png', DISPLAY_SIZE)
overlay_clean =     render_image('graphics/n_clean.png', DISPLAY_SIZE)
overlay_stink =     render_image('graphics/n_stink.png', DISPLAY_SIZE)
overlay_hungry =    null_img # render_image('graphics/n_hungry.png', DISPLAY_SIZE)
overlay_starving =  render_image('graphics/n_starving2.png', DISPLAY_SIZE)

# weapon options
smash_img =     render_image('graphics/option_buttons/wo_smsh.png', SELECTOR_SIZE)
spray_img =     render_image('graphics/option_buttons/wo_spr.png', SELECTOR_SIZE)
bleach_img =    render_image('graphics/option_buttons/wo_blch.png', SELECTOR_SIZE)
freeze_img =    render_image('graphics/option_buttons/wo_frz.png', SELECTOR_SIZE)
cat_img =       render_image('graphics/option_buttons/wo_ct.png', SELECTOR_SIZE)
ignite_img =    render_image('graphics/option_buttons/wo_ign.png', SELECTOR_SIZE)
electr_img =    render_image('graphics/option_buttons/wo_elec.png', SELECTOR_SIZE)
boil_img =      render_image('graphics/option_buttons/wo_bl.png', SELECTOR_SIZE)
bomb_img =      render_image('graphics/option_buttons/wo_bmb.png', SELECTOR_SIZE)
cruc_img =      render_image('graphics/option_buttons/wo_crc.png', SELECTOR_SIZE)
exist_img =     render_image('graphics/option_buttons/wo_crisis.png', SELECTOR_SIZE)
heartbrk_img =  render_image('graphics/option_buttons/wo_hrtbrk.png', SELECTOR_SIZE)
smoke_img =     render_image('graphics/option_buttons/wo_smok.png', SELECTOR_SIZE)
vaxx_img =      render_image('graphics/option_buttons/wo_vaxx.png', SELECTOR_SIZE)
#schrod_img =      render_image('graphics/option_buttons/wo_schrod.png', SELECTOR_SIZE)
eat_img =       render_image('graphics/option_buttons/wo_eat.png', SELECTOR_SIZE)
roll_img =      render_image('graphics/option_buttons/wo_rolld20.png', SELECTOR_SIZE)
swrd_img =      render_image('graphics/option_buttons/wo_sword.png', SELECTOR_SIZE)
asasin_img =    render_image('graphics/option_buttons/wo_assassin.png', SELECTOR_SIZE)

# weapon layers
overlay_flip_flop =     render_image('graphics/weapon_layers/w_flipflop.png', DISPLAY_SIZE)
overlay_spray =         render_image('graphics/weapon_layers/w_spray.png', DISPLAY_SIZE)
overlay_bleach =        render_image('graphics/weapon_layers/w_bleach.png', DISPLAY_SIZE)
overlay_freeze =        render_image('graphics/weapon_layers/w_freeze.png', DISPLAY_SIZE)
overlay_cat =           render_image('graphics/weapon_layers/w_cat.png', DISPLAY_SIZE)
overlay_ignite =        render_image('graphics/weapon_layers/w_ignite.png', DISPLAY_SIZE)
underlay_electr_chair = render_image('graphics/weapon_layers/w_electric_chair.png', DISPLAY_SIZE)
overlay_boil =          render_image('graphics/weapon_layers/w_boil.png', DISPLAY_SIZE)
overlay_bomb =          render_image('graphics/weapon_layers/w_bomb.png', DISPLAY_SIZE)
underlay_crucify =      render_image('graphics/weapon_layers/w_cross.png', DISPLAY_SIZE)
overlay_exist =         render_image('graphics/weapon_layers/w_exist1.png', DISPLAY_SIZE)
overlay_tear =          render_image('graphics/weapon_layers/w_tear.png', DISPLAY_SIZE)
overlay_heartbreak =    render_image('graphics/weapon_layers/w_heartbreak1.png', DISPLAY_SIZE)
overlay_heartbreak2 =   render_image('graphics/weapon_layers/w_heartbreak2.png', DISPLAY_SIZE)
overlay_smoking =       render_image('graphics/weapon_layers/w_smoking.png', DISPLAY_SIZE)
overlay_vaccine =       render_image('graphics/weapon_layers/w_vaxx.png', DISPLAY_SIZE)
overlay_burger =        render_image('graphics/weapon_layers/w_burger.png', DISPLAY_SIZE)
overlay_roll20 =        render_image('graphics/weapon_layers/w_roll20.png', DISPLAY_SIZE)
overlay_sword =         render_image('graphics/weapon_layers/w_sword.png', DISPLAY_SIZE)
overlay_assassin =      render_image('graphics/weapon_layers/w_assassin_ol.png', DISPLAY_SIZE)
underlay_assassin =     render_image('graphics/weapon_layers/w_assassin_ul.png', DISPLAY_SIZE)

# game over overlay
overlay_game_over = render_image('graphics/game_over.png', DISPLAY_SIZE)
welcome_img =       render_image('graphics/welcome.png', DISPLAY_SIZE)