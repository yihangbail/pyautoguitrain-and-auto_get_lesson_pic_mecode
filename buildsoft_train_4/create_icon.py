from PIL import Image

# 创建一个 32x32 像素的简单图标
img = Image.new('RGB', (32, 32), color='red')
img.save('app.ico', format='ICO', sizes=[(32, 32)])
print("✅ 已生成 app.ico")