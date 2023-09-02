height = float(input("Enter your Height : "))
weight = float(input("Enter your Weight in kg : "))


if height > 3:
    raise ValueError("Human height should not to be over 3 meters.")


bmi = weight / height ** 2
print(bmi)

# input and Output:-
# Enter your Height : 45  # 45 height is accepted where that is not possible height for human.
# Enter your Weight in kg : 46
# 0.02271604938271605

