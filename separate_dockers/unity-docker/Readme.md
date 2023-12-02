# How to run
```
fkaminski@thebrain:~/benchmarks$
$ cd Unity/framework_comparison/separate_dockers/unity-docker/
$ chmod +x ./doAllTests.sh
$ ./doAllTests.sh | tee doAllTestsLogs.txt
```
# How to read the results
- (optional) Use the `LogFilter.ipynb` to filter the logs (you get ~50% less logs)
- For Game Of Life search for `Finished GameOfLife E2E`, read seconds per iterations
- For Evaluation search for `Finished Evaluation E2E`, read seconds per simulation. Then from the logs above (Unity logs) read how many iterations were made per simulation. Divide seconds per simulation by iterations per simulation to get seconds per iteration
- For Ants search for `Finished Ants E2E`, read seconds per iterations
## Extras
- Every simulation has bootup section, ex. search for `Finished GameOfLife Bootups`, where simulation was initialized, but not a signle iteration was made. That might be found useful to compare bootup times

# Misc
`git fetch && git reset --hard origin/Unity && chmod +x doAllTests.sh && ./doAllTests.sh 2>&1 | tee doAllTestsLogs.txt`