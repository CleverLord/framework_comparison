# How to run
`chmod +x ./doAllTests.sh`
`./doAllTests.sh | tee doAllTestsLogs.txt`
# How to read the results
- (optional) Use the `LogFilter.ipynb` to filter the logs (you get ~80% less logs)
- For Game Of Life search for `Finished GameOfLife E2E`, read fps (to make it tricky, this is not fps, this is time per frame "spf")
- For Evaluation search for `Finished Evaluation E2E`, read fps (to make it even trickier this is time per simulation). Read iterations count from right above in the Unity Logs and divide fps by the iterations count to get the spf
- For Ants search for `Finished Ants E2E`, read fps (to make it tricky, this is not fps, this is time per frame "spf")