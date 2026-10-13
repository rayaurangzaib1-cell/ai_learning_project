from utils import calculate_total

laptop = calculate_total(10000, 2)
mouse = calculate_total(20, 100)
keyboard = calculate_total(200, 25)

print("Laptop:", laptop)
print("Mouse:", mouse)
print("Keyboard:", keyboard)

# Naya configuration wala code

import os
from dotenv import load_dotenv

load_dotenv()

app_name = os.getenv("APP_NAME")
student_name = os.getenv("STUDENT_NAME")
daily_hours = os.getenv("DAILY_HOURS")

print("App:", app_name)
print("Student:", student_name)
print("Daily Hours:", daily_hours)