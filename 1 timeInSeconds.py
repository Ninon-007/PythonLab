total_seconds = int(input("Enter the time in seconds: "))

hours = total_seconds // 3600
remaining_seconds = total_seconds % 3600
minutes = remaining_seconds // 60
seconds = remaining_seconds % 60

print(f'HH:MM:SS :- {hours:02d}:{minutes:02d}:{seconds:02d}')
print('Levi')
