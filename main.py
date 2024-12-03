import requests
import os

# 환경 변수로 토큰과 채널 ID를 가져옵니다.
SLACK_BOT_TOKEN= "your-slack-bot-token"
SLACK_CHANNEL = "#슬랙-봇-테스트4"
FILE_PATH = "C:/Users/Kurly/Downloads/Kurly Introduction_국문_241119_aT_final.pdf"  # 파일 경로

def upload_file_to_slack(file_path, channel, token):
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
            print(f"Slack API 오류: {response_data.get('error')}")
    else:
        print(f"HTTP 요청 실패: {response.status_code}, {response.text}")

if __name__ == "__main__":
    if not SLACK_BOT_TOKEN or not SLACK_CHANNEL:
        print("SLACK_BOT_TOKEN 또는 SLACK_CHANNEL 환경 변수를 설정하세요.")
    else:
        upload_file_to_slack(FILE_PATH, SLACK_CHANNEL, SLACK_BOT_TOKEN)
