import os
from PIL import Image
import cv2


def method_two():
    path ='/home/xcg/huang/superglue/test/'
    img_list = os.listdir(path)
    img_file = [img[:-5] for img in img_list if img[-5:] == '.jpeg']
    for img in img_file:
        img_dir = path + img + '.jpeg'
        #image = Image.open(img_dir)


        #if image.size == (1440,2560):
    #左右水平翻转
    #out =image.transpose(Image.FLIP_LEFT_RIGHT)
    #上下翻转
    #out = image.transpose(Image.FLIP_TOP_BOTTOM)
            #顺时针旋转90度
            #out = image.transpose(Image.ROTATE_90)
    #逆时针旋转45度
    #out = image.rotate(45)
            #out.save(path + img + '.jpeg','jpeg')
        img = cv2.imread(img_dir)
        print(img.size)
        imgRes = cv2.resize(img, (2560, 1440), interpolation=cv2.INTER_LINEAR)
        cv2.imwrite(img_dir, imgRes)

if __name__ == '__main__':

    method_two()
