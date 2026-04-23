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
        grades.append('A')
    elif score >= 80:
        grades.append('B')
    elif score >= 70:
        grades.append('C')
    elif score >= 60:
        grades.append('D')
    else:
        grades.append('F')
print(f'{total / n:.1f}')
print(pass_count)
print(' '.join(grades))
