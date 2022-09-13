import sys
input = sys.stdin.readline

n = int(input())
meeting = []
time, cnt = 0, 0

for _ in range(n):
    s, e = map(int, input().split())
    meeting.append((s, e))

meeting.sort(key=lambda x:(x[1], x[0]))

for m in meeting:
    if time <= m[0]:
        time = m[1]
        cnt += 1
print(cnt)
