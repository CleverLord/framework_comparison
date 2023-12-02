import time
import subprocess
import os

MAPS_PATHS = ['--mapFilePath=./EvacuationMaps/board_1_500.csv', '--mapFilePath=./EvacuationMaps/board_2_500.csv', '--mapFilePath=./EvacuationMaps/board_3_100.csv']
REPETITIONS= [1, 10, 1000]

print("Running Evacuation E2E! Current time: " + time.strftime("%H:%M:%S", time.localtime()), flush=True)
for x,map_path in enumerate(MAPS_PATHS):
    start = time.time()
    lastPrintTime=0
    reps=REPETITIONS[x]
    for y in range(reps):
        if y >= 2:
            subprocess.run(["./Evacuation_LinuxServerBuild.x86_64", map_path, "--repetitionsCount=1"],
                    stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        else:
            subprocess.run(["./Evacuation_LinuxServerBuild.x86_64", map_path, "--repetitionsCount=1"])
        if time.time()-lastPrintTime>10:
            print("Working on Evacuation E2E!, map: <<{}>>, rep: <<{}>>, time elapsed: <<{}>>".format(map_path, y, time.time()-start), flush=True)
            lastPrintTime=time.time()
    end = time.time()
    total_time = end - start
    sfs = (total_time / reps) 
    print("Finished Evacuation E2E!, map: <<{}>>, rep: <<{}>>, time: <<{}>>, seconds per simulation<<{}>>".format(map_path, reps, total_time, sfs), flush=True)
    print("Current time: " + time.strftime("%H:%M:%S", time.localtime()), flush=True)