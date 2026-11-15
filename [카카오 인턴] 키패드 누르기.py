def solution(numbers, hand):
    answer = ''

    l_cur = [0,3]
    r_cur = [0,3]
    if(hand == "right"):
        check = 0
    else:
        check = 1
    for i in numbers:
        if (i == 1 ):
            l_cur = [0,0]
            answer += "L"
        elif(i==2):
            L_dis = abs(l_cur[0]-1) + l_cur[1]
            R_dis = abs(r_cur[0]-1) + r_cur[1]
            if(check == 0 and R_dis <= L_dis):
                answer += "R"
                r_cur = [1,0]
            elif(check == 0 and L_dis < R_dis):
                answer += "L"
                l_cur = [1,0]
            elif(check==1 and L_dis <= R_dis):
                answer+="L"
                l_cur = [1,0]
            else:
                answer += "R"
                r_cur = [1,0]
        elif(i==3):
            answer += "R"
            r_cur = [0,0]
        elif (i==4):
            l_cur = [0,1]
            answer += "L"
        elif (i==5):
            L_dis = abs(l_cur[0]-1) + abs(l_cur[1]-1)
            R_dis = abs(r_cur[0]-1) + abs(r_cur[1]-1)
            if(check == 0 and R_dis <= L_dis):
                answer += "R"
                r_cur = [1,1]
            elif(check == 0 and L_dis < R_dis):
                answer += "L"
                l_cur = [1,1]
            elif(check==1 and L_dis <= R_dis):
                answer+="L"
                l_cur = [1,1]
            else:
                answer += "R"
                r_cur = [1,1]
        elif (i==6):
            r_cur = [0,1]
            answer += "R"
        elif (i==7):
            l_cur = [0,2]
            answer += "L"
        elif (i==8):
            L_dis = abs(l_cur[0]-1) + abs(l_cur[1]-2)
            R_dis = abs(r_cur[0]-1) + abs(r_cur[1]-2)
            if(check == 0 and R_dis <= L_dis):
                answer += "R"
                r_cur = [1,2]
            elif(check == 0 and L_dis < R_dis):
                answer += "L"
                l_cur = [1,2]
            elif(check==1 and L_dis <= R_dis):
                answer+="L"
                l_cur = [1,2]
            else:
                answer += "R"
                r_cur = [1,2]
        elif (i==9):
            r_cur = [0,2]
            answer += "R"
        else:
            L_dis = abs(l_cur[0]-1) + abs(l_cur[1]-3)
            R_dis = abs(r_cur[0]-1) + abs(r_cur[1]-3)
            if(check == 0 and R_dis <= L_dis):
                answer += "R"
                r_cur = [1,3]
            elif(check == 0 and L_dis < R_dis):
                answer += "L"
                l_cur = [1,3]
            elif(check==1 and L_dis <= R_dis):
                answer+="L"
                l_cur = [1,3]
            else:
                answer += "R"
                r_cur = [1,3]
        
    return answer