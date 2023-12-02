cd GameOfLife
chmod +x run_all_v2.sh
chmod +x GameOfLife_LinuxServerBuild.x86_64
docker build -t gameoflife__unity_brainbuild .
docker run gameoflife__unity_brainbuild
cd ..

cd Evacuation
chmod +x run_all_v2.sh
chmod +x Evacuation_LinuxServerBuild.x86_64
docker build -t evacuation__unity_brainbuild .
docker run evacuation__unity_brainbuild
cd ..

cd Ants
chmod +x run_all_v2.sh
chmod +x Ants_LinuxServerBuild.x86_64
docker build -t ants__unity_brainbuild .
docker run ants__unity_brainbuild
cd ..
