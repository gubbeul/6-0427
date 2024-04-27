noise = 0
OLED.init(128, 64)
pins.digital_write_pin(DigitalPin.P15, 0)

def on_forever():
    global noise
    OLED.clear()
    noise = Environment.read_noise(AnalogPin.P1)
    OLED.write_string("noise meter")
    OLED.new_line()
    OLED.write_string("Noise: ")
    if noise > 60:
        basic.show_icon(IconNames.NO)
        pins.digital_write_pin(DigitalPin.P15, 1)
    else:
        basic.show_icon(IconNames.YES)
        pins.digital_write_pin(DigitalPin.P15, 0)
    OLED.write_num(noise)
basic.forever(on_forever)
