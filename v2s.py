# MIT License
# Copyright (c) 2024 SI Xiaolong

import whisper
import pysrt
import os
import subprocess
import sys
from opencc import OpenCC

# 检查命令行参数是否提供了视频文件路径
if len(sys.argv) != 3 and len(sys.argv) != 2:
    print("Usage: python script.py <video_file_path> [<language_code>]")
    sys.exit(1)

# 获取视频文件路径
video_file_path = sys.argv[1]

# 获取语言代码（如果提供了的话）
if len(sys.argv) == 3:
    language_code_origin = sys.argv[2]
    
    # 处理简体中文
    if language_code_origin == "zh-Hans":
        language_code = "zh"
    else:
        language_code = language_code_origin
else:
    language_code_origin = None
    language_code = None

# 确保提供的路径是有效的文件
if not os.path.isfile(video_file_path):
    print(f"Error: {video_file_path} is not a valid file.")
    sys.exit(1)

# 获取视频文件的文件名（不包括扩展名）
video_file_name = os.path.splitext(os.path.basename(video_file_path))[0]

# 获取视频文件所在目录
video_directory = os.path.dirname(video_file_path)

whisper_model = whisper.load_model("large")
result = whisper_model.transcribe(video_file_path, language=language_code)

# 创建一个新的 SRT 对象
subs = pysrt.SubRipFile()

# 遍历生成的文本结果，并将其添加到 SRT 对象中
for idx, segment in enumerate(result["segments"]):
    if segment is not None:
        # 如果识别结果包含特定文本，则丢弃该行
        if "请不吝点赞 订阅 转发 打赏支持明镜与点点栏目" in segment["text"]:
            continue
        
        # 计算 SRT 的开始和结束时间（以毫秒为单位）
        start_time = int(segment["start"] * 1000)
        end_time = int(segment["end"] * 1000)
        
        # 将生成的文本添加到 SRT 字幕中
        text = segment["text"]
        
        # 如果提供了语言代码，并且是 zh-Hans，则将繁体中文转换为简体中文
        if language_code_origin and language_code_origin == "zh-Hans":
            cc = OpenCC('t2s')  # 繁体转简体
            text = cc.convert(text)
        
        subs.append(pysrt.SubRipItem(
            index=idx+1,
            start=pysrt.SubRipTime(milliseconds=start_time),
            end=pysrt.SubRipTime(milliseconds=end_time),
            text=text
        ))

# 设置输出字幕文件的文件名（与视频文件名相同，但扩展名为.srt），并指定输出路径为视频文件所在目录
output_subtitle_path = os.path.join(video_directory, f"{video_file_name}.srt")

# 将 SRT 字幕保存到文件中
subs.save(output_subtitle_path)

print(f"字幕文件已保存为：{output_subtitle_path}")