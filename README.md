# similarity_img
图片相似度匹配

```
# 安装 Flask: pip install Flask
from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

if __name__ == '__main__':
    app.run(debug=True, port=8080)
```



```
pip install imagehash

import imagehash
from PIL import Image
 
# 加载图像
image1 = Image.open('path/to/your/image1.jpg')
image2 = Image.open('path/to/your/image2.jpg')
 
# 生成图像哈希
hash1 = imagehash.average_hash(image1)
hash2 = imagehash.average_hash(image2)
 
# 计算哈希值的汉明距离（Hamming distance）来评估相似度
similarity = hash1 - hash2
print(f"Similarity based on Hamming distance: {similarity}")
```
