import random

question_limit = 15
question_count = 0
categoryOfQuestions = input(
    "Choose the category of questions:\n"
    "1) Addition and Subtraction of integer numbers\n"
    "2) Multiply and Division of integer numbers\n"
    "3) Expressions\n"
    "4) Powers and Roots\n"
    "5) Fractions\n"
    "6) Equations with one Variable\n"
    "7) Trigonometry \n"
    "8) Logarythms \n"
    "9) Mix questions \n"
)

def ask_question(question, correct_answer):
    user_answer = input(question).strip().lower()
    if user_answer == correct_answer:
        return True
    else:
        print(f"Incorrect. Correct answer is {correct_answer}")
        return False
if categoryOfQuestions == "1":
 questions = {
    1: ("What is 2+5? ", "7"),
    2: ("What is 1+1+2-5+1? ", "0"),
    3: ("What is 17+33? ", "50"),
    4: ("What is 41 - 19? ", "22"),
    5: ("What is 13+45? ", "58"),
    6: ("What is -25+25? ", "0"),
    7: ("What is 4+7-8+2? ", "5"),
    8: ("What is 125-75+40? ", "90"),
    9: ("What is 24+75-63? ", "36"),
    10: ("What is 72+57? ", "129"),
    11: ("What is 17-9? ", "8"),
    12: ("What is 1-1-3+2-7? ", "-8"),
    13: ("What is 23-13? ", "10"),
    14: ("What is 47+47? ", "94"),
    15: ("What is 56+44+100-300? ", "-100"),
    16: ("What is 7-1? ", "6"),
    17: ("What is 17+81? ", "98"),
    18: ("What is 25-23+(-3)? ", "-1"),
    19: ("What is (-5) + (-3)? ", "-8"),
    20: ("What is -100-(-72)-25? ", "-53"),
    21: ('What is 27+91-(-30) ', '148'),
    22: ('What is 3+18-1+80 ', '100'),
    23: ('What is 45-17+52 ', '80'),
    24: ('What is -25+26 ', '1'),
    25: ('What is 97-94+27 ', '30'),
    26: ('What is 16-8 ', '8'),
    27: ('What is 2a+a-13a ', '-10a'),
    28: ('What is 3c-4c+c ' , '0'),
    29: ('What is 72x+28x-21 ' , '100x-21'),
    30: ('What is 0+5b-17+12b ' , '17b-17'),
}
 score = 0

 while question_count < question_limit:
    question_count += 1
    random_question = random.randint(1,30)
    print(f"Question {question_count}: {questions[random_question][0]}")
    if ask_question(questions[random_question][0], questions[random_question] [1]):
        score += 1

 print(f"You got {score}/{question_limit} questions correct.")

elif categoryOfQuestions == "2":
 questions2 = {
    1: ("What is 3*5? ", "15"),
    2: ("What is 7*7? ", "49"),
    3: ("What is 72/8? ", "9"),
    4: ("What is 4*8? ", "32"),
    5: ("What is 77/11? ", "7"),
    6: ("What is 108/36? ", "3"),
    7: ("What is 12*11? ", "121"),
    8: ("What is 2*2*2*2*2/2? ", "16"),
    9: ("What is 24*5? ", "120"),
    10: ("What is 640/8? ", "80"),
    11: ("What is 60*20? ", "1200"),
    12: ("What is 13*13? ", "169"),
    13: ("What is -5*7? ", "-35"),
    14: ("What is -65/-13? ", "5"),
    15: ("What is 35*124*629*0? ", "0"),
    16: ("What is 60/-12? ", "-5"),
    17: ("What is 17*4? ", "68"),
    18: ("What is 24/6? ", "4"),
    19: ("What is 63/9? ", "7"),
    20: ("What is 27/9*12/6*15/30*100? ", "300"),
    21: ("What is 14*3/7? ", "6"),
    22: ("What is 35/5? ", "7"),
    23: ("What is 6*6*6? ", "216"),
    24: ("What is 10*100? ", '1000'),
    25: ("What is -39/-13 ", "3"),
    26: ("What is 144/-9? ", "-16"),
    27: ("What is 3a*2b? ", "6ab"),
    28: ("What is 24z*(-3j)? ", "-72jz"),
    29: ("What is 3a/a*21? ", "63"),
    30: ("What is -4x/2x*(-8x)*2 ", "32x"),
 }

 score = 0

 while question_count < question_limit:
    question_count += 1
    random_question = random.randint(1, 30)
    print(f"Question {question_count}: {questions2[random_question][0]}")
    if ask_question(questions2[random_question][0], questions2[random_question] [1]):
        score += 1

 print(f"You got {score}/{question_limit} questions correct.")
  
