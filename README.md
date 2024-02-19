# Solution for the problem of the ranges

To solve the problem two iterators were used: **_i_** and **_j_** <br>
The _first iterator_ is used to store an index of the minimum value of a current range. <br>
The _second iterator_ is used to store an index of the maximum value of a current range. <br>
We are moving **_j_** to the right on every iteration.
1. If the previous number in the sequence is not lower than the current by one, then this is not the end of the range
2. Else, we end the range with the previous number, and assign **_i_** with the current index.

# Running the code
To run the code, download the `python_solution` file and run it with the following command:<br>
`python python_solution.py`<br>
Enter in one line sequence of integers, press `Enter` and the program will print out the result
