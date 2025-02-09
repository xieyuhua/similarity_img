import imagehash
from PIL import Image
import os

# 计算图片的感知哈希值
def get_image_hash(image_path):
    image = Image.open(image_path)
    image_hash = imagehash.average_hash(image)
    return image_hash

# 比较两张图片的相似度
def compare_images(image_path1, image_path2):
    hash1 = get_image_hash(image_path1)
    hash2 = get_image_hash(image_path2)
    similarity = 1 - (hash1 - hash2) / len(hash1.hash) ** 2
    return similarity

# 示例
image1_path = '2.jpg'
image2_path = '22.jpg'
similarity = compare_images(image1_path, image2_path)
print(f"Similarity: {similarity}")
