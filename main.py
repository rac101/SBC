import time
# import board
# from analogio import AnalogIn

# import random
# import microcontroller
from adafruit_circuitplayground.express import cpx

# This is a special command that will cause a single-press RESET to go
# into bootloader mode (instead of double-click) to make it easier for
# MakeCode-rs who don't intend to use CircuitPython!
# ####microcontroller.on_next_reset(microcontroller.RunMode.BOOTLOADER)

# Set this to True to turn on the capacitive touch tones
TOUCH_PIANO = True

# music scale octaves - both just and well tempered scales
just1 = (262, 294, 327, 349, 392, 436, 491, 523)
just2 = (523, 589, 654, 698, 785, 872, 981, 1047)
just3 = (1047, 1177, 1308, 1395, 1570, 1744, 1962, 2093)
well1 = (262, 294, 330, 349, 392, 440, 494, 523)
well2 = (523, 587, 659, 698, 784, 880, 988, 1047)
well3 = (1047, 1175, 1319, 1397, 1568, 1760, 1976, 2093)

# play music scales
# NOTE: I cannot distinguish between the just and well tempered scales
def play_scale(scale):
    for n in range(8):
        cpx.start_tone(scale[n])
        time.sleep(0.5)
        cpx.stop_tone()

#play_scale(just1)
#play_scale(well1)
#play_scale(just2)
#play_scale(well2)
#play_scale(just3)
#play_scale(well3)

# Define NeoPixel (R, G, B) color names
W = (25, 25, 25)
OFF = (0,  0,  0)
R = (25,  0,  0)
G = (0, 25,  0)
B = (0,  0, 25)
Y = (25, 25, 0)
C = (0, 25, 25)
M = (25, 0, 25)

# Not too bright!
cpx.pixels.brightness = 0.1

# swirling rainbow colors
def wheel(pos):
    # Input a value 0 to 255 to get a color value.
    # The colours are a transition r - g - b - back to r.
    if (pos < 0) or (pos > 255):
        return (0, 0, 0)
    if pos < 85:
        return (int(255 - pos*3), int(pos*3), 0)
    elif pos < 170:
        pos -= 85
        return (0, int(255 - (pos*3)), int(pos*3))
    else:
        pos -= 170
    return (int(pos*3), 0, int(255 - pos*3))

# This math makes a 'comet' of swirling rainbow colors!
def do_wheels(rep):
    for i in range(rep):
        for pixeln in range(10):
            for p in range(10):
                color = wheel(25 * ((pixeln + p)%10))
                cpx.pixels[p] = [int(c * ( (10 - (pixeln+p)%10)) / 10.0) for c in color]
    for i in range(10):
        cpx.pixels[i] = OFF

def light_pulse(led, colour, duration=1):
    cpx.pixels[led] = colour
    time.sleep(duration)
    cpx.pixels[led] = OFF

def light_wheel(colour, step=0.03):
    for p in range(10):
        cpx.pixels[p] = colour
        time.sleep(step)

def light_VU(colour, peak, step=0.03):
    for p in range(peak):
        mp = 9 - p
        cpx.pixels[mp] = colour
        time.sleep(step)
    time.sleep(0.1)
    for p in range(peak):
        mp = p + 10 - peak
        cpx.pixels[mp] = OFF
#        time.sleep(step)

def get_voltage(pin):
    return (pin.value * 3.3) / 65536

# show light and sound for boot indicator
cpx.pixels[9] = B
cpx.play_file("hello4.wav")   # Play a Coin sound on boot
cpx.pixels[9] = OFF

# Set up the accelerometer to detect tapping
cpx.detect_taps = 1    # detect single tap only
cpx.red_led = False  # turn off the small red LED to the right of the USB plug

AccelThreshold = 5.5   # m/s^2
sw = cpx.switch

while True:
    cpx.red_led = True       # Turns the little LED next to USB on
#    analog_in = AnalogIn(board.A1)
#    volts = get_voltage(analog_in)
    x, y, z = cpx.acceleration
    sw = cpx.switch
    print("(%0.1f, %0.1f, %0.1f, %d, %f)" % (x, y, z, sw, AccelThreshold))
#    print("(%0.1f, %0.1f, %0.1f, %0.1f)" % (x, y, z, volts))
    time.sleep(0.05)
    cpx.red_led = False      # Turns the little LED next to USB off
    time.sleep(0.05)

    # Depending on the buttons, make it more or less sensitive
    if cpx.button_a:    # make more sensitive
        AccelThreshold /= 1.2
        cpx.pixels[4] = G
        cpx.play_file("Boing.wav")
        cpx.pixels[4] = OFF

#        print("Button A pressed. Accelerometer more sensitive")
    if cpx.button_b:
        AccelThreshold *= 1.2    # make less sensitive
        cpx.pixels[5] = R
        cpx.play_file("eep.wav")
        cpx.pixels[5] = OFF
#        print("Button B pressed. Accelerometer less sensitive")

    if not sw:
        continue

    if (abs(z) > AccelThreshold):
        do_wheels(2)
        cpx.play_file("Fanfare.wav")
    #    light_wheel(OFF, step=0)
    elif (abs(z) > AccelThreshold*0.9):
        cpx.start_tone(1177)
        light_VU(M,9)
        cpx.stop_tone()
    elif (abs(z) > AccelThreshold*0.81):
        cpx.start_tone(1047)
        light_VU(B,8)
        cpx.stop_tone()
    elif (abs(z) > AccelThreshold*0.72):
        cpx.start_tone(981)
        light_VU(C,7)
        cpx.stop_tone()
    elif (abs(z) > AccelThreshold*0.63):
        cpx.start_tone(872)
        light_VU(G,6)
        cpx.stop_tone()
    elif (abs(z) > AccelThreshold*0.54):
        cpx.start_tone(785)
        light_VU(G,5)
        cpx.stop_tone()
    elif (abs(z) > AccelThreshold*0.45):
        cpx.start_tone(698)
        light_VU(Y,4)
        cpx.stop_tone()
    elif (abs(z) > AccelThreshold*0.36):
        cpx.start_tone(654)
        light_VU(Y,3)
        cpx.stop_tone()
    elif (abs(z) > AccelThreshold*0.27):
        cpx.start_tone(589)
        light_VU(R,2)
        cpx.stop_tone()
    elif (abs(z) > AccelThreshold*0.18):
        cpx.start_tone(523)
        light_VU(R,1)
        cpx.stop_tone()

   # loop to the beginning!