elif categoryOfQuestions == "3":
 questions3 = {
    1: ("What is 1-5*4? ", "-19"),
    2: ("What is (4+10)/2+37? ", "44"),
    3: ("What is 36/12+32/8? ", "7"),
    4: ("What is (72+28)/4*3-150? ", "-75"),
    5: ("What is 26/13*4+(24*5)? ", "128"),
    6: ("What is 3(45+32)? ", "231"),
    7: ("What is (5-2a)*3? ", "15-6a"),
    8: ("What is 123/3+32? ", "73"),
    9: ("What is -35(x+2)+35(x-2)? ", "0"),
    10: ("What is (2048/8-56)/100? ", "2"),
    11: ("What is 2a+4c(3+4b)? ", "2a+16bc+12c"),
    12: ("What is (103-3)/25*18? ", "72"),
    13: ("What is -5*7+27? ", "-8"),
    14: ("What is 2*2-2/2+2 ", "5"),
    15: ("What is 35/7+16(x-5)? ", "16x-75"),
    16: ("What is 60/-12+5? ", "0"),
    17: ("What is a-a+3bc? ", "3bc"),
    18: ("What is 12/4+(45-20)? ", "28"),
    19: ("What is 63/9+23? ", "30"),
    20: ("What is (1+2-3)*1000000? ", "0"),
    21: ("What is (67*2)-44 ", "90"),
    22: ("What is 35/5-23? ", "-16"),
    23: ("What is 6b-2(3b+4c)? ", "-8c"),
    24: ("What is (1000/25)*40? ", '1600'),
    25: ("What is -39/13+44 ", "41"),
    26: ("What is 4ab*31c? ", "124abc"),
    27: ("What is (3a*2b)+28ab? ", "34ab"),
    28: ("What is 24z*(-3j)? ", "-72jz"),
    29: ("What is 3a/a*21? ", "63"),
    30: ("What is -4x/2x*(-8x)*2 ", "32x"),
 }

 score = 0

 while question_count < question_limit:
    question_count += 1
    random_question = random.randint(1, 30)
    print(f"Question {question_count}: {questions3[random_question][0]}")
    if ask_question(questions3[random_question][0], questions3[random_question] [1]):
        score += 1

 print(f"You got {score}/{question_limit} questions correct.")

elif categoryOfQuestions == "4":
 questions4 = {
    1: ("What is (2^3)^0? ", "1"),
    2: ("What is √2*√8? ", "4"),
    3: ("What is 5^4? ", "625"),
    4: ("What is ∛(27/729)? ", "1/3"),
    5: ("What is 4* √324 /9? ", "8"),
    6: ("What is 4^5*4^3/4^5 ", "64"),
    7: ("What is (∜a)^4? ", "a"),
    8: ("What is -3^5-13? ", '-256'),
    9: ("What is (5-x)^2? ", "25-10x+x^2"),
    10: ("What is √60*√15? ", "30"),
    11: ("What is 2^4*4^3/16^2 ", "4"),
    12: ("What is ∛27 - √169 + fiveroot 243 ", "-7"),
    13: ("Remove the number from under the root sign √48 ", "4√3"),
    14: ("Remove the number from under the root sign √72 ", "3√8"),
    15: ("Remove the number from under the root sign √108 ", "6√3"),
    16: ("What is 2^3-6+3^5? ", "245"),
    17: ("What is √45 + √125? ", "8√5"),
    18: ("What is -8^2 * ∛27? ", "192"),
    19: ("What is √(32+49)? ", "9"),
    20: ("What is √(125/25)? ", "√5"),
    21: ("Remove the number from under the root sign ∛72", "2∛9"),
    22: ("What is (√7)^2? ", "7"),
    23: ("What is (a-1)^2-(a+2)^2 if a = -2? ", "9"),
    24: ("What is 36t^2-49u^2 ", '(6t-7u)(6t+7u)'),
    25: ("What is 8x^3-1 ", "(2x-1)(4x^2+2x+1)"),
    26: ("What is (3x-5y)^2? ", "9x^2-30xy+25y^2"),
    27: ("What is 100000^0? ", "1"),
    28: ("What is 25a^2-9c^2 ", "(5a-3c)(5a+3c)"),
    29: ("What is 1^10000000? ", "1"),
    30: ('Remove the number from under the root sign √128', '8√2'),
 }

 score = 0

 while question_count < question_limit:
    question_count += 1
    random_question = random.randint(1, 30)
    print(f"Question {question_count}: {questions4[random_question][0]}")
    if ask_question(questions4[random_question][0], questions4[random_question] [1]):
        score += 1

 print(f"You got {score}/{question_limit} questions correct.")
  
