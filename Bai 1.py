#Bai 1

while True:
    print("Enter your grade: ")
    score = int(input())
    if score >= 90:
        print("grade is A")
    elif score >= 80:
        print("grade is B")
    elif score >= 70:
        print("grade is C")
    elif score >= 60:
        print("grade is D")
    elif score < 60 and score >= 0:
        print("grade is F")
    else:
        break