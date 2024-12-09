import matplotlib.pyplot as plt

kategorie = ['Żywność', 'Odzież', 'Elektronika', 'Meble', 'Książki']
sprzedane = [120, 100, 160, 50, 80]

plt.bar(kategorie, sprzedane, color='darkblue')

plt.xlabel('')
plt.ylabel('Sprzedane produkty')
plt.title('Sprzedaż w kategoriach')

plt.show()
