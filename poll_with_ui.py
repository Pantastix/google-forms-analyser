import csv
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk

output_file = 'answers.csv'  # Dateiname der CSV-Datei

# reading csv file
with open(output_file, 'r', encoding='utf-8') as file:
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

# Funktion zum Erstellen und Anzeigen des Tortendiagramms
def create_pie_chart(attribute):
    # Zähle die Häufigkeit jedes Wertes des gewählten Schlüssels
    values_count = {}
    for entry in data_list:
        value = entry.get(attribute, "N/A")
        if value in values_count:
            values_count[value] += 1
        else:
            values_count[value] = 1

    # Erstelle das Tortendiagramm
    plt.figure(figsize=(8, 6))
    plt.pie(values_count.values(), labels=values_count.keys(), autopct='%1.1f%%', startangle=140)
    plt.title(f'Verteilung von "{attribute}"')
    plt.axis('equal')  # Sorgt dafür, dass das Diagramm kreisförmig ist
    plt.show()

# GUI erstellen
root = tk.Tk()
root.title("Datenanalyse")

# Funktion, die aufgerufen wird, wenn ein Element ausgewählt wird
def on_select(event):
    # Finde das ausgewählte Element
    selected_item = tree.focus()
    # Extrahiere den Text des ausgewählten Elements
    attribute = tree.item(selected_item)['text']
    # Erstelle und zeige das Tortendiagramm für das ausgewählte Attribut
    create_pie_chart(attribute)

# Baumansicht (Treeview) erstellen und konfigurieren
tree = ttk.Treeview(root)
tree.bind("<<TreeviewSelect>>", on_select)
tree.pack(expand=True, fill=tk.BOTH)

# Füge die Fragen in der Reihenfolge der CSV-Datei hinzu
for key in all_keys:
    tree.insert("", "end", text=key)

root.mainloop()