# data files

with open("weather_data.csv") as csv:
    contents = [n.strip() for n in csv.readlines()][1:]

all_days = []

for item in contents:
    day, celsius, weather = item.split(',')
    all_days.append({"day": day, "degrees": celsius, "weather": weather})

for item in all_days:
    print(item)