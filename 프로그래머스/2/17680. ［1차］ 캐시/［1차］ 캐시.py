def update_cache(cache, n):
    old = -1
    del_key = ""
    for city in cache:
        cache[city] += 1

        if old < cache[city]:                    
            old = cache[city]
            del_key = city
    
    if n < len(cache):
        del cache[del_key]
            
def solution(n, cities):
    cache = {}
    answer = 0
    for city in cities:
        city = city.lower()
        if city not in cache:
            cache[city] = 0
            update_cache(cache, n)                  
            answer += 5
        else:
            cache[city] = 0
            update_cache(cache, n)                  
            answer += 1  
            
    return answer