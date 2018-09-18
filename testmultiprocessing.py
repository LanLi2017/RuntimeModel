from multiprocessing import Pool, Process
from time import sleep
import os


def sum(task, a, b):
    return a+b

if __name__=="__main__":
    myPool = Pool(5)

    tasks=[]

    for i in range(10):
        tuple=("task"+str(i), i+10, i+20)
        tasks.append(tuple)

    print(tasks)

    print("Submitted tasks to pool")
    results = myPool.starmap(sum, tasks)
    print("Got the results")

    for result in results:
        print(result)
