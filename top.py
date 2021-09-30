# import pygame
import random
import sys
import os
import platform

from params import *
from weapon_operations import *
from pygame.locals import *
import serial
import queue
import random
# from numpy import format_parser
# from pygame.surface import Surface, SurfaceType

if platform.system() == 'Windows':
    os.environ['SDL_VIDEODRIVER'] = 'windib'


def render_display(image_surface, color):
    pygame.draw.rect(screen, color, (DISPLAY_X, DISPLAY_Y, DISPLAY_SIZE[0], DISPLAY_SIZE[1]))   # draw rect in window
    screen.blit(image_surface, (DISPLAY_X, DISPLAY_Y))  # places the display surface in window


def render_weapons(stage):
    y = 0
    for weapon_list in all_weapons[0:stage]:    # row
        x = 256
        for weapon in weapon_list:              # columns
            render_option(x, y * SELECTOR_Y_GAP, weapon)
            x += SELECTOR_X_GAP
        y = y + 1


def render_caring():
    x = 0
    y = 0
    for option in option_images:
        render_option(x, y, option)
        x += SELECTOR_X_GAP


def render_option(x, y, image):
    feed_option = pygame.Surface(SELECTOR_SIZE)
    feed_option.fill(OPTION_COLOR)      # fills the option surface with a color
    feed_option.blit(image, (0, 0))     # overlays the option surface with an img
    color = TRANSPARENT_COLOR
    pygame.draw.rect(screen, color, (SELECTOR_X + x, SELECTOR_Y + y, SELECTOR_SIZE[0], SELECTOR_SIZE[1]))
    screen.blit(feed_option, (SELECTOR_X + x, SELECTOR_Y + y))  # places the display surface in window


def render_buttons(x, y):
    for i in range(0, 3 * BTN_GAP, BTN_GAP):
        pygame.draw.ellipse(screen, BTN_BORDER_COLOR, (x + i, y, BTN_BORDER_SIZE, BTN_BORDER_SIZE))
        pygame.draw.ellipse(screen, BTN_CENTER_COLOR, (x + i + 4, y + 4, BTN_CENTER_SIZE, BTN_CENTER_SIZE))
        pygame.draw.ellipse(screen, BTN_SHADOW_COLOR, (x + i, y, BTN_BORDER_SIZE, BTN_BORDER_SIZE), 1)


def render_debug(font, pet, stage):
    # stats board
    surf = font.render('DEBUG --', True, PIXEL_COLOR)
    screen.blit(surf, (360, 360))
    debug = (('HUNGER: %s', 'AGE: %s', 'WASTE: %d', 'ENERGY: %s', 'HAPPINESS: %s', 'POWER: %s'),
             ('hunger', 'age', 'waste', 'energy', 'happy', 'power'))
    for pos, y in enumerate(i for i in range(370, 430, 10)):
        surf = font.render(debug[0][pos] % pet[debug[1][pos]], True, PIXEL_COLOR)   # debug stats text
        screen.blit(surf, (360, y))
    surf = font.render('STAGE: %s' % stage, True, PIXEL_COLOR)
    screen.blit(surf, (360, 430))

    # stage up/down buttons
    pygame.draw.polygon(screen, BTN_BORDER_COLOR, ((DBG_BTN_X1, DBG_BTN_UP_Y2), (DBG_BTN_X2, DBG_BTN_UP_Y2),
                                                   (DBG_BTN_X3, DBG_BTN_UP_Y1)))
    pygame.draw.polygon(screen, BTN_BORDER_COLOR, ((DBG_BTN_X1, DBG_BTN_DOWN_Y1), (DBG_BTN_X2, DBG_BTN_DOWN_Y1),
                                                   (DBG_BTN_X3, DBG_BTN_DOWN_Y2)))


