def solution(users, emoticons):
    answer = 0

    # 할인율 10 20 30 40
    # 자기 기준 할인율 넘어가면 이모티콘 삼 (비율)
    # 할인품 다 사려고 했는데 특정 금액 넘어가면 이모티콘 플러스를 산다

    # 목표 
    # 이모티콘 플러스 서비스 가입자를 최대한 늘리는 것.
    # 이모티콘 판매액을 최대한 늘리는 것.

    rate = [10,20,30,40]
    all_rates = []
    rates = []
    def dfs(depth):
        if depth >= len(emoticons):
            all_rates.append(rates[:])
            return
        
        for i in rate:
            rates.append(i)
            dfs(depth+1)    
            rates.pop()

    dfs(0)
    
    for i in range(len(all_rates)):
        for j in range(len(users)):
            if( users[j][0] ):
                answer += 1

    return answer


print(solution([[40, 10000], [25, 10000]],	[7000, 9000]))