import json
import os

# 创建一个包含JSON对象的Python字典
data = {
    "text": "能给我介绍一下武汉大学吗",
    "emotion": "happy",
    "action": "sit"
}

# 将Python字典写入JSON文件
with open('data_incorrected.json', 'w') as f:
    json.dump(data, f)

os.system("python3 ./TextCorrection.py")
os.system("python3 ./cyberdog_gpt.py")

