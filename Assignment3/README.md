# Assignment 3

- Username: ttbrowne
- Commit hash used for grading: 2766d99f68fd90ad7cb78711a0a1b7b543614ffb

Grader :Grayson Clark

| Criterion           | Total Points |
| ------------------- | ------------ |
| Code Tests            | 50         |
| Code Review   | 50         |



## Total Score: 86/100
Please double-check that your Canvas score reflects what is shown here. 


## Code Tests (36/50 pts)
Here you can find information about the Unittest results and the failed test cases. See the Unittest section for more information. 

- Problem 1:
    - `N`: 2/2
    - `N_t`: 1/1
    - `W`: 1/1
    - `L`: 1/1
    - TA Comments: TA did not add any comments.

- Problem 2:
    - `q`: 4/5
    - TA Comments: Should have used >=

- Problem 3:
    - `amt`:5/5
    - TA Comments: TA did not add any comments.

- Problem 4:
    - `f`: 5/5
    - TA Comments: TA did not add any comments.


- Problem 5:
    - `arithmeticmean`: 0/1
    - `geomean`: 2/2
    - `harmean`: 2/2
    -`rmsmean`: 2/2
    - TA Comments: rounding not necessary, make sure to only round when pdf tells you to


- Problem 6:
    - `F`: 1/1 
    - `V`: 0/1
    - `C`: 2/3
    - TA Comments: V: didn't need if statement, could have just returned the equation
    C: V was wrong, so C failed. Gave points back on this because it is correct


- Problem 7:
    - `Mortgage`: 2/2
    - `totalpaid`: 0/3
    - TA Comments: totalpaid: didn't use variables from house list.


- Problem 8:
    - `geo`: 0/5
    - `twomin`: 1/1
    - `mm`: 2/2
    - `w`: 1/1
    - `dis`: 0/1
    - `trip`: 0/2
    - TA Comments: geo: seems like you didn't understand the problem. Feel free to attend office hours if you're confused.
    mm: we had a mistake in our test cases for mm, so you get full points on this regardless!

## Code Review & style (50/50 pts)

Here we look at your code to check for proper style and legibility.
1. Your code has to meet the requirements described in the homework pdf file.
2. It has to a proper python code.
3. Your logic has to correct.
4. You may pass our test cases but loose points in this section.
5. You may also fail test cases but get points in this section if your code is reasonable at some degree.

- Problem 1:
    - `N`: 2/2
    - `N_t`: 1/1
    - `W`: 1/1
    - `L`: 1/1
    - TA Comments: TA did not add any comments.

- Problem 2:
    - `q`: 5/5
    - TA Comments: TA did not add any comments.

- Problem 3:
    - `amt`: 5/5
    - TA Comments: TA did not add any comments.

- Problem 4:
    - `f`: 5/5
    - TA Comments: TA did not add any comments.


- Problem 5:
    - `arithmeticmean`: 1/1
    - `geomean`: 2/2
    - `harmean`: 2/2
    -`rmsmean`: 2/2
    - TA Comments: TA did not add any comments.


- Problem 6:
    - `F`:1/1 
    - `V`:1/1
    - `C`: 3/3
    - TA Comments: TA did not add any comments.


- Problem 7:
    - `Mortgage`:2/2
    - `totalpaid`: 3/3
    - TA Comments: TA did not add any comments.


- Problem 8:
    - `geo`:5/5
    - `twomin`:1/1
    - `mm`: 2/2
    - `w`: 1/1
    - `dis`: 1/1
    - `trip`: 2/2
    - TA Comments: TA did not add any comments.


