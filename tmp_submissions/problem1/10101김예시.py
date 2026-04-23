kor, eng, math = map(int, input().split())
total = kor + eng + math
average = total / 3
if average >= 60 and kor >= 40 and eng >= 40 and math >= 40:
    result = '합격'
else:
    result = '불합격'
print(total)
print(f'{average:.1f}')
print(result)
