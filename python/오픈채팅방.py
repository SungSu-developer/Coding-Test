def solution(record):
    answer = []
    user_info = {}  

    for i in record:
        arr = i.split(" ")
        command = arr[0]
        user_id = arr[1]
        
        if command == "Enter" or command == "Change":
            nickname = arr[2]
            user_info[user_id] = nickname

    for i in record:
        arr = i.split(" ")
        command = arr[0]
        user_id = arr[1]

        if command == "Enter":
            nickname = user_info[user_id]
            answer.append(f"{nickname}님이 들어왔습니다.")
        elif command == "Leave":
            nickname = user_info[user_id]
            answer.append(f"{nickname}님이 나갔습니다.")
            
    return answer