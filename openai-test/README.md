# OpenAI API 테스트 프로젝트

Poetry를 사용한 OpenAI GPT API 테스트 프로젝트입니다.

## 설치 방법

1. Poetry 설치 (이미 설치되어 있지 않은 경우)
```
pip install poetry
```

2. 의존성 설치
```
python -m poetry install
```

## 환경 변수 설정

1. `.env-example` 파일을 복사하여 `.env` 파일 생성
```
copy .env-example .env
```

2. `.env` 파일을 열고 `OPENAI_API_KEY` 값을 실제 OpenAI API 키로 변경
```
# OpenAI API 키
OPENAI_API_KEY=your-api-key-here
```

## 실행 방법

Poetry 가상환경에서 스크립트 실행:
```
python -m poetry run python gpt_api_test.py
```

## 주요 기능

- OpenAI의 GPT 모델 API 호출
- .env 파일을 통한 API 키 관리
- API 응답 데이터 출력
- 응답 내용 표시 