import csv
import matplotlib.pyplot as plt

# Abfrage des Dateipfads von Benutzer
file_path = input("Please paste the file path: ")

# reading csv file
with open(file_path, 'r', encoding='utf-8') as file:
    # creating a csv reader object mit dem Semikolon als Trennzeichen
    csv_reader = csv.DictReader(file, delimiter=',')

    # Initialize an empty list to store the dictionaries
    data_list = []

    # Iterate through each row in the CSV file
    for row in csv_reader:
        # Append each row (as a dictionary) to the list
        data_list.append(row)

# Extrahiere alle Schlüssel
all_keys = list(set().union(*(d.keys() for d in data_list)))

# Gib die nummerierte Liste der Schlüssel aus
print("Wähle eine Nummer aus, um das entsprechende Attribut anzuzeigen:")
for i, key in enumerate(all_keys, 1):
    print(f"{i}. {key}")

# Benutzer wählt die Nummer des Attributs
selection = int(input("Nummer des zu anzeigenden Attributs eingeben: "))

# Überprüfe, ob die Auswahl gültig ist
if 1 <= selection <= len(all_keys):
    selected_key = all_keys[selection - 1]
    print(f"\nGewähltes Attribut: {selected_key}\n")

    # Zähle die Häufigkeit jedes Wertes des gewählten Schlüssels
    values_count = {}
    for entry in data_list:
        value = entry.get(selected_key, "N/A")
        if value in values_count:
            values_count[value] += 1
        else:
            values_count[value] = 1

    # Erstelle das Tortendiagramm
    plt.figure(figsize=(8, 6))
    plt.pie(values_count.values(), labels=values_count.keys(), autopct='%1.1f%%', startangle=140)
    plt.title(f'Verteilung von "{selected_key}"')
    plt.axis('equal')  # Sorgt dafür, dass das Diagramm kreisförmig ist
    plt.show()

else:
    print("Ungültige Auswahl!")

#TODO: Abfrage welche bedingung erfüllt sein muss
#TODO: kann auch 0 sein dann keine Bedingung