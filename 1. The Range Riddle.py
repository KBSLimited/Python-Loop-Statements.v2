#Task 1: Your Mood Today:
import random

# List of moods
moods = ["Happy", "Sad", "Energetic", "Calm", "Excited", "Tired", "Content"]

# List of days in the week
days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]

# Loop through the days of the week
for day in days_of_week:
    # Randomly select a mood from the list
    mood = random.choice(moods)
    # Print the mood for the current day
    print(f"On {day}, you were feeling {mood}.")