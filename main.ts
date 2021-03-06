input.onButtonPressed(Button.A, function () {
    Rover.setBrightness(255)
    Rover.setALLRGB(Rover.colors(RoverColors.Violet))
    basic.pause(2000)
    Rover.setBrightness(162)
    Rover.setALLRGB(Rover.colors(RoverColors.Orange))
    basic.pause(2000)
    Rover.setBrightness(255)
    Rover.setALLRGB(Rover.colors(RoverColors.Blue))
    basic.pause(2000)
    Rover.setBrightness(255)
    Rover.setRGBLED(Rover.ledIndex(LEDIndex.LED1), Rover.colors(RoverColors.White))
    Rover.setRGBLED(Rover.ledIndex(LEDIndex.LED2), Rover.colors(RoverColors.Blue))
    Rover.setRGBLED(Rover.ledIndex(LEDIndex.LED3), Rover.colors(RoverColors.Indigo))
})
input.onButtonPressed(Button.B, function () {
    Rover.setBrightness(255)
    Rover.setALLRGB(Rover.rgb(128, 177, 255))
    basic.pause(2000)
    Rover.setBrightness(255)
    Rover.setALLRGB(Rover.showColor(0xff8000))
    basic.pause(2000)
    Rover.setBrightness(255)
    Rover.setALLRGB(Rover.rgb(128, 177, 255))
    basic.pause(2000)
    Rover.setBrightness(255)
    Rover.setRGBLED(Rover.ledIndex(LEDIndex.LED1), Rover.colors(RoverColors.Red))
    Rover.setRGBLED(Rover.ledIndex(LEDIndex.LED2), Rover.colors(RoverColors.Blue))
    Rover.setRGBLED(Rover.ledIndex(LEDIndex.LED3), Rover.colors(RoverColors.Yellow))
})
let blue_val = 0
let green_val = 0
let red_val = 0
music.playMelody("C D E F G A B C5 ", 120)
basic.forever(function () {
    basic.showIcon(IconNames.Heart)
    basic.showIcon(IconNames.SmallHeart)
})
basic.forever(function () {
    red_val = randint(0, 255)
    green_val = randint(0, 255)
    blue_val = randint(0, 255)
    Rover.setALLRGB(Rover.rgb(red_val, green_val, blue_val))
    basic.pause(200)
})
