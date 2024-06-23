# 프로젝트 문제 2번
input = ")))()"

def problem2(input):
    # 이 곳에 코드를 작성하세요.
    # 입력 힌트

    add_close = 0  # 추가해야 할 ')'의 개수
    add_open = 0   # 추가해야 할 '('의 개수
    
    for char in input:           
        if char == '(':
            add_close += 1       # ')'가 부족하므로 +1
        elif char == ')':
            if add_close > 0:    # 이미 '(' 가 있으면 괄호가 안부족 하므로 -1  
                add_close -= 1
            else:
                add_open += 1    # '('가 부족하므로 +1

    result = add_close + add_open
    return result

result = problem2(input)

assert result == 3
print("정답입니다.")
