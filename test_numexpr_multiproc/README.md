#Benchmark: Numpy with/without Numexpr and with/without multiprocessing

This a litle benchmark between Numpy with Numexpr and without Numexpr and with/without multiprocessing.

Numexpr is a fast numerical array expression evaluator for Python, NumPy, PyTables, pandas, bcolz and more:
https://github.com/pydata/numexpr


##Results
TODO: write test results here...

In [1]: %%timeit -n1
   ...: %run testing_poolmultiprocessing_numexpr.py
   ...: 
	Creating random arrays - Pid: 8637
	Creating random arrays - Pid: 8638
	Creating random arrays - Pid: 8640
	Creating random arrays - Pid: 8639
	Starting computations... - Pid: 8640
	Starting computations... - Pid: 8637
	Starting computations... - Pid: 8639
	Starting computations... - Pid: 8638
	Process completed successfully! - Pid: 8640
	Array size: 25000000
	Process completed successfully! - Pid: 8639
	Array size: 25000000
	Creating random arrays - Pid: 8640
	Creating random arrays - Pid: 8639
	Process completed successfully! - Pid: 8637
	Array size: 25000000
	Creating random arrays - Pid: 8637
	Process completed successfully! - Pid: 8638
	Array size: 25000000
	Creating random arrays - Pid: 8638
	Starting computations... - Pid: 8639
	Starting computations... - Pid: 8637
	Starting computations... - Pid: 8638
	Starting computations... - Pid: 8640
	Process completed successfully! - Pid: 8638
	Array size: 25000000
	Creating random arrays - Pid: 8638
	Process completed successfully! - Pid: 8639
	Array size: 25000000
	Creating random arrays - Pid: 8639
	Process completed successfully! - Pid: 8637
	Array size: 25000000
	Creating random arrays - Pid: 8637
	Process completed successfully! - Pid: 8640
	Array size: 25000000
	Creating random arrays - Pid: 8640
	Starting computations... - Pid: 8638
	Starting computations... - Pid: 8639
	Starting computations... - Pid: 8637
	Starting computations... - Pid: 8640
	Process completed successfully! - Pid: 8638
	Array size: 25000000
	Creating random arrays - Pid: 8638
	Process completed successfully! - Pid: 8639
	Array size: 25000000
	Creating random arrays - Pid: 8639
	Process completed successfully! - Pid: 8637
	Array size: 25000000
	Creating random arrays - Pid: 8637
	Process completed successfully! - Pid: 8640
	Array size: 25000000
	Creating random arrays - Pid: 8640
	Starting computations... - Pid: 8638
	Starting computations... - Pid: 8639
	Starting computations... - Pid: 8637
	Starting computations... - Pid: 8640
	Process completed successfully! - Pid: 8639
	Array size: 25000000
	Creating random arrays - Pid: 8639
	Process completed successfully! - Pid: 8638
	Array size: 25000000
	Creating random arrays - Pid: 8638
	Process completed successfully! - Pid: 8637
	Array size: 25000000
	Creating random arrays - Pid: 8637
	Process completed successfully! - Pid: 8640
	Array size: 25000000
	Creating random arrays - Pid: 8640
	Starting computations... - Pid: 8638
	Starting computations... - Pid: 8639
	Starting computations... - Pid: 8637
	Starting computations... - Pid: 8640
	Process completed successfully! - Pid: 8639
	Array size: 25000000
	Creating random arrays - Pid: 8639
	Process completed successfully! - Pid: 8638
	Array size: 25000000
	Creating random arrays - Pid: 8638
	Process completed successfully! - Pid: 8637
	Array size: 25000000
	Creating random arrays - Pid: 8637
	Process completed successfully! - Pid: 8640
	Array size: 25000000
	Creating random arrays - Pid: 8640
	Starting computations... - Pid: 8639
	Starting computations... - Pid: 8638
	Starting computations... - Pid: 8637
	Starting computations... - Pid: 8640
	Process completed successfully! - Pid: 8639
	Array size: 25000000
	Creating random arrays - Pid: 8639
	Process completed successfully! - Pid: 8638
	Array size: 25000000
	Creating random arrays - Pid: 8638
	Process completed successfully! - Pid: 8637
	Array size: 25000000
	Creating random arrays - Pid: 8637
	Process completed successfully! - Pid: 8640
	Array size: 25000000
	Starting computations... - Pid: 8639
	Starting computations... - Pid: 8638
	Starting computations... - Pid: 8637
	Process completed successfully! - Pid: 8639
	Array size: 25000000
	Creating random arrays - Pid: 8639
	Process completed successfully! - Pid: 8638
	Array size: 25000000
	Creating random arrays - Pid: 8638
	Process completed successfully! - Pid: 8637
	Array size: 25000000
	Creating random arrays - Pid: 8637
	Starting computations... - Pid: 8639
	Starting computations... - Pid: 8638
	Starting computations... - Pid: 8637
	Process completed successfully! - Pid: 8639
	Array size: 25000000
	Process completed successfully! - Pid: 8638
	Array size: 25000000
	Process completed successfully! - Pid: 8637
	Array size: 25000000
	Creating random arrays - Pid: 8660
	Creating random arrays - Pid: 8661
	Creating random arrays - Pid: 8662
	Creating random arrays - Pid: 8663
	Starting computations... - Pid: 8662
	Starting computations... - Pid: 8661
	Starting computations... - Pid: 8660
	Starting computations... - Pid: 8663
	Process completed successfully! - Pid: 8661
	Array size: 25000000
	Creating random arrays - Pid: 8661
	Process completed successfully! - Pid: 8663
	Array size: 25000000
	Creating random arrays - Pid: 8663
	Process completed successfully! - Pid: 8660
	Array size: 25000000
	Creating random arrays - Pid: 8660
	Process completed successfully! - Pid: 8662
	Array size: 25000000
	Creating random arrays - Pid: 8662
	Starting computations... - Pid: 8661
	Starting computations... - Pid: 8663
	Starting computations... - Pid: 8660
	Starting computations... - Pid: 8662
	Process completed successfully! - Pid: 8661
	Array size: 25000000
	Creating random arrays - Pid: 8661
	Process completed successfully! - Pid: 8663
	Array size: 25000000
	Process completed successfully! - Pid: 8662
	Array size: 25000000
	Creating random arrays - Pid: 8662
	Creating random arrays - Pid: 8663
	Process completed successfully! - Pid: 8660
	Array size: 25000000
	Creating random arrays - Pid: 8660
	Starting computations... - Pid: 8661
	Starting computations... - Pid: 8663
	Starting computations... - Pid: 8660
	Starting computations... - Pid: 8662
	Process completed successfully! - Pid: 8661
	Array size: 25000000
	Creating random arrays - Pid: 8661
	Process completed successfully! - Pid: 8660
	Array size: 25000000
	Creating random arrays - Pid: 8660
	Process completed successfully! - Pid: 8663
	Array size: 25000000
	Creating random arrays - Pid: 8663
	Process completed successfully! - Pid: 8662
	Array size: 25000000
	Creating random arrays - Pid: 8662
	Starting computations... - Pid: 8660
	Starting computations... - Pid: 8661
	Starting computations... - Pid: 8663
	Starting computations... - Pid: 8662
	Process completed successfully! - Pid: 8660
	Array size: 25000000
	Creating random arrays - Pid: 8660
	Process completed successfully! - Pid: 8661
	Array size: 25000000
	Creating random arrays - Pid: 8661
	Process completed successfully! - Pid: 8663
	Array size: 25000000
	Creating random arrays - Pid: 8663
	Process completed successfully! - Pid: 8662
	Array size: 25000000
	Creating random arrays - Pid: 8662
	Starting computations... - Pid: 8660
	Starting computations... - Pid: 8661
	Starting computations... - Pid: 8663
	Starting computations... - Pid: 8662
	Process completed successfully! - Pid: 8660
	Array size: 25000000
	Creating random arrays - Pid: 8660
	Process completed successfully! - Pid: 8663
	Array size: 25000000
	Creating random arrays - Pid: 8663
	Process completed successfully! - Pid: 8661
	Array size: 25000000
	Creating random arrays - Pid: 8661
	Process completed successfully! - Pid: 8662
	Array size: 25000000
	Creating random arrays - Pid: 8662
	Starting computations... - Pid: 8660
	Starting computations... - Pid: 8663
	Starting computations... - Pid: 8661
	Process completed successfully! - Pid: 8660
	Array size: 25000000
	Creating random arrays - Pid: 8660
	Starting computations... - Pid: 8662
	Process completed successfully! - Pid: 8661
	Array size: 25000000
	Process completed successfully! - Pid: 8663
	Array size: 25000000
	Creating random arrays - Pid: 8661
	Creating random arrays - Pid: 8663
	Process completed successfully! - Pid: 8662
	Array size: 25000000
	Starting computations... - Pid: 8660
	Starting computations... - Pid: 8661
	Starting computations... - Pid: 8663
	Process completed successfully! - Pid: 8660
	Array size: 25000000
	Creating random arrays - Pid: 8660
	Process completed successfully! - Pid: 8661
	Array size: 25000000
	Creating random arrays - Pid: 8661
	Process completed successfully! - Pid: 8663
	Array size: 25000000
	Creating random arrays - Pid: 8663
	Starting computations... - Pid: 8660
	Starting computations... - Pid: 8661
	Process completed successfully! - Pid: 8660
	Array size: 25000000
	Starting computations... - Pid: 8663
	Process completed successfully! - Pid: 8661
	Array size: 25000000
	Process completed successfully! - Pid: 8663
	Array size: 25000000
	Creating random arrays - Pid: 8683
	Creating random arrays - Pid: 8684
	Creating random arrays - Pid: 8685
	Creating random arrays - Pid: 8686
	Starting computations... - Pid: 8683
	Starting computations... - Pid: 8684
	Starting computations... - Pid: 8686
	Starting computations... - Pid: 8685
	Process completed successfully! - Pid: 8683
	Array size: 25000000
	Creating random arrays - Pid: 8683
	Process completed successfully! - Pid: 8686
	Array size: 25000000
	Process completed successfully! - Pid: 8684
	Array size: 25000000
	Creating random arrays - Pid: 8686
	Creating random arrays - Pid: 8684
	Process completed successfully! - Pid: 8685
	Array size: 25000000
	Creating random arrays - Pid: 8685
	Starting computations... - Pid: 8683
	Starting computations... - Pid: 8685
	Starting computations... - Pid: 8686
	Starting computations... - Pid: 8684
	Process completed successfully! - Pid: 8683
	Array size: 25000000
	Creating random arrays - Pid: 8683
	Process completed successfully! - Pid: 8685
	Array size: 25000000
	Creating random arrays - Pid: 8685
	Process completed successfully! - Pid: 8684
	Array size: 25000000
	Creating random arrays - Pid: 8684
	Process completed successfully! - Pid: 8686
	Array size: 25000000
	Creating random arrays - Pid: 8686
	Starting computations... - Pid: 8685
	Starting computations... - Pid: 8686
	Starting computations... - Pid: 8683
	Starting computations... - Pid: 8684
	Process completed successfully! - Pid: 8685
	Array size: 25000000
	Creating random arrays - Pid: 8685
	Process completed successfully! - Pid: 8683
	Array size: 25000000
	Creating random arrays - Pid: 8683
	Process completed successfully! - Pid: 8684
	Array size: 25000000
	Process completed successfully! - Pid: 8686
	Creating random arrays - Pid: 8684
	Array size: 25000000
	Creating random arrays - Pid: 8686
	Starting computations... - Pid: 8685
	Starting computations... - Pid: 8683
	Starting computations... - Pid: 8686
	Starting computations... - Pid: 8684
	Process completed successfully! - Pid: 8685
	Array size: 25000000
	Creating random arrays - Pid: 8685
	Process completed successfully! - Pid: 8683
	Array size: 25000000
	Creating random arrays - Pid: 8683
	Process completed successfully! - Pid: 8686
	Array size: 25000000
	Creating random arrays - Pid: 8686
	Process completed successfully! - Pid: 8684
	Array size: 25000000
	Creating random arrays - Pid: 8684
	Starting computations... - Pid: 8685
	Starting computations... - Pid: 8683
	Starting computations... - Pid: 8686
	Process completed successfully! - Pid: 8685
	Array size: 25000000
	Creating random arrays - Pid: 8685
	Starting computations... - Pid: 8684
	Process completed successfully! - Pid: 8683
	Array size: 25000000
	Creating random arrays - Pid: 8683
	Process completed successfully! - Pid: 8686
	Array size: 25000000
	Creating random arrays - Pid: 8686
	Process completed successfully! - Pid: 8684
	Array size: 25000000
	Creating random arrays - Pid: 8684
	Starting computations... - Pid: 8685
	Starting computations... - Pid: 8683
	Starting computations... - Pid: 8686
	Process completed successfully! - Pid: 8685
	Array size: 25000000
	Creating random arrays - Pid: 8685
	Process completed successfully! - Pid: 8683
	Array size: 25000000
	Creating random arrays - Pid: 8683
	Starting computations... - Pid: 8684
	Process completed successfully! - Pid: 8686
	Array size: 25000000
	Creating random arrays - Pid: 8686
	Process completed successfully! - Pid: 8684
	Array size: 25000000
	Starting computations... - Pid: 8685
	Starting computations... - Pid: 8683
	Starting computations... - Pid: 8686
	Process completed successfully! - Pid: 8685
	Array size: 25000000
	Creating random arrays - Pid: 8685
	Process completed successfully! - Pid: 8683
	Array size: 25000000
	Creating random arrays - Pid: 8683
	Process completed successfully! - Pid: 8686
	Array size: 25000000
	Creating random arrays - Pid: 8686
	Starting computations... - Pid: 8685
	Starting computations... - Pid: 8683
	Starting computations... - Pid: 8686
	Process completed successfully! - Pid: 8685
	Array size: 25000000
	Process completed successfully! - Pid: 8683
	Array size: 25000000
	Process completed successfully! - Pid: 8686
	Array size: 25000000
1 loops, best of 3: 22.9 s per loop



