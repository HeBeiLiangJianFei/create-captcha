# coding=utf-8
import random
import string
import sys
import math
from PIL import Image, ImageDraw, ImageFont, ImageFilter
from io import BytesIO

# 字体的位置，不同版本的系统会有不同
font_path = './font-family/UniTortred.ttf'
# 生成几位数的验证码
number = 4
# 生成验证码图片的高度和宽度
size = (100, 50)
# 背景颜色，默认为白色
bgcolor = (255, 255, 255)
# 字体颜色，默认为蓝色
fontcolor = (0, 0, 255)
# 干扰线颜色。默认为红色
linecolor = (random.randrange(0,255), random.randrange(0,255),random.randrange(0,255))
if linecolor == (255,255,255):
    linecolor = (255,0,0)
# 是否要加入干扰线
draw_line = True
# 加入干扰线条数的上下限
line_number = random.randrange(4,8)


num = ['0','1','2','3','4','5','6','7','8','9']
alph = [chr(65+i) for i in range(26)]
ALPH = [chr(97+i) for i in range(26)]


#得到含有4个字母或数字的验证码
def random_captcha_text(size=4 ,charset=num+alph+ALPH):
    capta_text = ""
    for i in range(size):
        capta_text+=(random.choice(charset))
    return capta_text


# 用来绘制干扰线
def gene_line(draw, width, height):
    begin = (random.randint(0, width), random.randint(0, height))
    end = (random.randint(0, width), random.randint(0, height))
    draw.line([begin, end], fill=linecolor)


# 生成验证码
def gene_code():
    width, height = size  # 宽和高
    image = Image.new('RGBA', (width, height), bgcolor)  # 创建图片
    font = ImageFont.truetype(font_path, 25)  # 验证码的字体
    draw = ImageDraw.Draw(image)  # 创建画笔
    text = random_captcha_text()  # 生成字符串
    font_width, font_height = font.getsize(text)
    draw.text(((width - font_width) / number, (height - font_height) / number), text,
              font=font, fill=fontcolor)  # 填充字符串
    if draw_line:
        for i in range(line_number):
            gene_line(draw, width, height)
    # image = image.transform((width+30,height+10), Image.AFFINE, (1,-0.3,0,-0.1,1,0),Image.BILINEAR)  #创建扭曲
    # image = image.transform((width + 20, height + 10), Image.AFFINE, (1, -0.3, 0, -0.1, 1, 0), Image.BILINEAR)  # 创建扭曲
    image = image.filter(ImageFilter.EDGE_ENHANCE_MORE)  # 滤镜，边界加强
    image.save('./image/captcha-02.png')  # 保存验证码图片
    f = BytesIO()
    data = f.getvalue()
    return text,data



if __name__ == "__main__":
    print(gene_code())