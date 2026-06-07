"""
TTS_HTTP.py - 语音合成模块
功能：调用字节跳动 TTS API 将文本转换为语音，生成 OGG 音频文件
"""
from intNodeInterface import interactionNodeInterface, CyberdogResponse
import cyberdog_gpt
# coding=utf-8

'''
requires Python 3.6 or later
pip install requests
'''
import base64
import json
import uuid
import requests
import base64
import shutil
import random
import re

DEFAULT_RESPONSES = [
    CyberdogResponse("对不起，我没听清楚", "angry", 111),
    CyberdogResponse("不想搭理你", "sad", 101),
    CyberdogResponse("我感觉你说的话问题很大，我想假装听不懂", "novel_dialog", 111),
    CyberdogResponse("哈哈，你真行，把我CPU干烧喽", "happy", 143),
    CyberdogResponse("啊？啊？", "scared", 111),
]

motion_to_int = {
    '站立': 111,
    '站起来': 111,
    "坐下": 143,
    "趴下": 101,
    "慵懒地伸展身体": 146,
    "伸展身体": 146,
    "可怜地作揖": 123,
    "作揖": 123,
    "兴奋地原地踏步点头": 161,
    "原地踏步点头": 161,
    "原地转圈": 901,
    "转圈": 901,
    "走正方形": 902,
    "扭屁股": 144,
    "在地上翻滚": 903,
}

appid = "5994661922"
access_token = "F5v2xp5XcUA3EH_r4K_h0SlDD2MpDraJ"
cluster = "volcano_tts"

# voice_type = "BV104_streaming"
# voice_type = "BV120_streaming"
# voice_type = "BV021_streaming"
# voice_type = "BV002_streaming"
voice_type = "BV700_streaming"
host = "openspeech.bytedance.com"
api_url = f"https://{host}/api/v1/tts"

header = {"Authorization": f"Bearer;{access_token}"}

####convert函数
# 调用TTS API 
# 生成OGG音频文件
# 保存到指定存储路径

#convert 函数的核心功能是调用内部的 utilFunc（位于同一模块 TTS_HTTP.py 中）
# 将传入的字典数据（通常由 GPT 模型产生的回复 JSON 数据）进行处理
# 生成一个 CyberdogResponse 对象
#该对象封装了回复文本（utterance）、情感（emotion）以及动作编号（action）

#当 utilFunc 成功生成 CyberdogResponse 后
#convert 会调用传入的交互节点对象提供的 voice_callback 方法（符合 interactionNodeInterface 接口）
#将生成的 CyberdogResponse 传递出去
#这样做的目的是触发后续步骤，比如语音播放以及可能的动作执行

#CyberdogResponse类 用于封装从 GPT 回复或 TTS 处理后的最终数据
def convert(node: interactionNodeInterface, dict):
    res = utilFunc(dict)
    print(f"res.action: {res.action}")
    if not res == None:
        node.voice_callback(res)


####utilFunc(dict)
#传入的 dict 中一般包含 GPT 回复的 JSON 数据（例如包含 "response", "emotion", "action" 字段的数据）
#utilFunc 解析该数据，若成功提取出文本、情感和动作信息，就构建一个 CyberdogResponse 对象
#否则根据默认回复生成一个备用对象
def utilFunc(dataDict) -> CyberdogResponse:
    text: str = ''
    emotion: str = 'happy'
    action: int = 111
    print(dataDict)

    try:
        data = dataDict
        if 'response' in data:
            text = data['response']
            print(f"response: {text}")
        if 'emotion' in data:
            if data['emotion'] in ['happy', 'sad', 'angry', 'scare', 'hate', 'surprise']:
                emotion = data['emotion']
        if 'action' in data:
            actionLiteral = data['action']

            if isinstance(actionLiteral, int):
                action = actionLiteral
            else:
                matches = re.findall(r'\d+', actionLiteral)
                if matches:
                    action = int(matches[0])
                    print('found action.')
                elif actionLiteral in motion_to_int:
                    action = motion_to_int[actionLiteral]
                else:
                    print('not matched.')
                    action = 101
    except json.JSONDecodeError as e:

        print(e)
    except KeyError as e:
        print(e)
    finally:
        if text == "":
            print('text is none.')
            randRes = random.choice(DEFAULT_RESPONSES)
            text = randRes.utterance
            emotion = randRes.emotion
            action = randRes.action

        request_json = {
            "app": {
                "appid": appid,
                "token": "access_token",
                "cluster": cluster
            },
            "user": {
                "uid": "2100950100"
            },
            "audio": {
                "voice_type": voice_type,
                "encoding": "ogg_opus",
                "speed_ratio": 1.0,
                "volume_ratio": 1.0,
                "pitch_ratio": 1.0,
                "emotion": emotion
            },
            "request": {
                "reqid": str(uuid.uuid4()),
                "text": text,
                "text_type": "plain",
                "operation": "query",
                "with_frontend": 1,
                "frontend_type": "unitTson"
            }
        }
        try:
#使用 requests.post 方法将请求 JSON 发送至预定义的 api_url（TTS 服务端点）。
#调用 cyberdog_gpt.dPrint(resp)（调试打印函数）输出响应信息。
#检查响应 JSON 中是否含有 "data" 字段（该字段存放 base64 编码后的语音数据）。
            print(request_json)
            resp = requests.post(api_url, json.dumps(request_json), headers=header)
            cyberdog_gpt.dPrint(resp)
            if "data" in resp.json():
                data = resp.json()["data"]

                # 保存到指定路径
                target_path = "/SDCARD/sound/custom/voiceOut.ogg"
                with open("test_submit.ogg", "wb") as file_to_save:
                    file_to_save.write(base64.b64decode(data))

                # 移动文件并覆盖目标位置的原有文件
                shutil.move("test_submit.ogg", target_path)
                print(f"File moved to {target_path}")
                return CyberdogResponse(text, emotion, action)

        except Exception as e:
            print("error sending request!!!")
            print(e)
            return None
        return CyberdogResponse(text, emotion, action)


if __name__ == '__main__':
    utilFunc(None)
