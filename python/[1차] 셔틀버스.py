def solution(n, t, m, timetable):
    
    crew_arrive = []
    for time_str in timetable:
        H, M = map(int, time_str.split(":"))
        crew_arrive.append(H * 60 + M)
    
    crew_arrive.sort()
    
    bus_times = []
    start_time = 9 * 60 
    for i in range(n):
        bus_times.append(start_time + t * i)
        
    my_turn = -1 
    
    for i, bus_time in enumerate(bus_times):
        current_bus = []
        
        j = 0
        while j < len(crew_arrive):
            crew_time = crew_arrive[j]
            
            if crew_time <= bus_time and len(current_bus) < m:
                current_bus.append(crew_time)
                j += 1
            else:
                break
        
        crew_arrive = crew_arrive[j:]
        if i == n - 1:
            if len(current_bus) < m:
                my_turn = bus_time
            else:
                last_crew = current_bus[-1]
                my_turn = last_crew - 1

    final_H = my_turn // 60
    final_M = my_turn % 60
    
    return f"{final_H:02d}:{final_M:02d}"