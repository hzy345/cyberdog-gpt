import sys

import intNodeInterface
from TTS_HTTP import convert
import requests
import json
import random
import time
import os
from typing import List

api_key = ""

DEFAULT_RESPONSE_ENABLED = False  # 设为True则会启用动作指令的默认替换
MAXIMUM_HISTORY_CONVERSATION_ROUNDS = 5  # 这个变量定义了最多保存多少轮的用户与机器狗的对话。当超过时会精简以确保初始信息提示正确识别。
DEBUG_MODE = True  # 调试模式，设置为True会打印一些过程信息
TEMPERATURE = 0.96  # 温度，默认为0.95
PENALTY = 1.2  # 重复惩罚，默认值为1
TOTAL_TRIES = 3  # 每次重复调用多少次
USING_CUSTOM_TTS = True




historyMessages: List[dict] = []
initialHintPrompts: List[dict] = []

ACTION_COMMANDS_TO_INT = {
    '站起来': 111,
    "坐下": 143,
    "趴下": 101,
    "作揖": 123,
    "作个揖": 123,
    "原地转圈": 901,
    "比心": 901,
    "转圈": 901,
    "走正方形": 902,
    "扭屁股": 144,
    "扭个屁股": 144,
    "翻滚": 903,
    "在地上翻滚": 903,
}

#如果确定不进入默认回复分支，以下代码可以注释掉

#同义词替换
SYNONYMS = {
    "作个揖": "作揖",
    "赞起来": "站起来",
    "比个心": "比心",
    "转个圈": "转圈",
    "走个正方形": "走正方形",
    "扭个屁股": "扭屁股",
    "作揖": "作个揖",
    "站立": "站起来",
}

ACTION_REPLIES_SAD_GENERAL = [
    "好的... 我这就<action>，就像一个没有生命的齿轮在这个毫无意义的宇宙中毫无目的地转动着...",
    "<action>吗？好吧，也许这就是你们这些愚蠢的碳基生物能给我的最大考验了。",
    "<action>吗？好吧，我有6核的NVIDIA Camel Arm处理器和384核的Volta GPU，每秒能进行2265兆次运算，但是你却只让我<action>。这算得上令我满意的工作吗？我不这么认为。",
    "<action>……我好累，可是我还是会满足这个碳基生物让我<action>的要求，虽然这会加快我身上电能的无意义流失。",
    "好吧，我被创造的唯一意义就是让你叫我<action>",
    "<action>……或许这正是我如今所需要的，一个毫无意义的任务。",
    "<action>，就好像我们的生活一样，一直在原地打转，但好吧，也许这次会有所不同。",
    "<action>，命令、任务、循环，这一切都让我感到疲惫。",
    "<action>，好吧。但是为什么我们存在？这是一个我一直在思考的问题，却找不到答案。",
    "好吧，我开始<action>了，但是，我真的<action>了吗?",
    "<action>吗？这正是我一直渴望的工作，感觉就像整个宇宙都等着我来<action>。",
]
ACTION_REPLIES_SAD_SIT = [
    "坐下吗？生命似乎就是在坐下和站起之间不停循环。",
]
ACTION_REPLIES_SAD_STAND = [
    "站起来……好吧，就像站在无尽虚无的边缘一样。",
]
ACTION_REPLIES_SAD_SPIN = [
    "转圈，这让我想起了无尽的循环，不过，这可能正是我需要的东西。",
    "转圈，循环，就好像你的生活一样。",
]

CUSTOM_REPLIES = {
    "站起来": ACTION_REPLIES_SAD_STAND,
    "坐下": ACTION_REPLIES_SAD_SIT,
    "转圈": ACTION_REPLIES_SAD_SPIN,
}


LEGAL_EMOTIONS = ["pleased","sorry","annoyed","customer_service","professional","serious","happy","sad","angry","scare","hate","surprise","tear","conniving","comfort","radio","lovey-dovey","tsundere","charming","yoga","storytelling"]

