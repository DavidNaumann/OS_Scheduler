from _collections import deque
from Process import Process


class ProcessorInformation:
    def __init__(self):
        self.ready = deque()
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

            proc_info.ready.popleft()
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
        if procList[i].startTime == currTime:
            proc_info.ready.append(i)

    if proc_info.currProcess != -1:
        if procList[proc_info.currProcess].isDone:
            cpuAvailable = False
            proc_info.currProcess = -1

    return 0


def ShortestRemainingTime(currTime, procList):
    # TODO: complete Shortest Remaining Time (SRT) function handling
    return 0


def HighestResponseTime(currTime, procList):
    # TODO: complete Highest Response Time (SPN) function handling
    return 0
