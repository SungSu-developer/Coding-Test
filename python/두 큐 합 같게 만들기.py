from collections import deque

def solution(queue1, queue2):
    answer = 0

    q1 = deque(queue1)
    q2 = deque(queue2)
    sum1 = sum(q1)
    sum2 = sum(q2)
    total = sum1 + sum2

    if(total % 2 != 0):
        return -1
    goal = total//2
    max_try = len(queue1)*3

    while sum1 != goal:
        if(answer > max_try):
            return -1
        
        if(sum1 > goal):
            num = q1.popleft()
            q2.append(num)
            sum1 -= num
            sum2 += num
        else:
            num = q2.popleft()
            q1.append(num)
            sum1 += num
            sum2 -= num
        answer+=1
    
    return answer