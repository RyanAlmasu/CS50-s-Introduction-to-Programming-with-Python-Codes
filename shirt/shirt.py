import sys
from PIL import Image, ImageOps
from os.path import splitext

if len(sys.argv) > 3:
    sys.exit("Too many command-line arguments")
elif len(sys.argv) < 3:
    sys.exit("Too few command-line arguments")
_, ext1 = splitext(sys.argv[1])
_, ext2 = splitext(sys.argv[2])

if ext1 not in [".jpg", ".jpeg", ".png"]:
    sys.exit("Invalid Input")
if ext1 != ext2:
    sys.exit("Input and output have different extensions")

try:
    input = Image.open(sys.argv[1])

except FileNotFoundError:
    sys.exit("Input data does not exist")

im = Image.open("shirt.png")
input = ImageOps.fit(input, im.size)

input.paste(im , im)
input.save(sys.argv[2])