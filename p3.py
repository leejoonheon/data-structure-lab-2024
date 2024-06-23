# 프로젝트 문제 3번
input = [[4, 3, 2, 1],
         [0, 0, 0, 0],
         [0, 0, 9, 0],
         [1, 2, 3, 4]]
N = 4

forest = []

def problem3(input):
    bear_size = 2
    honeycomb_count = 0
    time = 0
    bear_x, bear_y = 0, 0
    # 입력 힌트

    # forest 리스트를 input 리스트로 초기화
    forest = [row[:] for row in input]
    
    # 곰의 초기 위치 찾기
    for i in range(N):
        for j in range(N):
            if forest[i][j] == 9:
                bear_x, bear_y = i, j
                forest[i][j] = 0
    print("곰의 초기 위치 x : {0}, y : {1}".format(bear_x, bear_y))

    #여기에서부터 코드를 작성하세요.
    
    distance=0                                       # 시작 지점으로 부터 이동 거리                                       
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]  # 곰이 이동할 수 있는 방향 (상,하,좌,우)
    queue=[(bear_x,bear_y,distance)]                 # 곰의 시작위치
    
    
    while True:
        bear_x,bear_y,distance=queue.pop(0)       #현재 곰의 위치와 이동 거리

        if 0< forest[bear_x][bear_y]< bear_size:  #곰이 먹을수 있는 꿀에 도달
            forest[bear_x][bear_y]=0              
            honeycomb_count+=1
            time+=distance
            distance=0                            # 거리와 queue를 초기화해 다음 꿀에 가는 최단거리 탐색
            queue.clear()
        
        if honeycomb_count==bear_size:            # 곰 사이즈에 맞게 꿀을 먹으면 사이즈 +1
            bear_size+=1
            honeycomb_count=0
        
        
        finish=True                               # 숲에 먹을 수 있는 꿀이 남아있으면 계속해서 탐색
        for i in range(N):                       
            for j in range(N):
                if 0< forest[i][j] < bear_size:   
                    finish=False
                    break
            if finish==False:
                break
            
        for dx,dy in directions:                  #queue에 다음에 이동할 곳과 이동 거리 추가
                next_bear_x, next_bear_y= bear_x+dx, bear_y+dy
                if 0 <= next_bear_x < N and 0 <= next_bear_y < N and forest[next_bear_x][next_bear_y] <= bear_size :
                        queue.append((next_bear_x, next_bear_y, distance+1))
    
        if finish==True:                          # 숲에 남아있는 꿀이 없으면 탐색 중지
            break
    
    result = time
    return result

result = problem3(input)

assert result == 14
print("정답입니다.")
