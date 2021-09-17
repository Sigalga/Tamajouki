# import pygame
import random
import sys
import os
import platform

from params import *
from graphics import *
from pygame.locals import *
import serial
# from numpy import format_parser
# from pygame.surface import Surface, SurfaceType

if platform.system() == 'Windows':
    os.environ['SDL_VIDEODRIVER'] = 'windib'


def render_display(image_surface, color):
    pygame.draw.rect(screen, color, (DISPLAY_X, DISPLAY_Y, DISPLAY_SIZE[0], DISPLAY_SIZE[1]))   # draw rect in window
    screen.blit(image_surface, (DISPLAY_X, DISPLAY_Y))  # places the display surface in window


def render_weapon(stage):
    y = 0
    for weapon_list in all_weapons[0:stage]:    # row
        x = 256
        for weapon in weapon_list:              # columns
            render_option(x, y * SELECTOR_Y_GAP, weapon)
            x += SELECTOR_X_GAP
        y = y + 1


def render_option(x, y, image):
    feed_option = pygame.Surface(SELECTOR_SIZE)
    feed_option.fill(OPTION_COLOR)      # this fills the option surface with a color
    feed_option.blit(image, (0, 0))     # this overlays the option surface with an img
    color = TRANSPARENT_COLOR
    pygame.draw.rect(screen, color, (SELECTOR_X + x, SELECTOR_Y + y, SELECTOR_SIZE[0], SELECTOR_SIZE[1]))
    screen.blit(feed_option, (SELECTOR_X + x, SELECTOR_Y + y))  # places the display surface in window


def render_buttons(x, y):
    for i in range(0, 3 * BTN_GAP, BTN_GAP):
        pygame.draw.ellipse(screen, BTN_BORDER_COLOR, (x + i, y, BTN_BORDER_SIZE, BTN_BORDER_SIZE))
        pygame.draw.ellipse(screen, BTN_CENTER_COLOR, (x + i + 4, y + 4, BTN_CENTER_SIZE, BTN_CENTER_SIZE))
        pygame.draw.ellipse(screen, BTN_SHADOW_COLOR, (x + i, y, BTN_BORDER_SIZE, BTN_BORDER_SIZE), 1)


def render_debug(font, pet):
    surf = font.render('DEBUG --', True, PIXEL_COLOR)
    screen.blit(surf, (360, 360))
    debug = (('HUNGER: %s', 'AGE: %s', 'WASTE: %d', 'ENERGY: %s', 'HAPPINESS: %s', 'POWER: %s'),
             ('hunger', 'age', 'waste', 'energy', 'happiness', 'power'))
    for pos, y in enumerate(i for i in range(370, 430, 10)):
        surf = font.render(debug[0][pos] % pet[debug[1][pos]], True, PIXEL_COLOR)   # debug stats text
        screen.blit(surf, (360, y))


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
        pet['happiness'] += 1
    elif num == 4:
        pet['happiness'] -= 1


def do_cycle(pet, is_game_over):
    pet['age'] += 2
    if not is_game_over:
        do_random_event(pet)
        pet['hunger'] += 1
        pet['waste'] += 1
        pet['energy'] -= 1
        if pet['waste'] >= WASTE_EXPUNGE:
            pet['happiness'] -= 1


def get_offset():
    return random.randint(-3, 2)


def trigger_sleep(stage):
    sleeping = True
    current_img = sleep_pet_images[stage - 1]
    overlay_img = overlay_sleep
    has_overlay = True
    return current_img, overlay_img, sleeping, has_overlay


def trigger_weapon(sel_colid, sel_rowid, pet):
    using_weapon = True
    wid = (sel_colid - 4) + (3 * sel_rowid)
    img = weapon_outcomes[wid][IMAGE]
    overlay_img = img
    underlay_img = img
    has_overlay = weapon_outcomes[wid][OVERLAY]
    has_underlay = weapon_outcomes[wid][UNDERLAY]
    pet[weapon_outcomes[wid][STATS]] += weapon_outcomes[wid][POINTS]
    return overlay_img, underlay_img, using_weapon, has_overlay, has_underlay


def get_button_at_pixel(x, y):
    if BTN_Y < y < BTN_Y + BTN_BORDER_SIZE:
        button = 0
        for i in range(0, 3 * BTN_GAP, BTN_GAP):
            if BTN_X + i < x < BTN_X + BTN_BORDER_SIZE + i:
                return button
            else:
                button += 1
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
    return clock, screen, font, stat_font


