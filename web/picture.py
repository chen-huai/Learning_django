from PIL import Image, ImageDraw, ImageFont, ImageFilter
import random, string

# 学习
# img = Image.new(mode='RGB', size=(120, 30), color=(255, 255, 255))
# draw = ImageDraw.Draw(img, mode='RGB')
# font = ImageFont.truetype('Monaco.ttf', 28)
# draw.text([0, 0], 'chenhuai', 'red', font=font)
# with open('code.png', 'wb') as f:
#     img.save(f, format='png')


# #获取随机4个字符组合
# def getRandomChar():
#     chr_all = string.ascii_letters+string.digits
#     chr_4 = ''.join(random.sample(chr_all,4))
#     return chr_4
# #获取随机颜色
# def getRandomColor(low,high):
#     return (random.randint(low,high),random.randint(low,high),random.randint(low,high))
# #制作验证码图片
# def getPicture():
#     width,height = 180,60
#     #创建空白画布
#     image = Image.new('RGB',(width,height),getRandomColor(20,100))
#     #验证码的字体
#     font = ImageFont.truetype('C:/Windows/fonts/stxinwei.ttf',40)
#     #创建画笔
#     draw = ImageDraw.Draw(image)
#     #获取验证码
#     char_4 = getRandomChar()
#     #向画布上填写验证码
#     for i in range(4):
#         draw.text((40*i+10,0),char_4[i],font = font,fill=getRandomColor(100,200))
#     #绘制干扰点
#     for x in range(random.randint(200,600)):
#         x = random.randint(1,width-1)
#         y = random.randint(1,height-1)
#         draw.point((x,y),fill=getRandomColor(50,150))
#     #模糊处理
#     image = image.filter(ImageFilter.BLUR)
#     image.save('./%s.jpg' % char_4)
#
# getPicture()

# 有问题
# import gvcode
# s, v = gvcode.generate()
# s.save('./%s.jpg' % v)

from captcha.image import ImageCaptcha
import random, string
def get_picture():
    chr_all = string.ascii_letters + string.digits
    chr_4 = ''.join(random.sample(chr_all, 4))
    image = ImageCaptcha().generate_image(chr_4)
    print(image)
    # image.save('./%s.jpg' % chr_4)
    return image, chr_4
# res = get_picture()
# print(res)