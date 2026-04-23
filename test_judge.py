#!/usr/bin/env python3
"""
채점 시스템 테스트 스크립트
각 난이도별로 모범 풀이가 정확하게 채점되는지 확인합니다.
"""

import io
import sys
from judge import Judge


def test_judge_system():
    """채점 시스템 테스트"""
    judge = Judge()
    
    print("="*70)
    print("【채점 시스템 테스트】")
    print("="*70)
    
    # 하 (쉬움) 풀이 테스트
    print("\n[하] 리스트에서 최댓값과 최솟값 찾기 테스트")
    print("-"*70)
    
    easy_code = """
n = int(input())
numbers = list(map(int, input().split()))

max_val = numbers[0]
min_val = numbers[0]

for num in numbers:
    if num > max_val:
        max_val = num
    if num < min_val:
        min_val = num

sum_val = max_val + min_val

print(max_val)
print(min_val)
print(sum_val)
"""
    
    passed, message = judge.test_solution(easy_code, "하")
    print(f"결과: {'✓ 통과' if passed else '✗ 실패'}")
    print(f"메시지: {message}\n")
    
    # 중 (중간) 풀이 테스트
    print("[중] 학점 계산 및 성적 순위 테스트")
    print("-"*70)
    
    medium_code = """
n = int(input())
scores = []

for i in range(n):
    score = int(input())
    scores.append(score)

grades = []
count_a = 0

for score in scores:
    if score >= 90:
        grades.append('A')
        count_a += 1
    elif score >= 80:
        grades.append('B')
    elif score >= 70:
        grades.append('C')
    elif score >= 60:
        grades.append('D')
    else:
        grades.append('F')

average = sum(scores) / len(scores)

sorted_scores = sorted(scores, reverse=True)

print(count_a)
print(f"{average:.1f}")
print(' '.join(map(str, sorted_scores)))
"""
    
    passed, message = judge.test_solution(medium_code, "중")
    print(f"결과: {'✓ 통과' if passed else '✗ 실패'}")
    print(f"메시지: {message}\n")
    
    # 상 (어려움) 풀이 테스트
    print("[상] 소수 판별 및 필터링 테스트")
    print("-"*70)
    
    hard_code = """
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

n = int(input())
numbers = list(map(int, input().split()))

primes = []
is_prime_list = []

for num in numbers:
    if is_prime(num):
        primes.append(num)
        is_prime_list.append(True)
    else:
        is_prime_list.append(False)

count = len(primes)
sum_primes = sum(primes)

print(count)
print(sum_primes)
print(' '.join(map(str, is_prime_list)))
"""
    
    passed, message = judge.test_solution(hard_code, "상")
    print(f"결과: {'✓ 통과' if passed else '✗ 실패'}")
    print(f"메시지: {message}\n")
    
    print("="*70)
    print("테스트 완료!")
    print("="*70)


if __name__ == "__main__":
    test_judge_system()
