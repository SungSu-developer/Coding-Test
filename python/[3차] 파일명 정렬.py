def solution(files):
    answer = []
    file_name = []

    for f in files:
        head = ""
        number = ""
        tail = ""

        start = 0
        for i in range(len(f)):
            if f[i].isdigit():
                start = i
                break
        
        end = len(f) 
        for i in range(start, len(f)):
            if not f[i].isdigit() or (i - start) >= 5:
                end = i
                break
        
        head = f[:start]
        number = f[start:end]
        tail = f[end:]
        
        file_name.append([head, number, tail])
    
    file_name.sort(key=lambda x: (x[0].lower(), int(x[1])))

    for i in file_name:
        final = i[0] + i[1] + i[2]
        answer.append(final)
            
    return answer