def do_random_event(pet):
    num = random.randint(0, 31)
    if num == 12:
        pet['hunger'] += 1
    elif num == 16:
        pet['energy'] -= 1
    elif num == 18:
        pet['energy'] += 1
    elif num == 20:
        pet['waste'] += 1
    elif num == 7:
        pet['happy'] += 1
    elif num == 4:
        pet['happy'] -= 1


def do_cycle(pet, is_game_over):
    pet['age'] += 2
    if not is_game_over:
        do_random_event(pet)
        pet['hunger'] += 1
        pet['waste'] += 1
        pet['energy'] -= 1
        if pet['waste'] >= WASTE_DIRTY:
            pet['happy'] -= 1


def trigger_sleep(stage):
    sleeping = True
    current_img = sleep_pet_images[stage]
    overlay_img = overlay_sleep
    has_overlay = True
    return current_img, overlay_img, sleeping, has_overlay


def trigger_death():
    dead = True
    current_img = dead_img
    has_overlay = has_overlay2 = has_underlay = has_dice = False
    return dead, current_img, has_overlay, has_overlay2, has_underlay, has_dice

def get_button_at_pixel(x, y):
    if BTN_Y < y < BTN_Y + BTN_BORDER_SIZE:
        button = 0
        for i in range(0, 3 * BTN_GAP, BTN_GAP):
            if BTN_X + i < x < BTN_X + BTN_BORDER_SIZE + i:
                return button
            else:
                button += 1
    if __debug__ and DBG_BTN_X1 < x < DBG_BTN_X2:
        button = 3
        if DBG_BTN_DOWN_Y1 < y < DBG_BTN_DOWN_Y2:
            button = 4
        return button
    return None


def get_keyboard_button(serial_string):
    if serial_string == "A":    # left
        button = 0
    elif serial_string == "B":  # right
        button = 2
    elif serial_string == "C":  # enter
        button = 1
    else:
        button = None
    return button


def update_serial_string(serial_port):
    # Wait until there is data waiting in the serial buffer
    if serial_port.in_waiting > 0:
        # Read data out of the buffer until a carriage return / new line is found
        serial_string = serial_port.read().decode()
    else:
        serial_string = ""
    return serial_string


def init_serial():
    # get the keyboard port
    serial_port = serial.Serial(port=SERIAL_PORT, baudrate=115200, bytesize=8, timeout=2,
                                stopbits=serial.STOPBITS_ONE)
    serial_string = str("")
    return serial_port, serial_string


def init_game():
    global screen, clock
    pygame.init()
    clock = pygame.time.Clock()
    pygame.time.set_timer(USEREVENT + 1, SECOND)

    # Create a canvas on which to display everything
    if __debug__ or not USING_KEYBOARD_BUTTONS:
        screen_height = SCREEN_HEIGHT_L
    else:
        screen_height = SCREEN_HEIGHT_S
    window_dimensions = (SCREEN_WIDTH, screen_height)
    screen = pygame.display.set_mode(window_dimensions, 0, 32)
    pygame.display.set_caption('Tamajouki')

    # init fonts
    font = pygame.font.SysFont('Arial', 14)
    stat_font = pygame.font.SysFont('ani', 45)
    return font, stat_font


