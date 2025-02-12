import matplotlib.pyplot as plt

day = {
    "day": ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"],
    "Temperatures": [20, 25, 22, 23, 27, 29, 30]
}
plt.figure(figsize=(10, 5))
plt.bar(day["day"], day["Temperatures"], color='skyblue')
plt.xlabel('Day')
plt.ylabel('Temperature (°C)')
plt.title('Temperature by Day of the Week')
plt.show()

plt.figure(figsize=(7, 7))
plt.pie(day["Temperatures"], labels=day["day"], autopct='%1.1f%%', startangle=140, colors=plt.cm.Paired.colors)
plt.title('Temperature Distribution Throughout the Week')
plt.axis('equal')
plt.show()