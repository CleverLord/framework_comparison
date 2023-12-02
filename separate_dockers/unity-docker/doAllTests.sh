echo "Running GameOfLife"
date +"Current time: %Y-%m-%d %H:%M:%S"
cd GameOfLife
echo "setting permissions for .sh's for GameOfLife"
chmod +x run_all_v2.sh
chmod +x GameOfLife_LinuxServerBuild.x86_64
echo "building GameOfLife docker image"
docker build -t gameoflife__unity_brainbuild .
echo "running GameOfLife docker image"
docker run gameoflife__unity_brainbuild
echo "done with GameOfLife"
cd ..

echo "Running Evacuation"
date +"Current time: %Y-%m-%d %H:%M:%S"
cd Evacuation
echo "setting permissions for .sh's for Evacuation"
chmod +x run_all_v2.sh
chmod +x Evacuation_LinuxServerBuild.x86_64
echo "building Evacuation docker image"
docker build -t evacuation__unity_brainbuild .
echo "running Evacuation docker image"
docker run evacuation__unity_brainbuild
echo "done with Evacuation"
cd ..

echo "Running Ants"
date +"Current time: %Y-%m-%d %H:%M:%S"
cd Ants
echo "setting permissions for .sh's for Ants"
chmod +x run_all_v2.sh
chmod +x Ants_LinuxServerBuild.x86_64
echo "building Ants docker image"
docker build -t ants__unity_brainbuild .
echo "running Ants docker image"
docker run ants__unity_brainbuild
echo "done with Ants"
cd ..

echo "Done with all tests"
date +"Current time: %Y-%m-%d %H:%M:%S"
