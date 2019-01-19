import os
from aip import AipSpeech
from aip import AipNlp

""" 你的 APPID AK SK """
APP_ID = 'YOUR-APP_ID'  # 'YOUR-APP_ID'
API_KEY = 'YOUR-API_KEY'    # 'YOUR-API_KEY'
SECRET_KEY = 'YOUR-SECRET_KEY'  # 'YOUR-SECRET_KEY'

client = AipSpeech(APP_ID,API_KEY,SECRET_KEY)
# 用于将任何形式的语音文件格式转化成pcm格式
# 这里使用的是py3.6的模板语法，其他语言可以使用字符串的格式化语法


def get_file_content(filePath):
    os.system(f"ffmpeg -y -i {filePath}.mp3 -acodec pcm_s16le -f s16le -ac 1 -ar 16000 {filePath}.pcm")
    with open(f"{filePath}.pcm",'rb') as fp:
        return fp.read()


def text2audio(text):
    result = client.synthesis(text, 'zh', 1, {
        "spd": 4,
        'vol': 7,
        "pit": 8,
        "per": 4
    })

    if not isinstance(result, dict):
        # 创建一个auido.mp3文件
        with open('audio.mp3', 'wb') as f:
            f.write(result)
            return get_file_content('audio')