elif categoryOfQuestions == "5":
 questions5 = {
    1: ("What is 1/2 + 3/4 and if it possible, reduce? ", "5/4"),
    2: ("Reduce the fraction: 49/343 ", "1/7"),
    3: ("What is 23/45 * 90/92 and if it possible, reduce", "1/2"),
    4: ("What is (0,5+0,7)^2 ", "1.44"),
    5: ("What is √(64/81) ", "8/9"),
    6: ("Reduce the fraction 8m/32m^2? ", "1/4m"),
    7: ("Compare this two fractions -0,4 and 0.01 ", "<"),
    8: ("What is 1.2/2 *100 * 1/2 ? ", "30"),
    9: ("What is: 10a^2/(a-1) / 5a/(a-1) if a = 18 ? ", "36"),
    10: ("What is: (x^3 - y^3) / (x-y) if x = 2, y = 3? ", "19"),
    11: ("What is (0,17 - 0.07)*20*0,25? ", "0.5 "),
    12: ("What is (3/5)^3 ", "27/125"),
    13: ("Reduce the fraction 56/128? ", "7/16"),
    14: ("Is this fraction correct 5/(x-2) x =2 ", "no"),
    15: ("What is 2,5+4,5 - 5*1,4? ", "0"),
    16: ("What is √2,56 ", "1.6"),
    17: ("What is 100000000/50000000-4^1/2? ", "0"),
    18: ("What is 3/4 - 5/7? ", "1/28"),
    19: ("What is 3/4 * 8/15? ", "2/5"),
    20: ("What is (-9.2 + 7)/2 ", "-1.1"),
    21: ("What is 6/7 + 8/9? ", "110/63"),
    22: ("What is √49*26/35? ", "26/5"),
    23: ("What is (2/5 - 3/4)^2 ? ", "49/400"),
    24: ("What is (1.5 *2 - 5.4) * -30? ", '72'),
    25: ("What is (11/12)^2 ", "121/144"),
    26: ("What is 3/7 * 1/6? ", "3.5"),
    27: ("What is 24*0,3 ? ", "7.2"),
    28: ("What is 1/2+2/3? ", "5/6"),
    29: ("What is 2/3 / 5/6? ", "4/5"),
    30: ("Reduce the fraction 1024m^3 / 4096m^5  ", "1/4m^2"),
 }

 score = 0

 while question_count < question_limit:
    question_count += 1
    random_question = random.randint(1, 30)
    print(f"Question {question_count}: {questions5[random_question][0]}")
    if ask_question(questions5[random_question][0], questions5[random_question] [1]):
        score += 1

 print(f"You got {score}/{question_limit} questions correct.")
elif categoryOfQuestions == "6":
 questions6 = {
    1: ("Solve the equation: x-4 = 46? ", "50"),
    2: ("Solve the equation: x^2-1 = 0 ", "1 and -1"),
    3: ("Solve the equation: 2x-8 = 7-3x ", "3"),
    4: ("Solve the equation: 3^x = 27 ", "3"),
    5: ("Solve the equation: √x = 5 ", "25"),
    6: ("Solve the equation: 2x^2-5x+2=0 ", "2 and 0.5"),
    7: ("Solve the equation: 4x+2 = x^2+5x ", "-2 and 1 "),
    8: ("Solve the equation: x^2-3x = 0 ", "0 and 3"),
    9: ("Solve the equation: 7x-21 = 0 ", "3"),
    10: ("Solve the equation: 2x/5 + 1/4 = 4 ", "75/8"),
    11: ("Solve the equation: (x-1)(x+1)=5 ", "√6 and -√6"),
    12: ("Does this equation have a root? √x = -32 ", "No"),
    13: ("Solve the equation: 3/x-2/5 = 1/10x ", "15"),
    14: ("Solve the equation: 26-7x = 103 " , "-11"),
    15: ("Solve the equation: 3x^2-8x-3 ", "3 and -1/2"),
    16: ("Solve the equation: √4x = x+2 If equation will not have roots just write No roots ", "No roots"),
    17: ("Solve the equation: 4^x-9*2^x+8=0 ", "3 and 0"),
    18: ("Solve the equation: 3a +2a = 25 ", "5"),
    19: ("Solve the equation: 2x-4=16-3x ", "4"),
    20: ("Solve the equation: (x-3)^2 + 6x = 0 ", "3 and -3"),
    21: ("Solve the equation: x^2-12x+32=0 ", "8 and 4"),
    22: ("Solve the equation: 9x+7=52 ", "5"),
    23: ("Are these two equations equivalent? x+49=56 and x^2=49 ", "No"),
    24: ("Are these two equations equivalent? x-3=6 and √x = 3 ", 'Yes'),
    25: ("Solve the equation: 2x-6=72 ", "39"),
    26: ("Solve the equation: (x-2)^2-x^2=0 ", "1"),
    27: ("Solve the equation: 3x-4=7x+8 ", "-3"),
    28: ("Solve the equation: √(36-x^2) = 2x ", "2"),
    29: ("Solve the equation: x^2-6x = 0 ", "0 and 6"),
    30: ("Solve the equation: x^3-1/x^2+x+1 = (x+3)(x+1). If equation will not have roots just write No roots ","No roots"),
 }

 score = 0

 while question_count < question_limit:
    question_count += 1
    random_question = random.randint(1, 30)
    print(f"Question {question_count}: {questions6[random_question][0]}")
    if ask_question(questions6[random_question][0], questions6[random_question] [1]):
        score += 1

 print(f"You got {score}/{question_limit} questions correct.")

