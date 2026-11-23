import os
import base64

def get_b64(path):
    with open(path, 'rb') as f:
        return 'data:image/png;base64,' + base64.b64encode(f.read()).decode('utf-8')

b64_nycu = get_b64('wiki/slides/assets/NYCU.png')
b64_logo2 = get_b64('wiki/slides/assets/logo2.png')
b64_image = get_b64('wiki/slides/assets/image.png')

# 建立極致專業的 26 頁 HTML 簡報生成腳本
with open('build_final_slides.py', 'w', encoding='utf-8') as f:
    pass # 稍後寫入完整內容
print("Ready to construct build_final_slides.py")
