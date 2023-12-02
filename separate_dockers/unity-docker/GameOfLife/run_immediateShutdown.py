import time
import subprocess
import os

MAPS_PATHS = ['--mapFilePath=./MockMaps/10x10board.csv', '--mapFilePath=./MockMaps/100x100board.csv', '--mapFilePath=./MockMaps/1000x1000board.csv']
REPETITIONS= [30, 30, 30]

print("Running GameOfLife Bootups! Current time: " + time.strftime("%H:%M:%S", time.localtime()), flush=True)
for x,map_path in enumerate(MAPS_PATHS):
    start = time.time()
    lastPrintTime=0
    reps=REPETITIONS[x]
    for y in range(reps):
        subprocess.run(["./GameOfLife_LinuxServerBuild.x86_64", map_path, "--immediateShutdown=true"],
                stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        if time.time()-lastPrintTime>10:
            print("Working on GameOfLife Bootups!, map: <<{}>>, rep: <<{}>>, time elapsed: <<{}>>".format(map_path, y, time.time()-start), flush=True)
            lastPrintTime=time.time()
    end = time.time()
    total_time = end - start    
    print("Finished GameOfLife Bootups!, map: <<{}>>, rep: <<{}>>, time: <<{}>>".format(map_path, reps, total_time), flush=True)
    print("Current time: " + time.strftime("%H:%M:%S", time.localtime()), flush=True)