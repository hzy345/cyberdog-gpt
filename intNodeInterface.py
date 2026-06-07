"""
intNodeInterface.py - 交互节点接口定义
功能：定义机器人与 GPT 交互的抽象接口
"""
from abc import ABC, abstractmethod


class CyberdogResponse:
    utterance: str
    emotion: str
    action: int

    def __init__(self, text: str, emotion: str, action: int):
        self.utterance = text
        self.emotion = emotion
        self.action = action


class interactionNodeInterface(ABC):
    @abstractmethod
    def llm_callback(self, llm_json_data: dict, usingCustomTTS: bool = True):
        pass

    @abstractmethod
    def setEmotion(self, emotion: str):
        pass

    @abstractmethod
    def setPose(self, pose: str):
        pass

    @abstractmethod
    def voice_callback(self, response: CyberdogResponse):
        pass
    #用于在语音合成或 TTS 处理完成后，将生成的回复数据传回给交互节点。
    #其他接口方法例如 llm_callback、setEmotion、setPose 等，用于进一步处理 GPT 响应和执行动作
