from skimage.metrics import structural_similarity as ssim
import numpy as np
from PIL import Image
import cv2
 
# 加载图像并转换为灰度图（SSIM需要灰度图）
image1 = cv2.imread('22.jpg')
image2 = cv2.imread('2.jpg')
image1_gray = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
image2_gray = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
 
# 计算SSIM值（值越高，相似度越高）
similarity, diff = ssim(image1_gray, image2_gray, full=True)
print(f"SSIM: {similarity}")
