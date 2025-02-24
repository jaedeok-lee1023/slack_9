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
        header = f":loudspeaker: *『인사총무팀 공지』*\n\n"

        notice_msg = (
            f"안녕하세요? 평택 클러스터 구성원 여러분!\n\n*물류 클러스터 내 모성 보호 관련 사항을 다음과 같이 안내 드립니다.*\n\n"
            f"\n"
            f":one: *임산부* 는 *임신중인 여성* 혹은 *산후 1년 이내이신분* 들을 포함합니다.\n"
            f"(근로기준법 제65조 1항)\n\n"
            f":two: *임산부* 는 *고열 작업* 및 *한랭 작업(드라이 아이스 등)*, *중량물을 취급하는 업무* 등에 근로가 *불가* 합니다.\n"
            f"(근로기준법 제65조 2항, 근로기준법 시행령 제40조)\n\n"
            f":three: *임산부* 는 *야간근로, 연장근로 및 휴일근로* 가 *불가* 합니다.\n"
            f"(근로기준법 제70조 2항, 제74조 5항)\n\n"
            f"\n"
            f"*본인 혹은 주변 동료가 임산부 이신 경우, 모성 보호를 위해 전담 창구로 말씀해주시길 바랍니다.*\n" 
            f"*(전담 창구 : 각 센터 인사총무팀)*\n\n"
            f"\n"
            f"*작은 배려* 가 큰 힘이 됩니다.\n"
            f"*미래의 희망을 위한 배려* , 아끼지 말아 주세요.\n"
            f"\n\n"
            f"기타 문의 사항은 인사총무팀 으로 연락 바랍니다.\n"
            f"*세부사항은* <https://sites.google.com/kurlycorp.com/hr-system/%EC%9D%B8%EC%82%AC%EA%B7%BC%EB%AC%B4%EC%A0%9C%EB%8F%84/%EB%AA%A8%EC%84%B1%EB%B3%B4%ED%98%B8?authuser=0|컬리 인사잡학사전 모성보호 제도> 를 *참고해주시길 바랍니다.*\n\n"
            f"*2025년 02월 23일 부터 육아지원제도가 변경 되었으며 첨부된 카드뉴스를 통해 확인 하실 수 있습니다!! <https://50072f98-e1d6-4b35-b1e5-5564ad1fcebf.usrfiles.com/ugd/50072f_763873d7e3c447c3960e863ea0b601f0.pdf|육아지원제도_변경사항_안내>* :point_left: *(Click)*\n"
            f"감사합니다.\n"
        )

        # 메시지 본문
        body = header + notice_msg

        # 슬랙 채널에 전송
        send_slack_message(body, cluster.channel)

if __name__ == "__main__":
    main()