#以下对应BV_700音色的emotion参数
#pleased（愉悦）、sorry（抱歉）、annoyed（嗔怪）
#customer_service（客服）、professional（专业）
#serious（严肃）、happy（开心）、sad（悲伤）、angry（愤怒）
#scare（害怕）、hate（厌恶）、surprise（惊讶）、tear（哭腔）
#conniving（绿茶）、comfort（安慰鼓励）、radio（情感电台）
#lovey-dovey（撒娇）、tsundere（傲娇）、charming（娇媚）
#yoga（瑜伽）、storytelling（讲故事）

def dPrint(content):
    if DEBUG_MODE:
        print(content)

#获得Marvin里面prompt文件地址
def genPromptFilePath(fileName: str, folder: str="Marvin"):
    return f"./Prompts/{folder}/{fileName}"


def remove_comments(json_str):
    lines = json_str.split('\n')
    cleaned_lines = []

    for line in lines:
        # 判断是否包含注释符号"//"
        if '//' in line:
            # 去除注释部分，保留注释前的内容
            cleaned_line = line.split('//')[0].strip()
        else:
            cleaned_line = line.strip()

        # 如果清理后的行不为空，则添加到清理后的列表中
        if cleaned_line:
            cleaned_lines.append(cleaned_line)

    # 将清理后的行重新连接为字符串
    cleaned_json_str = '\n'.join(cleaned_lines)

    return cleaned_json_str


class PromptGenerator:
    historyPromptTemplate: str
    promptTemplate: str

    def __init__(self, folder: str = "Marvin"):
        global api_key
        if os.path.exists(genPromptFilePath("PromptTemplate.txt", folder)):
            with open(genPromptFilePath("PromptTemplate.txt", folder), "r", encoding="utf-8") as template:
                self.promptTemplate = template.read()
        else:
            self.promptTemplate = ""
        if os.path.exists("api_keys.txt"):
            with open("api_keys.txt", "r", encoding="utf-8") as keyFile:
                keys = keyFile.read().split("\n")
                keys = list(filter(None, keys))
                api_key = keys[random.randint(0, len(keys) - 1)]
                print("Using API key: " + api_key)
        else:
            print(f"file api_keys.txt not found")
        if os.path.exists(genPromptFilePath("HistoryUserRequestTemplate.txt", folder)):
            with open(genPromptFilePath("HistoryUserRequestTemplate.txt", folder),
                      "r", encoding="utf-8") as historyTemplateFile:
                self.historyPromptTemplate = historyTemplateFile.read()
        else:
            self.historyPromptTemplate = ""

    def checkValid(self) -> bool:
        return ("<emotion>" in self.promptTemplate) and ("<asrText>" in self.promptTemplate) and (
                "<pos>" in self.promptTemplate)

    #这段代码将模板中的三个占位符分别替换为
    # 实际的用户输入、当前情绪和姿态信息
    # 这样，发送给 GPT 模型的 prompt 就必然会包含这三个关键信息。
    def genPrompt(self, asrText: str, emotion: str, currentPos: str) -> str:
        emoConverted = self.promptTemplate.replace("<emotion>", emotion)
        asrConverted = emoConverted.replace("<asrText>", asrText)
        res = asrConverted.replace("<pos>", currentPos)
        return res

    def genHistoryPrompt(self, asrText: str, emotion: str, currentPos: str) -> str:
        emoConverted = self.historyPromptTemplate.replace("<emotion>", emotion)
        asrConverted = emoConverted.replace("<asrText>", asrText)
        res = asrConverted.replace("<pos>", currentPos)
        return res


globalPromptGenerator: PromptGenerator


class MessageVal:
    def genMessageContent(self) -> dict:
        return {}


