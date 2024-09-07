score = int(input("score: "))

if score >100 :
    print('not range')
elif score>=90 and score <=100:
    print("Grade A")
elif score>= 80 and score <= 90 :
    print("Grade B")
if score>=60 and score <=70:
    print("Grade C")
elif score>= 50 and score <= 60 :
    print("Grade D")
elif score < 50 :
    print("Grade E")