let noise = 0
OLED.init(128, 64)
pins.digitalWritePin(DigitalPin.P15, 0)
basic.forever(function () {
    OLED.clear()
    noise = Environment.ReadNoise(AnalogPin.P1)
    OLED.writeString("noise meter")
    OLED.newLine()
    OLED.writeString("Noise: ")
    if (noise > 60) {
        basic.showIcon(IconNames.No)
        pins.digitalWritePin(DigitalPin.P15, 1)
    } else {
        basic.showIcon(IconNames.Yes)
        pins.digitalWritePin(DigitalPin.P15, 0)
    }
    OLED.writeNum(noise)
})
