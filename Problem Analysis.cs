Problem Analysis
  Lecturers currently record examination marks,
  compute weighed totals and assign grades manually
   which is time consuming and prone to human errors.

Inputs:
  Student Registration Number(string)
  Student Full Name(string)
  CAT1 Marks (Float/Interger,range 0-100)
  CAT 2 Marks (Float/Interger,range 0-100)
  End-Of-Semester Exam Marks
   (Float/Interger,range 0-100)
  Menu selection Choices and Search queries

Processing:
  Validate that all entered mrks fal strictly
   between 0-100
  Calculate the final score using weighed components
   Total marks=(CAT1*0.15)+(CAT2*0.15)+(Exam*0.70)
  Map the final score to a leter grade 
   (A:70-100,B:60-69,C:50-59,D:40-49,E:Below 40)
  Classify status as Pass(>=40) or Fail(<40)
  Perform a linear search across stored records
   using registration number.
  Compute class statistics such as highest score,
   lowest score, average score, and grade distribution.

Outputs:
  Display the final score, letter grade, 
   and pass/fail status for each student.
  Display search results based on registration
   number queries.
  Display class statistics including highest score,
   lowest score, average score, and grade distribution.
  