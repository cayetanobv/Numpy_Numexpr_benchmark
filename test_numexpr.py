# -*- coding: utf-8 -*-
#
#  Author: Cayetano Benavent, 2015.
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
# 



import numpy as np
import numexpr as ne


def testNumexpr(n):
    
    print "Testing numpy with numexpr"
    print "Starting computations..."
    
    
    # Creating first array
    arr1 = np.random.random((n,n))
    # Creating second array
    arr2 = np.random.random((n,n))
    
    # Several computations for testing
    a = ne.evaluate("sin(arr1) + arr1**3 + sqrt(arr2)")
    
    b = ne.evaluate("(arr1**3) * (arr2**3)")
    
    ne.evaluate("a * b")
    
    print "Process completed successfully!\n"


def main():
    # ndarray shape is (n, n) 
    # Default array size is 25*10^6
    n = 5000
    
    testNumexpr(n)

if __name__ == '__main__':
  main()

