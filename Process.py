'''
Process class used to control all of the processes that need to be simulated.
'''
class Process:
    def __init__(self):
        self.id = ""
        self.startTime = -1
        self.totalTimeNeeded = -1
        self.isDone = False
        self.timeScheduled = 0
        self.timeFinished = -1

    def getProcessState(self, curr_time):
        if self.isDone:
            return "done"

        if self.startTime <= curr_time:
            return "ready"
        else:
            return "not started"
