def drawKeys():
    global key_locations
    key_locations = []

    ## Top row
    global key_locations_top
    key_locations_top = []
    topRowX = 162
    topRowY = 532

    for i in range(0,10):
        key_locations_top.append(((topRowX + 56 * i), topRowY))

    ## Middle Row
    global key_locations_mid
    key_locations_mid = []
    midRowX = 184
    midRowY = 590

    for i in range(0,9):
        key_locations_mid.append(((midRowX + 56 * i), midRowY))

    ## Bottom Row
    global key_locations_bot
    key_locations_bot = []
    botRowX = 207
    botRowY = 645

    for i in range(0,7):
        key_locations_bot.append(((botRowX + 56 * i), botRowY))
        
    ## Whole Keyboard
    key_locations.append(key_locations_top)
    key_locations.append(key_locations_mid)
    key_locations.append(key_locations_bot)

drawKeys()
print(key_locations)
