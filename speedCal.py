from time import time
import random as r

def mistake(paraTest, userTest):
    error = 0
    for i in range(min(len(paraTest), len(userTest))):  
        if paraTest[i] != userTest[i]:
            error = error + 1
    return error

def speed_time(time_s, time_e, user_input):
    time_delay = time_e - time_s
    time_R = round(time_delay, 2)
    speed = len(user_input) / time_R
    return round(speed, 2)




test = [
    "A paragraph is a self-contained unit of discourse in writing with a particular point or idea.",
    "Writing a paragraph about something reveals the writer's knowledge or thinking about that particular thing.",
    "If one is writing for others, he/she should keep in mind that the para should be easy to comprehend, grammatically correct and should contain valid content.",
]

test1 = r.choice(test)

print("          *****Typing Speed*****             ")
print(test1)

print()
print()

time_1 = time()

testInput = input("Enter: ")

time_2 = time()

print("Speed: w/sec", speed_time(time_1, time_2, testInput))
print("Error:", mistake(test1, testInput))  