import os

import arrow
from dotenv import load_dotenv
from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from kurly import clusters

# 환경 변수에서 Slack 토큰, 채널을 로드
load_dotenv()
SLACK_TOKEN = os.environ.get("SLACK_TOKEN")
def send_slack_message(message, channel):
    try:
        client = WebClient(token=SLACK_TOKEN)
        client.chat_postMessage(channel=channel, text=message)
    except SlackApiError as e:
        print(f"Error sending message to {channel} : {e}")
def main():
    for cluster in clusters:
        # 메시지 제목 설정
        header = f":loudspeaker: *『인사총무팀 공지』* <!channel>\n\n"

        notice_msg = (
            f"안녕하세요? 인사총무팀 *알리미 봇* 입니다!:smile:\n평택 클러스터 금일 *신규 입사자 사물함 배정*을 아래와 같이 공유 드립니다.\n\n"
            f"\n"
            f"\n"
            f":k체크: *락카룸 장소*는 6층에 있습니다.\n"
            f":k체크: 락카룸 배정 후 *자물쇠는 본인 지참*부탁드립니다.\n"
            f":k체크: 락카룸 내부는 *CCTV 미 설치 구역*으로 꼭! 자물쇠를 이용하여 시건 부탁드립니다.\n"
            f":k체크: *배정 받은 사물함 외 사용 불가*하오니 꼭! 배정 받은 사물함을 이용 부탁드립니다.\n"
            f":k체크: 사물함 배정은 순차적으로 진행 되며, *사유불문 하고 변경 불가* 하오니 참고 부탁드립니다.\n"
            f"\n"
            f"\n"
            f"사물함 배정 번호 등 자료는 스레드로 남겨드리오니 참고 부탁드리겠습니다.\n"
            f"\n"
            f"\n"
            f"*문의사항 : 인사총무팀 총무/시설 담당자*\n\n"
            f"감사합니다.\n"
        )
 
        # 메시지 본문
        body = header + notice_msg

        # 슬랙 채널에 전송
        send_slack_message(body, cluster.channel)

if __name__ == "__main__":
    main()
