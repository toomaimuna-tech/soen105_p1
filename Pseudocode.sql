Pseudocode:
 START
 INPUT reg_no,name
 INPUT cat1,cat2,exam
 IF any mark<0 or >100 THEN 
  DISPLAY "Invalid mark"
 ELSE
  total=cat*0.15+cat2*0.15+exam*0.7
    IF total>=90 THEN
     grade="A"
    ELSE IF total>=80 THEN
     grade="B"
    ELSE IF total>=70 THEN
     grade="C"
    ELSE IF total>=60 THEN
     grade="D"
    ELSE
     grade="F"
     status="pass" IF total >=40 ELSE
        status="fail"
    SAVE Student in list
    END IF
    END