## Unittest Results
  -------------------------------------
 test_C_3_one failed.
 Traceback (most recent call last):
   File "C:\Users\smish\Documents\FALL-2022\FALL-2022\Gradingdata\Assignment3\ttbrowne\a3_hidden_tests.py", line 184, in test_C_3_one
     self.assertEqual(a3.C(x),result)
 AssertionError: 10000 != -8106382.700900001
 ======================================
 -------------------------------------
 test_V_1_one failed.
 Traceback (most recent call last):
   File "C:\Users\smish\Documents\FALL-2022\FALL-2022\Gradingdata\Assignment3\ttbrowne\a3_hidden_tests.py", line 178, in test_V_1_one
     self.assertAlmostEqual(a3.V(x),result,2)
 AssertionError: 0 != 240567.7056 within 2 places (240567.7056 difference)
 ======================================
 -------------------------------------
 test_arithemticmean_1_one failed.
 Traceback (most recent call last):
   File "C:\Users\smish\Documents\FALL-2022\FALL-2022\Gradingdata\Assignment3\ttbrowne\a3_hidden_tests.py", line 128, in test_arithemticmean_1_one
     self.assertAlmostEqual(a3.arithmetic_mean(lst),sum(lst)/len(lst),2)
 AssertionError: -10.62 != -10.625 within 2 places (0.005000000000000782 difference)
 ======================================
 -------------------------------------
 test_dis_1_one failed.
 Traceback (most recent call last):
   File "C:\Users\smish\Documents\FALL-2022\FALL-2022\Gradingdata\Assignment3\ttbrowne\a3_hidden_tests.py", line 281, in test_dis_1_one
     self.assertAlmostEqual(a3.dis(lst1,lst2),result,2)
 AssertionError: 39.97499218261337 != 41.21 within 2 places (1.2350078173866308 difference)
 ======================================
 -------------------------------------
 test_geo_2_one failed.
 Traceback (most recent call last):
   File "C:\Users\smish\Documents\FALL-2022\FALL-2022\Gradingdata\Assignment3\ttbrowne\a3_hidden_tests.py", line 240, in test_geo_2_one
     self.assertEqual(a3.geo(input[i][0],input[i][1]),output[i])
   File "C:\Users\smish\Documents\FALL-2022\FALL-2022\Gradingdata\Assignment3\ttbrowne\a3.py", line 184, in geo
     f = lst(len(lst)- 1)
 TypeError: 'list' object is not callable
 ======================================
 -------------------------------------
 test_geo_3_two failed.
 Traceback (most recent call last):
   File "C:\Users\smish\Documents\FALL-2022\FALL-2022\Gradingdata\Assignment3\ttbrowne\a3_hidden_tests.py", line 249, in test_geo_3_two
     self.assertEqual(a3.geo(i,j),result)
   File "C:\Users\smish\Documents\FALL-2022\FALL-2022\Gradingdata\Assignment3\ttbrowne\a3.py", line 184, in geo
     f = lst(len(lst)- 1)
 TypeError: 'list' object is not callable
 ======================================
 -------------------------------------
 test_mm_2_one failed.
 Traceback (most recent call last):
   File "C:\Users\smish\Documents\FALL-2022\FALL-2022\Gradingdata\Assignment3\ttbrowne\a3_hidden_tests.py", line 261, in test_mm_2_one
     self.assertEqual(a3.mm(lst),a3_sol.mm(lst))
 AssertionError: Lists differ: [8, 2] != [8, 1]
 
 First differing element 1:
 2
 1
 
 - [8, 2]
 ?     ^
 
 + [8, 1]
 ?     ^
 
 ======================================
 -------------------------------------
 test_mo_1_one failed.
 Traceback (most recent call last):
   File "C:\Users\smish\Documents\FALL-2022\FALL-2022\Gradingdata\Assignment3\ttbrowne\a3_hidden_tests.py", line 266, in test_mo_1_one
     self.assertEqual(a3.mo(lst),a3_sol.mo(lst))
 AssertionError: False != True
 ======================================
 -------------------------------------
 test_q_1_three failed.
 Traceback (most recent call last):
   File "C:\Users\smish\Documents\FALL-2022\FALL-2022\Gradingdata\Assignment3\ttbrowne\a3_hidden_tests.py", line 72, in test_q_1_three
     self.assertEqual(a3.q([4, 4, 1]),True)
 AssertionError: False != True
 ======================================
 -------------------------------------
 test_totalpaid_3_one failed.
 Traceback (most recent call last):
   File "C:\Users\smish\Documents\FALL-2022\FALL-2022\Gradingdata\Assignment3\ttbrowne\a3_hidden_tests.py", line 221, in test_totalpaid_3_one
     self.assertAlmostEqual(a3.total_paid(input[i]),result[i],2)
 AssertionError: -84162.0 != 115838.0 within 2 places (200000.0 difference)
 ======================================
 -------------------------------------
 test_trip_2_one failed.
 Traceback (most recent call last):
   File "C:\Users\smish\Documents\FALL-2022\FALL-2022\Gradingdata\Assignment3\ttbrowne\a3_hidden_tests.py", line 299, in test_trip_2_one
     self.assertAlmostEqual(a3.trip(input[i]),output[i],2)
   File "C:\Users\smish\Documents\FALL-2022\FALL-2022\Gradingdata\Assignment3\ttbrowne\a3.py", line 267, in trip
     distance += dis(lst[count], lst[count+1])
 IndexError: list index out of range
 ======================================
