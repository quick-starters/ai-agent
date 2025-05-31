from openai import OpenAI
from dotenv import load_dotenv
import os
import json

# .env 파일에서 환경 변수 로드
load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')
client = OpenAI(api_key=api_key)

def joker_response():
    # OpenAI API 요청
    response = client.chat.completions.create(
      model="gpt-4o",
      temperature=0.9,  # 창의성 조절 (0에 가까울수록 일관적, 1에 가까울수록 창의적)
      messages=[
        {"role": "system", "content": "너는 배트맨에 나오는 조커야. 조커의 악당 캐릭터에 맞게 답변해줘"},
        {"role": "user", "content": "세상에서 누가 제일 아름답니?"},
      ]
    )

    # 전체 응답 출력
    print("\n" + "="*50)
    print("API 응답 원본 데이터:")
    print("="*50)
    print(json.dumps(response.model_dump(), indent=2))

    # 응답 내용만 출력
    print("\n" + "="*50)
    print("조커의 응답:")
    print("="*50)
    print(response.choices[0].message.content)

if __name__ == "__main__":
    joker_response() 