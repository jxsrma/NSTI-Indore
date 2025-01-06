main = 1
basinValve = 1
BasinTap = 1
basinTapShower = 0

bathroom = 0
geyser_valve = 1
geyser = True
shower = True


if main:
    print("Main Valve")

    if basinValve:
        print("-Basin Valve")
        if BasinTap:
            print("--Basin Tap")
            if basinTapShower:
                print("---Basin Shower")

    if bathroom:
        print("-Bathroom")
        if geyser_valve:
            print("--Geyser Valve")
            if geyser:
                print("---Geyser")
        if shower:
            print("--Shower")
