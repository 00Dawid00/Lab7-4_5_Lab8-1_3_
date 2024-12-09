import pandas as pd

dane_pracownicy = {
    'Numer ID': [1, 2, 3, 4, 5],
    'Imię': ['Anna', 'Jan', 'Katarzyna', 'Tomasz', 'Michał'],
    'Nazwisko': ['Kowalska', 'Nowak', 'Wiśniewska', 'Kaczmarek', 'Zieliński'],
    'Stanowisko': ['Manager', 'Programista', 'Konsultant', 'Programista', 'Manager'],
    'Wiek': [35, 28, 40, 30, 45],
    'Pensja': [8000, 4500, 6000, 5500, 7000]
}

df = pd.DataFrame(dane_pracownicy)

print("Dane o pracownikach:")
print(df)

#A
pracownicy_pensja_over_5000 = df[df['Pensja'] > 5000]
print("\nPracownicy z pensją większą niż 5000 PLN:")
print(pracownicy_pensja_over_5000)

#B
pracownicy_posortowani_wiek = df.sort_values(by='Wiek')
print("\nPracownicy posortowani według wieku:")
print(pracownicy_posortowani_wiek)

#C
srednia_pensja = df.groupby("Stanowisko")["Pensja"].mean()
print("\nŚrednia pensja według stanowiska:")
print(srednia_pensja)

#D
dane_awans = {
    "Numer ID": [2, 4],
    "Nowe Stanowisko": ["Senior Programista", "Kierownik Projektu"],
}
awans = pd.DataFrame(dane_awans)

polaczenie = pd.merge(df, awans, on="Numer ID", how="left")

print("\nPołączona ramka danych z informacją o aktualnym i nowym stanowisku:")
print(polaczenie)

#E
file_path = "pracownicy.csv"
polaczenie.to_csv(file_path, index=False)

#F
wczytywanie_dane = pd.read_csv(file_path)
print("\nDane wczytane z pliku CSV:")
print(wczytywanie_dane)
