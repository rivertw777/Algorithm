def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    my_map=draw_map(rectangle)
    queue=[]
    ret=0
    xy=[[0,1],[0,-1],[1,0],[-1,0]]
    queue.append([2*characterX,2*characterY,0])
    my_map[2*characterX][2*characterY]=0

    while(queue):
        X,Y,ret=queue.pop(0)

        if X == 2*itemX and Y == 2*itemY:
            answer = ret
            break

        for in_xy in xy:
            if (my_map[X+in_xy[0]][Y+in_xy[1]] == 1) and (my_map[X+2*in_xy[0]][Y+2*in_xy[1]] == 1):
                my_map[X+2*in_xy[0]][Y+2*in_xy[1]]=0
                queue.append([X+2*in_xy[0],Y+2*in_xy[1],ret+1])

    return answer

def draw_map(rectangle):
    ret_map=[[ -1 for i in range(2*52)] for j in range(2*52)]

    for points in rectangle:
        for x in range(2*points[0], 2*(points[2])+1):
            ret_map[x][2*points[1]]=1
            ret_map[x][2*points[3]]=1
        for y in range(2*points[1], 2*(points[3])+1):
            ret_map[2*points[0]][y]=1
            ret_map[2*points[2]][y]=1

    for points in rectangle:
        for x in range(2*(points[0])+1, (2*(points[2]))):
            for y in range(2*(points[1])+1, (2*(points[3]))):
                ret_map[x][y]=-1

    return ret_map