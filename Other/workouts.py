#workouts.py
import random
from datetime import datetime
#
#
exer = ["30s Straight Leg abs",
    "3x15 Lat Raises",
    "30s Box Press Ups",
    "3x10 Explosive Squat",
    "3x15 Shoulder Press",
    "3x2 Length Lunges",
    "3x10/Leg Lateral Lunges",
    "30s Russian Twists",
    "30s Bicep Curls",
    "3x15 Box Burpees",
    "30s Reverse Lunges",
    "3x15 Dips"]
#
rounds = 6
#
print("Workout for: ", datetime.today().strftime('%d-%m'))
for i in range(rounds):
    rand1 = random.randint(1,6)
    rand2 = random.randint(1,6) + rand1
    print("Round: ", i + 1)
    print("     1: [",rand1,"]  ", exer[rand1 - 1])
    print("     2: [",rand2,"]  ", exer[rand2 - 1])
#