Routine Name: pi

Author: Ethan Allred

Language: Python

pi.py

Description/Purpose: Finds the an approximation of pi

Input: Asks user for number of iterations

Output: The output is an approximate value for pi.

Usage/Example: Use to estimate pi

Implementation/Code: Call with pi.py)

if __name__ == '__main__':
    it = input("How many iterations do you want to run? ")
    while not it.isdigit():
        it = input("Please enter an integer: ")

    pi =0
    count = 1
    for i in range(int(it)):
        if i % 2 == 0: count = count
        else: count = -count

        pi = pi + 1 / count
        count = np.sqrt(count**2) + 2
    pi = pi * 4
    print(pi)
    
Last Modified: December/2022
