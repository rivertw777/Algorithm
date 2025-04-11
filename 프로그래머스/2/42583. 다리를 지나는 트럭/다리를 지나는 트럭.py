# bl 다리 길이, w 무게 제한, tw 트럭 무게 리스트
def solution(bl, w, tw):
    bridge = []
    time = 0
    while True:
        
        # 지나간 트럭 삭제
        if bridge and bridge[0][1] == bl:
            bridge.pop(0)
            
        # 트럭 삽입                
        if tw and not bridge:
            bridge.append([tw[0], 0])
            tw.pop(0)    
            
        # 다리 길이 체크
        elif tw and len(bridge) <= bl:
            total = 0           
            for i in bridge:
                total += i[0]
                            
            # 무게 초과
            if total + tw[0] <= w:
                bridge.append([tw[0], 0])
                tw.pop(0)
                
        # 시간 경과
        time += 1
        for i in bridge:
            i[1] += 1
                               
        if not tw and not bridge:
            break
                 
    return time