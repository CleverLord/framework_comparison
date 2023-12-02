import time
import subprocess
import os

MAPS_PATHS = ['--mapFilePath=./EvacuationMaps/board_1_500.csv', '--mapFilePath=./EvacuationMaps/board_2_500.csv', '--mapFilePath=./EvacuationMaps/board_3_100.csv']
REPETITIONS= [30, 30, 30]

for x,map_path in enumerate(MAPS_PATHS):
    start = time.time()
    lastPrintTime=0
    reps=REPETITIONS[x]
    for y in range(reps):
        subprocess.run(["./Evacuation_LinuxServerBuild.x86_64", map_path, "--immediateShutdown=true"],
                stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        if time.time()-lastPrintTime>10:
            print("map: <<{}>>, rep: <<{}>>, time elapsed: <<{}>>".format(map_path, y, time.time()-start), flush=True)
            lastPrintTime=time.time()
    end = time.time()
    total_time = end - start    
    print("Finished Bootups!, map: <<{}>>, rep: <<{}>>, time: <<{}>>".format(map_path, reps, total_time), flush=True)
