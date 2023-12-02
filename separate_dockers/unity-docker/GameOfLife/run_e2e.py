import time
import subprocess
import os

MAPS_PATHS = ['--mapFilePath=./MockMaps/10x10board.csv', '--mapFilePath=./MockMaps/100x100board.csv', '--mapFilePath=./MockMaps/1000x1000board.csv']
ITERATIONS = [10000, 1000, 100]
REPETITIONS= [100, 10, 10]

for x,map_path in enumerate(MAPS_PATHS):
    start = time.time()
    lastPrintTime=0
    reps=REPETITIONS[x]
    its=ITERATIONS[x]
    for y in range(reps):
        if y >= 2:
            subprocess.run(["./GameOfLife_LinuxServerBuild.x86_64", map_path, "--iterationCount="+str(its), "--repetitionsCount=1"],
                    stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        else:
            subprocess.run(["./GameOfLife_LinuxServerBuild.x86_64", map_path, "--iterationCount="+str(its), "--repetitionsCount=1"])
        if time.time()-lastPrintTime>10:
            print("Working on GameOfLife E2E!, map: <<{}>>, rep: <<{}>>, time elapsed: <<{}>>".format(map_path, y, time.time()-start), flush=True)
            lastPrintTime=time.time()
    end = time.time()
    total_time = end - start
    fps = ((total_time / reps)*1000 / its)
    print("Finished GameOfLife E2E!, map: <<{}>>, rep: <<{}>>, time: <<{}>>, fps <<{}e-3>>".format(map_path, reps, total_time, fps), flush=True)
