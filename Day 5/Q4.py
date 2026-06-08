# Voting Eligibility Check using Short-Circuit Evaluation

age = int(input("Enter age: "))
is_citizen = input("Are you a citizen? (True/False): ") == "True"
is_registered = input("Are you registered to vote? (True/False): ") == "True"

if age >= 18 and is_citizen and is_registered:
    print("Eligible to vote")
else:
    print("Not eligible to vote")