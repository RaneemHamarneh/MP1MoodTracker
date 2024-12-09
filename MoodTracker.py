#project 1
mood_mapping = {
    "1": "happy",
    "2": "sad",
    "3": "stressed"  
}
days = ["Sunday", "Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday"]

mood_counts = {"1": 0, "2": 0, "3": 0}
total_days = len(days)

# Looping
for day in days:
    while True:  
        mood = input(f"What's your mood for {day} (happy=1, sad=2, stressed=3): ")
        if mood in mood_mapping:
            print(f"Your mood on {day} is: {mood_mapping[mood]}")
            mood_counts[mood] += 1  
            break  
        else:
            print(f"Invalid mood value for {day}: {mood}. Please try again.")

# Calculate percentages
print("\n--- Ur Mood Percentages per week ---")
for mood, count in mood_counts.items():
    percentage = (count / total_days) * 100
    print(f"Mood {mood_mapping[mood]} ({mood}): {percentage:.2f}%")