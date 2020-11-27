from Process import Process
from Schedulers import RoundRobin, ShortestProcessNext, ShortestRemainingTime, HighestResponseTime
from FileHandling import ProcListFromFile
from GraphHandling import GraphHandler, GifHandler

if __name__ == '__main__':
    # Process Handling Variables
    schedChoice = 1

    # pre-run init
    done = False
    curr_time = 0
    proc_idx = -1
    timeQuantum = 1

    # Input name and output name
    input_file_name = "Samples/sample_proc_list.txt"
    output_file_name = "Samples/sample_proc_output.gif"

    proc_list = ProcListFromFile(input_file_name)

    while not done:
        if schedChoice == 1:
            proc_idx = RoundRobin(curr_time, proc_list, timeQuantum)
        elif schedChoice == 2:
            proc_idx = ShortestProcessNext(curr_time, proc_list)
        elif schedChoice == 3:
            proc_idx = ShortestRemainingTime(curr_time, proc_list)
        elif schedChoice == 4:
            proc_idx = HighestResponseTime(curr_time, proc_list)

        if 0 <= proc_idx < len(proc_list):
            curr_proc = proc_list[proc_idx]
            if isinstance(curr_proc, Process):
                curr_proc.timeScheduled += 1
                if curr_proc.timeScheduled == curr_proc.totalTimeNeeded:
                    curr_proc.isDone = True
                    curr_proc.timeFinished = curr_time
                proc_list[proc_idx] = curr_proc

        GraphHandler(proc_list, curr_time, proc_idx)

        done = True
        for proc in proc_list:
            if isinstance(proc, Process):
                done = (done and proc.isDone)

        if not done:
            curr_time += 1

GifHandler(output_file_name, False)