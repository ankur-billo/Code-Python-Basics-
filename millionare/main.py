# the questions
questions=[
    ["Who is Elon Musk?", "WWE Wrestler", "Actor", "Entrepreneur", "Cricketer", 3],
    ["What is the capital of France?", "Berlin", "Madrid", "Paris", "Rome", 3],
    ["Which planet is known as the Red Planet?", "Earth", "Mars", "Jupiter", "Venus", 2],
    ["Who wrote 'Romeo and Juliet'?", "William Wordsworth", "William Shakespeare", "Charles Dickens", "Mark Twain", 2],
    ["What is the largest ocean on Earth?", "Indian Ocean", "Pacific Ocean", "Atlantic Ocean", "Arctic Ocean", 2],
    ["Who is known as the Father of Computers?", "Albert Einstein", "Isaac Newton", "Charles Babbage", "Nikola Tesla", 3],
    ["Which country invented pizza?", "France", "Italy", "USA", "Spain", 2],
    ["What does CPU stand for?", "Central Processing Unit", "Computer Personal Unit", "Central Program Utility", "Control Processing Unit", 1],
    ["Which gas do plants absorb?", "Oxygen", "Nitrogen", "Carbon Dioxide", "Hydrogen", 3],
    ["Who won the Cricket World Cup 2011?", "Australia", "England", "India", "Pakistan", 3]
]

# prizes
prizes = [ 1000, 2000, 5000, 10000, 20000, 40000, 80000, 160000, 320000, 640000 ]


# the questions with option
i=0
sum=0
for question in questions:
    print(question[0])
    print(f"a.{question[1]}")
    print(f"b.{question[2]}")
    print(f"c.{question[3]}")
    print(f"d.{question[4]}")
    
    
    # question answer checking
    a=int(input("Enter your answer -- 1 for a, 2 for b, 3 for c or 4 for d: "))
    if(question[5]==a):
        print("LaJawab! Sahi Uttar!!")
    else:
        print(f"Galat Jawab! Sahi uttar hain {question[5]}")
        print("Agli bar fir se Kosish Kare!")
        break
    sum+=prizes[i]
    print(f"You won {sum}")
    i+=1