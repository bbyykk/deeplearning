# coding: utf-8
import sys, os
sys.path.append(os.pardir)  # 愛囥佇和書頂仔仝款ê 目錄deep-learning-from-scratch/ch03/
import numpy as np
from dataset.mnist import load_mnist
from PIL import Image


def img_show(img):
    pil_img = Image.fromarray(np.uint8(img))
    pil_img.show()

(x_train, t_train), (x_test, t_test) = load_mnist(flatten=True, normalize=False)

xasis = 0
img3 = None
for i in range(20):
    img = x_train[i]
    label = t_train[i]
    print(label)  # 5
    
    if i == 0:
        img3 = img
    else:
        img3 = np.append(img3, img)

    xasis = 28 + xasis

img3 = img3.reshape(xasis, 28)  # 形状を元の画像サイズに変形
print(img3.shape)  # (28, 28)



img_show(img3)
