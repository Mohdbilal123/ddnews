import turtle as t
import pywhatkit
img_path='E:\\ \\audiobook\\auau.jpg'
text='audiobook.txt'
pywhatkit.image_to_ascii_art(img_path, text)
print('done..')

s_x=-320
s_y=250
p=t.Pen()
t.bgcolor('black')
p.up()
p.width(2)
f_m=0
d_m=4

def set_col(c):
    chars = {"*": 'white', "S": 'green', "#": 'green', "&": 'blue'}
    col=chars[c]
    p.pencolor(col)

def d(m,s_char):
    p.up()
    if s_char!='\n':
        set_col(s_char)

    p.goto(s_x-m,s_y)
    p.down()
    p.forward(1)

text=open(text,'r')
te=text.readlines()
for i in te:
    for j in i:
        d(f_m,j)
        f_m-=4
    s_y-=9
    s_x=-320
    f_m=0
    d_m=4
t.done()
print('completed')




"""from typing import Optional

from PIL import Image


def image_to_ascii_art(
    img_path: str, output_file: Optional[str] = "pywhatkit_asciiart"
) -> str:
    """#Convert an Image to ASCII Art
"""

    img = Image.open(img_path).convert("L")

    width, height = img.size
    aspect_ratio = height / width
    new_width = 80
    new_height = aspect_ratio * new_width * 0.55
    img = img.resize((new_width, int(new_height)))

    pixels = img.getdata()

    chars = ["*", "S", "#", "&", "@", "$", "%", "*", "!", ":", "."]
    new_pixels = [chars[pixel // 25] for pixel in pixels]
    new_pixels = "".join(new_pixels)

    new_pixels_count = len(new_pixels)
    ascii_image = [
        new_pixels[index : index + new_width]
        for index in range(0, new_pixels_count, new_width)
    ]
    ascii_image = "\n".join(ascii_image)

    with open(f"{output_file}.txt", "w") as f:
        f.write(ascii_image)
    return ascii_image

"""