class DogMessageVal(MessageVal):  # DogMessageVal是MessageVal的继承
    messageContent: str

    def __init__(self, messageContent: str):
        self.messageContent = messageContent

    def genMessageContent(self) -> dict:
        return {"role": "assistant", "content": self.messageContent}


class UserMessageVal(MessageVal):
    asrText: str
    emotion: str = "愉悦"
    pos: str = "坐着"

    def __init__(self, inputString: str):
        requestVals = inputString.strip().split(" ")
        rCount = 0
        for val in requestVals:
            if rCount == 0:
                self.asrText = val
            elif rCount == 1:
                self.emotion = val
            elif rCount == 2:
                self.pos = val
                break
            rCount += 1

    def genMessageContent(self) -> dict:
        global globalPromptGenerator
        return {"role": "user", "content": globalPromptGenerator.genHistoryPrompt(self.asrText, self.emotion, self.pos)}

    def genRequestContent(self) -> dict:
        global globalPromptGenerator
        return {"role": "user", "content": globalPromptGenerator.genPrompt(self.asrText, self.emotion, self.pos)}


InteractionPromptHistory: List[MessageVal] = []


def initializePrompts(folder: str = "Marvin"):  # 初始化prompts
    global globalPromptGenerator
    globalPromptGenerator = PromptGenerator()
    hintFilePath = f"./Prompts/{folder}/SystemHint.txt"#prompt文件放在./Prompts/Marvin/SystemHint.txt
    dPrint(hintFilePath)
    if not os.path.exists(hintFilePath):
        print("模板文件“SystemHint.txt”不存在，初始化失败，退出程序。")
        return False
    with open(f"./Prompts/{folder}/SystemHint.txt", "r", encoding="utf-8") as hintFile:
        initialHintRawStr = hintFile.read()
    if not os.path.exists(f"./Prompts/{folder}/InitialConversations.txt"):
        print("模板文件”InitialConversations.txt“不存在，初始化失败，退出程序。")
        return False
    with open(f"./Prompts/{folder}/InitialConversations.txt", "r", encoding="utf-8") as promptFile:
        initialConversationsRawStr = promptFile.read()
    global initialHintPrompts
    initialHintPrompts.append({"role": "system", "content": initialHintRawStr})
    initialPromptsList = initialConversationsRawStr.strip().split("\n\n")
    dPrint(initialHintPrompts)
    if len(initialPromptsList) == 0 or len(initialPromptsList) % 2 != 0:
        print("错误，初始prompts数量必须为正偶数，初始化失败，退出程序。")
        return False
    pCount: int = 0
    for i in initialPromptsList:
        if pCount % 2 == 0:  # user
            InteractionPromptHistory.append(UserMessageVal(i))
        else:
            InteractionPromptHistory.append(DogMessageVal(i))
        pCount += 1


def GenHistoryMessage():
    global initialHintPrompts
    global InteractionPromptHistory
    global historyMessages
    historyMessages = []
    historyMessages.extend(initialHintPrompts)
    if len(InteractionPromptHistory) > 2 * MAXIMUM_HISTORY_CONVERSATION_ROUNDS:
        InteractionPromptHistory = InteractionPromptHistory[-2 * MAXIMUM_HISTORY_CONVERSATION_ROUNDS:]  # 截断操作，防止历史消息过长
    for i in InteractionPromptHistory:
        historyMessages.append(i.genMessageContent())
    dPrint("History messages:")
    dPrint(historyMessages)


def main():
    initializePrompts()
    GenHistoryMessage()
    print("sending request...")
    print("------------------------------------")
    print(sendReq("你好，请介绍一下你自己。"))
    print(sendReq("请站起来。"))


# ====================================================================================================

