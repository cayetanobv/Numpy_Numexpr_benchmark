# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <markdowncell>

# #Benchmark: Numpy with Numexpr and without Numexpr
# 
# This a litle benchmark between Numpy with Numexpr and without Numexpr.
# 
# Numexpr is a fast numerical array expression evaluator for Python, NumPy, PyTables, pandas, bcolz and more:
# https://github.com/pydata/numexpr
# 
# 
# ##Requeriments
# - Numpy
# - Numexpr
# - IPython
# - Line profiler
# - Memory profiler
# - Psutil (optional but highly recommended)
# 
# 
# ##Results
# 
# All scripts are launched inside IPython.
# Default ndarray size used in test is 25*10^6.
# This is a limited test because I have used only one ndarray size (large but only one).
# Under these conditions the result is that Numpy with Numexpr is more than seven times faster than without it.
# 
# Computer used in test: AMD Athlon(tm) X4 750K Quad Core Processor, 16 GB RAM

# <markdowncell>

# ###Time
# - Run script with Numexpr:

# <codecell>

%%timeit -n1
%run /home/cayetano/Dropbox/documentos/python/GIS/Numpy_Numexpr_benchmark/test_numexpr.py

# <markdowncell>

# - Run script without Numexpr:

# <codecell>

%%timeit -n1
%run /home/cayetano/Dropbox/documentos/python/GIS/Numpy_Numexpr_benchmark/test_nonumexpr.py

# <markdowncell>

# 
# ###Code profiling: testNumexpr() 
# 
# - Profiling function testNumexpr() with IPython %prun magic function:

# <rawcell>

# %prun testNumexpr(5000)

# <markdowncell>

# ```   
#    65 function calls in 1.340 seconds
# 
#    Ordered by: internal time
# 
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         2    0.817    0.408    0.817    0.408 {method 'random_sample' of 'mtrand.RandomState' objects}
#         3    0.518    0.173    0.518    0.173 necompiler.py:662(evaluate)
#         1    0.004    0.004    1.340    1.340 <string>:1(<module>)
#         1    0.001    0.001    1.336    1.336 test_numexpr.py:27(testNumexpr)
#         3    0.000    0.000    0.000    0.000 necompiler.py:462(getContext)
#         3    0.000    0.000    0.000    0.000 {sorted}
#         6    0.000    0.000    0.000    0.000 {numpy.core.multiarray.array}
#         6    0.000    0.000    0.000    0.000 necompiler.py:611(getType)
#         6    0.000    0.000    0.000    0.000 numeric.py:394(asarray)
#         6    0.000    0.000    0.000    0.000 {sys._getframe}
#         3    0.000    0.000    0.000    0.000 {method 'items' of 'dict' objects}
#         3    0.000    0.000    0.000    0.000 {zip}
#         3    0.000    0.000    0.000    0.000 {method 'get' of 'dict' objects}
#         3    0.000    0.000    0.000    0.000 {isinstance}
#         3    0.000    0.000    0.000    0.000 {method 'copy' of 'dict' objects}
#         6    0.000    0.000    0.000    0.000 {method 'append' of 'list' objects}
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}
#         6    0.000    0.000    0.000    0.000 {method 'pop' of 'dict' objects}
# ```

# <markdowncell>

# - Line profiling function testNumexpr() with IPython %lprun magic function (line_profiler library required):

# <codecell>

%load_ext memory_profiler

# <codecell>

%load_ext line_profiler

# <codecell>

%lprun -f testNumexpr testNumexpr(5000)

# <markdowncell>

# ```
# Timer unit: 1e-06 s
# 
# Total time: 1.33757 s
# File: test_numexpr.py
# Function: testNumexpr at line 27
# 
# Line #      Hits         Time  Per Hit   % Time  Line Contents
# ==============================================================
#     27                                           def testNumexpr(n):
#     28                                               
#     29         1          126    126.0      0.0      print "Testing numpy with numexpr"
#     30         1           53     53.0      0.0      print "Starting computations..."
#     31                                               
#     32                                               
#     33                                               # Creating first array
#     34         1       411007 411007.0     30.7      arr1 = np.random.random((n,n))
#     35                                               # Creating second array
#     36         1       407123 407123.0     30.4      arr2 = np.random.random((n,n))
#     37                                               
#     38                                               # Several computations for testing
#     39         1       333881 333881.0     25.0      a = ne.evaluate("sin(arr1) + arr1**3 + sqrt(arr2)")
#     40                                               
#     41         1        95651  95651.0      7.2      b = ne.evaluate("(arr1**3) * (arr2**3)")
#     42                                               
#     43         1        89678  89678.0      6.7      ne.evaluate("a * b")
#     44                                               
#     45         1           55     55.0      0.0      print "Process completed successfully!\n"```

# <markdowncell>

# - Memory profiling function testNoNumexpr() with IPython %mprun magic function (memory_profiler library required):

# <codecell>

