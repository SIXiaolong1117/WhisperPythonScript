# Whisper Python Script

一个简单的 Whisper Python 脚本，可以将媒体文件的音频通过 `whisper` 识别成文字，并通过 `pysrt` 保存为字幕。

## 依赖安装

> 需要安装 Python （在 Python 3.10.12 经过测试）

> 如果想要将字幕和媒体文件封装成 `.mkv`，还需要安装 `ffmpeg`。

```bash
git clone https://github.com/SIXiaolong1117/WhisperPythonScript.git
cd WhisperPythonScript
pip install -r requirements.txt
```

## 使用方法

- 文件 `v2s.py` 识别媒体文件的音频部分，输出 `.srt` 字幕文件。
    ```bash
    python ./v2s.py <媒体文件路径> <语言代码（可选）>
    ``` 
- 文件 `v2mkv_s.py` 识别媒体文件的音频部分，输出 `.srt` 字幕文件，并将输出的字幕文件和媒体文件封装成 `.mkv`。
    ```bash
    python ./v2mkv_s.py <媒体文件路径> <语言代码（可选）>
    ``` 
- 文件 `s2mkv_s.py` 将输出的字幕文件和媒体文件封装成 `.mkv`。
    ```bash
    python ./v2s.py <媒体文件路径>
    ``` 

## 开源许可

[MIT License](./LICENSE)