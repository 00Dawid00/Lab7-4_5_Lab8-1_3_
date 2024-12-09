import pandas as pd

dane_studenci = {
    'Nr_albumu': [1, 2, 3, 4, 5],
    'Imię': ['Anna', 'Jan', 'Katarzyna', 'Tomasz', 'Michał'],
    'Nazwisko': ['Kowalska', 'Nowak', 'Wiśniewska', 'Kaczmarek', 'Zieliński'],
    'Ocena': [4.5, 3.0, 5.0, 4.0, 2.5],
    'Wiek': [22, 21, 24, 23, 25],
}

df_studenci = pd.DataFrame(dane_studenci)

#A
studenci_ocena_over_4 = df_studenci[df_studenci['Ocena'] > 4]
print("\nStudenci z oceną wyższą niż 4:")
print(studenci_ocena_over_4)

#B
studenci_posortowani_wiek = df_studenci.sort_values(by='Wiek')
print("\nStudenci posortowani według wieku:")
print(studenci_posortowani_wiek)

#C
srednia_wiek_oceny = df_studenci.groupby("Ocena")["Wiek"].mean()
print("\nŚrednia wieku dla poszczególnych ocen:")
print(srednia_wiek_oceny)

#D
dane_poprawa = {
    'Nr_albumu': [1, 5],
    'Ocena_poprawa': [5.0, 3.0],
}

df_poprawa = pd.DataFrame(dane_poprawa)

df_polaczone = pd.merge(df_studenci, df_poprawa, on="Nr_albumu", how="left")

print("\nPołączona ramka danych:")
print(df_polaczone)

#E
file_path = "studenci.csv"
df_polaczone.to_csv(file_path, index=False)

#F
wczytywanie_dane = pd.read_csv(file_path)
print("\nDane wczytane z pliku CSV:")
print(wczytywanie_dane)

#G
nowy_student = {
    'Nr_albumu': 6,
    'Imię': 'Krzysztof',
    'Nazwisko': 'Kononowicz',
    'Ocena': 4.0,
    'Wiek': 22,
}

df_nowy_student = pd.DataFrame([nowy_student])
df_studenci = pd.concat([df_studenci, df_nowy_student], ignore_index=True)

print("\nDataFrame po dodaniu nowego studenta:")
print(df_studenci)

#H
unikalne_oceny = df_studenci['Ocena'].unique()
print("\nUnikalne wartości w kolumnie Ocena:")
print(unikalne_oceny)

#I
studenci_ocena_5 = df_studenci[df_studenci['Ocena'] == 5]
liczba_studentow_ocena_5 = studenci_ocena_5.shape[0]

print("\nLiczba studentów z oceną równą 5:")
print(liczba_studentow_ocena_5)