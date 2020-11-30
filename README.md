# CS3800: Operating Systems Final Project
Authors: David Naumann and Dani Baker
## Process Animation Project
This project's goal is to be able to animate processes running through states of a processor. The intent is to allow for the project to be used in educational settings and to give a better source of information and clarity to the student of what is happening realtime to their processes.
### Design
The project was designed to be modular as possible allowing for the processes to be used in many different scenarios and scheduling algorithms as seen in the Schedulers.py. The processes are then taken into the graph handler and gif handler to create gifs of everything that occurred during the execution of the code.
### Benefits
The benefits of this project is that it keeps data from the entire session and only deletes it during the end so if the scheduler breaks a person can go back and see what happened during execution and what processes are getting stuck. Furthermore the project can be expanded on and possibly used in the future as a homework assignment or reference for a homework assignment if the homework needed to be in Python.
### Installation
```bash
pip install -r requirements.txt
```
### Usage
The main.py file has examples of how the graph handler, gif handler and scheduling of processes should be done.
### Thanks
Thanks to the CS3800 class that allowed us to make a cool final project and experiment in things we haven't used just yet. Thanks to Professor Yeung for teaching our section and providing us with the knowledge we need to be successful in the future when it comes to Operating Systems.