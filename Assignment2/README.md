# Assignment 2

- Username: ttbrowne
- Commit hash used for grading: 1403ba9e32b616c981498d716f9f6eb125bb1512

Rubric (see Canvas page):Chhavi Thakur

| Criterion           | Total Points |
| ------------------- | ------------ |
| Code Tests            | 50         |
| Code Review   | 50         |



## Total Score:94.5/100
Please double-check that your Canvas score reflects what is shown here. 


## Code Tests (47.0/50 pts)
Here you can find information about the Unittest results and the failed test cases. See the Unittest section for more information. 

- Problem 1:
    - `g`: 5.0/5
    - TA Comments: good.

- Problem 2:
    - `f`: 5.0/5
    - TA Comments: good.

- Problem 3:
    - `h_0`: 1.0/1
    - `h_1`: 1.0/1
    - `h`: 3.0/3
    - TA Comments: good.

- Problem 4:
    - `q`: 5.0/5
    - TA Comments: good.


- Problem 5:
    - `eq`: 5.0/5
    - TA Comments: good.


- Problem 6:
    - `path`: 2.0/5
    - TA Comments: try again


- Problem 7:
    - `max2d`: 3.0/3
    - `max3d`: 5.0/5
    - TA Comments: good

- Problem 8:
    - `Rectangle`: 5.0/5
    - `box`: 2.0/2
    - `rR`: 5.0/5
    - TA Comments: good



## Code Review & style (47.5/50 pts)

Here we look at your code to check for proper style and legibility.
1. Your code has to meet the requirements described in the homework pdf file.
2. It has to a proper python code.
3. Your logic has to correct.
4. You may pass our test cases but loose points in this section.
5. You may also fail test cases but get points in this section if your code is reasonable at some degree.

 Problem 1:
    - `g`: 5/5
    - TA Comments:good

- Problem 2:
    - `f`: 5/5
    - TA Comments: good

- Problem 3:
    - `h_0`: 1/1
    - `h_1`: 1/1
    - `h`: 3/3
    - TA Comments: good

- Problem 4:
    - `q`: 5/5
    - TA Comments: good.


- Problem 5:
    - `eq`: 5/5
    - TA Comments: good.


- Problem 6:
    - `path`: 2.5/5
    - TA Comments: Try:
    def path(lst):
    s0,s1,s2,s3,s4 = lst
    return bool(s0*(s2 + s1*(s3 + s4)))


- Problem 7:
    - `max2d`: 3/3
    - `max3d`: 5/5
    - TA Comments: good

- Problem 8:
    - `Rectangle`: 5/5
    - `box`: 2/2
    - `rR`: 5/5
    - TA Comments: good



## Unittest Results
-------------------------------------

test_path_1_one failed.



Traceback (most recent call last):

  File "C:\Users\smish\Spring-2022\Gradingdata\Assignment2\ttbrowne\a2_hidden_test.py", line 150, in test_path_1_one

    self.assertEqual(a2.path([1,0,0,1,0]), False)

AssertionError: None != False



======================================



-------------------------------------

test_path_2_three failed.



Traceback (most recent call last):

  File "C:\Users\smish\Spring-2022\Gradingdata\Assignment2\ttbrowne\a2_hidden_test.py", line 163, in test_path_2_three

    self.assertEqual(a2.path(switch_i), result)

AssertionError: None != False



======================================



40.0

24.0

12.0

25.0

12.5

Code tests: 47.0/50.0

g: 5/5

f: 5/5

h0: 1/1

h1: 1/1

h: 3/3

q: 5/5

eq: 5/5

path: 2/5

max2d: 3/3

max3d: 5/5

rectangle: 5/5

box: 2/2

rR: 5/5

