# Recreate a Damian Hirst point painting
# Import colorgram and extract color palette
import colorgram

colors = colorgram.extract('image.jpg', 10)
colors_list = [(color.rgb.r, color.rgb.g, color.rgb.b) for color in colors]

print(colors_list)

color_list = [(198, 12, 32), (250, 237, 17), (39, 76, 189), (38, 217, 68), (238, 227, 5), (229, 159, 46), (27, 40, 157)]