%mprun -f testNumexpr testNumexpr(5000)

# <markdowncell>

# ```
# Filename: test_numexpr.py
# 
# Line #    Mem usage    Increment   Line Contents
# ================================================
#     27     30.4 MiB      0.0 MiB   def testNumexpr(n):
#     28                                 
#     29     30.4 MiB      0.0 MiB       print "Testing numpy with numexpr"
#     30     30.4 MiB      0.0 MiB       print "Starting computations..."
#     31                                 
#     32                                 
#     33                                 # Creating first array
#     34    221.1 MiB    190.7 MiB       arr1 = np.random.random((n,n))
#     35                                 # Creating second array
#     36    411.8 MiB    190.7 MiB       arr2 = np.random.random((n,n))
#     37                                 
#     38                                 # Several computations for testing
#     39    602.6 MiB    190.7 MiB       a = ne.evaluate("sin(arr1) + arr1**3 + sqrt(arr2)")
#     40                                 
#     41    793.3 MiB    190.8 MiB       b = ne.evaluate("(arr1**3) * (arr2**3)")
#     42                                 
#     43    793.2 MiB     -0.1 MiB       ne.evaluate("a * b")
#     44                                 
#     45    793.2 MiB      0.0 MiB       print "Process completed successfully!\n"```

# <markdowncell>

# 
# ###Code profiling: testNoNumexpr() 
# 
# - Profiling function testNoNumexpr() with IPython %prun magic function:

# <codecell>

%prun testNoNumexpr(5000)

# <markdowncell>

# ``` 
#   5 function calls in 9.435 seconds
# 
#    Ordered by: internal time
# 
#    ncalls  tottime  percall  cumtime  percall filename:lineno(function)
#         1    8.613    8.613    9.430    9.430 test_nonumexpr.py:25(testNoNumexpr)
#         2    0.817    0.409    0.817    0.409 {method 'random_sample' of 'mtrand.RandomState' objects}
#         1    0.004    0.004    9.435    9.435 <string>:1(<module>)
#         1    0.000    0.000    0.000    0.000 {method 'disable' of '_lsprof.Profiler' objects}```

# <markdowncell>

# - Line profiling function testNoNumexpr() with IPython %lprun magic function (line_profiler library required):

# <codecell>

%lprun -f testNumexpr testNoNumexpr(5000)

# <markdowncell>

# ```
# Timer unit: 1e-06 s
# 
# Total time: 9.447 s
# File: test_nonumexpr.py
# Function: testNoNumexpr at line 25
# 
# 
# Line #      Hits         Time  Per Hit   % Time  Line Contents
# ==============================================================
#     25                                           def testNoNumexpr(n):
#     26                                               
#     27         1          190    190.0      0.0      print "Testing numpy without numexpr"
#     28         1           56     56.0      0.0      print "Starting computations..."
#     29                                               
#     30                                               # Creating first array
#     31         1       413514 413514.0      4.4      arr1 = np.random.random((n,n))
#     32                                               # Creating second array
#     33         1       407463 407463.0      4.3      arr2 = np.random.random((n,n))
#     34                                               
#     35                                               # Several computations for testing
#     36         1      3521544 3521544.0     37.3      a = np.sin(arr1) + arr1**3 + np.sqrt(arr2)
#     37                                               
#     38         1      4988239 4988239.0     52.8      b = (arr1**3) * (arr2**3)
#     39                                               
#     40         1       115940 115940.0      1.2      a * b
#     41                                               
#     42         1           55     55.0      0.0      print "Process completed successfully!\n"```

# <markdowncell>

# 
# - Memory profiling function testNoNumexpr() with IPython %mprun magic function (memory_profiler library required):

# <codecell>

%mprun -f testNumexpr testNoNumexpr(5000)

# <markdowncell>

# ```
# Filename: test_nonumexpr.py
# 
# Line #    Mem usage    Increment   Line Contents
# ================================================
#     25     30.4 MiB      0.0 MiB   def testNoNumexpr(n):
#     26                                 
#     27     30.4 MiB      0.0 MiB       print "Testing numpy without numexpr"
#     28     30.4 MiB      0.0 MiB       print "Starting computations..."
#     29                                 
#     30                                 # Creating first array
#     31    221.1 MiB    190.7 MiB       arr1 = np.random.random((n,n))
#     32                                 # Creating second array
#     33    411.8 MiB    190.7 MiB       arr2 = np.random.random((n,n))
#     34                                 
#     35                                 # Several computations for testing
#     36    602.6 MiB    190.7 MiB       a = np.sin(arr1) + arr1**3 + np.sqrt(arr2)
#     37                                 
#     38    793.3 MiB    190.7 MiB       b = (arr1**3) * (arr2**3)
#     39                                 
#     40    793.3 MiB      0.0 MiB       a * b
#     41                                 
#     42    793.3 MiB      0.0 MiB       print "Process completed successfully!\n"```

