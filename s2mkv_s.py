import whisper
import pysrt
import os
import subprocess
import sys

# 检查命令行参数是否提供了视频文件路径
if len(sys.argv) != 2:
    print("Usage: python script.py <video_file_path>")
    sys.exit(1)

# 获取视频文件路径
video_file_path = sys.argv[1]

# 确保提供的路径是有效的文件
if not os.path.isfile(video_file_path):
    print(f"Error: {video_file_path} is not a valid file.")
    sys.exit(1)

# 获取视频文件的文件名（不包括扩展名）
video_file_name = os.path.splitext(os.path.basename(video_file_path))[0]

# 获取视频文件所在目录
video_directory = os.path.dirname(video_file_path)

# 设置输出字幕文件的文件名（与视频文件名相同，但扩展名为.srt），并指定输出路径为视频文件所在目录
output_subtitle_path = os.path.join(video_directory, f"{video_file_name}.srt")

print(f"字幕文件已保存为：{output_subtitle_path}")

# 设置输出视频文件的文件名（与视频文件名相同，但扩展名为.mkv），并指定输出路径为视频文件所在目录
output_video_path = os.path.join(video_directory, f"{video_file_name}.mkv")

# 使用 FFmpeg 合并视频和字幕为 MKV 文件（仅封装字幕）
ffmpeg_command = [
    "ffmpeg",
    "-i", video_file_path,
    "-i", output_subtitle_path,
    "-c:v", "copy",
    "-c:a", "copy",
    "-c:s", "copy",
    "-map", "0:v:0",
    "-map", "0:a:0",
    "-map", "1:s:0",
    output_video_path
]

subprocess.run(ffmpeg_command, check=True)

print(f"已将字幕封装到 MKV 文件：{output_video_path}")
