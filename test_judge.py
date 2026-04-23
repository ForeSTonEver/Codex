#!/usr/bin/env python3
"""
채점 시스템 테스트 스크립트
두 문항의 모범 풀이가 정확하게 채점되는지 확인합니다.
"""

from judge import Judge


def test_judge_system():
    judge = Judge()

    print("=" * 70)
    print("【채점 시스템 테스트】")
    print("=" * 70)

    print("\n[문항 1] 세 과목 평균과 합격 판정 테스트")
    print("-" * 70)

    problem1_code = """
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

    passed, message = judge.test_solution(problem1_code, "1")
    print(f"결과: {'✓ 통과' if passed else '✗ 실패'}")
    print(f"메시지: {message}\n")

    print("[문항 2] 점수 목록 분석과 등급 출력 테스트")
    print("-" * 70)

    problem2_code = """
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

    passed, message = judge.test_solution(problem2_code, "2")
    print(f"결과: {'✓ 통과' if passed else '✗ 실패'}")
    print(f"메시지: {message}\n")

    print("=" * 70)
    print("테스트 완료!")
    print("=" * 70)


if __name__ == "__main__":
    test_judge_system()
