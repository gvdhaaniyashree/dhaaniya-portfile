
# ==========================================
#          REVERSE FITNESS APP
#              BASE CODE
# ==========================================
import random
import json
import os
from datetime import date

# ---------------- SAVED DATA ----------------

DATA_FILE = "fitness_data.json"

if os.path.exists(DATA_FILE):
    with open(DATA_FILE, "r") as file:
        data = json.load(file)
else:
    data = {
    "streak": 0,
    "completed_days": 0,
    "badges": [],
    "last_checkin": ""
}

print("==========================================")
print("          REVERSE FITNESS APP")
print("==========================================")

# ---------------- USER PROFILE ----------------

name = input("\nEnter your name: ")
age = int(input("Enter your age: "))

# ---------------- SLEEP ----------------

print("\n--- Sleep Cycle ---")
sleep_time = input("What time do you usually sleep? (HH:MM): ")
wake_time = input("What time do you usually wake up? (HH:MM): ")
# ---------------- SLEEP DURATION ----------------

from datetime import datetime

sleep = datetime.strptime(sleep_time, "%H:%M")
wake = datetime.strptime(wake_time, "%H:%M")

# If wake-up time is on the next day
if wake <= sleep:
    wake = wake.replace(day=wake.day + 1)

sleep_duration = (wake - sleep).total_seconds() / 3600

print("\n😴 SLEEP DURATION:", round(sleep_duration, 1), "hours")
if sleep_duration < 7:
    print("😴 SLEEP REMINDER: Try to maintain a consistent sleep routine.")
elif sleep_duration <= 9:
    print("✅ Your recorded sleep duration is within a typical healthy range.")
else:
    print("💙 Your recorded sleep duration is longer than usual. Keep monitoring your routine.")

# ---------------- ACTIVITY ----------------

print("\n--- Daily Activity ---")

activity = input("What activity did you do today? ")
activity_minutes = int(input("How many minutes were you active? "))

# Step sensor placeholder
steps = 0

# ---------------- FOOD ANALYSIS ----------------

print("\n--- Food Analysis ---")

food_photo = input(
    "Enter food photo name (or type 'skip'): "
)

if food_photo.lower() == "skip":
    food_analysis = "No food photo analyzed."
else:
    food_analysis = "Food photo saved for AI analysis."

# ---------------- HYDRATION ----------------

print("\n--- Hydration ---")
water_glasses = int(input("How many glasses of water did you have today? "))

# ---------------- REST ----------------

print("\n--- Rest ---")
active_hours = float(
    input("How many hours have you been continuously active/studying? ")
)

# ---------------- SMART REMINDERS ----------------

print("\n🔔 SMART REMINDERS")

reminders = []

if water_glasses < 4:
    reminders.append("💧 Drink some water and remember to stay hydrated.")
elif water_glasses < 6:
    reminders.append("💧 Keep your water intake regular throughout the day.")

if active_hours >= 2:
    reminders.append("🧘 You've been active/studying for a while. Take a short break.")
elif active_hours >= 1:
    reminders.append("🧘 Consider taking a short break soon.")

if sleep_duration < 7:
    reminders.append("😴 Try to maintain a consistent sleep routine.")

if activity_minutes < 30:
    reminders.append("🚶 Consider adding some light movement to your day.")

if reminders:
    for reminder in reminders:
        print(reminder)
else:
    print("✅ No urgent reminders. Keep maintaining your routine!")

# ---------------- DAILY GOALS ----------------

print("\n--- Daily Goals ---")

goals_completed = 0

# Activity goal
if activity_minutes >= 30:
    goals_completed += 1
    print("✅ Activity goal completed!")
else:
    print("⬜ Activity goal not completed.")

# Hydration goal
if water_glasses >= 6:
    goals_completed += 1
    print("✅ Hydration goal completed!")
else:
    print("⬜ Hydration goal not completed.")

# Rest goal
if active_hours < 2:
    goals_completed += 1
    print("✅ Rest-break goal completed!")
else:
    print("⬜ Remember to take regular breaks.")

# ---------------- STREAK SYSTEM ----------------

# ---------------- DAILY STREAK SYSTEM ----------------

today = str(date.today())

if goals_completed >= 2:

    if data.get("last_checkin") != today:
        data["streak"] += 1
        data["completed_days"] += 1
        data["last_checkin"] = today

        print("\n🔥 STREAK INCREASED!")
        print("Current streak:", data["streak"], "day(s)")

    else:
        print("\n✅ Today's check-in is already counted.")
        print("🔥 Current streak:", data["streak"], "day(s)")

else:
    print("\n⚠️ Complete at least 2 daily goals to maintain your streak.")
# ---------------- BADGES ----------------

badges = []


# ---------------- BADGES ----------------

# ---------------- BADGE PROGRESSION ----------------

# First check-in
if data["completed_days"] >= 1:
    if "🌱 First Step" not in data["badges"]:
        data["badges"].append("🌱 First Step")

# 3-day streak
if data["streak"] >= 3:
    if "🔥 3-Day Streak" not in data["badges"]:
        data["badges"].append("🔥 3-Day Streak")

# 7-day streak
if data["streak"] >= 7:
    if "🏆 7-Day Streak" not in data["badges"]:
        data["badges"].append("🏆 7-Day Streak")

