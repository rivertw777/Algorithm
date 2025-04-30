def solution(a, b):
    alpha = "abcdefghijklmnopqrstuvwxyz"
    
    a = list(a.lower())
    b = list(b.lower())

    al = []
    bl = []
    for i in range(1, len(a)):
        if a[i-1] in alpha and a[i] in alpha:
            al.append(a[i-1:i+1])
            
    for i in range(1, len(b)):    
        if b[i-1] in alpha and b[i] in alpha:
            bl.append(b[i-1:i+1])

    print(al, bl)
            
    hap = len(al+bl)
    gyo = 0
    for i in al:
        if i in bl:
            gyo += 1
            bl.remove(i)
    hap -= gyo

    print(hap, gyo)
        
    if hap == 0 and gyo == 0:
        return 65536    
    
    return int((gyo / hap) * 65536)