elif categoryOfQuestions == "7":
 questions7 = {
    1: ("What is sin^2a + cos^2a: ", "1"),
    2: ("What is tan135: ", "-1"),
    3: ("What is cos2a - cos^2a : ", "-sin^2a"),
    4: ("What is tan46*cot124*sin91*cos90: ", "0"),
    6: ("Does this expression have sense: tan 90? ", "no"),
    5: ("Solve the equation: cosx = 1/2", "arccos(pi/3)+2pi*n"),
    7: ("What expression is the most here: sin 135, tan 135, cos 135, cot 135 ", "sin 135"),
    8: ("What is sin 2a * tan a: ", "2sin^2a"),
    9: ("What period will the graph of the function have?: y = tanx ", "pi"),
    10: ("What can be the maximum value of sine and cosine?: ", "1"),
    11: ("What is pi number in degs? ", "180"),
    12: ("What is the inverse function of tan? ", "arctan"),
    13: ("How can we say 360 degrees on radians ", "2pi"),
    14: ("What is cot 30 * tan 30 * sin 30: " , "0.5"),
    15: ("On the unit circle we marked point A(0.5; 0.7). What is the sine of this point? ", "0.7"),
    16: ("1 radian is how many degrees? ", "57.3"),
    17: ("What is arccos (√3/2) (write in radians)", "pi/6"),
    18: ("Solve the equation: sin2x = 1/2 ", "(-1)^k*pi/12+(pi*k)/2"),
    19: ("Match the formulas and their meanings. In response, write a sequence of letters (no spaces): \n 1) sin^2a + cos^2a --- N)sin^2a \n 2) (sina*cosa)cota --- S)1 \n 3)1-cos^2a --- E)2cosa \n 4) sin2a/sina --- I)cos^2a" , "SINE"),
    20: ("What is: tanx*cotx ", "1"),
    21: ("On the unit circle we marked point A(0.5; 0.7). What is the cosine of this point?: ", "0.5"),
    22: ("(sin45 * cos45)arccos (in radians): ", "pi/3"),
    23: ("What is cos 225 ", "-(√2/2)"),
    24: ("What expression is the most here: sin30, cos30, tan30, cot30 ", 'cot30'),
    25: ("Does the function change using the casting formula: sin(pi - a)? ", "no"),
    26: ("Does the function change using the casting formula: cos((3pi/2)-a)? ", "yes"),
    27: ("Does the sign of a function change using the reduction formula: sin(pi + a) ", "yes"),
    28: ("What is the period of graph of function: y = sinx ", "2pi"),
    29: ("What is (cos225)^2 ", "0.5"),
    30: ("What angle from 0 to 180 degrees does not have a tangent? ","90"),
 }
 score = 0

 while question_count < question_limit:
      question_count += 1
      random_question = random.randint(1, 30)
      print(f"Question {question_count}: {questions7[random_question][0]}")
      if ask_question(questions7[random_question][0], 
 questions7[random_question] [1]):
          score += 1

 print(f"You got {score}/{question_limit} questions correct.")

