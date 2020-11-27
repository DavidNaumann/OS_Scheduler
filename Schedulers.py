from _collections import deque
from Process import Process


class ProcessorInformation:
    def __init__(self):
        self.ready = []
        self.time_next_schedule = -1
        self.currProcess = -1


proc_info = ProcessorInformation()


def RoundRobin(currTime, procList, timeQuantum):
    # Sees if time_next_schedule has been set
    if proc_info.time_next_schedule == -1:
        proc_info.time_next_schedule = timeQuantum

    for i in range(len(procList)):
        if isinstance(procList[i], Process):
            if procList[i].startTime == currTime:
                proc_info.ready.append(i)

    if len(proc_info.ready) > 0:
        if proc_info.time_next_schedule == 0 or procList[proc_info.ready[0]].isDone:
            if not procList[proc_info.ready[0]].isDone:
                proc_info.ready.append(proc_info.ready[0])

            proc_info.ready.pop(0)
            proc_info.time_next_schedule = timeQuantum

        idx = proc_info.ready[0]
        proc_info.time_next_schedule -= 1
    else:
        idx = -1
        proc_info.time_next_schedule = 0

    return idx


def ShortestProcessNext(currTime, procList):
    cpuAvailable = True
    shortestTime = -1

    for i in range(len(procList)):
        if isinstance(procList[i], Process):
            if procList[i].startTime == currTime:
                proc_info.ready.append(i)

    if proc_info.currProcess != -1:
        cpuAvailable = False
        if procList[proc_info.currProcess].isDone:
            proc_info.currProcess = -1
            cpuAvailable = True

    if cpuAvailable:
        if len(proc_info.ready) > 0:
            proc_info.currProcess = -1
            for i in range(len(proc_info.ready)):
                if procList[proc_info.ready[i]].totalTimeNeeded < shortestTime or shortestTime == -1:
                    if not procList[proc_info.ready[i]].isDone:
                        proc_info.currProcess = proc_info.ready[i]
                        shortestTime = procList[proc_info.currProcess].totalTimeNeeded

    print(proc_info.currProcess)
    return proc_info.currProcess


def ShortestRemainingTime(currTime, procList):
    shortestTime = -1

    for i in range(len(procList)):
        if isinstance(procList[i], Process):
            if procList[i].startTime == currTime:
                proc_info.ready.append(i)

    if len(proc_info.ready) > 0:
        proc_info.currProcess = -1
        for i in range(len(proc_info.ready)):
            time_left = procList[proc_info.ready[i]].totalTimeNeeded - procList[proc_info.ready[i]].timeScheduled
            if time_left < shortestTime or shortestTime == -1:
                if not procList[proc_info.ready[i]].isDone:
                    proc_info.currProcess = proc_info.ready[i]
                    shortestTime = procList[proc_info.currProcess].totalTimeNeeded

    print(proc_info.currProcess)
    return proc_info.currProcess


def HighestResponseTime(currTime, procList):
    cpuAvailable = True
    biggestHRRN_priority = -1

    for i in range(len(procList)):
        if isinstance(procList[i], Process):
            if procList[i].startTime == currTime:
                proc_info.ready.append(i)

    if proc_info.currProcess != -1:
        cpuAvailable = False
        if procList[proc_info.currProcess].isDone:
            proc_info.currProcess = -1
            cpuAvailable = True

    if cpuAvailable:
        if len(proc_info.ready) > 0:
            proc_info.currProcess = -1
            firstRun = True
            for i in range(len(proc_info.ready)):
                burst_time = procList[proc_info.ready[i]].totalTimeNeeded
                waiting_time = currTime - procList[proc_info.ready[i]].startTime
                HRRN_priority = (waiting_time + burst_time)/burst_time
                if HRRN_priority > biggestHRRN_priority or firstRun:
                    if not procList[proc_info.ready[i]].isDone:
                        proc_info.currProcess = proc_info.ready[i]
                        biggestHRRN_priority = HRRN_priority
                        firstRun = False

    print(proc_info.currProcess)
    return proc_info.currProcess
