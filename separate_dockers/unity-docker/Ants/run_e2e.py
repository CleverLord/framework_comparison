import time
import subprocess
import os

MAPS_PATHS = ['--mapFilePath=./Maps/updated_dungeon_map_100x100.csv','--mapFilePath=./Maps/updated_dungeon_map_100x100.csv','--mapFilePath=./Maps/updated_dungeon_map_100x100.csv',
               '--mapFilePath=./Maps/medium_dungeon_map_300x300.csv','--mapFilePath=./Maps/medium_dungeon_map_300x300.csv','--mapFilePath=./Maps/medium_dungeon_map_300x300.csv', 
               '--mapFilePath=./Maps/large_dungeon_map_500x500.csv','--mapFilePath=./Maps/large_dungeon_map_500x500.csv','--mapFilePath=./Maps/large_dungeon_map_500x500.csv']
ITERATIONS = [10,100,100,
                10,100,100,
                10,100,100]
REPETITIONS = [2,2,2,
                2,2,2,
                2,2,2]

print("Running Ants E2E! Current time: " + time.strftime("%H:%M:%S", time.localtime()), flush=True)
for x,map_path in enumerate(MAPS_PATHS):
    start = time.time()
    lastPrintTime=0
    reps=REPETITIONS[x]
    its=ITERATIONS[x]
    for y in range(reps):
        if y >= 2:
            subprocess.run(["./Ants_LinuxServerBuild.x86_64", map_path,"--iterationCount="+str(its), "--repetitionsCount=1","printInterval=15" ],
                    stdout=subprocess.DEVNULL, stderr=subprocess.STDOUT)
        else:
            subprocess.run(["./Ants_LinuxServerBuild.x86_64", map_path,"--iterationCount="+str(its), "--repetitionsCount=1"])
        if time.time()-lastPrintTime>10:
            print("Working on Ants E2E map: <<{}>>, rep: <<{}>>, time elapsed: <<{}>>".format(map_path, y, time.time()-start), flush=True)
            lastPrintTime=time.time()
    end = time.time()
    total_time = end - start    
    spf = (total_time / reps) * 10000 / its
    print("Finished Ants E2E!, map: <<{}>>, rep: <<{}>>, time: <<{}>>, seconds per frame<<{}e-4>>".format(map_path, reps, total_time, spf), flush=True)
    print("Current time: " + time.strftime("%H:%M:%S", time.localtime()), flush=True)