elif categoryOfQuestions == "8":
 print("Attention please! Number in () are logarythm's base!!!") 
 questions8 = {
    1: ("What is: log(7)49 ", "2"),
    2: ("What is: log(x)729 = 3 ", "9"),
    3: ("What is: lg 100000 ", "5"),
    4: ("Rewrite this expression with using log: 5^x=35 ", "log(5)35=x"),
    5: ("What is: log(6)4+log(6)9 ", "2"),
    6: ("What is: log(3)x=5 ", "243"),
    7: ("What is bigger: lg14 or lg121 ", "lg121 "),
    8: ("What is log(25)125: ", "6"),
    9: ("What is log(0.5)0.25: ", "2"),
    10: ("What is 4^log(4)5: ", "5"),
    11: ("What is x in log(5)256/log(5)x=4: ", "4"),
    12: ("What is log(34)34 ", "1"),
    13: ("What is x in log(x)64=3: ", "4"),
    14: ("What is log(√2)4 " , "4"),
    15: ("Solve the equation: log(2)x-3=log(2)2x-5 ", "2"),
    16: ("Solve the equation: log(4)x+log(4)x-5 = log(4)14", "7"),
    17: ("What is: 3^lg95 ", "95"),
    18: ("How can we write a logarythm with 10 as base: ", "lg"),
    19: ("How can we write a logarythm with the e number as base: ", "ln"),
    20: ("What is a logarythm?: (write in one word) ", "exponent"),
    21: ("What is log(x)128+log(x)2=4: ", "4"),
    22: ("What is bigger log(2)16, lg1000 or log(4)16 ", "log(2)16"),
    23: ("What is lgx=-3? ", "0.001"),
    24: ("What is the domain of the function: y=log(2)x ", 'D(y)∈(0;+∞)'),
    25: ("Does the function y=log(0.5)x increase or fall: (write increase or fall in Present Simple)", "falls"),
    26: ("Solve the equation: lgx-3=1 ", "13"),
    27: ("What is: log(3)343/log3(√7) ", "6"),
    28: ("Simplify the expression: log(3)16 ", "2log(3)4"),
    29: ("Simplify the expression: log(64)126 ", "0.5log(8)126"),
    30: ("Simplify the expression: 1/log(c)b ","log(b)c"),
 }

 score = 0

 while question_count < question_limit:
    question_count += 1
    random_question = random.randint(1, 30)
    print(f"Question {question_count}: {questions8[random_question][0]}")
    if ask_question(questions8[random_question][0], questions8[random_question] [1]):
        score += 1

 print(f"You got {score}/{question_limit} questions correct.")

