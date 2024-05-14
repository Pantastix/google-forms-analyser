import csv
import matplotlib.pyplot as plt

MAX_LEGEND_TEXT_LENGTH = 30


# Funktion zum Kürzen von Text
def shorten_text(text, max_length=MAX_LEGEND_TEXT_LENGTH):
    if len(text) > max_length:
        return text[:max_length] + "..."
    return text


# Ask for the file path from the user
file_path = input("Enter the file path of the CSV file: ")

# Read the CSV file
with open(file_path, 'r', encoding='utf-8') as file:
    csv_reader = csv.DictReader(file, delimiter=',')

    data_list = []

    for row in csv_reader:
        data_list.append(row)

all_keys = list(set().union(*(d.keys() for d in data_list)))

print("Select a number to display the corresponding question:")
for i, key in enumerate(all_keys, 1):
    print(f"{i}. {key}")

selection = int(input("Enter the number of the attribute to display: "))

if 1 <= selection <= len(all_keys):
    selected_key = all_keys[selection - 1]
    print(f"\nSelected attribute: {selected_key}\n")

    values_count = {}
    for entry in data_list:
        value = entry.get(selected_key, "N/A")
        if value in values_count:
            values_count[value] += 1
        else:
            values_count[value] = 1

    plt.figure(figsize=(8, 6))
    patches, texts, autotexts = plt.pie(values_count.values(), labels=values_count.keys(), autopct='%1.1f%%',
                                        startangle=140)

    # Ask for a condition
    condition_question = input("Would you like to set a condition? (yes/no): ").lower()
    if condition_question == "yes" or condition_question == "y":
        # Choose a condition question
        print("Select a number to choose the condition question, or 0 for no condition:")
        for i, key in enumerate(all_keys, 1):
            if key != selected_key:  # Skip the already selected question
                print(f"{i}. {key}")
        print("0. No condition")

        condition_selection = int(input("Enter the number of the condition question: "))
        if 0 <= condition_selection <= len(all_keys) and (all_keys[condition_selection - 1] != selected_key):

            condition_key = all_keys[condition_selection - 1]
            print(f"\nSelected condition question: {condition_key}\n")

            print(f"Options for the question '{condition_key}':")
            condition_values = []
            for i, entry in enumerate(data_list, 1):
                value = entry.get(condition_key, "N/A")
                if value not in condition_values:
                    condition_values.append(value)
                    print(f"{len(condition_values)}. {value}")

            condition_input = input("Enter the numbers of the options separated by commas: ")
            selected_conditions = [condition_values[int(i) - 1] for i in condition_input.split(',') if
                                   0 < int(i) <= len(condition_values)]

            filtered_data = [entry for entry in data_list if entry.get(condition_key, "N/A") in selected_conditions]

            values_count = {}
            for entry in filtered_data:
                value = entry.get(selected_key, "N/A")
                if value in values_count:
                    values_count[value] += 1
                else:
                    values_count[value] = 1

            fig, ax = plt.subplots(figsize=(8, 6))
            patches, _, _ = ax.pie(values_count.values(), labels=None, autopct='%1.1f%%', startangle=140,
                               radius=0.7)  # Remove labels and reduce radius

            ax.set_title(
                f'Distribution of "{selected_key}"\nwhere "{condition_key}\nin "{", ".join(selected_conditions)}"')

            # Create custom legend with questions and answers
            legend_texts = [f"{shorten_text(key)}: {value}" for key, value in values_count.items()]
            ax.legend(handles=patches, labels=legend_texts, loc="lower right", fontsize='small')

            plt.axis('equal')
            plt.tight_layout()
            plt.show()

            print("\nVotes count for each option under the condition:")
            for key, value in values_count.items():
                print(f"{key}: {value}")

        else:
            print("Invalid selection for the condition question!")

    elif condition_question == "no" or condition_question == "n":

        fig, ax = plt.subplots(figsize=(8, 6))
        patches, _, _ = ax.pie(values_count.values(), labels=None, autopct='%1.1f%%', startangle=140,
                               radius=0.7)  # Remove labels and reduce radius
        ax.set_title(selected_key)

        # Create custom legend with questions and answers
        legend_texts = [f"{shorten_text(key)}: {value}" for key, value in values_count.items()]
        ax.legend(handles=patches, labels=legend_texts, loc="lower right", fontsize='small')

        plt.axis('equal')
        plt.tight_layout()
        plt.show()

        print("\nVotes count for each option:")
        for key, value in values_count.items():
            print(f"{key}: {value}")

    else:
        print("Invalid input for the condition!")

else:
    print("Invalid selection!")
