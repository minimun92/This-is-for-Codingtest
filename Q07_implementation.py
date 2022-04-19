import sys
input = sys.stdin.readline

data = str(input().rstrip())
length = len(data)

sum1,sum2 = 0,0
for i in range(length//2):
    sum1 += int(data[i])

for i in range(length//2,length):
    sum2 += int(data[i])

if sum1 == sum2:
    print("LUCKY")
else :
    print("READY")
