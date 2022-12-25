"""
# =====================================================================================================
# ======================================== Day 1: Data Types ==========================================
# =====================================================================================================

Task
Complete the code in the editor below. The variables i, d, and s are already declared and initialized for you. You must:

1. Declare 3 variables: one of type int, one of type double, and one of type String.
2. Read 3 lines of input from stdin (according to the sequence given in the Input Format section below) and initialize your 3 variables.
3. Use the + operator to perform the following operations:
    1. Print the sum of  plus your int variable on a new line.
    2. Print the sum of  plus your double variable to a scale of one decimal place on a new line.
    3. Concatenate  with the string you read as input and print the result on a new line.
    
Note: If you are using a language that doesn't support using  for string concatenation (e.g.: C), you can just print one variable immediately following the other on the same line. The string provided in your editor must be printed first, immediately followed by the string you read as input.

Input Format
The first line contains an integer that you must sum with i.
The second line contains a double that you must sum with d.
The third line contains a string that you must concatenate with s.

Output Format
Print the sum of both integers on the first line, the sum of both doubles (scaled to 1 decimal place) on the second line, and then the two concatenated strings on the third line.

Sample Input
12
4.0
is the best place to learn and practice coding!

Sample Output
16
8.0
HackerRank is the best place to learn and practice coding!
"""

# ========================= Solved ===========================
i = 4
d = 4.0
s = 'HackerRank '
# Declare second integer, double, and String variables.
    # Python has no command for declaring a variable.
    # A variable is created the moment you first assign a value to it.
# Read and save an integer, double, and String to your variables.
i_, d_, s_ = int(input()), float(input()), input()
# Print the sum of both integer variables on a new line.
print(i+i_)
# Print the sum of the double variables on a new line.
print(d+d_)
# Concatenate and print the String variables on a new line
print(s+s_)
