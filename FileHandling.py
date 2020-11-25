from Process import Process

'''
fileName: input file name to read from in order to get the process info
'''
def ProcListFromFile(fileName):
    proc_list = []
    f = open(fileName, 'r')

    for l in f:
        id, start_time, time_needed = l.split()
        temp_process = Process()
        temp_process.id = id
        temp_process.startTime = int(start_time)
        temp_process.totalTimeNeeded = int(time_needed)
        proc_list.append(temp_process)

    f.close()

    return proc_list