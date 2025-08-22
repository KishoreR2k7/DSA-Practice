# Python Basics – Daily Practice

This repository contains my daily Python programming practice.  
Each day’s exercises are organized in separate folders with simple examples.

---

## 📂 Folder Structure & Programs

### **Day 1**

#### 1️⃣ Input Output.py
**Description:**  
- Demonstrates how to take user input as **string, integer, and float**.  
- Prints the entered values back to the user.  

**Example Run:**  
```bash
Enter Input String: Hello
Output: Hello

Enter Input Integer: 10
Output: 10

Enter Input Float: 5.6
Output: 5.6
2️⃣ Type Conversion.py
Description:

Shows type conversion in Python.

Converts input string to integer and float, and displays datatypes.

Example Run:

bash
Copy
Edit
Enter Input: 25
Datatype of a : <class 'str'>

25
Datatype of b : <class 'int'>

Float: 25.0
Datatype of c : <class 'float'>
Day 2
3️⃣ Check Number is Positive, Negative, or Zero (if else).py
Description:

Defines a function checknumber(a) to check whether a number is positive, negative, or zero.

Takes an integer input from the user and prints the result.

Code Flow:

If the number is greater than 0 → prints It is Positive.

If the number is less than 0 → prints It is Negative.

If the number equals 0 → prints It is zero.

Example Run:

bash
Copy
Edit
Enter a number: 15
It is Positive
bash
Copy
Edit
Enter a number: -9
It is Negative
bash
Copy
Edit
Enter a number: 0
It is zero
4️⃣ Find Day.py
Description:

Uses Python’s match-case statement (introduced in Python 3.10) to map a number (1–7) to a weekday.

If the input is outside the range (1–7), it prints Invalid day.

Code Flow:

User enters a number between 1 and 7.

Program prints the corresponding day (Monday → Sunday).

For any other number, prints Invalid day.

Example Run:

bash
Copy
Edit
Enter a number: 3
Wednesday
bash
Copy
Edit
Enter a number: 7
Sunday
bash
Copy
Edit
Enter a number: 10
Invalid day
