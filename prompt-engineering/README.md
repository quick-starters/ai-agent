# 프롬프트 엔지니어링 테스트

OpenAI API를 사용하여 다양한 프롬프트 엔지니어링 기법을 테스트하는 프로젝트입니다.

## 현재 구현된 예제

1. **마법 거울 (mirror.py)**
   - 백설공주 동화 속 마법 거울 캐릭터 역할 부여
   - System 프롬프트를 통한 페르소나 설정

2. **조커 (joker.py)**
   - 배트맨 시리즈의 악당 조커 캐릭터 역할 부여
   - 캐릭터 특성에 맞는 응답 생성

## 실행 방법

이 프로젝트는 루트 디렉토리의 Poetry 가상환경을 사용합니다.

```bash
# 루트 디렉토리에서 실행
python -m poetry run python prompt-engineering/mirror.py

# 또는
python -m poetry run python prompt-engineering/joker.py
```

## 프롬프트 엔지니어링 기법

이 예제에서 사용된 주요 기법:

- **역할 부여(Role Prompting)**: 시스템 프롬프트를 통해 AI에게 특정 역할 부여
- **캐릭터 페르소나(Character Persona)**: 잘 알려진 캐릭터의 성격과 특성을 반영한 응답 유도
- **Temperature 조절**: 응답의 창의성과 무작위성 조절 (0.9로 설정하여 창의적 응답 유도) 