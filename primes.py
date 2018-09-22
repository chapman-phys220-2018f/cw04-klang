#!/usr/bin/env python3
# -*- coding: utf-8 -*-

###
# General Notes:
###

###
# Name: Trevor Kling
# Student ID: 002270716
# Email: kling109@mail.chapman.edu
# Course: PHYS220/MATH220/CPSC220 Fall 2018
# Assignment: CW04-klang primes.py
###

import math as math
import sys

"""
This module finds Prime Numbers based on the Eratosthenes Sieve.  The module takes a positive integer "n" and returns all prime integers less than n.
"""

def eratosthenes(n):
    try:
        nums = list(range(2, int(n)+1))
        nonPrimes = []
        for j in range(0, len(nums)):
            for i in range(2, round(math.sqrt(int(j+1))+1)):
                if (nums[j] % (i)) == 0 and (nums[j] / i) != 1:
                    nonPrimes.append(nums[j])
        """List Comprehension found at:  https://stackoverflow.com/questions/4211209/remove-all-the-elements-that-occur-in-one-list-from-another"""
        primes = [p for p in nums if p not in nonPrimes]
        return primes
    except ValueError:
        print("Please input a positive integer.")

"""
The Prime generator finds the next prime number, then returns it.  The function generates a list of prime numbers by starting with a list of numbers, then checking if each one is divisible by any number between 2 and sqrt(n).  If the number is divisible, it is added to a list of non-primes, which are then removed from the list of all numbers to create a list of only primes.  The system also tracks what prime number was produced last, and continues to run each time next() is called until a new prime is found.
"""

def gen_eratosthenes():
    n = 2
    currentPrime = 0;
    genNums = []
    lenNums = 0
    while True:
        genNums.append(n)
        lenNums += 1
        for i in range(2, round(math.sqrt(int(n))+1)):
            if (genNums[-1] % (i)) == 0 and (genNums[-1] / i) != 1:
                del genNums[-1]
                break
        lenNums = len(genNums)
        n += 1
        if (genNums[-1] != currentPrime):
            currentPrime = genNums[-1]
            yield genNums[-1]

def main(argv):
    if len(argv) == 2:
        print(eratosthenes(argv[1]))
    else:
        print("Input an integer argument.")

if __name__ == "__main__":
    main(sys.argv)
