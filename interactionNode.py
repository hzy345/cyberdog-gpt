import Utils
import intNodeInterface
import cyberdog_gpt

from rclpy.node import Node
from std_msgs.msg import String
from protocol.srv import AudioTextPlay
from protocol.srv import AudioVolumeGet
from protocol.srv import AudioVolumeSet
from protocol.srv import LedExecute
from protocol.srv import MotionResultCmd
from protocol.msg import MotionServoCmd
from protocol.msg import AudioPlay
from std_msgs.msg import UInt8
from std_srvs.srv import Empty
import rclpy
from functools import partial
import time
import threading
import json
from typing import List
from enum import Enum

DEBUG_MODE = False

#控制调试输出、定义LED颜色参数、限制情感状态范围
HAPPY_NECK_WHITE = (255, 255, 255)  # RGB颜色定义
HAPPY_EYE_TEAL = (10, 255, 211)
HAPPY_BUTT_YELLOW = (251, 255, 36)
SAD_EYE_ORANGE = (98, 65, 17)       # 情绪相关LED配置
SAD_NECK_PURPLE = (198, 36, 255)
SAD_BUTT_BROWN = (144, 96, 39)
EMOTION_TUPLE = ('happy', 'sad','pleased')    # 合法情感状态

# 系统操作枚举
class opEnum(Enum):
    SHUT_DOWN = 1
    SET_VOL = 2
    DANCE = 3
    FORWARD = 4
    TURN_LEFT = 5
    TURN_RIGHT = 6
    RETREAT = 7
    TURN_AROUND = 8
    SING = 9
    MUTE = 10
    FUCK_OFF = 11


class PredefinedCommand:
    def __init__(self):
        pass

# 动作指令（指令id）
class Motion(PredefinedCommand):
    motion_id: int

    def __init__(self, motion_id: int):
        self.motion_id = motion_id

# 系统操作指令（枚举）
class sysOperation(PredefinedCommand):
    opType: opEnum

    def __init__(self, opType: opEnum):
        self.opType = opType

# 指令映射表（映射成汉字）
PREDEFINED_COMMANDS = {'坐下': Motion(143),                     #动作指令映射
                       '趴下': Motion(101),
                       '站起来': Motion(111),
                       '关机': sysOperation(opEnum.SHUT_DOWN),  #系统枚举指令映射
                       '跳舞': sysOperation(opEnum.DANCE),
                       '跳个舞': sysOperation(opEnum.DANCE),
                       '前进': sysOperation(opEnum.FORWARD),
                       '后退': sysOperation(opEnum.RETREAT),
                       '左转': sysOperation(opEnum.TURN_LEFT),
                       '右转': sysOperation(opEnum.TURN_RIGHT),
                       '起立': Motion(111),
                       '闭嘴': sysOperation(opEnum.MUTE),
                       '滚蛋': sysOperation(opEnum.FUCK_OFF),
                       '转个圈': sysOperation(opEnum.TURN_AROUND),
                       '唱歌': sysOperation(opEnum.SING),
                       }

MOTION_DURATION = {
    111: 0,
    101: 0,
    102: 0,
    136: 678,
    130: 800,
    132: 800,
    131: 930,
    136: 780,
    143: 1311,
    144: 4000,
    145: 4000,
    146: 3301,
    174: 15000,
    123: 8900,
}

# ROS命名空间占位符
current_workspace_name_prefix = ""


def dprint(s):
    if DEBUG_MODE:
        print(s)


def find_current_workspace_name(node):
    global current_workspace_name_prefix
    if current_workspace_name_prefix == "":
        node_service_names = node.get_topic_names_and_types()
        for name, _ in node_service_names:
            if name.startswith("/mi_desktop"):
                parts = name.split('/')
                current_workspace_name_prefix = "/" + parts[1] + '/'
                break


def find_service_by_suffix(node, suffix):
    global current_workspace_name_prefix
    find_current_workspace_name(node)
    return current_workspace_name_prefix + suffix


