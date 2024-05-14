# Google Forms Poll Analysis Tool

The Google Forms Poll Analysis Tool is a command-line utility designed to assist users in analyzing poll data collected via Google Forms. This tool allows users to visualize the distribution of responses to various questions, both overall and under specific conditions.

### How It Works

1. **Input CSV Data**: The tool begins by prompting the user to input the file path of the CSV file containing the poll data exported from Google Forms.

2. **Select Attribute**: After reading the CSV file, the user is presented with a list of attributes (questions) present in the dataset. The user selects the attribute they want to analyze.

3. **Pie Chart Visualization**: The tool generates a pie chart illustrating the distribution of responses for the selected attribute. Each slice of the pie represents a response option, and the size of each slice corresponds to the percentage of respondents who chose that option.

4. **Conditional Analysis**: The user has the option to set a condition for further analysis. They can choose another attribute as a condition, and then specify one or more response options for that attribute. The tool then filters the data based on the selected condition and updates the pie chart to display the distribution of responses under that condition.

5. **Legend**: The pie chart includes a legend that provides a concise overview of the response options and their corresponding counts. If the legend text is too long, it is automatically truncated to maintain readability.

6. **Interactive Interface**: The tool interacts with the user through a series of prompts and input requests, guiding them through the process of selecting attributes, setting conditions, and interpreting the results.

7. **Output**: Alongside the visualization, the tool also displays the vote count for each response option, allowing users to analyze the data more thoroughly.

### Features

- **Dynamic Visualization**: Users can dynamically explore and visualize poll data, gaining insights into respondent preferences and trends.
- **Conditional Analysis**: Users can perform conditional analysis to understand how responses vary under different conditions or demographics.
- **Detailed Legend**: The legend in the pie chart provides detailed information about response options, ensuring clarity and understanding.
- **Automated Truncation**: Text in the legend is automatically truncated to prevent overcrowding and maintain readability in the visualization.
- **Error Handling**: The tool includes error handling mechanisms to guide users and prevent invalid inputs, ensuring a smooth user experience.

### Usage

1. **Input File**: Provide the file path of the CSV file containing poll data exported from Google Forms when prompted.
2. **Attribute Selection**: Choose the attribute (question) you want to analyze by selecting the corresponding number.
3. **Conditional Analysis**: Optionally set a condition by selecting another attribute and specifying response options.
4. **Visualization**: View the pie chart visualization of response distributions, both overall and under the specified condition.
5. **Legend**: Refer to the legend for detailed information about response options and their counts.
6. **Interpretation**: Analyze the results and gain insights into respondent behavior and preferences.

### Dependencies

- Python 3.x
- matplotlib library

### Getting Started <a href="https://github.com/Pantastix/google-forms-analyser/releases/tag/1.0.0"><img src="https://img.shields.io/github/downloads/Pantastix/google-forms-analyser/total?label=Download" /></a>

1. **Download the Executable**: Download the executable file of the Google Forms Poll Analysis Tool from the repository or the provided source.

2. **Run the Executable**: Simply double-click the executable file to run the tool. Since it's in the form of an .exe file, there's no need to have Python installed on your system.

3. **Follow the Instructions**: The tool will guide you through the process via prompts and input requests. Input the file path of the CSV file containing your Google Forms poll data when prompted.

4. **Explore and Analyze**: Once the tool loads the data, follow the prompts to select attributes, set conditions, and visualize the poll data. Gain insights into respondent behavior and preferences.

By providing the tool in the form of an executable file, users can easily run it without the need for any additional installations or dependencies. Enjoy analyzing your Google Forms poll data effortlessly!

### Contributing
Contributions are welcome! Feel free to submit bug reports, feature requests, or pull requests to enhance the tool's functionality and usability.

### Acknowledgments
- Special thanks to the contributors and maintainers of the matplotlib library for providing powerful data visualization tools.
- Inspired by the need for simple yet effective tools for analyzing poll and survey data collected via Google Forms.
