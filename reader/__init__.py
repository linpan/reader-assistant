from aip import AipSpeech

APP_ID = "25730658"
API_KEY = "cYu21a2cA9MiTPDCnlR0Enpr"
SECRET_KEY = "VBdFWjEoayK6tIdX1oicXSDkAHlPPlR4"

client = AipSpeech(APP_ID, API_KEY, SECRET_KEY)

# 读取文件
path = "/Users/hiro/2022/reader-assistant/reader/test2-linpan.pcm"


def get_file_content(path):
    with open(path, "rb") as fp:
        return fp.read()


if __name__ == "__main__":

    data = client.asr(
        get_file_content(path),
        "pcm",
        16000,
        {
            "dev_pid": 1537,
        },
    )
    print(data)
