#https://www.acmicpc.net/problem/14888
import sys
input = sys.stdin.readline

n = int(input())
data = list(map(int, input().split()))
operator = list(map(int, input().split()))
max = -1e9
min = 1e9

# print(data)
# print(operator)

def go(index, plus, minus, mul, div, last):
    global max,min
    
    if index == n-1:
        if min > last:
            min = last
        if max < last:
            max = last
        return

    if plus < operator[0] :
        go(index+1, plus+1, minus, mul, div, last + data[index+1])
    if minus < operator[1] :
        go(index+1, plus, minus+1, mul, div, last - data[index+1])
    if mul < operator[2] :
        go(index+1, plus, minus, mul+1, div, last * data[index+1])
    if div < operator[3] :
        go(index+1, plus, minus, mul, div+1, int(last / data[index+1]))

go(0,0,0,0,0,data[0])
print(max)
print(min)