def main():
    if USING_KEYBOARD_BUTTONS:
        serial_port, serial_string = init_serial()
    font, stat_font = init_game()

    # Tamajouki
    pet = {'hunger': 0, 'energy': 256, 'waste': 0, 'age': 0, 'happy': 0, 'power': 0}

    # Counters
    sel_colid = 0
    sel_rowid = 0
    statid = 0
    stage = 0
    weapon_timer = 0
    care_timer = 0

    # Flags
    has_overlay = False
    has_overlay2 = False
    has_underlay = False
    cleaning = False
    eating = False
    stats = False
    sleeping = False
    using_weapon = False
    update_game = False
    evolving = False    # enables routine points cycle and weapon options for a developing pet.
    dead = False        # removes caring and weapon options, overlays with a grave, keeps final stats.
    game_over = False   # removes weapon options and the effect of caring options on stats. sets all stats to max.

    # debug
    dbg_lvlup = False
    dbg_lvldown = False

    # Image overlays
    current_img = egg_img
    overlay_img = null_img
    underlay_img = null_img

    weapons_used = queue.Queue(2)
    weapons_used.put(-1)
    has_dice = False
    dice_result = -1

    # -------------- Game loop -----------------------------------------------------
    while True:
        if USING_KEYBOARD_BUTTONS:
            serial_string = update_serial_string(serial_port)

        screen.fill(BG_COLOR)
        mousex = 0
        mousey = 0

        # Event handler
        for event in pygame.event.get():
            if event.type == QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == MOUSEBUTTONUP:
                mousex, mousey = event.pos
            elif event.type == USEREVENT + 1 and not dead:
                update_game = True

        # Buttons logic -----------------------------------------------------
        if not USING_KEYBOARD_BUTTONS or __debug__:
            button = get_button_at_pixel(mousex, mousey)
        else:
            button = get_keyboard_button(serial_string)

        # move left
        if button == 0:
            if stats:
                statid -= 1
                if statid < 0:
                    statid = 4
            else:
                sel_colid -= 1
                if (sel_colid < 0) or (sel_rowid > 0 and sel_colid < 4):  # jump to end
                    if sel_rowid == 0:
                        if evolving:
                            sel_colid = 6
                            sel_rowid = stage - 1
                        else:
                            sel_colid = 3
                    else:
                        sel_colid = 6
                        sel_rowid = sel_rowid - 1
        # enter/exit
        elif button == 1 and not dead:
            if sel_colid == 2:          # stats
                stats = not stats
            elif stage == 0:            # non-stats options, egg stage
                current_img = egg_bounce_img
            else:                       # non-stats options
                if sel_colid == 0 and (pet['hunger'] >= HUNGER_CANEAT or game_over):        # eat
                    eating = True
                    overlay_img = overlay_feed
                    has_overlay = True
                elif sel_colid == 1 and (pet['waste'] >= WASTE_CANCLEAN or game_over):      # clean
                    cleaning = True
                    overlay_img = overlay_clean
                    has_overlay = True
                elif sel_colid == 3 and (pet['energy'] <= ENERGY_CANSLEEP or game_over):    # sleep
                    current_img, overlay_img, sleeping, has_overlay = trigger_sleep(stage)
                elif 4 <= sel_colid <= 6 and not using_weapon:                              # use weapon
                    overlay_img, overlay_img2, underlay_img, using_weapon, has_overlay, has_underlay, wid =\
                        trigger_weapon(sel_colid, sel_rowid, pet)
                    weapons_used.put(wid)
                    current_img = sleep_pet_images[stage]
                    if overlay_img == overlay_bomb:
                        screen.fill(BOMB_FILL_COLOR)
                        pygame.time.set_timer(USEREVENT + 1, SECOND)
                has_overlay2 = False
                has_dice = False
        # move right
        elif button == 2:
            if stats:
                statid += 1
                statid %= 5
            else:
                sel_colid += 1
                if evolving:
                    sel_colid %= 7
                    if sel_colid == 0:
                        sel_rowid += 1
                        sel_rowid %= stage
                        if sel_rowid > 0:
                            sel_colid = 4
                else:
                    sel_colid %= 4
        # debug stage up/down buttons
        if __debug__:
            if button == 3 and stage < 9:
                dbg_lvlup = True
                update_game = True
            elif button == 4 and stage > 0:
                dbg_lvldown = True
                update_game = True

        # Game logic -----------------------------------------------------
        if update_game:
            # debug stage up/down
            if __debug__:
                if dbg_lvlup:
                    stage += 1
                    dbg_lvlup = False
                    pet['age'] = 0
                    pet['power'] = 0
                elif dbg_lvldown:
                    stage -= 1
                    dbg_lvldown = False
                    pet['age'] = 0
                    pet['power'] = 0
                current_img = pet_images[stage]

            # life phases
            if stage == 0 and pet['age'] > AGE_HATCH:
                stage += 1
                has_overlay = has_overlay2 = has_underlay = has_dice = False
            elif stage == 1 and pet['age'] > AGE_MATURE:
                stage += 1
            elif 1 < stage < 9:
                if pet['power'] > evil_powers[stage - 2] and\
                        pet['waste'] <= WASTE_CANCLEAN and pet['hunger'] <= HUNGER_NEEDSTOEAT:  # level-up combo
                    stage += 1
            elif stage == 9:
                game_over = True
                if sel_colid > 3:
                    sel_colid = 0
                    sel_rowid = 0
                has_overlay = has_overlay2 = has_underlay = has_dice = False
                pet['hunger'] = 0
                pet['energy'] = ENERGY_FULL
                pet['waste'] = 0
                pet['happy'] = BLISSFUL
            current_img = pet_images[stage]
            if pet['age'] >= AGE_DEATHFROMNATURALCAUSES:
                dead, current_img, has_overlay, has_overlay2, has_underlay, has_dice = trigger_death()
            evolving = 0 < stage < 9

            # using options - care / weapons
            if eating:
                if care_timer >= CARE_TIME:
                    care_timer = 0
                    eating = False
                    pet['hunger'] = 0
                    pet['power'] += 1
                    has_overlay = has_overlay2 = has_underlay = has_dice = False
                    # death combo 3 ----
                    curr_wid = weapons_used.get()
                    if curr_wid == HRTBRK:
                        dead, current_img, has_overlay, has_overlay2, has_underlay, has_dice = trigger_death()
                    else:
                        weapons_used.put(curr_wid)
                    # ------------------

                else:
                    care_timer += 1
            if sleeping:
                if care_timer >= CARE_TIME:
                    care_timer = 0
                    sleeping = False
                    pet['energy'] = ENERGY_FULL
                    pet['power'] += 1
                    has_overlay = has_overlay2 = has_underlay = has_dice = False
                    current_img = pet_images[stage]
                else:
                    care_timer += 1
            if cleaning:
                if care_timer >= CARE_TIME:
                    care_timer = 0
                    cleaning = False
                    pet['waste'] = 0
                    pet['power'] += 1
                    has_overlay = has_overlay2 = has_underlay = has_dice = False
                else:
                    care_timer += 1
            if using_weapon:
                if overlay_img == overlay_roll20:
                    has_dice = True
                    if dice_result == -1:
                        dice_result = random.randint(1, 20)
                if weapon_timer >= WEAPON_TIME:
                    weapon_timer = 0
                    dice_result = -1
                    if overlay_img == overlay_heartbreak:
                        overlay_img = overlay_heartbreak2
                        overlay_img2 = overlay_tear
                        has_overlay2 = True
                    elif overlay_img == overlay_exist:
                        overlay_img = overlay_tear
                    else:
                        current_img = pet_images[stage]
                        last_wid = weapons_used.get()
                        # death combo 1 ----
                        if last_wid == SPRAY and pet['energy'] >= ENERGY_CANSLEEP and pet['waste'] >= WASTE_DIRTY:
                            curr_wid = weapons_used.get()
                            if curr_wid == IGNITE:
                                dead, current_img, has_overlay, has_overlay2, has_underlay, has_dice = trigger_death()
                            else:
                                weapons_used.put(curr_wid)
                        # death combo 2 ----
                        elif last_wid == (BOIL or SMOKE) \
                                and pet['hunger'] <= HUNGER_NEEDSTOEAT and pet['waste'] <= WASTE_DIRTY:
                            curr_wid = weapons_used.get()
                            if curr_wid == BURGER:
                                dead, current_img, has_overlay, has_overlay2, has_underlay, has_dice = trigger_death()
                            else:
                                weapons_used.put(curr_wid)
                        # ------------------
                        weapon_timer = 0
                        using_weapon = False
                        has_overlay = has_overlay2 = has_underlay = has_dice = False
                else:
                    weapon_timer += 1
                pet['power'] += 1
            else:
                # routine points add/reduce
                if not sleeping and not dead:
                    do_cycle(pet, game_over)

            if evolving and not sleeping and not cleaning and not eating and not using_weapon and not dead:
                # stink
                if pet['waste'] >= WASTE_DIRTY:
                    overlay_img = overlay_stink
                    has_overlay = True
                # hungry
                if HUNGER_SICKFROMNOTEATING > pet['hunger'] >= HUNGER_NEEDSTOEAT:
                    overlay_img2 = overlay_hungry
                    has_overlay2 = True
                # think about food
                elif pet['hunger'] >= HUNGER_SICKFROMNOTEATING:
                    overlay_img2 = overlay_starving
                    has_overlay2 = True
                # pass out
                if evolving and pet['energy'] < ENERGY_PASSOUT:
                    current_img, overlay_img, sleeping, has_overlay = trigger_sleep(stage)

            update_game = False

        # Rendering  -----------------------------------------------------
        # Render care options
        if not dead:
            render_caring()

        # Render weapon choices to appear according to stage
        if evolving and not dead:
            render_weapons(stage)

        # Render selector
        if not dead:
            screen.blit(pygame.transform.flip(selector_img, True, False),
                        (SELECTOR_X + (sel_colid * SELECTOR_X_GAP), SELECTOR_Y + (sel_rowid * SELECTOR_Y_GAP)))

        # Render display (Create a surface for pet display)
        display = pygame.Surface(DISPLAY_SIZE)

        # Render debug
        if __debug__:
            render_debug(font, pet, stage)

        # Render buttons
        if not USING_KEYBOARD_BUTTONS:
            render_buttons(BTN_X, BTN_Y)

        # Stats display logic  -----------------------------------------------------
        if stats:
            display.blit(stat_bg_img, (0, 0))
            if statid == 4:     # energy, happiness
                bar_prog = 13 - int(pet[stat_keys[statid]] * 13 / stat_bar_limits[statid])
            else:
                bar_prog = int(pet[stat_keys[statid]] * 13 / stat_bar_limits[statid])
            if bar_prog > 13:
                bar_prog = 13
            if bar_prog < 0:
                bar_prog = 0
            display.blit(stat_images[statid], (0, 0))
            if statid == 1:     # age
                text = "{}".format(pet['age'])
                stat_data = stat_font.render(text, True, STAT_COLOR)
                text_rect = stat_data.get_rect(center=(DISPLAY_WIDTH / 2, DISPLAY_WIDTH / 2 + 32))
                display.blit(stat_data, text_rect)
            else:
                display.blit(bar_img[bar_prog], (0, 0))
            render_display(display, NONPIXEL_COLOR)

        # Pet display logic
        else:
            display.blit(bg_img, (0, 0))
            if has_underlay:
                display.blit(underlay_img, (0, 0))  # underlays display with an image
            display.blit(current_img, (0, 0))       # overlays display with an image
            if has_overlay:
                display.blit(overlay_img, (0, 0))   # overlays display with an image
            if has_overlay2:
                display.blit(overlay_img2, (0, 0))  # overlays display with an image
            if has_dice:
                text = "{}".format(dice_result)
                d20 = stat_font.render(text, True, PIXEL_COLOR)
                text_rect = d20.get_rect(center=(DISPLAY_WIDTH / 2 - 55, DISPLAY_WIDTH / 2 + 45))
                display.blit(d20, text_rect)
            render_display(display, NONPIXEL_COLOR)
        pygame.display.update()
        clock.tick(FPS)


if __name__ == '__main__':
    if len(sys.argv) > 2 and sys.argv[1] == "-K":
        USING_KEYBOARD_BUTTONS = True
        SERIAL_PORT = sys.argv[2]
    main()


