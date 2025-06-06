from openai import OpenAI
import os
from dotenv import load_dotenv
import json

# .env 파일에서 환경 변수 로드
load_dotenv()

# API 키 환경 변수에서 가져오기
api_key = os.environ.get("OPENAI_API_KEY")
if not api_key:
    print("오류: OPENAI_API_KEY 환경 변수가 설정되지 않았습니다.")
    print("프로젝트 루트에 .env 파일을 생성하고 다음 내용을 추가하세요:")
    print("OPENAI_API_KEY=your-api-key-here")
    exit(1)

# OpenAI 클라이언트 초기화
client = OpenAI(api_key=api_key)

def test_openai_api():
    try:
        # GPT 모델 API 호출
        print("OpenAI API에 요청을 보내는 중...")
        
        response = client.chat.completions.create(
            model="gpt-4o",
            temperature=1, # 무작위성 조절, 실제론 나온 확률을 나누니까 1이면 그대로, 그 외는 무작위성 커짐
            messages=[ # 과거 대화 기반 적절한 응답에 필요한 매개변수
                {"role": "system", "content": "You are a helpful assistant."}, # 시스템 메시지, 모델의 행동 방식 정의
                {"role": "user", "content": "2022년 월드컵 우승 팀은 어디인가?"} # 사용자 메시지, 모델에게 제공할 입력 데이터
            ]
        )
        
        # 원본 응답 출력
        print("\n" + "="*50)
        print("API 응답 원본 데이터:")
        print("="*50)
        # 보기 좋게 JSON 형태로 출력
        print(json.dumps(response.model_dump(), indent=2))
        
        # 응답 내용만 출력
        print("\n" + "="*50)
        print("응답 내용:")
        print("="*50)
        print(response.choices[0].message.content)
        
    except Exception as e:
        print(f"오류 발생: {e}")

if __name__ == "__main__":
    test_openai_api() 