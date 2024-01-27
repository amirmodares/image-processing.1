import tkinter
from PIL import Image, ImageDraw, ImageFont
import text_to_image

window = tkinter.Tk()
window.title('Watermark')
window.minsize(width=500, height=500)
window.config(padx=30, pady=30, bg="#A84448")


def get_input():
    path = input_test.get()
    with Image.open(path) as img:
        draw = ImageDraw.Draw(img)
        logo = "Amir"
        font_size = int(img.size[1] * 0.05)
        font = ImageFont.truetype("arial.ttf", size=font_size)
        text_size = draw.textsize(logo, font=font)
        x_axis = img.size[0] - text_size[0] - 30
        y_axis = img.size[1] - text_size[1] - 30
        draw.text((x_axis, y_axis), logo, font=font, fill=(120, 120, 120, 120))
        img.show()


input_test = tkinter.Entry()
input_test.pack(pady=20, padx=20)
input_test.insert(0, "photo.jpg")
btn = tkinter.Button(text='Get the Square Root', command=get_input)
btn.pack()
window.mainloop()