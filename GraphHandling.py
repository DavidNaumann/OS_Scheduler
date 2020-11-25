from graphviz import Digraph
import glob
from PIL import Image
from Process import Process
from shutil import rmtree

'''
proc_list: list of process objects that are currently in the system
curr_time: current clock time from start of processes to now
curr_idx: is id of current process running
'''
def GraphHandler(proc_list, curr_time, curr_idx):
    g = Digraph('G', filename='./Outputs/cluster_' + str(curr_time), format='png')

    g.attr(size='20,20')

    g.node('not started', shape='box')
    g.node('ready', shape='box')
    g.node('running', shape='box')
    g.node('done', shape='box')

    g.edge('not started', 'ready')
    g.edge('ready', 'running')
    g.edge('running', 'done')

    for i in range(len(proc_list)):
        proc = proc_list[i]
        if isinstance(proc, Process):
            with g.subgraph(name=proc.id) as c:
                c.attr(color='blue')
                c.node_attr['style'] = 'filled'
                state = proc.getProcessState(curr_time)
                if i == curr_idx and state != "done":
                    state = "running"

                c.edges([(state, proc.id)])
                c.attr(label=proc.id)
    g.render()

    return


'''
filepath_name: complete file path and name for where to save the gif to
keep_images: boolean for whether or not to keep the images (true keeps images generated)
'''
def GifHandler(filepath_name, keep_images=False):
    # filepaths
    fp_in = "./Outputs/*.png"
    fp_out = filepath_name

    width, height = 1000, 500
    file_list = glob.glob(fp_in)
    list.sort(file_list, key=lambda x: int(
        x.split('_')[1].split('.png')[0]))

    # https://pillow.readthedocs.io/en/stable/handbook/image-file-formats.html#gif
    img, *imgs = [Image.open(f).resize((width, height), Image.ANTIALIAS) for f in file_list]
    img.save(fp=fp_out, format='GIF', append_images=imgs,
             save_all=True, duration=200, loop=1, background=255)

    if not keep_images:
        try:
            rmtree("./Outputs/")
        except OSError as ex:
            print(ex)