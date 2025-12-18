def func_a(times):
    hour = int(times[:2])
    minute = int(times[3:])
    return hour*60 + minute

def solution(subway_times, current_time):
    current_minute = func_a(current_time)
    INF = 1000000000
    answer = INF
    for s in subway_times:
        subway_minute = func_a(s)
        if current_minute <= subway_minute :
            answer = subway_minute - current_minute
            break
    if answer == INF:
        return -1
    return answer
subway_times=input("Nhập thời gian đến của tàu(dạng XX:YY,cách nhau bởi dấu cách):").split()
current_time =times=input("Nhập thời gian hiện tại:")
kq=solution(subway_times,current_time)
print(kq)
