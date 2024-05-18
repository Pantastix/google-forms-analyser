import csv
from collections import defaultdict

# Ask for the file path from the user
# file_path = input("Geben Sie den Dateipfad der CSV-Datei ein: ")
file_path = "./answers.csv"

# Read the CSV file
with open(file_path, 'r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file, delimiter=',')
    all_keys = csv_reader.fieldnames  # Get the field names in the order they appear in the CSV
    data_list = list(csv_reader)

# Aggregierte Antworten zählen
aggregated_data = defaultdict(lambda: defaultdict(int))

for response in data_list:
    for question, answer in response.items():
        aggregated_data[question][answer] += 1

# LaTeX-kompatible Ausgabe erstellen
latex_output = []

for question, answers in aggregated_data.items():
    latex_output.append(f"Frage: {question}")
    latex_output.append("\\begin{itemize}")
    for answer, count in answers.items():
        latex_output.append(f"    \\item Antwort: {answer} - Anzahl an Antworten: {count}")
    latex_output.append("\\end{itemize}")
    latex_output.append("\\noindent")
    latex_output.append("")  # Leerzeile für bessere Lesbarkeit

# Ausgabe in einer LaTeX-kompatiblen Form
latex_output_str = "\n".join(latex_output)
print(latex_output_str)

# Optional: Ausgabe in eine Datei schreiben
with open('output.txt', 'w') as file:
    file.write(latex_output_str)