

total_days = 365

years = total_days // 365
remaining_days = total_days % 365

weeks = remaining_days // 7
days = remaining_days % 7

print(f"{years}y, {weeks}w, {days}d")