import heapq

def solution(food_times, k):
    answer = 0
    if sum(food_times) <= k:
        return -1
    
    q = []
    n = len(food_times)
    for i in range(n):
        heapq.heappush(q, (food_times[i],i+1))
        
    previous = 0
    
    #time이 가장 작은 음식부터 차례로 제거해간다.
    while (q[0][0] - previous) * n <= k: # 사이클 m번 도는거 가능한지 여부 (예. 먹는시간이 3이면 3*남은음식수 <= k)
        time, now_food = heapq.heappop(q)
        
        eating_time = (time - previous) * n # 이전의 사이클 수(previous)만큼 제거해줘야한다
        
        if k < eating_time:
            break
        n -= 1
        k -= eating_time
        previous = time
        
    q.sort(key = lambda x:x[1]) #음식번호순으로 정렬
    answer = q[k%n][1]
    
    return answer
        
# 먹는시간이 가장 작게 걸리는 음식부터 제거해나가면 된다. << 가장 중요한 풀이 포인트!
# 이전에 먹은 시간을 빼는 이유는 앞에서 이전 먹은 시간만큼 이미 사이클을 돌았기 때문이다
