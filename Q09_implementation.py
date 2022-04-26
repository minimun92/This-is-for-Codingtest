import sys
input = sys.stdin.readline

s = input().rstrip()

def solution(s):
    ans = len(s)
    # cutting : 자르는 단위
    for cutting in range(1, len(s)//2+1):
        # check_str = 자른 문자열
        result = ""
        check_str = s[:cutting]
        repeat = 1
        # 자르는 단위로 잘라서 
        for i in range(cutting,len(s),cutting):
            #print("check_str =",check_str)
            if check_str == s[i:i+cutting]:
                repeat += 1
            else :
                if repeat >= 2:
                    result += str(repeat) + check_str
                else :
                    result += check_str
                check_str = s[i:i+cutting]
                repeat = 1

        #print("check_str =",check_str)
        if repeat >= 2:
            result += str(repeat) + check_str
        else :
            result += check_str
        ans = min(ans, len(result))    
        #print("result =",result)
    return ans

print(solution(s))