elif categoryOfQuestions == "9":
 questions9 = {
    1: ("What is 2+5? ", "7"),
    2: ("What is 1+1+2-5+1? ", "0"),
    3: ("What is 17+33? ", "50"),
    4: ("What is 41 - 19? ", "22"),
    5: ("What is 13+45? ", "58"),
    6: ("What is -25+25? ", "0"),
    7: ("What is 4+7-8+2? ", "5"),
    8: ("What is 125-75+40? ", "90"),
    9: ("What is 24+75-63? ", "36"),
    10: ("What is 72+57? ", "129"),
    11: ("What is 17-9? ", "8"),
    12: ("What is 1-1-3+2-7? ", "-8"),
    13: ("What is 23-13? ", "10"),
    14: ("What is 47+47? ", "94"),
    15: ("What is 56+44+100-300? ", "-100"),
    16: ("What is 7-1? ", "6"),
    17: ("What is 17+81? ", "98"),
    18: ("What is 25-23+(-3)? ", "-1"),
    19: ("What is (-5) + (-3)? ", "-8"),
    20: ("What is -100-(-72)-25? ", "-53"),
    21: ('What is 27+91-(-30) ', '148'),
    22: ('What is 3+18-1+80 ', '100'),
    23: ('What is 45-17+52 ', '80'),
    24: ('What is -25+26 ', '1'),
    25: ('What is 97-94+27 ', '30'),
    26: ('What is 16-8 ', '8'),
    27: ('What is 2a+a-13a ', '-10a'),
    28: ('What is 3c-4c+c ' , '0'),
    29: ('What is 72x+28x-21 ' , '100x-21'),
    30: ('What is 0+5b-17+12b ' , '17b-17'),
    31: ("Solve the equation: x-4 = 46? ", "50"),
    32: ("Solve the equation: x^2-1 = 0", "1 and -1"),
    33: ("Solve the equation: 2x-8 = 7-3x", "3"),
    34: ("Solve the equation: 3^x = 27", "3"),
    35: ("Solve the equation: sqrtx = 5", "25"),
    36: ("Solve the equation: 2x^2-5x+2=0", "2 and 0.5"),
    37: ("Solve the equation: 4x+2 = x^2+5x", "-2 and 1 "),
    38: ("Solve the equation: x^2-3x = 0", "0 and 3"),
    39: ("Solve the equation: 7x-21 = 0", "3"),
    40: ("Solve the equation: 2x/5 + 1/4 = 4", "75/8"),
    41: ("Solve the equation: (x-1)(x+1)=5", "sqrt6 and -sqrt6"),
    42: ("Does this equation have a root? sqrtx = -32", "No"),
    43: ("Solve the equation: 3/x-2/5 = 1/10x", "15"),
    44: ("Solve the equation: 26-7x = 103", "-11"),
    45: ("Solve the equation: 3x^2-8x-3", "3 and -1/2"),
    46: ("Solve the equation: sqrt4x = x+2 If equation will not have roots just write 'No roots'"),
    47: ("Solve the equation: 4^x-9*2^x+8=0 ", "3 and 0"),
    48: ("Solve the equation: 3a +2a = 25 ", "5"),
    49: ("Solve the equation: 2x-4=16-3x", "4"),
    50: ("Solve the equation: (x-3)^2 + 6x = 0", "3 and -3"),
    51: ("Solve the equation: x^2-12x+32=0", "8 and 4"),
    52: ("Solve the equation: 9x+7=52", "5"),
    53: ("Are these two equations equivalent? x+49=56 and x^2=49", "No"),
    54: ("Are these two equations equivalent? x-3=6 and sqrtx = 3 ", 'Yes'),
    55: ("Solve the equation: 2x-6=72", "39"),
    56: ("Solve the equation: (x-2)^2-x^2=0 ", "1"),
    57: ("Solve the equation: 3x-4=7x+8 ", "-3"),
    58: ("Solve the equation: sqrt(36-x^2) = 2x ", "2"),
    59: ("Solve the equation: x^2-6x = 0 ", "0 and 6"),
    60: ("Solve the equation: x^3-1/x^2+x+1 = (x+3)(x+1). If equation will not have roots just write 'No roots' "),
    61: ("What is 1/2 + 3/4 and if it possible, reduce? ", "5/4"),
    62: ("Reduce the fraction: 49/343 ", "1/7"),
    63: ("What is 23/45 * 90/92 and if it possible, reduce", "1/2"),
    64: ("What is (0,5+0,7)^2 ", "1.44"),
    65: ("What is sqrt64/81 ", "8/9"),
    66: ("Reduce the fraction 8m/32m^2? ", "1/4m"),
    67: ("Compare this two fractions -0,4 and 0.01 ", "<"),
    68: ("What is 1.2/2 *100 * 1/2 ? ", "30"),
    69: ("What is: 10a^2/(a-1) / 5a/(a-1) if a = 18 ? ", "36"),
    70: ("What is: (x^3 - y^3) / (x-y) if x = 2, y = 3? ", "19"),
    71: ("What is (0,17 - 0.07)*20*0,25? ", "0.5 "),
    72: ("What is (3/5)^3 ", "27/125"),
    73: ("Reduce the fraction 56/128? ", "7/16"),
    74: ("Is this fraction correct 5/(x-2) x =2 ", "no"),
    75: ("What is 2,5+4,5 - 5*1,4? ", "0"),
    76: ("What is sqrt 2,56 ", "1.6"),
    77: ("What is 100000000/50000000-4^1/2? ", "0"),
    78: ("What is 3/4 - 5/7? ", "1/28"),
    79: ("What is 3/4 * 8/15? ", "2/5"),
    80: ("What is (-9.2 + 7)/2 ", "-1.1"),
    81: ("What is 6/7 + 8/9? ", "110/63"),
    82: ("What is sqrt49*26/35? ", "26/5"),
    83: ("What is (2/5 - 3/4)^2 ? ", "49/400"),
    84: ("What is (1.5 *2 - 5.4) * -30? ", '72'),
    85: ("What is (11/12)^2 ", "121/144"),
    86: ("What is 3/7 * 1/6? ", "3.5"),
    87: ("What is 24*0,3 ? ", "7.2"),
    88: ("What is 1/2+2/3? ", "5/6"),
    89: ("What is 2/3 / 5/6? ", "4/5"),
    90: ("Reduce the fraction 1024m^3 / 4096m^5  ", "1/4m^2"),
    91: ("What is 1-5*4? ", "-19"),
    92: ("What is (4+10)/2+37? ", "44"),
    93: ("What is 36/12+32/8? ", "7"),
    94: ("What is (72+28)/4*3-150? ", "-75"),
    95: ("What is 26/13*4+(24*5)? ", "128"),
    96: ("What is 3(45+32)? ", "231"),
    97: ("What is (5-2a)*3? ", "15-6a"),
    98: ("What is 123/3+32? ", "73"),
    99: ("What is -35(x+2)+35(x-2)? ", "0"),
    100: ("What is (2048/8-56)/100? ", "2"),
    101: ("What is 2a+4c(3+4b)? ", "2a+16bc+12c"),
    102: ("What is (103-3)/25*18? ", "72"),
    103: ("What is -5*7+27? ", "-8"),
    104: ("What is 2*2-2/2+2 ", "5"),
    105: ("What is 35/7+16(x-5)? ", "16x-75"),
    106: ("What is 60/-12+5? ", "0"),
    107: ("What is a-a+3bc? ", "3bc"),
    108: ("What is 12/4+(45-20)? ", "28"),
    109: ("What is 63/9+23? ", "30"),
    110: ("What is (1+2-3)*1000000? ", "0"),
    111: ("What is (67*2)-44 ", "90"),
    112: ("What is 35/5-23? ", "-16"),
    113: ("What is 6b-2(3b+4c)? ", "-8c"),
    114: ("What is (1000/25)*40? ", '1600'),
    115: ("What is -39/13+44 ", "41"),
    116: ("What is 4ab*31c? ", "124abc"),
    117: ("What is (3a*2b)+28ab? ", "34ab"),
    118: ("What is 24z*(-3j)? ", "-72jz"),
    119: ("What is 3a/a*21? ", "63"),
    120: ("What is -4x/2x*(-8x)*2 ", "32x"),
    121: ("What is 3*5? ", "15"),
    122: ("What is 7*7? ", "49"),
    123: ("What is 72/8? ", "9"),
    124: ("What is 4*8? ", "32"),
    125: ("What is 77/11? ", "7"),
    126: ("What is 108/36? ", "3"),
    127: ("What is 12*11? ", "121"),
    128: ("What is 2*2*2*2*2/2? ", "16"),
    129: ("What is 24*5? ", "120"),
    130: ("What is 640/8? ", "80"),
    131: ("What is 60*20? ", "1200"),
    132: ("What is 13*13? ", "169"),
    133: ("What is -5*7? ", "-35"),
    134: ("What is -65/-13? ", "5"),
    135: ("What is 35*124*629*0? ", "0"),
    136: ("What is 60/-12? ", "-5"),
    137: ("What is 17*4? ", "68"),
    138: ("What is 24/6? ", "4"),
    139: ("What is 63/9? ", "7"),
    140: ("What is 27/9*12/6*15/30*100? ", "300"),
    141: ("What is 14*3/7? ", "6"),
    142: ("What is 35/5? ", "7"),
    143: ("What is 6*6*6? ", "216"),
    144: ("What is 10*100? ", '1000'),
    145: ("What is -39/-13 ", "3"),
    146: ("What is 144/-9? ", "-16"),
    147: ("What is 3a*2b? ", "6ab"),
    148: ("What is 24z*(-3j)? ", "-72jz"),
    149: ("What is 3a/a*21? ", "63"),
    150: ("What is -4x/2x*(-8x)*2 ", "32x"),
    151: ("What is (2^3)^0? ", "1"),
    152: ("What is √2*√8? ", "4"),
    153: ("What is 5^4? ", "625"),
    154: ("What is ∛(27/729)? ", "1/3"),
    155: ("What is 4* √324 /9? ", "8"),
    156: ("What is 4^5*4^3/4^5 ", "64"),
    157: ("What is (∜a)^4? ", "a"),
    158: ("What is -3^5-13? ", '-256'),
    159: ("What is (5-x)^2? ", "25-10x+x^2"),
    160: ("What is √60*√15? ", "30"),
    161: ("What is 2^4*4^3/16^2 ", "4"),
    162: ("What is ∛27 - √169 + fiveroot 243 ", "-7"),
    163: ("Remove the number from under the root sign √48 ", "4√3"),
    164: ("Remove the number from under the root sign √72 ", "3√8"),
    165: ("Remove the number from under the root sign √108 ", "6√3"),
    166: ("What is 2^3-6+3^5? ", "245"),
    167: ("What is √45 + √125? ", "8√5"),
    168: ("What is -8^2 * ∛27? ", "192"),
    169: ("What is √(32+49)? ", "9"),
    170: ("What is √(125/25)? ", "√5"),
    171: ("Remove the number from under the root sign ∛72", "2∛9"),
    172: ("What is (√7)^2? ", "7"),
    173: ("What is (a-1)^2-(a+2)^2 if a = -2? ", "9"),
    174: ("What is 36t^2-49u^2 ", '(6t-7u)(6t+7u)'),
    175: ("What is 8x^3-1 ", "(2x-1)(4x^2+2x+1)"),
    176: ("What is (3x-5y)^2? ", "9x^2-30xy+25y^2"),
    177: ("What is 100000^0? ", "1"),
    178: ("What is 25a^2-9c^2 ", "(5a-3c)(5a+3c)"),
    179: ("What is 1^10000000? ", "1"),
    180: ('Remove the number from under the root sign √128', '8√2'),
    181: ("What is: log(7)49 ", "2"),
    182: ("What is: log(x)729 = 3 ", "9"),
    183: ("What is: lg 100000 ", "5"),
    184: ("Rewrite this expression with using log: 5^x=35 ", "log(5)35=x"),
    185: ("What is: log(6)4+log(6)9 ", "2"),
    186: ("What is: log(3)x=5 ", "243"),
    187: ("What is bigger: lg14 or lg121 ", "lg121 "),
    188: ("What is log(25)125: ", "6"),
    189: ("What is log(0.5)0.25: ", "2"),
    190: ("What is 4^log(4)5: ", "5"),
    191: ("What is x in log(5)256/log(5)x=4: ", "4"),
    192: ("What is log(34)34 ", "1"),
    193: ("What is x in log(x)64=3: ", "4"),
    194: ("What is log(√2)4 " , "4"),
    195: ("Solve the equation: log(2)x-3=log(2)2x-5 ", "2"),
    196: ("Solve the equation: log(4)x+log(4)x-5 = log(4)14", "7"),
    197: ("What is: 3^lg95 ", "95"),
    198: ("How can we write a logarythm with 10 as base: ", "lg"),
    199: ("How can we write a logarythm with the e number as base: ", "ln"),
    200: ("What is a logarythm?: (write in one word) ", "exponent"),
    201: ("What is log(x)128+log(x)2=4: ", "4"),
    202: ("What is bigger log(2)16, lg1000 or log(4)16 ", "log(2)16"),
    203: ("What is lgx=-3? ", "0.001"),
    204: ("What is the domain of the function: y=log(2)x ", 'D(y)∈(0;+∞)'),
    205: ("Does the function y=log(0.5)x increase or fall: (write increase or fall in Present Simple)", "falls"),
    206: ("Solve the equation: lgx-3=1 ", "13"),
    207: ("What is: log(3)343/log3(√7) ", "6"),
    208: ("Simplify the expression: log(3)16 ", "2log(3)4"),
    209: ("Simplify the expression: log(64)126 ", "0.5log(8)126"),
    210: ("Simplify the expression: 1/log(c)b ","log(b)c"),
    211: ("What is sin^2a + cos^2a: ", "1"),
    212: ("What is tan135: ", "-1"),
    213: ("What is cos2a - cos^2a : ", "-sin^2a"),
    214: ("What is tan46*cot124*sin91*cos90: ", "0"),
    215: ("Does this expression have sense: tan 90? ", "no"),
    216: ("Solve the equation: cosx = pi/6", "arccos(√3/2)+2pi*n"),
    217: ("What expression is the most here: sin 135, tan 135, cos 135, cot 135 ", "sin 135"),
    218: ("What is sin 2a * tan a: ", "2sin^2a"),
    219: ("What period will the graph of the function have?: y = tanx ", "pi"),
    220: ("What can be the maximum value of sine and cosine?: ", "1"),
    221: ("What is pi number in degs? ", "180"),
    222: ("What is the inverse function of tan? ", "arctan"),
    223: ("How can we say 360 degrees on radians ", "2pi"),
    224: ("What is cot 30 * tan 30 * sin 30: " , "0.5"),
    225: ("On the unit circle we marked point A(0.5; 0.7). What is the sine of this point? ", "0.7"),
    226: ("1 radian is how many degrees? ", "57.3"),
    227: ("What is arccos (√3/2) (write in radians)", "pi/6"),
    228: ("Solve the equation: sin2x = 1/2 ", "(-1)^k*pi/12+(pi*k)/2"),
    229: ("Match the formulas and their meanings. In response, write a sequence of letters (no spaces): \n 1) sin^2a + cos^2a --- N)sin^2a \n 2) (sina*cosa)cota --- S)1 \n 3)1-cos^2a --- E)2cosa \n 4) sin2a/sina --- I)cos^2a" , "SINE"),
    230: ("What is: tanx*cotx ", "1"),
    231: ("On the unit circle we marked point A(0.5; 0.7). What is the cosine of this point?: ", "0.5"),
    232: ("(sin45 * cos45)arccos (in radians): ", "pi/3"),
    233: ("What is cos 225 ", "-(√2/2)"),
    234: ("What expression is the most here: sin30, cos30, tan30, cot30 ", 'cot30'),
    235: ("Does the function change using the casting formula: sin(pi - a)? ", "no"),
    236: ("Does the function change using the casting formula: cos((3pi/2)-a)? ", "yes"),
    237: ("Does the sign of a function change using the reduction formula: sin(pi + a) ", "yes"),
    238: ("What is the period of graph of function: y = sinx ", "2pi"),
    239: ("What is (cos225)^2 ", "0.5"),
    240: ("What angle from 0 to 180 degrees does not have a tangent? ","90"),
 }
 question_limit1 = 30
 score = 0

 while question_count < question_limit1:
    question_count += 1
    random_question = random.randint(1, 240)
    print(f"Question {question_count}: {questions9[random_question][0]}")
    if ask_question(questions9[random_question][0], questions9[random_question] [1]):
        score += 1

 print(f"You got {score}/{question_limit1} questions correct.")
