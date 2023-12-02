import time
import subprocess
import os

MAPS_PATHS = ['--mapFilePath=./Maps/updated_dungeon_map_100x100.csv', '--mapFilePath=./Maps/medium_dungeon_map_300x300.csv', '--mapFilePath=./Maps/large_dungeon_map_500x500.csv']
ITERATIONS = [10000, 10000, 10000]
REPETITIONS = [20, 1, 1]

for x,map_path in enumerate(MAPS_PATHS):
    start = time.time()
    lastPrintTime=0
    reps=REPETITIONS[x]
    its=ITERATIONS[x]
    for y in range(reps):
        if y >= 2:
            subprocess.run(["./Ants_LinuxServerBuild.x86_64", map_path,"--iterationCount="+str(its), "--repetitionsCount=1"],
                    stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        else:
            subprocess.run(["./Ants_LinuxServerBuild.x86_64", map_path,"--iterationCount="+str(its), "--repetitionsCount=1"])
        if time.time()-lastPrintTime>10:
            print("Working on Ants E2E map: <<{}>>, rep: <<{}>>, time elapsed: <<{}>>".format(map_path, y, time.time()-start), flush=True)
            lastPrintTime=time.time()
    end = time.time()
    total_time = end - start    
    fps = (total_time / reps)
    print("Finished Ants E2E!, map: <<{}>>, rep: <<{}>>, time: <<{}>>, fps<<{}e-4>>".format(map_path, reps, total_time, fps), flush=True)
