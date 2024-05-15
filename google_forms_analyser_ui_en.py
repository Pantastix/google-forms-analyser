import csv
import matplotlib.pyplot as plt
import tkinter as tk
from tkinter import ttk
from tkinterdnd2 import DND_FILES, TkinterDnD

MAX_LEGEND_TEXT_LENGTH = 50


# Function to shorten text
def shorten_text(text, max_length=MAX_LEGEND_TEXT_LENGTH):
    if len(text) > max_length:
        return text[:max_length] + "..."
    return text


# Function to process the dropped file
def process_file(file_path):
    file_path = file_path.strip("{}")  # Remove curly braces from path
    with open(file_path, 'r', encoding='utf-8') as file:
        csv_reader = csv.DictReader(file, delimiter=',')

        global data_list, all_keys
        data_list = [row for row in csv_reader]
        all_keys = csv_reader.fieldnames  # Preserve the order of keys as in the CSV file

    # Close the file selection window
    root.destroy()

    # Open the main application window
    open_main_window()


def open_main_window():
    def update_dependencies(*args):
        selected_question = question_listbox.get(tk.ACTIVE)
        dependency_menu['menu'].delete(0, 'end')
        for key in all_keys:
            if key != selected_question:  # Skip the already selected question
                dependency_menu['menu'].add_command(label=key, command=tk._setit(dependency_var, key))
        dependency_var.set("No dependency selected")
        for checkbox in checkboxes:
            checkbox.pack_forget()
        checkboxes.clear()

    def update_checkboxes(*args):
        selected_dependency = dependency_var.get()
        for checkbox in checkboxes:
            checkbox.pack_forget()
        checkboxes.clear()

        if selected_dependency != "No dependency selected":
            unique_values = list({entry.get(selected_dependency, "N/A") for entry in data_list})
            for value in unique_values:
                var = tk.BooleanVar()
                checkbox = tk.Checkbutton(right_frame, text=value, variable=var)
                checkbox.var = var
                checkbox.pack(anchor='w')
                checkboxes.append(checkbox)

    def generate_plot():
        selected_question = question_listbox.get(tk.ACTIVE)
        selected_dependency = dependency_var.get()
        selected_conditions = [cb.cget('text') for cb in checkboxes if cb.var.get()]

        values_count = {}
        if selected_dependency == "No dependency selected":
            for entry in data_list:
                value = entry.get(selected_question, "N/A")
                if value in values_count:
                    values_count[value] += 1
                else:
                    values_count[value] = 1
        else:
            filtered_data = [entry for entry in data_list if entry.get(selected_dependency, "N/A") in selected_conditions]
            for entry in filtered_data:
                value = entry.get(selected_question, "N/A")
                if value in values_count:
                    values_count[value] += 1
                else:
                    values_count[value] = 1

        fig, ax = plt.subplots(figsize=(8, 6))
        patches, _, _ = ax.pie(values_count.values(), labels=None, autopct='%1.1f%%', startangle=140, radius=0.7)

        if selected_dependency == "No dependency selected":
            ax.set_title(selected_question)
        else:
            ax.set_title(f'Distribution of "{selected_question}"\nwith "{selected_dependency}"\nin "{", ".join(selected_conditions)}"')

        legend_texts = [f"{shorten_text(key)}: {value}" for key, value in values_count.items()]
        ax.legend(handles=patches, labels=legend_texts, loc="lower right", fontsize='small')

        plt.axis('equal')
        plt.tight_layout()
        plt.show()

    main_root = tk.Tk()
    main_root.title("Google Forms-Analysis Tool")
    main_root.geometry("800x600")  # Set the size of the main window

    # Frame for the left side (questions list)
    left_frame = tk.Frame(main_root)
    left_frame.pack(side=tk.LEFT, fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Frame for the right side (dependencies and checkboxes)
    right_frame = tk.Frame(main_root)
    right_frame.pack(side=tk.RIGHT, fill=tk.BOTH, expand=True, padx=10, pady=10)

    # Listbox for the questions with wrapping
    question_listbox = tk.Listbox(left_frame, selectmode=tk.SINGLE, width=40, height=25)
    question_listbox.pack(fill=tk.BOTH, expand=True)
    question_listbox.bind('<<ListboxSelect>>', update_dependencies)

    # Dropdown menu for dependencies
    dependency_var = tk.StringVar()
    dependency_var.set("No dependency selected")
    dependency_var.trace('w', update_checkboxes)
    dependency_menu = ttk.OptionMenu(right_frame, dependency_var, "No dependency selected")
    dependency_menu.pack()

    # Checkbuttons for conditions
    checkboxes = []

    # Button to generate plot
    generate_button = tk.Button(right_frame, text="Generate", command=generate_plot)
    generate_button.pack(side=tk.BOTTOM, pady=10)

    # Populate the question listbox
    for key in all_keys:
        question_listbox.insert(tk.END, key)

    main_root.mainloop()


# Create the file selection window
root = TkinterDnD.Tk()
root.title("Select CSV File")
root.geometry("600x400")  # Set the size of the file selection window

# Create and place a label that provides instructions to the user
label = tk.Label(root, text="Drag your CSV file here", width=40, height=10)
label.pack(padx=10, pady=10)

# Enable the window to accept files
root.drop_target_register(DND_FILES)
root.dnd_bind('<<Drop>>', lambda event: process_file(event.data))

# Run the file selection window
root.mainloop()
