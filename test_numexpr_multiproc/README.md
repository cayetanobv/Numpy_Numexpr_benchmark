#Benchmark: Numpy with/without Numexpr and with/without multiprocessing

This a litle benchmark between Numpy with Numexpr and without Numexpr and with/without multiprocessing.

Numexpr is a fast numerical array expression evaluator for Python, NumPy, PyTables, pandas, bcolz and more:
https://github.com/pydata/numexpr


##Requeriments
- Numpy
- Numexpr
- IPython

Computer used in test: AMD Athlon(tm) X4 750K Quad Core Processor, 16 GB RAM

TODO: ipython notebooks, 

##Results

```
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
```

```
In [2]: %%timeit -n1
%run testing_poolmultiprocessing.py
   ...: 
	Creating random arrays - Pid: 8708
	Creating random arrays - Pid: 8709
	Creating random arrays - Pid: 8710
	Creating random arrays - Pid: 8711
	Starting computations... - Pid: 8708
	Starting computations... - Pid: 8711
	Starting computations... - Pid: 8709
	Starting computations... - Pid: 8710
	Process completed successfully! - Pid: 8708
	Array size: 25000000
	Process completed successfully! - Pid: 8711
	Array size: 25000000
	Creating random arrays - Pid: 8708
	Creating random arrays - Pid: 8711
	Process completed successfully! - Pid: 8709
	Array size: 25000000
	Creating random arrays - Pid: 8709
	Process completed successfully! - Pid: 8710
	Array size: 25000000
	Creating random arrays - Pid: 8710
	Starting computations... - Pid: 8708
	Starting computations... - Pid: 8711
	Starting computations... - Pid: 8709
	Starting computations... - Pid: 8710
	Process completed successfully! - Pid: 8711
	Array size: 25000000
	Creating random arrays - Pid: 8711
	Process completed successfully! - Pid: 8709
	Array size: 25000000
	Creating random arrays - Pid: 8709
	Process completed successfully! - Pid: 8708
	Array size: 25000000
	Creating random arrays - Pid: 8708
	Process completed successfully! - Pid: 8710
	Array size: 25000000
	Creating random arrays - Pid: 8710
	Starting computations... - Pid: 8711
	Starting computations... - Pid: 8709
	Starting computations... - Pid: 8708
	Starting computations... - Pid: 8710
	Process completed successfully! - Pid: 8711
	Array size: 25000000
	Creating random arrays - Pid: 8711
	Process completed successfully! - Pid: 8708
	Array size: 25000000
	Creating random arrays - Pid: 8708
	Process completed successfully! - Pid: 8709
	Array size: 25000000
	Creating random arrays - Pid: 8709
	Process completed successfully! - Pid: 8710
	Array size: 25000000
	Creating random arrays - Pid: 8710
	Starting computations... - Pid: 8711
	Starting computations... - Pid: 8708
	Starting computations... - Pid: 8709
	Starting computations... - Pid: 8710
	Process completed successfully! - Pid: 8711
	Array size: 25000000
	Creating random arrays - Pid: 8711
	Process completed successfully! - Pid: 8708
	Array size: 25000000
	Creating random arrays - Pid: 8708
	Process completed successfully! - Pid: 8709
	Array size: 25000000
	Creating random arrays - Pid: 8709
	Process completed successfully! - Pid: 8710
	Array size: 25000000
	Creating random arrays - Pid: 8710
	Starting computations... - Pid: 8711
	Starting computations... - Pid: 8709
	Starting computations... - Pid: 8708
	Starting computations... - Pid: 8710
	Process completed successfully! - Pid: 8711
	Array size: 25000000
	Creating random arrays - Pid: 8711
	Process completed successfully! - Pid: 8709
	Array size: 25000000
	Creating random arrays - Pid: 8709
	Process completed successfully! - Pid: 8710
	Array size: 25000000
	Creating random arrays - Pid: 8710
	Process completed successfully! - Pid: 8708
	Array size: 25000000
	Creating random arrays - Pid: 8708
	Starting computations... - Pid: 8711
	Starting computations... - Pid: 8709
	Starting computations... - Pid: 8710
	Starting computations... - Pid: 8708
	Process completed successfully! - Pid: 8711
	Array size: 25000000
	Creating random arrays - Pid: 8711
	Process completed successfully! - Pid: 8709
	Array size: 25000000
	Creating random arrays - Pid: 8709
	Process completed successfully! - Pid: 8710
	Array size: 25000000
	Creating random arrays - Pid: 8710
	Process completed successfully! - Pid: 8708
	Array size: 25000000
	Starting computations... - Pid: 8711
	Starting computations... - Pid: 8709
	Starting computations... - Pid: 8710
	Process completed successfully! - Pid: 8711
	Array size: 25000000
	Creating random arrays - Pid: 8711
	Process completed successfully! - Pid: 8709
	Array size: 25000000
	Creating random arrays - Pid: 8709
	Starting computations... - Pid: 8711
	Process completed successfully! - Pid: 8710
	Array size: 25000000
	Creating random arrays - Pid: 8710
	Starting computations... - Pid: 8709
	Starting computations... - Pid: 8710
	Process completed successfully! - Pid: 8711
	Array size: 25000000
	Process completed successfully! - Pid: 8709
	Array size: 25000000
	Process completed successfully! - Pid: 8710
	Array size: 25000000
	Creating random arrays - Pid: 8796
	Creating random arrays - Pid: 8797
	Creating random arrays - Pid: 8798
	Creating random arrays - Pid: 8799
	Starting computations... - Pid: 8798
	Starting computations... - Pid: 8799
	Starting computations... - Pid: 8796
	Starting computations... - Pid: 8797
	Process completed successfully! - Pid: 8796
	Array size: 25000000
	Creating random arrays - Pid: 8796
	Process completed successfully! - Pid: 8797
	Array size: 25000000
	Creating random arrays - Pid: 8797
	Process completed successfully! - Pid: 8798
	Array size: 25000000
	Creating random arrays - Pid: 8798
	Process completed successfully! - Pid: 8799
	Array size: 25000000
	Creating random arrays - Pid: 8799
	Starting computations... - Pid: 8796
	Starting computations... - Pid: 8797
	Starting computations... - Pid: 8798
	Starting computations... - Pid: 8799
	Process completed successfully! - Pid: 8796
	Array size: 25000000
	Creating random arrays - Pid: 8796
	Process completed successfully! - Pid: 8797
	Array size: 25000000
	Creating random arrays - Pid: 8797
	Process completed successfully! - Pid: 8799
	Array size: 25000000
	Creating random arrays - Pid: 8799
	Process completed successfully! - Pid: 8798
	Array size: 25000000
	Creating random arrays - Pid: 8798
	Starting computations... - Pid: 8796
	Starting computations... - Pid: 8797
	Starting computations... - Pid: 8799
	Starting computations... - Pid: 8798
	Process completed successfully! - Pid: 8796
	Array size: 25000000
	Creating random arrays - Pid: 8796
	Process completed successfully! - Pid: 8797
	Array size: 25000000
	Creating random arrays - Pid: 8797
	Process completed successfully! - Pid: 8799
	Array size: 25000000
	Creating random arrays - Pid: 8799
	Process completed successfully! - Pid: 8798
	Array size: 25000000
	Creating random arrays - Pid: 8798
	Starting computations... - Pid: 8796
	Starting computations... - Pid: 8797
	Starting computations... - Pid: 8798
	Starting computations... - Pid: 8799
	Process completed successfully! - Pid: 8796
	Array size: 25000000
	Creating random arrays - Pid: 8796
	Process completed successfully! - Pid: 8797
	Array size: 25000000
	Creating random arrays - Pid: 8797
	Process completed successfully! - Pid: 8799
	Array size: 25000000
	Creating random arrays - Pid: 8799
	Process completed successfully! - Pid: 8798
	Array size: 25000000
	Creating random arrays - Pid: 8798
	Starting computations... - Pid: 8796
	Starting computations... - Pid: 8797
	Starting computations... - Pid: 8799
	Starting computations... - Pid: 8798
	Process completed successfully! - Pid: 8796
	Array size: 25000000
	Creating random arrays - Pid: 8796
	Process completed successfully! - Pid: 8799
	Array size: 25000000
	Creating random arrays - Pid: 8799
	Process completed successfully! - Pid: 8797
	Array size: 25000000
	Creating random arrays - Pid: 8797
	Process completed successfully! - Pid: 8798
	Array size: 25000000
	Creating random arrays - Pid: 8798
	Starting computations... - Pid: 8796
	Starting computations... - Pid: 8799
	Starting computations... - Pid: 8797
	Starting computations... - Pid: 8798
	Process completed successfully! - Pid: 8796
	Array size: 25000000
	Creating random arrays - Pid: 8796
	Process completed successfully! - Pid: 8797
	Array size: 25000000
	Creating random arrays - Pid: 8797
	Process completed successfully! - Pid: 8799
	Array size: 25000000
	Creating random arrays - Pid: 8799
	Starting computations... - Pid: 8796
	Process completed successfully! - Pid: 8798
	Array size: 25000000
	Starting computations... - Pid: 8797
	Starting computations... - Pid: 8799
	Process completed successfully! - Pid: 8796
	Array size: 25000000
	Creating random arrays - Pid: 8796
	Process completed successfully! - Pid: 8799
	Array size: 25000000
	Creating random arrays - Pid: 8799
	Process completed successfully! - Pid: 8797
	Array size: 25000000
	Creating random arrays - Pid: 8797
	Starting computations... - Pid: 8796
	Starting computations... - Pid: 8799
	Starting computations... - Pid: 8797
	Process completed successfully! - Pid: 8799
	Array size: 25000000
	Process completed successfully! - Pid: 8796
	Array size: 25000000
	Process completed successfully! - Pid: 8797
	Array size: 25000000
	Creating random arrays - Pid: 8870
	Creating random arrays - Pid: 8871
	Creating random arrays - Pid: 8873
	Creating random arrays - Pid: 8872
	Starting computations... - Pid: 8870
	Starting computations... - Pid: 8872
	Starting computations... - Pid: 8873
	Starting computations... - Pid: 8871
	Process completed successfully! - Pid: 8872
	Array size: 25000000
	Process completed successfully! - Pid: 8870
	Array size: 25000000
	Creating random arrays - Pid: 8872
	Creating random arrays - Pid: 8870
	Process completed successfully! - Pid: 8871
	Array size: 25000000
	Creating random arrays - Pid: 8871
	Process completed successfully! - Pid: 8873
	Array size: 25000000
	Creating random arrays - Pid: 8873
	Starting computations... - Pid: 8870
	Starting computations... - Pid: 8872
	Starting computations... - Pid: 8871
	Starting computations... - Pid: 8873
	Process completed successfully! - Pid: 8872
	Array size: 25000000
	Creating random arrays - Pid: 8872
	Process completed successfully! - Pid: 8870
	Array size: 25000000
	Creating random arrays - Pid: 8870
	Process completed successfully! - Pid: 8871
	Array size: 25000000
	Creating random arrays - Pid: 8871
	Process completed successfully! - Pid: 8873
	Array size: 25000000
	Creating random arrays - Pid: 8873
	Starting computations... - Pid: 8872
	Starting computations... - Pid: 8870
	Starting computations... - Pid: 8871
	Starting computations... - Pid: 8873
	Process completed successfully! - Pid: 8870
	Array size: 25000000
	Creating random arrays - Pid: 8870
	Process completed successfully! - Pid: 8872
	Array size: 25000000
	Creating random arrays - Pid: 8872
	Process completed successfully! - Pid: 8873
	Array size: 25000000
	Creating random arrays - Pid: 8873
	Process completed successfully! - Pid: 8871
	Array size: 25000000
	Creating random arrays - Pid: 8871
	Starting computations... - Pid: 8870
	Starting computations... - Pid: 8872
	Starting computations... - Pid: 8873
	Starting computations... - Pid: 8871
	Process completed successfully! - Pid: 8870
	Array size: 25000000
	Creating random arrays - Pid: 8870
	Process completed successfully! - Pid: 8873
	Array size: 25000000
	Creating random arrays - Pid: 8873
	Process completed successfully! - Pid: 8872
	Array size: 25000000
	Creating random arrays - Pid: 8872
	Process completed successfully! - Pid: 8871
	Array size: 25000000
	Creating random arrays - Pid: 8871
	Starting computations... - Pid: 8870
	Starting computations... - Pid: 8873
	Starting computations... - Pid: 8871
	Starting computations... - Pid: 8872
	Process completed successfully! - Pid: 8870
	Array size: 25000000
	Creating random arrays - Pid: 8870
	Process completed successfully! - Pid: 8873
	Array size: 25000000
	Creating random arrays - Pid: 8873
	Process completed successfully! - Pid: 8872
	Array size: 25000000
	Creating random arrays - Pid: 8872
	Process completed successfully! - Pid: 8871
	Array size: 25000000
	Creating random arrays - Pid: 8871
	Starting computations... - Pid: 8870
	Starting computations... - Pid: 8873
	Starting computations... - Pid: 8872
	Starting computations... - Pid: 8871
	Process completed successfully! - Pid: 8870
	Array size: 25000000
	Creating random arrays - Pid: 8870
	Process completed successfully! - Pid: 8873
	Array size: 25000000
	Creating random arrays - Pid: 8873
	Process completed successfully! - Pid: 8872
	Array size: 25000000
	Creating random arrays - Pid: 8872
	Starting computations... - Pid: 8870
	Process completed successfully! - Pid: 8871
	Array size: 25000000
	Starting computations... - Pid: 8873
	Starting computations... - Pid: 8872
	Process completed successfully! - Pid: 8870
	Array size: 25000000
	Creating random arrays - Pid: 8870
	Process completed successfully! - Pid: 8872
	Array size: 25000000
	Creating random arrays - Pid: 8872
	Process completed successfully! - Pid: 8873
	Array size: 25000000
	Creating random arrays - Pid: 8873
	Starting computations... - Pid: 8870
	Starting computations... - Pid: 8873
	Starting computations... - Pid: 8872
	Process completed successfully! - Pid: 8870
	Array size: 25000000
	Process completed successfully! - Pid: 8873
	Array size: 25000000
	Process completed successfully! - Pid: 8872
	Array size: 25000000

1 loops, best of 3: 1min 28s per loop
```

```
In [3]: %%timeit -n1
%run test_nopoolmultiprocessing_numexpr.py
   ...: 
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000

1 loops, best of 3: 40.8 s per loop
```

```
In [4]: %%timeit -n1
%run /home/cayetano/Dropbox/documentos/python/GIS/Numpy_Numexpr_benchmark/test_numexpr_multiproc/test_nopoolmultiprocessing.py
   ...: 
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
	Creating random arrays - Pid: 8544
	Starting computations... - Pid: 8544
	Process completed successfully! - Pid: 8544
	Array size: 25000000
1 loops, best of 3: 4min 46s per loop
```
