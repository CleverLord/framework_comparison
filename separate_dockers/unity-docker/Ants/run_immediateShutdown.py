import time
import subprocess
import os

MAPS_PATHS = ['--mapFilePath=./Maps/updated_dungeon_map_100x100.csv', '--mapFilePath=./Maps/medium_dungeon_map_300x300.csv', '--mapFilePath=./Maps/large_dungeon_map_500x500.csv']
REPETITIONS= [30, 30, 30]

for x,map_path in enumerate(MAPS_PATHS):
    start = time.time()
    lastPrintTime=0
    reps=REPETITIONS[x]
    for y in range(reps):
        subprocess.run(["./Ants_LinuxServerBuild.x86_64", map_path, "--immediateShutdown=true"],
                stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        if time.time()-lastPrintTime>10:
            print("map: <<{}>>, rep: <<{}>>, time elapsed: <<{}>>".format(map_path, y, time.time()-start), flush=True)
            lastPrintTime=time.time()
    end = time.time()
    total_time = end - start    
    print("Finished Ants Bootups!, map: <<{}>>, rep: <<{}>>, time: <<{}>>".format(map_path, reps, total_time), flush=True)
