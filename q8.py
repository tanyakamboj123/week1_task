from datetime import date, timedelta

start = date(1985, 6, 28)
end = date(2009, 3, 27)

delta = timedelta(days=1)
weekend_count = 0

while start <= end:
    if start.weekday() in (5, 6):  # 5 = Saturday, 6 = Sunday
        weekend_count += 1
    start += delta

print("Total weekend days:", weekend_count)
