# if ...else


# if ( 10 > 4):
#     print("10 is greater")
# else:
#     print("4 is greater")

# x=10
# y=4

    
# if  x > y:
#     print(f"{x} is greater")
# else:
#     print(f"{y} is greater"


# Task
# Get two person name
# Case 1:
# Yuma, Yoshi
# 173cm, 163cm
# Expected
# Yuma is taller than Yoshi by 10cm

user1 = input("give me a name of first user ?")
user1_cm = float(input("how long ?"))
user2 = input("give me a name of second user?")
user2_cm = float(input("how long ?"))
# diff_height = abs(user1_cm - user2_cm)

if user1_cm>user2_cm:
    print(f"{user1} is taller then {user2} by {user1_cm - user2_cm} cm")
elif user1_cm==user2_cm:
    print(f"{user1} and {user2} are of same height ")
else:
    print(f"{user2} is taller then {user1} by {user2_cm - user1_cm} cm")




# Case 2:
# Yuma, Yoshi
# 173cm, 185cm
# Expected
# Yoshi is taller than Yuma by 12cm
