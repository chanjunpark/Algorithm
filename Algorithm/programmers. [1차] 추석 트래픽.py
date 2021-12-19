import datetime


def solution(lines):
    proc_list = []
    count_list = []
    tps = []

    for log in lines:
        log = log.split(" ")
        time = log[-1][:-1]
        ymd = log[0].split("-")
        hms = log[1].split(":")
        ts = hms[2].split(".")
        end_time = datetime.datetime(int(ymd[0]), int(ymd[1]), int(ymd[2]), int(hms[0]), int(hms[1]), int(ts[0]),
                                     int(ts[1]) * 1000)
        start_time = end_time - datetime.timedelta(milliseconds=(float(time) * 1000 - 1))
        proc_list.append([start_time, end_time])

    end = proc_list[-1][1]
    proc_list = sorted(proc_list, key=lambda x: x[1])
    pointer = proc_list[0][0]
    window = datetime.timedelta(milliseconds=999)
    count = 0

    for proc in proc_list:
        for current in proc_list:
            if (current[0] >= proc[0] and current[0] <= proc[0] + window) or (
                    current[1] >= proc[0] and current[1] <= proc[0] + window) or (
                    current[1] > proc[0] + window and current[0] < proc[0]):
                count += 1
        count_list.append(count)
        count = 0
        for current in proc_list:
            if (current[0] >= proc[0] - window and current[0] <= proc[0]) or (
                    current[1] >= proc[0] - window and current[1] <= proc[0]) or (
                    current[1] > proc[0] and current[0] < proc[0] - window):
                count += 1
        count_list.append(count)
        count = 0

    answer = max(count_list)

    return answer