# 14-day streak
if data["streak"] >= 14:
    if "💎 14-Day Streak" not in data["badges"]:
        data["badges"].append("💎 14-Day Streak")

# 30-day streak
if data["streak"] >= 30:
    if "👑 30-Day Champion" not in data["badges"]:
        data["badges"].append("👑 30-Day Champion")

# Perfect day
if goals_completed == 3:
    if "🌟 Perfect Day" not in data["badges"]:
        data["badges"].append("🌟 Perfect Day")

# Hydration badge
if water_glasses >= 6:
    if "💧 Hydration Hero" not in data["badges"]:
        data["badges"].append("💧 Hydration Hero")

# Rest badge
if active_hours < 2:
    if "🧘 Rest Champion" not in data["badges"]:
        data["badges"].append("🧘 Rest Champion")


# Save updated data
with open(DATA_FILE, "w") as file:
    json.dump(data, file, indent=4)


# ---------------- ENCOURAGEMENT ----------------

messages = [
    "Great job! Keep building healthy habits! 💪",
    "You're doing well! Consistency matters. 🌟",
    "Small steps every day can make a difference. ✨",
    "Keep going! Remember to balance activity and rest. 💙",
    "You've got this! Keep your streak alive! 🔥"
]

# ---------------- SUMMARY ----------------

print("\n==========================================")
print("             DAILY SUMMARY")
print("==========================================")

print("\n👤 Profile")
print("Name:", name)
print("Age:", age)

print("\n😴 Sleep")
print("Sleep time:", sleep_time)
print("Wake-up time:", wake_time)

print("\n🏃 Activity")
print("Activity:", activity)
print("Active minutes:", activity_minutes)

print("\n💧 Hydration")
print("Water glasses:", water_glasses)

# ---------------- REST REMINDER ----------------

if active_hours >= 2:
    print("\n🔔 REST REMINDER")
    print("You've been active for a while.")
    print("Take a short break and relax.")
else:
    print("\n✅ Good job taking regular breaks!")

# ---------------- HYDRATION ALERT ----------------

if water_glasses < 4:
    print("\n💧 HYDRATION ALERT")
    print("Remember to drink water regularly.")
elif water_glasses < 6:
    print("\n💧 HYDRATION REMINDER")
    print("Keep drinking water throughout the day.")
else:
    print("\n💧 HYDRATION STATUS")
    print("Great job staying hydrated!")

# ---------------- BADGES ----------------

print("\n🏆 BADGES EARNED")

if data["badges"]:
    for badge in data["badges"]:
        print(badge)
else:
    print("No badges yet. Keep going!")

# ---------------- STREAK ----------------

print("\n🔥 CURRENT STREAK:", data["streak"], "DAY(S)")
print("📅 COMPLETED DAYS:", data["completed_days"])
# ---------------- ENCOURAGEMENT ----------------

print("\n🌟 MESSAGE")
print(random.choice(messages))

print("\n==========================================")
print("       DAILY CHECK-IN COMPLETED! ❤️")
print("==========================================")
print("==========================================")
# ---------------- SMART RECOMMENDATION ----------------

print("\n🧠 TODAY'S PERSONALIZED RECOMMENDATION")

if water_glasses < 4:
    print("💧 Focus on regular hydration breaks today.")

elif active_hours >= 2:
    print("🧘 You've been active for a while. Take a short rest break.")

elif activity_minutes < 30:
    print("🚶 Consider adding some light movement to your day.")

elif goals_completed == 3:
    print("🌟 Excellent balance today! Keep following your routine.")

else:
    print("💙 Keep maintaining a balanced routine of activity and rest.")

    # ---------------- AI INSTRUCTOR ----------------

print("\n🤖 AI INSTRUCTOR")

if sleep_duration < 7:
    instructor_message = "Prioritize a consistent sleep routine and give yourself enough recovery time."
elif water_glasses < 4:
    instructor_message = "Remember to stay hydrated throughout the day."
elif active_hours >= 2:
    instructor_message = "You've been active for a while. Take a short rest break."
elif activity_minutes < 30:
    instructor_message = "Consider adding some comfortable movement to your day."
else:
    instructor_message = "Great job maintaining a balanced routine! Keep going."

print(instructor_message)

# ---------------- PROGRESS DASHBOARD ----------------

print("\n==========================================")
print("       📊 REVERSE FITNESS DASHBOARD")
print("==========================================")

print("\n👤 PROFILE")
print("Name:", name)

print("\n😴 SLEEP")
print("Sleep duration:", round(sleep_duration, 1), "hours")

print("\n🚶 ACTIVITY")
print("Activity:", activity)
print("Active time:", activity_minutes, "minutes")
print("Steps:", steps)

print("\n💧 HYDRATION")
print("Water:", water_glasses, "glasses")

print("\n🔥 STREAK")
print("Current streak:", data["streak"], "day(s)")
print("Completed days:", data["completed_days"])

print("\n🏆 BADGES")
print("Total badges:", len(data["badges"]))

for badge in data["badges"]:
    print(" ", badge)

print("\n📷 FOOD ANALYSIS")
print(food_analysis)

print("\n🤖 AI INSTRUCTOR")
print(instructor_message)

print("\n==========================================")
print("        END OF DASHBOARD")
print("==========================================")