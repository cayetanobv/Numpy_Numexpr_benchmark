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

# <codecell>

%prun testNumexpr(5000)

# <markdowncell>

# 
#    65 function calls in 1.340 seconds

# <markdowncell>

# - Line profiling function testNumexpr() with IPython %lprun magic function (line_profiler library required):

# <codecell>

%load_ext memory_profiler

# <codecell>

%load_ext line_profiler

# <codecell>

%lprun -f testNumexpr testNumexpr(5000)

# <rawcell>

# 
# Timer unit: 1e-06 s
# 
# Total time: 1.33757 s
# File: test_numexpr.py
# Function: testNumexpr at line 27

# <markdowncell>

# - Memory profiling function testNoNumexpr() with IPython %mprun magic function (memory_profiler library required):

# <codecell>

%mprun -f testNumexpr testNumexpr(5000)

# <markdowncell>

# 
# ###Code profiling: testNoNumexpr() 
# 
# - Profiling function testNoNumexpr() with IPython %prun magic function:

# <codecell>

%prun testNoNumexpr(5000)

# <rawcell>

#  
#   5 function calls in 9.435 seconds

# <markdowncell>

# - Line profiling function testNoNumexpr() with IPython %lprun magic function (line_profiler library required):

# <codecell>

%lprun -f testNumexpr testNoNumexpr(5000)

# <rawcell>

# 
# Timer unit: 1e-06 s
# 
# Total time: 9.447 s
# File: test_nonumexpr.py
# Function: testNoNumexpr at line 25

# <markdowncell>

# 
# - Memory profiling function testNoNumexpr() with IPython %mprun magic function (memory_profiler library required):

# <codecell>

%mprun -f testNumexpr testNoNumexpr(5000)