def main():
    if USING_KEYBOARD_BUTTONS:
        serial_port, serial_string = init_serial()
    global screen, clock
    clock, screen, font, stat_font = init_game()

    # Tamajouki
    pet = {'hunger': 0, 'energy': 256, 'waste': 0, 'age': 0, 'happiness': 0, 'power': 0}

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
    update_game = False
    using_weapon = False
    evolving = False
    dead = False
    game_over = False

    # Image overlays
    current_img = egg_img
    overlay_img = null_img
    underlay_img = null_img

    # Game loop
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

        # Buttons logic
        if USING_KEYBOARD_BUTTONS:
            button = get_keyboard_button(serial_string)
        else:
            button = get_button_at_pixel(mousex, mousey)

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
                    overlay_img = overlay_eat
                    has_overlay = True
                elif sel_colid == 1 and (pet['waste'] >= WASTE_CANCLEAN or game_over):      # clean
                    cleaning = True
                    overlay_img = overlay_clean
                    has_overlay = True
                elif sel_colid == 3 and (pet['energy'] <= ENERGY_CANSLEEP or game_over):    # sleep
                    current_img, overlay_img, sleeping, has_overlay = trigger_sleep(stage)
                elif 4 <= sel_colid <= 6:                                                   # use weapon
                    overlay_img, underlay_img, using_weapon, has_overlay, has_underlay =\
                        trigger_weapon(sel_colid, sel_rowid, pet)
                    if overlay_img == overlay_bomb:
                        screen.fill(BOMB_FILL_COLOR)
                        pygame.time.set_timer(USEREVENT + 1, SECOND)
                has_overlay2 = False
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

        # Game logic
        if update_game:
            # life phases
            if current_img == egg_bounce_img:
                current_img = pet_images[stage]
            if stage == 0 and pet['age'] > AGE_HATCH:
                stage += 1
                evolving = True
                current_img = pet_images[stage]
                has_overlay = has_overlay2 = has_underlay = False
            elif stage == 1 and pet['age'] > AGE_MATURE:
                stage += 1
                current_img = pet_images[stage]
            elif 1 < stage < 9:
                if pet['power'] > evil_powers[stage - 2]:
                    stage += 1
                    current_img = pet_images[stage]
            elif stage == 9:
                evolving = False
                game_over = True
                if sel_colid > 3:
                    sel_colid = 0
                    sel_rowid = 0
                has_overlay = has_overlay2 = has_underlay = False
                current_img = pet_images[stage]
                pet['hunger'] = 0
                pet['energy'] = 256
                pet['waste'] = 0
                pet['happiness'] = 256
            if pet['age'] >= AGE_DEATHFROMNATURALCAUSES:
                evolving = False
                dead = True
                current_img = dead_img
                has_overlay = has_overlay2 = has_underlay = False

            # using options - care / weapons
            if eating:
                if care_timer >= CARE_TIME:
                    care_timer = 0
                    eating = False
                    has_overlay = has_overlay2 = has_underlay = False
                    pet['hunger'] = 0
                    pet['power'] += FOOD_BONUS
                else:
                    care_timer += 1
            if sleeping:
                if care_timer >= CARE_TIME:
                    care_timer = 0
                    pet['energy'] += 8
                    if pet['energy'] >= 256:
                        sleeping = False
                        has_overlay = has_overlay2 = has_underlay = False
                        current_img = pet_images[stage]
                else:
                    care_timer += 1
            if cleaning:
                if care_timer >= CARE_TIME:
                    care_timer = 0
                    cleaning = False
                    has_overlay = has_overlay2 = has_underlay = False
                    pet['waste'] = 0
                    pet['power'] += 5
                    pygame.time.set_timer(USEREVENT + 1, SECOND)
                else:
                    care_timer += 1
            if using_weapon:
                if weapon_timer >= WEAPON_TIME:
                    weapon_timer = 0
                    using_weapon = False
                    has_overlay = has_overlay2 = has_underlay = False
                    if pet['hunger'] < 5 and pet['energy'] >= 256 and pet['waste'] < 5:     # power-up combo
                        pet['power'] += WEAPON_BONUS
                else:
                    weapon_timer += 1
            else:
                # routine points add/reduce
                if not sleeping and not dead:
                    do_cycle(pet, game_over)

            if evolving and not sleeping and not cleaning and not eating and not using_weapon:
                # stink
                if pet['waste'] >= WASTE_EXPUNGE:
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
                    pet['happiness'] -= 64
                    current_img, overlay_img, sleeping, has_overlay = trigger_sleep(stage)

            update_game = False

        # Render care options
        if not dead:
            x = 0
            y = 0
            for option in option_images:
                render_option(x, y, option)
                x += SELECTOR_X_GAP

        # Render weapon choices to appear according to stage
        if evolving:
            render_weapon(stage)

        # Render selector
        if not dead:
            screen.blit(pygame.transform.flip(selector_img, True, False),
                        (SELECTOR_X + (sel_colid * SELECTOR_X_GAP), SELECTOR_Y + (sel_rowid * SELECTOR_Y_GAP)))

        # Render display (Create a surface for pet display)
        display = pygame.Surface(DISPLAY_SIZE)

        # Stats display logic
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
            render_display(display, NONPIXEL_COLOR)

        # Render debug
        if __debug__:
            render_debug(font, pet)

        # Render buttons
        if not USING_KEYBOARD_BUTTONS:
            render_buttons(BTN_X, BTN_Y)

        pygame.display.update()
        clock.tick(FPS)


if __name__ == '__main__':
    if len(sys.argv) > 2 and sys.argv[1] == "-K":
        USING_KEYBOARD_BUTTONS = True
        SERIAL_PORT = sys.argv[2]
    main()
