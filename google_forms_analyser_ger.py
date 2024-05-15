import csv
import matplotlib.pyplot as plt

MAX_LEGEND_TEXT_LENGTH = 30


# Function to shorten Text
def shorten_text(text, max_length=MAX_LEGEND_TEXT_LENGTH):
    if len(text) > max_length:
        return text[:max_length] + "..."
    return text


# Ask for the file path from the user
file_path = input("Geben Sie den Dateipfad der CSV-Datei ein: ")

# Read the CSV file
with open(file_path, 'r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file, delimiter=',')
    all_keys = csv_reader.fieldnames  # Get the field names in the order they appear in the CSV
    data_list = list(csv_reader)

# Display options for attributes
print("Wählen Sie eine Nummer aus, um die entsprechende Frage anzuzeigen:")
for i, key in enumerate(all_keys, 1):
    print(f"{i}. {key}")

# Select attribute to display
selection = int(input("Geben Sie die Nummer des Attributs ein, das angezeigt werden soll: "))

if 1 <= selection <= len(all_keys):
    selected_key = all_keys[selection - 1]
    print(f"\nAusgewähltes Attribut: {selected_key}\n")

    # Count occurrences of each value for the selected attribute
    values_count = {}
    for entry in data_list:
        value = entry.get(selected_key, "N/A")
        if value in values_count:
            values_count[value] += 1
        else:
            values_count[value] = 1

    # Create a pie chart
    fig, ax = plt.subplots(figsize=(8, 6))
    patches, _, _ = ax.pie(values_count.values(), labels=None, autopct='%1.1f%%', startangle=140,
                           radius=0.7)

    # Ask if a condition should be set
    condition_question = input("Möchten Sie eine Bedingung festlegen? (ja/nein): ").lower()
    if condition_question == "ja" or condition_question == "j":
        # Choose a condition question
        print("Wählen Sie eine Nummer, um die Bedingungsfrage auszuwählen, oder 0 für keine Bedingung:")
        for i, key in enumerate(all_keys, 1):
            if key != selected_key:  # Skip the already selected question
                print(f"{i}. {key}")

        condition_selection = int(input("Geben Sie die Nummer der Bedingungsfrage ein: "))
        if 0 <= condition_selection <= len(all_keys) and (all_keys[condition_selection - 1] != selected_key):

            condition_key = all_keys[condition_selection - 1]
            print(f"\nAusgewählte Bedingungsfrage: {condition_key}\n")

            print(f"Optionen für die Frage '{condition_key}':")
            condition_values = []
            for i, entry in enumerate(data_list, 1):
                value = entry.get(condition_key, "N/A")
                if value not in condition_values:
                    condition_values.append(value)
                    print(f"{len(condition_values)}. {value}")

            condition_input = input("Geben Sie die Nummern der Optionen durch Kommas getrennt ein: ")
            selected_conditions = [condition_values[int(i) - 1] for i in condition_input.split(',') if
                                   0 < int(i) <= len(condition_values)]

            # Filter data based on condition
            filtered_data = [entry for entry in data_list if entry.get(condition_key, "N/A") in selected_conditions]

            values_count = {}
            for entry in filtered_data:
                value = entry.get(selected_key, "N/A")
                if value in values_count:
                    values_count[value] += 1
                else:
                    values_count[value] = 1

            # Set title for the plot
            ax.set_title(
                f'Verteilung von "{selected_key}"\nbei "{condition_key}\nin "{", ".join(selected_conditions)}"')

            # Create custom legend with questions and answers
            legend_texts = [f"{shorten_text(key)}: {value}" for key, value in values_count.items()]
            ax.legend(handles=patches, labels=legend_texts, loc="lower right", fontsize='small')

            plt.axis('equal')
            plt.tight_layout()
            plt.show()

            # Print votes count for each option under the condition
            print("\nStimmenzahl für jede Option unter der Bedingung:")
            for key, value in values_count.items():
                print(f"{key}: {value}")

        else:
            print("Ungültige Auswahl für die Bedingungsfrage!")

    elif condition_question == "nein" or condition_question == "n":
        # Set title for the plot
        ax.set_title(selected_key)

        # Create custom legend with questions and answers
        legend_texts = [f"{shorten_text(key)}: {value}" for key, value in values_count.items()]
        ax.legend(handles=patches, labels=legend_texts, loc="lower right", fontsize='small')

        plt.axis('equal')
        plt.tight_layout()
        plt.show()

        # Print votes count for each option
        print("\nStimmenzahl für jede Option:")
        for key, value in values_count.items():
            print(f"{key}: {value}")

    else:
        print("Invalid input for the condition!")

else:
    print("Invalid selection!")
