def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    

    item_map = [[0 for i in range(102)] for j in range(102)]
    
    #사각범위 채우기기
    for i in rectangle:
        for j in range(i[1]*2,i[3]*2+1):
            for k in range(i[0]*2,i[2]*2+1):
                item_map[k][j] = 1
    
    #8방향 체크
    dx = [1,1,1,-1,-1,-1,0,0,0]
    dy = [-1,1,0,-1,0,1,-1,0,1]
    
    #테두리 탐색 시작점
    queue = [[0,0]]

    while queue:
        x, y = queue.pop()
        
        for i in range(9):
            posx = x + dx[i]
            posy = y + dy[i]
            
            if(0<=posx<=101 and 0<=posy<=101):
                if(item_map[posx][posy]==0):
                    item_map[posx][posy] = -1
                    queue.append([posx,posy])
                elif(item_map[posx][posy]==1):
                    item_map[posx][posy] = 2

    
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    ans = []
    queue = [[characterX*2, characterY*2, 0]]

    #길 탐색 
    while queue:

        x, y, dist = queue.pop() 
        
        for i in range(4):
            posx = x + dx[i]
            posy = y + dy[i]

            if(0<=posx<=101 and 0<=posy<=101):
                if(item_map[posx][posy]==2):
                    if(posx==itemX*2 and posy==itemY*2):
                        ans.append(dist+1)    
                    else:
                        queue.append([posx,posy,dist+1])
                        item_map[posx][posy]=1
                    


    answer = min(ans)//2
    return answer
