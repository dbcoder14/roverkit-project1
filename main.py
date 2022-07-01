def on_button_pressed_a():
    Rover.set_brightness(255)
    Rover.set_allrgb(Rover.colors(RoverColors.VIOLET))
    basic.pause(2000)
    Rover.set_brightness(162)
    Rover.set_allrgb(Rover.colors(RoverColors.ORANGE))
    basic.pause(2000)
    Rover.set_brightness(255)
    Rover.set_allrgb(Rover.colors(RoverColors.BLUE))
    basic.pause(2000)
    Rover.set_brightness(255)
    Rover.set_rgbled(Rover.led_index(LEDIndex.LED1),
        Rover.colors(RoverColors.WHITE))
    Rover.set_rgbled(Rover.led_index(LEDIndex.LED2),
        Rover.colors(RoverColors.BLUE))
    Rover.set_rgbled(Rover.led_index(LEDIndex.LED3),
        Rover.colors(RoverColors.INDIGO))
input.on_button_pressed(Button.A, on_button_pressed_a)

def on_button_pressed_b():
    Rover.set_brightness(255)
    Rover.set_allrgb(Rover.rgb(128, 177, 255))
    basic.pause(2000)
    Rover.set_brightness(255)
    Rover.set_allrgb(Rover.show_color(0xff8000))
    basic.pause(2000)
    Rover.set_brightness(255)
    Rover.set_allrgb(Rover.rgb(128, 177, 255))
    basic.pause(2000)
    Rover.set_brightness(255)
    Rover.set_rgbled(Rover.led_index(LEDIndex.LED1),
        Rover.colors(RoverColors.RED))
    Rover.set_rgbled(Rover.led_index(LEDIndex.LED2),
        Rover.colors(RoverColors.BLUE))
    Rover.set_rgbled(Rover.led_index(LEDIndex.LED3),
        Rover.colors(RoverColors.YELLOW))
input.on_button_pressed(Button.B, on_button_pressed_b)

blue_val = 0
green_val = 0
red_val = 0
music.play_melody("C D E F G A B C5 ", 120)

def on_forever():
    basic.show_icon(IconNames.HEART)
    basic.show_icon(IconNames.SMALL_HEART)
basic.forever(on_forever)

def on_forever2():
    global red_val, green_val, blue_val
    red_val = randint(0, 255)
    green_val = randint(0, 255)
    blue_val = randint(0, 255)
    Rover.set_allrgb(Rover.rgb(red_val, green_val, blue_val))
    basic.pause(200)
basic.forever(on_forever2)
