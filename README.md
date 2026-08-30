# Student Report Management System

## Objective
Built to apply Object-Oriented Programming concepts — encapsulation, 
composition, and separation of responsibilities — to a practical 
problem: turning student grading and reporting logic into a set of 
cooperating classes instead of one script.

## What it does
- Add students and record marks across multiple subjects
- Calculate average, highest, lowest, and total marks
- Assign a grade and pass/fail result based on average marks
- Generate a formatted report and simulate emailing it to the student

## What I focused on / learned
- Splitting responsibilities across classes (`Student`, `Grade`, 
  `Report_printer`, `Email`, `StudentManager`) instead of one large 
  function
- Using composition — `StudentManager` holds instances of the other 
  classes rather than doing everything itself

## Known limitations (next steps)
- No input validation yet — invalid input can crash the program
- No persistent storage — student records are lost when the program 
  closes
- No automated tests yet

## How to run
1. Make sure Python 3 is installed
2. Clone this repo
3. Run:
```
   python main.py
```
