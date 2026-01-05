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
        header = f"*[공지｜모성보호 관련 안내]*\n\n\n"

        notice_msg = (
    f"1. *중요도* : 중\n"
    f"2. *대상* : 평택 클러스터 임직원 전체\n"
    f"3. *주요 내용*\n\n"
    f"\n"
    f"안녕하세요? 컬리 구성원 여러분!\n\n"
    f"*모성보호 제도에 대해 다음과 같이 안내 드립니다.*\n\n"
    f"\n"
    f":one: *임산부 관련 주요 안내*\n"
    f"- *임산부* 는 *임신 중인 여성* 및 *산후 1년 이내이신 분* 을 포함합니다.\n"
    f"  (근로기준법 제65조 1항)\n\n"
    f"- *임산부* 는 *고열 작업* 및 *한랭 작업(드라이 아이스 등)*, "
    f"*중량물을 취급하는 업무* 등에 근무가 *불가* 합니다.\n"
    f"  (근로기준법 제65조 2항, 근로기준법 시행령 제40조)\n\n"
    f"- *임산부* 는 *야간 근무*, *연장 근무*, *휴일 근무* 가 *불가* 합니다.\n"
    f"  (근로기준법 제70조 2항, 제74조 5항)\n\n"
    f"\n"
    f":two: *출산 축하 선물 및 휴가 안내*\n"
    f"- *본인 출산 시(출산전후휴가)* : 출산 전후 *총 90일* 사용\n"
    f"  (*미숙아 출산 시 100일*, *다태아 출산 시 120일*, "
    f"*출산 후 45일은 반드시 보장*)\n\n"
    f"- *배우자 출산 시(배우자 출산휴가)* : *20일* 사용\n"
    f"  (3회 분할 사용 가능, 출산일로부터 120일 이내 신청)\n\n"
    f"- *본인 또는 배우자 출산 시*, *출산 축하금 30만원* 지급\n"
    f"  (입사 3개월 이후 적용)\n\n"
    f"\n"
    f":three: *신청 방법 및 필요 서류*\n"
    f"- *신청 방법* : e-HR(Jade) 시스템을 통해 신청\n"
    f"- *필요 서류* : 출생증명서, 주민등록등본 등\n\n"
    f"\n"
    f"*자세한 사항은* "
    f"*<https://sites.google.com/kurlycorp.com/hr-system/%EC%9D%B8%EC%82%AC%EA%B7%BC%EB%AC%B4%EC%A0%9C%EB%8F%84/%EB%AA%A8%EC%84%B1%EB%B3%B4%ED%98%B8?authuser=0|컬리 인사잡학사전 모성보호 제도>* "
    f"*에서 확인 가능합니다.*\n\n"
    f"\n"
    f"*본인 또는 주변 구성원이 임신 중인 경우,*\n"
    f"*임산부 보호를 위해 전담 창구로 알려주시기 바랍니다.*\n"
    f"*(전담 창구 : 각 클러스터 인사총무팀)*\n\n"
    f"\n"
    f"*작은 배려* 가 큰 힘이 됩니다.\n"
    f"*서로 따뜻한 마음으로 도와주세요.*\n\n"
    f"\n"
    f"감사합니다.\n"
)

        # 메시지 본문
        body = header + notice_msg

        # 슬랙 채널에 전송
        send_slack_message(body, cluster.channel)

if __name__ == "__main__":
    main()
