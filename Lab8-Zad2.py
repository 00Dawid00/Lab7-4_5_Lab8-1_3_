import matplotlib.pyplot as plt

kategorie = ['Żywność', 'Odzież', 'Elektronika', 'Meble', 'Książki']
sprzedane = [120, 100, 160, 50, 80]

plt.figure(figsize=(8, 8))
plt.pie(
    sprzedane,
    labels=kategorie,
    autopct='%1.1f%%',
    startangle=90,
    colors=['gold', 'green', 'red', 'brown', 'violet']
)

plt.title('Procentowy udział kategorii w sprzedaży')
plt.show()
