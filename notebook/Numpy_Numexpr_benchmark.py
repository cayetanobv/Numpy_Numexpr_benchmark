# -*- coding: utf-8 -*-
# <nbformat>3.0</nbformat>

# <codecell>

%%timeit -n1
%run Numpy_Numexpr_benchmark/test_numexpr.py

# <codecell>

%%timeit -n1
%run Numpy_Numexpr_benchmark/test_nonumexpr.py

# <codecell>

%prun testNumexpr(5000)

# <codecell>

%load_ext memory_profiler

# <codecell>

%load_ext line_profiler

# <codecell>

%lprun -f testNumexpr testNumexpr(5000)

# <codecell>

%mprun -f testNumexpr testNumexpr(5000)

# <codecell>

%prun testNoNumexpr(5000)

# <codecell>

%lprun -f testNumexpr testNoNumexpr(5000)

# <codecell>

%mprun -f testNumexpr testNoNumexpr(5000)

# <codecell>


