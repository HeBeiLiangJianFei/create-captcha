from PIL import Image, ImageDraw, ImageFont
from io import BytesIO
import random


def get_random_color():
    return (random.randint(0, 255), random.randint(0, 255), random.randint(0, 255))

def create_captcha():
    """
    生成背景颜色为黑色的，5位随机字体颜色的验证码；
    图片保存名称为captcha-03.png
    :return:  返回值为：5位随机字符；data类型的图片
    """
    img = Image.new('RGB', (236, 36), (0, 0, 0))
    draw = ImageDraw.Draw(img)
    font = ImageFont.truetype('./font-family/SIMYOU.TTF', size=30)

    random_check_code = ''
    for i in range(5):
        random_num = str(random.randint(0, 9))
        random_low_alpha = chr(random.randint(97, 122))
        random_upper_alpha = chr(random.randint(65, 90))
        random_char = random.choice([random_num, random_low_alpha, random_upper_alpha])
        draw.text((i*45+15, 4), random_char,font=font)
        random_check_code +=random_char

    width=236
    height=36
    for i in range(8):
        x1=random.randint(0,width)
        x2=random.randint(0,width)
        y1=random.randint(0,height)
        y2=random.randint(0,height)
        draw.line((x1,y1,x2,y2),fill=get_random_color())

    for i in range(36):
        draw.point([random.randint(0, width), random.randint(0, height)], fill=get_random_color())
        x = random.randint(0, width)
        y = random.randint(0, height)
        draw.arc((x, y, x + 4, y + 4), 0, 90, fill=get_random_color())

    f=BytesIO()
    with open("./image/captcha-03.png", "wb") as f1:
        img.save(f1, format="png")
    img.save(f, 'png')
    data = f.getvalue()
    return data,random_check_code


if __name__ == '__main__':
    create_captcha()