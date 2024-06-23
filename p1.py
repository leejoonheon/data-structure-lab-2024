# 프로젝트 문제 1번
input = [10, 40, 30, 60, 30]

def problem1(input):
    # 이곳에 코드를 작성하세요.
    mean = 0
    median = 0
    result = [0,0]
    
    for index in range(1,len(input)):                          # 중위값을 찾기 위해 insertion sorting을 이용해 정렬
        current_value=input[index]
        position=index

        while position>0 and input[position-1]>current_value:
            input[position]=input[position-1]
            position=position-1
        
        input[position]=current_value
    
    for i in input:                                             #평균값 구하기
        mean+=i
    mean/=len(input)
    
    median=input[len(input)//2]                                 #중앙값 구하기 
    
    result[0] = mean
    result[1] = median
    return result

result = problem1(input)

assert result == [34, 30]
print("정답입니다.")
