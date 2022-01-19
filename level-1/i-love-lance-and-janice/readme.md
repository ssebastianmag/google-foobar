## I Love Lance & Janice

You've caught two of your fellow minions passing coded notes back and forth
-- while they're on duty, no less! Worse, you're pretty sure it's not job-related
-- they're both huge fans of the space soap opera ""Lance & Janice"".
You know how much Commander Lambda hates waste, so if you can prove that these
minions are wasting time passing non-job-related notes,
it'll put you that much closer to a promotion.

Fortunately for you, the minions aren't exactly advanced cryptographers.
In their code, every lowercase letter [a..z] is replaced with the
corresponding one in [z..a], while every other character (including
uppercase letters and punctuation) is left untouched.  That is, 'a'
becomes 'z', 'b' becomes 'y', 'c' becomes 'x', etc.  For instance, 
the word ""vmxibkgrlm"", when decoded, would become ""encryption"".

Write a function called solution(s) which takes in a string and returns
the deciphered string so you can show the commander proof that these
minions are talking about ""Lance & Janice"" instead of doing their jobs.

### Languages

To provide a Python solution, edit solution.py

To provide a Java solution, edit Solution.java

### Test cases

Your code should pass the following test cases.
Note that it may also be run against hidden test cases not shown here.

#### -- Python cases --
#### Test case 1
Input:
```
solution.solution("wrw blf hvv ozhg mrtsg'h vkrhlwv?")
```
Output:
```
did you see last night's episode?
```

#### Test case 2
Input:
```
solution.solution("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!")
```
Output:
```    
Yeah! I can't believe Lance lost his job at the colony!!
```

#### -- Java cases --
#### Test case 1
Input:
```
Solution.solution("Yvzs! I xzm'g yvorvev Lzmxv olhg srh qly zg gsv xlolmb!!")
```
Output:
```
Yeah! I can't believe Lance lost his job at the colony!!
```

#### Test case 2
Input:
```
Solution.solution("wrw blf hvv ozhg mrtsg'h vkrhlwv?")
```
Output:
```
did you see last night's episode?
```

Use verify [file] to test your solution and see how it does.
When you are finished editing your code, use submit [file] to submit
your answer. 

If your solution passes the test cases, it will be
removed from your home folder.