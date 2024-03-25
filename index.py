import requests

# 创建一个集合来存储图片链接
image_urls = set()

# 反复访问API
for _ in range(1000):  # 这里的数字可以根据需要更改
    response = requests.get('YOUR WANT API LINK(JSON')
    data = response.json()

    # 添加新的图片链接到集合中,WTF
    image_urls.update([data['IMG'] for item in data['IMG']])

# 将图片链接写入到 img.txt 文件中
with open('img.txt', 'w') as f:
    for url in image_urls:
        f.write(url + '\n')
