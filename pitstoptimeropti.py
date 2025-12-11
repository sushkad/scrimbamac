# 🏁 Pit Stop Timing Optimizer 🔧
#
# 1. Ask the user for the total race time in seconds.
# 2. Ask how many pit stops were made.
# 3. Ask for the average pit stop duration (in seconds).
#
# Then:
# - Calculate the total pit stop time.
# - Calculate the percentage of the race spent in the pits.
# - Round the percentage to 2 decimal places.
#
# Finally, print all of the following:
# - Total pit stop time in seconds
# - Percentage of race time spent in pits
# - A final message if pit time > 5% of the race: "You need a new pit crew. 🛠️"




total_race = float(input("Enter total race: "))
num_pitstop = int(input("Enter pitstop: "))
avg_pit_duration = float(input("Enter avg duration: "))

# calculate total pit time

total_pit_time = num_pitstop * avg_pit_duration

# calculate pit time per %

pit_percentage =  (total_pit_time / total_race)  * 100
pit_percentage = round(pit_percentage, 2)


# print result
print("\n--- pit stop summary ---")
print(f"total pit stop time: {total_pit_time} seconds")
print(f"pit percentage: {pit_percentage} %")

if pit_percentage > 5:
    print(" You need a new pit crew. ")