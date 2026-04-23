"""
코딩 수행평가 - 모범 풀이 예시
"""

print("\n" + "="*70)
print("【모범 풀이 예시】")
print("="*70)

# ============ 하(쉬움) 문제 풀이 ============
print("\n\n【하 (쉬움) 풀이 예시】")
print("리스트에서 최댓값과 최솟값 찾기")
print("-"*70)

easy_solution = """
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

print("풀이 코드:")
print(easy_solution)

# ============ 중(중간) 문제 풀이 ============
print("\n\n【중 (중간) 풀이 예시】")
print("학점 계산 및 성적 순위")
print("-"*70)

medium_solution = """
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

print("풀이 코드:")
print(medium_solution)

# ============ 상(어려움) 문제 풀이 ============
print("\n\n【상 (어려움) 풀이 예시】")
print("소수 판별 및 필터링")
print("-"*70)

hard_solution = """
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

print("풀이 코드:")
print(hard_solution)

print("\n" + "="*70)
print("주요 학습 포인트:")
print("="*70)
print("""
【하 (쉬움)】
- 리스트 선언 및 초기화
- for 루프를 이용한 리스트 순회
- if 조건문을 이용한 값 비교
- 변수에 값 저장 및 계산

【중 (중간)】
- 여러 변수를 리스트에 저장
- if/elif/else를 이용한 다중 조건 판정
- for 루프 내에서 조건 처리
- 내장 함수 활용 (sum, sorted, join)
- 실수 데이터타입 및 소수점 포매팅

【상 (어려움)】
- 함수 정의 및 호출
- 중첩 반복문 (소수 판별 알고리즘)
- 소수 판별 로직 구현
- Boolean 자료형 활용
- 복합적인 리스트 조작
""")
