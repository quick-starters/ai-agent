# LLM을 활용한 AI 에이전트 개발 입문

이 프로젝트는 대형 언어 모델(LLM)을 활용한 AI 에이전트 개발의 입문 과정을 담고 있습니다.

## 프로젝트 구조

- **[openai-test](./openai-test)**: OpenAI API를 사용한 기본 테스트 프로젝트
  - GPT 모델 API 호출 (OpenAI API v1.0+ 형식 사용)
  - 환경 변수를 통한 API 키 관리

- **[prompt-engineering](./prompt-engineering)**: 프롬프트 엔지니어링 테스트 프로젝트
  - 다양한 캐릭터 페르소나 구현 (마법 거울, 조커)
  - 역할 부여를 통한 응답 제어

## 개발 환경

- Python 3.11.8
- Poetry 2.1.3 (패키지 및 가상환경 관리)
- Windows 10/11
- OpenAI API v1.82.1

## 설치 방법

프로젝트 루트에서 한 번만 Poetry를 설치하면 모든 하위 프로젝트에서 사용할 수 있습니다.

```bash
# Python 3.11 설치 확인
py -3.11 --version

# Poetry 설치 (필요한 경우)
py -3.11 -m pip install poetry

# 루트 디렉토리에서 의존성 설치
py -3.11 -m poetry install --no-root

# 환경 변수 설정 (.env 파일 생성)
# OPENAI_API_KEY=your-api-key-here
```

## 시작하기

각 하위 프로젝트는 루트의 가상환경을 공유합니다.

```bash
# openai-test 프로젝트 실행 예시
py -3.11 -m poetry run python openai-test/gpt_api_test.py

# prompt-engineering 프로젝트 실행 예시
py -3.11 -m poetry run python prompt-engineering/mirror.py
py -3.11 -m poetry run python prompt-engineering/joker.py
```

## 주요 패키지

- openai (v1.82.1): OpenAI API 클라이언트
- python-dotenv (v1.1.0): 환경 변수 관리
- pydantic (v2.11.5): 데이터 검증
- httpx (v0.28.1): HTTP 클라이언트

## 앞으로의 계획

- 다양한 LLM 모델 탐색
- 간단한 AI 에이전트 구현
- 특정 도메인에 특화된 에이전트 개발
- 멀티모달 기능 추가 