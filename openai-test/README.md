# OpenAI API 테스트 프로젝트

OpenAI GPT API를 테스트하는 프로젝트입니다.

## 실행 방법

이 프로젝트는 루트 디렉토리의 Poetry 가상환경을 사용합니다.

### 가상환경 설정 (루트 디렉토리에서 실행)

```bash
# 루트 디렉토리로 이동
cd ..

# 의존성 설치
python -m poetry install
```

### 환경 변수 설정

1. `.env-example` 파일을 복사하여 `.env` 파일 생성
```
copy .env-example .env
```

2. `.env` 파일을 열고 `OPENAI_API_KEY` 값을 실제 OpenAI API 키로 변경
```
# OpenAI API 키
OPENAI_API_KEY=your-api-key-here
```

### 스크립트 실행

현재 디렉토리에서:
```
python -m poetry run python gpt_api_test.py
```

또는 루트 디렉토리에서:
```
python -m poetry run python openai-test/gpt_api_test.py
```

## 주요 기능

- OpenAI의 GPT 모델 API 호출
- .env 파일을 통한 API 키 관리
- API 응답 데이터 출력
- 응답 내용 표시 