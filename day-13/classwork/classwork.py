score = int(input("enter your test score: "))

if score > 90 and score < 100:
    print("max")
elif score > 70 and score < 80:
    print("1500")
elif score > 40 and score < 70:
    print("500")
elif score < 40:
    print("0")