import matplotlib.pyplot as plt

czas = [0, 2, 4, 6, 8, 10, 12, 14, 16, 18, 20]
predkosc = [0, 10, 25, 40, 50, 55, 53, 50, 47, 45, 40]

plt.scatter(czas, predkosc, color='blue', label='Prędkość chwilowa')

plt.xlabel('Czas (sekundy)')
plt.ylabel('Prędkość (km/h)')
plt.title('Prędkość chwilowa pojazdu w czasie')
plt.legend()

plt.show()
