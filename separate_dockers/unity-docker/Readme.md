# How to run
`chmod +x ./doAllTests.sh`
`./doAllTests.sh | tee doAllTestsLogs.txt`
# How to read the results
- (optional) Use the `LogFilter.ipynb` to filter the logs (you get ~80% less logs)
- For Game Of Life search for `Finished GameOfLife E2E`, read fps
- For Evaluation search for `Finished Evaluation E2E`, there is no fps, since we don't know how many frames there was. Read the FPS value from inside the Unity logs
- For Ants search for `Finished Ants E2E`, read fps