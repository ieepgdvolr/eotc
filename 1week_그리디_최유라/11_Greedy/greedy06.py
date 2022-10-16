# 221016
# 06) 무지의 먹방라이브
# https://school.programmers.co.kr/learn/courses/30/lessons/42891

# 내가 푼 코드
def solution(food_times, k):
    result = 0
    food_num = len(food_times)
    for i in range(k):
        i = i % food_num
        if food_times[i] == 0:
            i = (i + 1) % food_num
        food_times[i] -= 1
        result = (i + 1) % food_num

    for i in range(food_num):
        i = (result + i) % food_num
        if food_times[i] != 0:
            result = (i + 1) % food_num
            break
        else:
            result = -1
    return result
# 풀다풀다 포기. 주어진 테스트케이스는 통과인데 나머지 다 실패&효율성 안나옴 현타.....^.^


# 큐...를 잘 알았더라면
from heapq import heappush, heappop

def solution(food_times, k):
    # 방송 중단 전 음식을 다 먹는 경우
    if sum(food_times) <= k:
        return - 1

    foodHeap = []
    length = len(food_times)    #남은 음식 개수
    for i in range(length):
        heappush(foodHeap, [food_times[i], i + 1]);

    time = 0
    while (foodHeap[0][0] - time) * length < k:
        k -= (foodHeap[0][0] - time) * length
        time += (foodHeap[0][0] - time)
        length -= 1
        heappop(foodHeap)

    result = sorted(foodHeap, key = lambda x : x[1])    # index를 기준으로 heap을 다시 정렬
    answer = result[k % length][1]
    return answer

# 책 해설
import heapq

def solution(food_times, k):
    # 전체 음식을 먹는 시간보다 k가 크거나 같다면 -1
    if sum(food_times) <= k:
        return -1

    # 시간이 작은 음식부터 빼야 하므로 우선순위 큐를 이용
    q = []
    for i in range(len(food_times)):
        # (음식 시간, 음식 번호) 형태로 우선순위 큐에 삽입
        heapq.heappush(q, (food_times[i], i + 1))  

    sum_value = 0 # 먹기 위해 사용한 시간
    previous = 0 # 직전에 다 먹은 음식 시간
    length = len(food_times) # 남은 음식의 개수

    # sum_value + (현재의 음식 시간 - 이전 음식 시간) * 현재 음식 개수와 k 비교
    while sum_value + ((q[0][0] - previous) * length) <= k:
        now = heapq.heappop(q)[0]
        sum_value += (now - previous) * length
        length -= 1 # 다 먹은 음식 제외
        previous = now # 이전 음식 시간 재설정

    # 남은 음식 중에서 몇 번째 음식인지 확인하여 출력
    result = sorted(q, key=lambda x: x[1]) # 음식의 번호 기준으로 정렬
    return result[(k - sum_value) % length][1]