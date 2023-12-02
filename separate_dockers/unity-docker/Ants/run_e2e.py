import time
import subprocess
import os

MAPS_PATHS = ['--mapFilePath=./Maps/updated_dungeon_map_100x100.csv', '--mapFilePath=./Maps/medium_dungeon_map_300x300.csv', '--mapFilePath=./MockMaps/1000x1000board.csv']
ITERATIONS = [10000, 10000, 10000]
REPETITIONS = [100, 1, 1]

for x,map_path in enumerate(MAPS_PATHS):
    start = time.time()
    lastPrintTime=0
    reps=REPETITIONS[x]
    its=ITERATIONS[x]
    for y in range(reps):
        targetStdout = subprocess.DEVNULL if y>=2 else subprocess.STDOUT
        targetStderr = subprocess.STDOUT
        subprocess.run(["./Ants_LinuxServerBuild.x86_64", map_path,"--iterationCount="+str(its), "--repetitionsCount=1"],
                       stdout=targetStdout, stderr=targetStderr)
        if time.time()-lastPrintTime>10:
            print("map: <<{}>>, rep: <<{}>>, time elapsed: <<{}>>".format(map_path, y, time.time()-start), flush=True)
            lastPrintTime=time.time()
    end = time.time()
    total_time = end - start    
    fps = (total_time / reps)+"e-4"
    print("Finished Ants E2E!, map: <<{}>>, rep: <<{}>>, time: <<{}>>, fps<<{}>>".format(map_path, reps, total_time, fps), flush=True)