class MyNode(Node, intNodeInterface.interactionNodeInterface):
    vol: int = 50
    querying_volume: bool = False
    current_emotion: str = 'happy'
    current_pose: str = '坐着'

    waiting_for_prev_to_stop: bool = False

    def __init__(self):
        super().__init__('my_node')  # type: ignore
        cyberdog_gpt.initializePrompts()# 调用cyberdog_gpt.py，初始化语言模型
        # 创建订阅和服务客户端
        self.text_subscription = self.create_subscription(
            String,
            find_service_by_suffix(self, "asr_text"),
            self.asr_callback,
            10)
        self.board_subscription = self.create_subscription(
            UInt8,
            find_service_by_suffix(self, "audio_board_state"),
            self.board_status_callback,
            10
        )
        self.speech_service = self.create_client(AudioTextPlay, find_service_by_suffix(self, "speech_text_play"))
        self.vol_set_service = self.create_client(AudioVolumeSet, find_service_by_suffix(self, "audio_volume_set"))
        self.vol_get_service = self.create_client(AudioVolumeGet, find_service_by_suffix(self, "audio_volume_get"))
        self.led_execute_service = self.create_client(LedExecute, find_service_by_suffix(self, "led_execute"))
        self.stop_playing_service = self.create_client(Empty, find_service_by_suffix(self, "stop_play"))
        self.motion_result_service = self.create_client(MotionResultCmd,
                                                        find_service_by_suffix(self, "motion_result_cmd"))
    # if not node == None:
    #     node.llm_callback()

    def setEmotion(self, emotion: str):
        self.current_emotion = emotion

    def setPose(self, pose: str):
        self.current_pose = pose

    #语音处理回调 asr_callback
    def asr_callback(self, msg):
        asrRes = msg.data   #接收语音识别结果
        print("received data: " + msg.data)

        if asrRes == '':
            self.call_volume_set_service(self.vol)
            return

        # 创建一个包含JSON对象的Python字典
        data = {
            "text": msg.data,
            "emotion": "happy",
            "action": "sit"
        }

        # 将Python字典写入JSON文件
        with open('data_incorrected.json', 'w') as f:
            json.dump(data, f)
        #调用 cyberdog_gpt.interact() 处理自然语言，生成响应（含动作、情感、文本）
        cyberdog_gpt.interact(self, asrRes, self.current_pose, self.current_emotion)

    def execute_motion(self, keyword: str, motion: int):
        if keyword == '站起来':
            print(keyword)
        self.send_motion_request(motion)

    def board_status_callback(self, msg):
        print(msg)
        if msg.data == 0:       # 播放完成
            print("Done speaking.")
            self.play_led_based_on_emotion_string(self.current_emotion)
            self.call_volume_set_service(self.vol)

        elif msg.data == 1:     # 开始识别
            print("starting to recognize....")
            self.querying_volume = True
            set_thread = threading.Thread(target=self.start_recognizing)
            self.play_listening_led()
            set_thread.start()
        elif msg.data == 2:
            print("recognition done.")
            self.play_thinking_led()
        elif msg.data == 3:
            print("beginning to speak.")
            self.play_led_based_on_emotion_string(self.current_emotion)

    #音量控制逻辑
    def start_recognizing(self):
        self.querying_volume = True
        query_thread = threading.Thread(target=self.call_volume_query_service)
        query_thread.start()

        while self.querying_volume:
            time.sleep(0.2)
            print("waiting...")
        self.call_volume_set_service(0)# 静音以提升识别精度

    def actually_send_speech_request(self, request):
        while (self.waiting_for_prev_to_stop):
            print('waiting...')
            time.sleep(0.1)

        if not isinstance(request, AudioTextPlay.Request):
            print("type not matched.")
            return
        print("sending speech request...")

        self.call_volume_set_service(self.vol)
        dprint("setting volume to original value...")

        while rclpy.ok() and self.speech_service.wait_for_service(0.2) == False:
            print("waiting for service to become available...")
        dprint("calling async request")
        self.speech_service.call_async(request)

    #异步处理与线程管理
    def send_speech_request(self, request):
        self.waiting_for_prev_to_stop = True
        # 先停止当前播放（使用 call_async 实现非阻塞服务调用）
        self.stop_playing_service.call_async(Empty.Request()).add_done_callback(self.stop_playing_callback)
        #通过线程处理音量查询等耗时操作，避免阻塞主循环
        wait_for_stop_done_thread = threading.Thread(target=partial(self.actually_send_speech_request, request))
        # 异步发送新请求
        wait_for_stop_done_thread.start()

    #动作执行，传入动作id
    def send_motion_request(self, num: int):
        # TODO: ensure num is valid
        if num == 0:
            return
        #构建 MotionResultCmd 请求，异步调用动作服务
        request = MotionResultCmd.Request()
        request.motion_id = num
        request.cmd_source = 2
        dprint(f"calling motion: {num}")
        self.motion_result_service.call_async(request).add_done_callback(self.motion_done_callback)


    def motion_done_callback(self, future):
        if DEBUG_MODE and future.done():
            msg = future.result()
            print(f"motion done: {msg}")

    def stop_playing_callback(self, msg):
        print("received callback.")
        if DEBUG_MODE and msg is not None:
            if msg.done():
                res = msg.result()
                print("got value: %d", res)
        self.waiting_for_prev_to_stop = False

    def call_volume_query_service(self):

        request: AudioVolumeGet.Request = AudioVolumeGet.Request()
        while rclpy.ok() and self.vol_get_service.wait_for_service(0.2) == False:
            print("waiting for service to become available...")

        self.vol_get_service.call_async(request).add_done_callback(self.query_callback)

    def query_callback(self, future):
        if future.done():
            msg = future.result()
            print("got value: %d", msg.volume)
            self.vol = msg.volume
        self.querying_volume = False


    def call_volume_set_service(self, vol):
        request: AudioVolumeSet.Request = AudioVolumeSet.Request()
        request.volume = vol
        while rclpy.ok() and self.vol_set_service.wait_for_service(0.2) == False:
            print("waiting for service to become available...")

        self.vol_set_service.call_async(request)    #人声识别完成后恢复原音量

