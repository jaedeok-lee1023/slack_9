import requests
import os

# Slack Bot Token 및 채널 설정
SLACK_BOT_TOKEN = "xoxb-4829346280432-7676013633684-81hS7JQ1XdUx3dKkVu2azKt0"  # Slack Bot Token (xoxb로 시작)
SLACK_CHANNEL = "C083DC5L2V8"  # 전송할 채널 이름 (예: #general)
FILE_PATH = "C:/Users/Kurly/Downloads/Kurly Introduction_국문_241119_aT_final.pdf"  # 전송할 파일 경로 (예: "C:/Users/Example/Documents/test.png")

def upload_file_to_slack(file_path, channel, token):
    """
    슬랙으로 파일을 업로드하는 함수
    """
    if not os.path.isfile(file_path):
        print(f"파일이 존재하지 않습니다: {file_path}")
        return

    url = "https://slack.com/api/files.upload"
    headers = {"Authorization": f"Bearer {token}"}
    data = {
        "channels": channel,
        "initial_comment": "GitHub에서 전송된 파일입니다.",
    }
    files = {"file": open(file_path, "rb")}

    response = requests.post(url, headers=headers, data=data, files=files)
    if response.status_code == 200:
        response_data = response.json()
        if response_data.get("ok"):
            print("파일이 성공적으로 업로드되었습니다!")
        else:
            print("Slack API 오류:", response_data.get("error"))
    else:
        print(f"HTTP 요청 실패: {response.status_code}, {response.text}")

if __name__ == "__main__":
    # 파일 업로드 함수 호출
    upload_file_to_slack(FILE_PATH, SLACK_CHANNEL, SLACK_BOT_TOKEN)
