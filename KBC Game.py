#KBC Game:
Questions = [
    [
        "which language is used to create facebook","python","french","javascript",
     "php","none",4
     
    ],
    [
        "which of the following is not a programming language","python","java","HTML",
     "C++","none",3
     
    ],
    [
        "who is known for father of the indian constitution","mahatma gandhi","Dr.B.R.Ambedkar",
     "jawaharlal nehru",
     "sardar vallabhbhai patel","none",2
     
    ],
    [
         "which planet is known as the RED PLANET","venus","mars",
      "jupiter","saturn","none",2
      
    ],
]

levels = [1000,2000,3000,5000,10000,20000,40000,80000,160000,320000,640000,1250000,2500000,5000000,
          10000000,70000000]
money = 0
for i in range(len(Questions)):
    question = Questions[i]
    print(f"question for rs.{levels[i]}")
    print(f"a.{question[1]}   b.{question[2]}")
    print(f"c.{question[3]}   d.{question[4]}")
    reply = int(input("enter your answer(1-4):"))
    if(reply == question[-1]):
        print("correct answer you won rs.{levels[i]}")
        if(i == 4):
            money = 10000
        elif(i == 9):
            money = 320000
        elif(i == 14):
            money = 10000000
    else:
        print("wrong answer!!!")
        break