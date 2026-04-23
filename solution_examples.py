"""
코딩 수행평가 - 모범 풀이 예시
"""

print("\n" + "=" * 70)
print("【모범 풀이 예시】")
print("=" * 70)

print("\n\n【문항 1 풀이 예시】")
print("세 과목 평균과 합격 판정")
print("-" * 70)

problem1_solution = """
kor, eng, math = map(int, input().split())

total = kor + eng + math
average = total / 3

if average >= 60 and kor >= 40 and eng >= 40 and math >= 40:
    result = "합격"
else:
    result = "불합격"

print(total)
print(f"{average:.1f}")
print(result)
"""

print("풀이 코드:")
print(problem1_solution)

print("\n\n【문항 2 풀이 예시】")
print("점수 목록 분석과 등급 출력")
print("-" * 70)

problem2_solution = """
n = int(input())
scores = list(map(int, input().split()))

total = 0
pass_count = 0
grades = []

for score in scores:
    total += score

    if score >= 60:
        pass_count += 1

    if score >= 90:
        grades.append("A")
    elif score >= 80:
        grades.append("B")
    elif score >= 70:
        grades.append("C")
    elif score >= 60:
        grades.append("D")
    else:
        grades.append("F")

average = total / n

print(f"{average:.1f}")
print(pass_count)
print(" ".join(grades))
"""

print("풀이 코드:")
print(problem2_solution)

print("\n" + "=" * 70)
print("주요 학습 포인트:")
print("=" * 70)
print("""
【문항 1】
- 여러 값을 변수에 나누어 저장하기
- 산술 연산으로 총점과 평균 구하기
- 단일 조건식으로 합격 여부 판정하기
- 출력 형식을 정확하게 맞추기

【문항 2】
- 입력값을 리스트에 저장하기
- 반복문 안에서 조건문으로 등급 판정하기
- 누적 합과 개수 세기
- 리스트 결과를 공백으로 연결하여 출력하기
""")
