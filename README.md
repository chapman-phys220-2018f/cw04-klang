[![Build Status](https://travis-ci.com/chapman-phys220-2018f/cw04-klang.svg?branch=master)](https://travis-ci.com/chapman-phys220-2018f/CHANGEME)

# PHYS220/MATH220/CPSC220 CW 4

**Author(s):** **CHANGEME**

## Specification

Complete the following exercises, saving your solutions in the indicated files. For Python files that include test functions, GitHub will automatically run your tests with ```nosetests3``` on every commit, indicating any failures via the Travis framework in the build status image above.

1. Remember that the [IPython/Jupyter Slides](https://slides.com/profdressel/jupyter-overview) exist as a reference. Also remember that Chapters 2--5 of your textbook should have been read by this point, and will also be a helpful reference. 
1. Have one group member create a new Jupyter notebook ```cw04-primes.ipynb``` and open it within CoCalc using the click-interface. Note that the shortcut keys follow vim conventions, and you can find them referenced in the Help menu. Use the template notebook in the info repository as a guide for how to format your notebook properly as a group. You will use notebooks to present your results for this class in a neat, clear, and professional way. Be sure to switch the default kernel to "Python 3 (Anaconda 5)" using the Kernel menu.
1. Create a new python module ```primes.py```. Be sure to reference the template in the info repository for how to structure a python module. 
1. Inside your primes module create a function ```eratosthenes(n)```. This function will take a positive integer ```n``` and return an ordered collection of all prime numbers smaller than ```n```. (Think carefully about which (basic) python data structure you want to use before you start coding. Recall: Basic data structures are list, dict, set, and tuple. Refer to the slides if you do not remember the basic data structures. You may also want to review the "modulo" operator ```%``` in python.) You should use the "Sieve of Eratosthenes" algorithm for computing these primes, which works as follows: 
      - First generate all positive integers less than ```n```, starting from the number 2. 
      - Remove all multiples of 2 (greater than 2) from the generated integers. 
      - Remove all multiples of the next largest remaining number (greater than that number). That number will be prime by construction.
      - Repeat the previous step until you remove multiples of all primes less than ```sqrt(n)```. (It turns out that stopping at $$\sqrt{n}$$ is sufficient, which saves some calculational steps.) 
      - Return the final set of remaining (prime) numbers less than ```n```. 
1. In your primes module ```primes.py```, create another function ```gen_eratosthenes()``` that creates a generator for all the prime numbers. Rather than generating a fixed number of primes as in the previous implementation, such a generator will produce one new prime per iteration and continue generating primes indefinitely. Modify the above algorithm to make this extension possible. (Your homework HW03 should be helpful for figuring this out.)
1. Ensure that the test functions in ```test_primes.py``` pass when you run ```nosetests3``` in the command line.
1. In your notebook, import the ```primes``` module at the top, and add a new section called "The Sieve of Eratosthenes". In this section, describe what the goal of the algorithm is, and how it works, in your own words. Describe your design decisions. Which data structure(s) did you use and why? Use $\LaTeX$ code as needed to format any math you write in a pretty way within the notebook. Finally, create code cells in the section that demonstrates the correct execution of your code, using the imported module.
1. In your Jupyter notebook, add a new section called "Generating Prime Numbers" that describes and demonstrates your prime number generator. Explain your design decisions, and what is different compared to the previous implementation. Comment on whether your modification makes the original algorithm more efficient or not.
1. In your notebook, add a new section called "Benchmarking Implementations". In this section, use the ```%time``` and ```%timeit``` magic commands to compare the efficiency of your implementations for obtaining large numbers of primes (try ```n``` of 1,000,000). Which implementation is faster? By how much? Does it match your prediction about efficiency above? Speculate about what is being slow about the slower implementation. When writing your notebook, be sure to present your analysis clearly so that others can read and understand it - we will be exchanging work between groups next week for evaluation.
1. After your notebook is complete, spell-checked, and formatted properly, add and commit it to GitHub. (Note that managing conflicts with Jupyter notebooks can be a pain, so I recommend having one person from your group be the official notebook editor, and having others in your group write code for the python modules. This is called delegating tasks within your team.)

## Assessment

Analyze in this section what you found useful about this assignment in your own words. Include any lingering questions or comments that you may have. You can use the GitHub web interface to edit this file directly for now.

**CHANGEME**

## Honor Pledge

I pledge that all the work in this repository is my own with only the following exceptions:

* Content of starter files supplied by the instructor;
* Code borrowed from another source, documented with correct attribution in the code and summarized here.

Signed,

**YOURNAMES**
