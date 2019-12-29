    import time
    from adafruit_circuitplayground.express import cpx
     
    cpx.pixels.brightness = 0.1  # adjust brightness to your liking
     
    REGION_LEDS = (
        (5, 6, 7),  # yellow region
        (2, 3, 4),  # blue region
        (7, 8, 9),  # red region
        (0, 1, 2),  # green region
    )
     
    REGION_COLOR = (
        (255, 255, 0),  # yellow region
        (0, 0, 255),    # blue region
        (255, 0, 0),    # red region
        (0, 255, 0),    # green region
    )
     
    def light_region(region, duration=1):
        # turn the LEDs for the selected region on
        for led in REGION_LEDS[region]:
            cpx.pixels[led] = REGION_COLOR[region]
        
        # wait the requested amount of time
        time.sleep(duration)
        
        # turn the LEDs for the selected region off
        for led in REGION_LEDS[region]:
            cpx.pixels[led] = (0, 0, 0)