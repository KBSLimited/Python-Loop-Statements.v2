#Task 1: Your Mood Tracker:
import random

# List of moods
moods = ["Happy", "Sad", "Energetic", "Calm", "Excited", "Tired", "Content"]

# List of days in the week
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# List of times of the day
times_of_day = ["morning", "afternoon", "evening"]

# Outer loop for each day
for day in days_of_week:
    # Inner loop for each time of the day
    for time in times_of_day:
        # Randomly select a mood from the list
        mood = random.choice(moods)
        # Print the mood for the specific day and time
        print(f"On {day} {time}, you were feeling {mood}.")