# llm callback for dog to show emotion and action, but not speech
    #语言模型回调
    #解析来自 cyberdog_gpt 的JSON响应
    #更新当前情感状态，触发对应LED效果
    #若包含动作指令，调用 send_motion_request 执行
    def llm_callback(self, llm_json_data: dict, usingCustomTTS: bool = True):
        utterance: str = ""
        emotion = ""
        action = -1
        dprint("calling function llm_callback.")
        dprint(f"llm_json_data: {llm_json_data}")
        try:
            if not usingCustomTTS:
                if 'response' in llm_json_data:
                    utterance = llm_json_data['response']
                    self.call_speech_service(utterance)
                else:
                    print('no utterance found.')
            if 'emotion' in llm_json_data:
                emotion = llm_json_data['emotion']
                self.setEmotion(emotion)
            else:
                print('no emotion attribute.')
            if 'action' in llm_json_data and isinstance(llm_json_data['action'], int):
                action = llm_json_data['action']
                self.setPose(Utils.find_key_by_value(cyberdog_gpt.ACTION_COMMANDS_TO_INT, action, "无"))

        except json.JSONDecodeError as e:
            print("json data parsing unsuccessful.")
            print(e)
        except KeyError as e:
            print("missing content.")

        # if not len(utterance) == 0:
        #     self.call_speech_service(utterance)
        if not len(emotion) == 0:
            dprint("emotion:")
            dprint(emotion)
            if emotion in EMOTION_TUPLE:
                self.current_emotion = emotion
                self.play_led_based_on_emotion_string(emotion)

        if action >= 0:
            print("action: ", action)

    def voice_callback(self, res):
        request = AudioTextPlay.Request()
        request.is_online = False
        request.module_name = 'LLM'
        if not res == None:
            self.current_emotion = res.emotion
            self.send_motion_request(res.action)

        audioPlay = AudioPlay()
        audioPlay.play_id = 36000       #即合成的ogg语音文件
        request.speech = audioPlay
        self.send_speech_request(request)

    def play_thinking_led(self):
        hreq: LedExecute.Request = LedExecute.Request()
        hreq.target = 3
        hreq.occupation = True
        hreq.mode = 1
        hreq.effect = 0x33
        hreq.client = 'vp'
        self.send_led_service([hreq])

    def play_listening_led(self):
        hreq: LedExecute.Request = LedExecute.Request()
        hreq.target = 3
        hreq.client = 'vp'
        hreq.occupation = True
        hreq.mode = 2
        hreq.effect = 0x30
        hreq.r_value = 255
        hreq.g_value = 0
        hreq.b_value = 0
        self.send_led_service([hreq])

    #LED控制
    def play_led_based_on_emotion_string(self, emotion: str):
        hreq: LedExecute.Request = LedExecute.Request()
        minireq: LedExecute.Request = LedExecute.Request()
        tailreq: LedExecute.Request = LedExecute.Request()

        hreq.occupation = True
        minireq.occupation = True
        tailreq.occupation = True
        hreq.target = 1
        tailreq.target = 2
        minireq.target = 3

        if emotion == 'happy':
            self.set_led_cmd_color(HAPPY_NECK_WHITE, hreq)
            self.set_led_cmd_color(HAPPY_EYE_TEAL, minireq)
            self.set_led_cmd_color(HAPPY_BUTT_YELLOW, tailreq)
            hreq.effect = 9
            tailreq.effect = 9
            minireq.effect = 0x30

            print('emotion: happy.')
            self.send_led_service([hreq, tailreq, minireq])
        elif emotion == 'sad':
            self.set_led_cmd_color(SAD_EYE_ORANGE, minireq)
            self.set_led_cmd_color(SAD_NECK_PURPLE, hreq)
            self.set_led_cmd_color(SAD_BUTT_BROWN, tailreq)

            hreq.effect = 9
            tailreq.effect = 9
            minireq.effect = 0x30
            print('emotion: sad')
            self.send_led_service([hreq, tailreq, minireq])

    
    def set_led_cmd_color(self, color: tuple, req: LedExecute.Request):
        req.client = LedExecute.Request.VP
        req.r_value = color[0]
        req.g_value = color[1]
        req.b_value = color[2]
        req.mode = 2  # user defined

    def send_led_service(self, msgs: List[LedExecute.Request]):
        for msg in msgs:
            dprint('sending led request.')
            self.led_execute_service.call_async(msg).add_done_callback(self.led_callback)

    def led_callback(self, future):
        if DEBUG_MODE and future.done():
            msg = future.result()
            print("led callback:")
            print(msg)

    #语音合成,创建语音播放请求，设置文本内容
    #调用 send_speech_request 发送请求，包括停止当前播放的预处理
    def call_speech_service(self, speechContent: str):

        print("calling speech service...")
        request = AudioTextPlay.Request()

        request.module_name = "LLM"
        request.is_online = True  # Set to True for online play
        audioPlay = AudioPlay()
        audioPlay.module_name = 'LLM'
        audioPlay.play_id = 0
        request.speech = audioPlay  # Define your audio play info here
        request.text = speechContent
        print(f"speech content: {speechContent}")
        print(request)
        self.send_speech_request(request)


#主函数与执行入口
    #初始化ROS 2上下文。
    #创建 MyNode 实例。
    #启动ROS事件循环（spin），等待回调触发。
    #关闭时清理资源。
def main(args=None):
    rclpy.init(args=args)
    node = MyNode()
    rclpy.spin(node)
    rclpy.shutdown()


if __name__ == '__main__':
    main()
