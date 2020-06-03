#!/usr/bin/python3
import os

print("parent proc ID: ", os.getppid())
print("proc ID", os.getpid())
child = os.fork()
if child == 0:
    print("child proc ID", os.getpid())
    os.system("ping -c 5 8.8.8.8")
    os._exit(0)

os.system("ping -c 2 1.1.1.1")
print("here is parent proc")
child_proc_exit_status = os.wait()
print("child exit with status: ", child_proc_exit_status[1])

