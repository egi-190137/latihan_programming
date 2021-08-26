def find_screen_height(width, ratio): 
    ratio = ratio.split(":")
    height = int(int(ratio[1]) / int(ratio[0]) * width) 
    return str(width) + "x" + str(height)

print(find_screen_height(3840, "32:9"))