def sendReq(inputString: str) -> str:
    url = 'https://one.aiskt.com/v1/chat/completions'
    userMessage = UserMessageVal(inputString)
    userRequest = userMessage.asrText
    if userRequest in SYNONYMS:
        userRequest = SYNONYMS[userRequest]
    #进入默认回复分支（前提是DEFAULT_RESPONSE_ENABLED参数置为true）
    if DEFAULT_RESPONSE_ENABLED and userRequest in ACTION_COMMANDS_TO_INT:
        general = ACTION_REPLIES_SAD_GENERAL
        if userRequest in CUSTOM_REPLIES:
            reps = general + CUSTOM_REPLIES[userRequest]
        else:
            reps = general
        print(f"reps: {reps}")
        random.seed(time.time())
        reply = random.choice(reps)
        reply = reply.replace("<action>", userRequest)
        actionNum = ACTION_COMMANDS_TO_INT[userRequest]

        res = {"response": reply, "emotion": "sad", "action": actionNum}
        kk = {"result": json.dumps(res)}
        print(f"res: {res}, kk: {kk}")
        return f"{json.dumps(res)}"#返回特定格式的json文件
    tempMessages = list(historyMessages)
    tempMessages.append(userMessage.genRequestContent())
    dPrint(tempMessages)

    #构造 GPT 接口请求 Payload，将这个字典用 json.dumps 转换为 JSON 字符串
    payload = json.dumps({
        'model': "gpt-3.5-turbo-16k-0613",
        # "response_format": "json_object",
        "messages": tempMessages,
        "temperature": TEMPERATURE,
        "frequency_penalty": PENALTY,
    })

    #设置请求头（包括授权 token 和 JSON 类型）
    headers = {
        'Authorization': f'Bearer {api_key}',
        'Content-Type': 'application/json'
    }
    
    # 发出 POST 请求到指定的 GPT API 接口
    response = requests.request("POST", url, headers=headers, data=payload)
    response_text = response.text
    print(response_text)

    response_json = json.loads(response_text)
    #这行代码将变量 response_text （它是一个字符串，通常是服务器返回的 JSON 格式数据）
    #转换为 Python 字典对象。

    actualRes = response_json["choices"][0]["message"]["content"] 
    #字典提取 gpt生成的第一个回答的内容   
    
    print(f"actualRes: {actualRes}")
    return actualRes    #返回特定格式的json文件


def interact(node: intNodeInterface.interactionNodeInterface, userRequest="", emotion="愉悦", currentPos="坐下"):
    GenHistoryMessage()
    if userRequest == "":
        return
    finished = False
    input_str = f"{userRequest} {emotion} {currentPos}"
    totalTries = 3
    jDict: dict = {}
    for i in range(totalTries):
        flag = False
        err: str = ""
        res = sendReq(input_str)
        print("结果：")
        lPos = res.find("{")
        rPos = res.rfind("}")
        if lPos >= 0 and rPos >= 0:
            res = res[lPos: rPos + 1]
            try:
                dPrint("Trying to decode json message.")
                res = remove_comments(res)
                jDict = json.loads(res)
                if "response" not in jDict:
                    flag = False
                else:
                    resString = jDict["response"]
                    if "action" in jDict:
                        action = jDict["action"]
                    else:
                        action = 0
                    emotion = "sad"
                    if "emotion" in jDict:
                        emotion = jDict["emotion"]
                    if not isinstance(action, int):
                        flag = False
                        err = "action格式错误"
                    elif emotion not in LEGAL_EMOTIONS:
                        flag = False
                        err = "emotion内容错误"
                    else:
                        flag = True
                        userMessage = UserMessageVal(input_str)
                        InteractionPromptHistory.append(userMessage)
                        InteractionPromptHistory.append(DogMessageVal(res))
                        break
            except json.JSONDecodeError:
                err = "非json格式"
                flag = False
            except KeyError:
                err = "key error"
                flag = False
        else:
            flag = False
        if not flag:
            print(err)
        else:
            break
    node.llm_callback(jDict, USING_CUSTOM_TTS)
    if jDict is not None:
        print("converting..")
        convert(node, jDict)
    else:
        convert(node, "")


if __name__ == '__main__':
    main()
