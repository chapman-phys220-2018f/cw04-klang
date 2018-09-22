#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import primes

"""primes.py Test Module

Verifies that the implementations for prime number generators are correct.

Here are the primes less than n=200 for completeness:
 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 
 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 
 101, 103, 107, 109, 113, 127, 131, 137, 139, 149, 
 151, 157, 163, 167, 173, 179, 181, 191, 193, 197, 199
"""

def test_eratosthenes_last():
    """Verify the largest prime number under 200.
    
    Note: The equality test for the assert here only works because the
    integers inside the list support exact equality. 
    
    Question: What data structures work with this sort of test?
    """
    assert primes.eratosthenes(200)[-1] == 199

def test_eratosthenes_number():
    """Verify the number of primes less than 200.
    """
    assert len(primes.eratosthenes(200)) == 46
    
def test_gen_eratosthenes_last():
    """Verify the largest prime number under 200.
    """
    g = primes.gen_eratosthenes()
    p = next(g)
    p2 = next(g)
    while p2 < 200:
        p, p2 = p2, next(g)
    assert p == 199

def test_gen_eratosthenes_number():
    """Verify the number of primes less than 200.
    """
    g = primes.gen_eratosthenes()
    ps = [next(g)]
    while ps[-1] < 200:
        ps.append(next(g))
    assert len(ps[:-1]) == 46

    
