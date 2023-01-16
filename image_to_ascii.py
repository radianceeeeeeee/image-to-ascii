from PIL import Image
import numpy as np
from tkinter import filedialog

def convert(n):
    characterValues =  {0: "#",
                        16: "@",
                        32: "&",
                        48: "%",
                        64: "?",
                        80: "+",
                        96: "*",
                        112: "^",
                        128: "!",
                        144: "=",
                        160: ";",
                        176: ":",
                        192: "~",
                        208: "-",
                        224: "'",
                        240: ".",
                        256: " "}

    return characterValues[round(n/16) * 16]

# Max dimensions is 40 by 40 square- hardcoded to 40 by 40 square 
# because maximum Discord characters is at about 2000 characters
# and it's a multiple of 10
MAX_WIDTH = 40
MAX_HEIGHT = 40 

f = filedialog.askopenfilename()    # opens a GUI to pick an image
img = Image.open(f)
bw_img = img.convert("L")   # opens an image and converts it to a black and white image 

width, height = img.size

scale = width//MAX_WIDTH if width > height else height//MAX_HEIGHT      # scale is based on what's the longer side - height or width
newWidth, newHeight = width//scale, height//scale

matrix = np.array(bw_img)

hA, hB = 0, scale

for h in range(newHeight):
    wA, wB = 0, scale
    for w in range(newWidth):
        print(convert(matrix[hA:hB, wA:wB].mean()), end = "")
        wA = wB
        wB += scale
    print()
    hA = hB
    hB += scale