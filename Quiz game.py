

questions = ("How many elements are in the periodic table?:", 
             "which animal lays the largest eggs?:",
             "what is the most abundant gas in the earth's atmosphere?:",
             "how many bones are in the human body?:",
             "which planet in the solar system is the hottest?: ")

options =   (("A. 116", "B. 117", "C. 118", "D. 119"),
             ("A. Whale", "B. crocodile", "C. Elephant", "D. Ostrich"), 
             ("A. Nitrogen", "B. Oxygen", "C. Carbon-Dioxide", "D. Hydrogen"), 
             ("A. 206", "B. 207", "C. 208", "D. 209"), 
             ("A. Mercury", "B.Venus", "C.Earth", "D.Mars"))

answers = ("C", "D", "A", "A", "B") 
guesses = [] 
score = 0
question_num = 0

for question in questions:
    print("-------------------------")
    print(question)
    for option in options[question_num]:
        print(option)
    guess = input("Enter (A, B, C, or D): ").upper()
    guesses.append(guess)
    
    if guess == answers[question_num]:
        score += 1
        print("CORRECT!")
    else:
        print("WRONG!")
        print(f"{answers[question_num]} is the correct answer.")
    
    question_num += 1