# 파이썬 코딩 수행평가 프로그램

고등학교 1학년 대상의 오프라인 파이썬 수행평가용 채점 프로그램입니다.

## 개요

- 문항 수: 2문항
- 문항 1: 리스트 없이, 중첩 제어문 없이 해결
- 문항 2: 리스트 사용, 반복문 안의 조건 분기 사용
- 채점 방식: 예시 입출력 자동 채점
- 활용 방식: 개별 입력 채점 + 제출 폴더 일괄 채점

## 문항 설명

### 문항 1 - 세 과목 평균과 합격 판정

- 입력: 한 줄에 세 과목 점수
- 출력:
  - 총점
  - 평균(소수점 첫째 자리)
  - 합격 또는 불합격
- 합격 조건:
  - 평균 60 이상
  - 세 과목 점수 모두 40 이상

### 문항 2 - 점수 목록 분석과 등급 출력

- 입력:
  - 첫째 줄: 학생 수
  - 둘째 줄: 학생 점수 목록
- 출력:
  - 평균(소수점 첫째 자리)
  - 60점 이상 학생 수
  - 각 학생의 등급
- 등급 기준:
  - A: 90 이상
  - B: 80 이상
  - C: 70 이상
  - D: 60 이상
  - F: 60 미만

## 실행 방법

### 1. 개별 채점 프로그램 실행

```bash
python3 judge.py
```

### 2. 모범 풀이 확인

```bash
python3 solution_examples.py
```

### 3. 채점 시스템 테스트

```bash
python3 test_judge.py
```

### 4. 오프라인 제출 폴더 일괄 채점

학생들이 제출한 `.py` 파일을 문항별 폴더에 모아둔 뒤 아래 명령으로 채점합니다.

```bash
python3 batch_grader.py --problem 1 --submissions-dir submissions/problem1
python3 batch_grader.py --problem 2 --submissions-dir submissions/problem2
```

선택적으로 결과 CSV 경로를 지정할 수 있습니다.

```bash
python3 batch_grader.py --problem 2 --submissions-dir submissions/problem2 --output reports/problem2_result.csv
```

채점이 끝나면:

- 터미널에 학생별 점수와 정답 여부가 표시됩니다.
- CSV 파일에 결과가 저장됩니다.

## 폴더 예시

```text
assessment/
├── judge.py
├── batch_grader.py
├── solution_examples.py
├── test_judge.py
├── README.md
└── submissions/
    ├── problem1/
    └── problem2/
```

## 채점 원칙

- 입력 형식과 출력 형식이 정확해야 합니다.
- 문항 1은 리스트와 중첩 제어문 없이 해결하는 것을 목표로 합니다.
- 문항 2는 리스트와 반복문 안의 조건 분기를 사용하는 것을 목표로 합니다.
- 자동 채점은 등록된 예시 테스트 케이스 기준으로 수행됩니다.
