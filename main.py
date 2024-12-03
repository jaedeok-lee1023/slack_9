import requests

# Slack Bot Token 및 채널 설정
SLACK_BOT_TOKEN = "xoxb-your-slack-bot-token"
SLACK_CHANNEL = "#슬랙-봇-테스트4"  # 원하는 채널 이름
FILE_PATH = "C:\\Users\\Kurly\\Downloads\\Kurly Introduction_국문_241119_aT_final"  # 전송할 파일 경로

def upload_file_to_slack(file_path, channel, token):
    """
    슬랙으로 파일 또는 이미지를 업로드하는 함수
    """
    url = "https://slack.com/api/files.upload"
    headers = {"Authorization": f"Bearer {token}"}
    data = {"channels": channel}
    files = {"file": open(file_path, "rb")}

    response = requests.post(url, headers=headers, data=data, files=files)
    if response.status_code == 200 and response.json().get("ok"):
        print("파일이 성공적으로 업로드되었습니다!")
    else:
        print("파일 업로드 실패:", response.text)

if __name__ == "__main__":
    upload_file_to_slack(FILE_PATH, SLACK_CHANNEL, SLACK_BOT_TOKEN)
