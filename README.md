# LLM을 활용한 AI 에이전트 개발 입문

이 프로젝트는 대형 언어 모델(LLM)을 활용한 AI 에이전트 개발의 입문 과정을 담고 있습니다.

## 프로젝트 구조

- **[openai-test](./openai-test)**: OpenAI API를 사용한 기본 테스트 프로젝트
  - GPT 모델 API 호출
  - 환경 변수를 통한 API 키 관리
  - Poetry를 이용한 가상환경 설정

## 개발 환경

- Python 3.13+
- Poetry (패키지 및 가상환경 관리)
- Windows 10/11

## 시작하기

각 하위 프로젝트 폴더의 README.md 파일을 참조하여 개별 프로젝트를 실행할 수 있습니다.

```bash
# openai-test 프로젝트 실행 예시
cd openai-test
python -m poetry install
# .env 파일 설정 후
python -m poetry run python gpt_api_test.py
```

## 앞으로의 계획

- 다양한 LLM 모델 탐색
- 간단한 AI 에이전트 구현
- 특정 도메인에 특화된 에이전트 개발
- 멀티모달 기능 추가 