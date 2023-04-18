print('''Welcome to the EMMAPP Short Quiz\nSelect the right answer from the options provided
\nYou will be graded at the end of the quiz\nGood Luck!''')

t_marks = int(0)
mark = int(0)

questions = ["1. What is the fastest animal on earth? A.Jaguar B.Cheetah  C.Hare",
             "2. How many continents are there in the world? A.Five B.Six C.Seven",
             "3. What is the name of Scooby Doo's van? A.Mistery Machine B.The Master Machine C.The Mystery Machine",
             "4. Which of the following is a fruit? A.Pepper B.Apple C.Ginger",
             "5. Toyota originates from which country? A.Korea B.USA C.Japan",
             "6. What is the capital city of Ghana? A.Cape Coast B.Accra C.Kumasi",
             "7. How many wheels does a motorcycle have? A.Two B.Three C.Four",
             "8. What is the first computer processor to be made? A.8086 B.Celeron C.Pentium",
             "9. When do we celebrate Christmas? A.4th April B.7th January C.25th December",
             "10. The tallest mountain in the world is? A.Everest B.Kilmanjaro C.Afadjato"]

answers = ["B", "B", "C", "B", "C", "B", "A", "A", "C", "A"]

for i in range(0, 10, 1):
    print(questions[i])
    user_input = input("Your Choice: ").upper()
    if user_input == answers[i]:
        mark = 1
        t_marks = t_marks + mark
    
print('''End of Quiz\nYour score is ''', t_marks, '''/10''')


