#!/usr/bin/env python3

import unittest
import numpy as np
import functions as F
import numpy.testing as npt

import newton

class TestNewton(unittest.TestCase):
    # passed after fixing bugs in newton.py and functions.py     
    def testLinear(self):
        # Just so you see it at least once, this is the lambda keyword
        # in Python, which allows you to create anonymous functions
        # "on the fly". As I commented in testFunctions.py, you can
        # define regular functions inside other
        # functions/methods. lambda expressions are just syntactic
        # sugar for that.  In other words, the line below is
        # *completely equivalent* under the hood to:
        #
        # def f(x):
        #     return 3.0*x + 6.0
        #
        # No difference.
        f = lambda x : 3.0*x + 6.0

        # Setting maxiter to 2 b/c we're guessing the actual root
        solver = newton.Newton(f, tol=1.e-15, maxiter=2)
        x = solver.solve(2.0)
        # Equality should be exact if we supply *the* root, ergo
        # assertEqual rather than assertAlmostEqual
        self.assertEqual(x, -2.0)
        
    def testQuard1(self):
        f = lambda x : x**2 - 7*x + 10
        solver = newton.Newton(f, tol=1.e-15, maxiter=10)
        x = solver.solve(100)
#        y = solver.solve(4)
#        print(x)
#        print(y)
#        self.assertAlmostEqual(x, 2.0)
#        self.assertAlmostEqual(y, 5.0)
        self.assertTrue((np.isclose(x, 2.0)) or (np.isclose(x, 5.0)))
        
    def testCubic1(self):
        f = F.Polynomial([-15, 23, -9, 1])
#        g = lambda x : 1*(x**2) + 1*(x**2) + 5
#        self.assertTrue(f == g)
        solver = newton.Newton(f, tol=1.e-15, maxiter=20)
        x = solver.solve(100)
#        print(x)
        y = solver.solve(2.108)   # interesting!
#        print(y)
        z = solver.solve(-1)
#        print(z)
        self.assertAlmostEqual(x, 5.0)
        self.assertAlmostEqual(y, 3.0)
        self.assertAlmostEqual(z, 1.0)
       
    def testExp(self):
        f = lambda x : np.exp(x) - 1
        solver = newton.Newton(f, tol=1.e-15, maxiter=20)
        x = solver.solve(5)
        self.assertAlmostEqual(x, 0)
        
    def test2Dfunc(self):
        A = np.matrix("1.0 2.0; 3.0 4.0")
        B = np.matrix("2.0; 3.0")
        def f(x):
            return A * x - B
        x0 = np.matrix("5.0; 6.0")
        solver = newton.Newton(f, tol=1.e-15, maxiter=20)
        x = solver.solve(x0)
        self.assertEqual(x.shape, (2,1))
        xreal = np.matrix("-1.0; 1.5")
        for i in range(x.size):
            self.assertTrue(np.asscalar(x[i]))
            self.assertTrue(np.asscalar(xreal[i]))
        npt.assert_array_almost_equal(x, xreal)
            

if __name__ == "__main__":
    unittest.main()

    
