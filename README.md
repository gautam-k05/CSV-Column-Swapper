# CSV Column Swapper

CSV Column Swapper is a Python script that allows you to rearrange the positions of columns in a CSV file.

## Features

- Select a CSV file using a graphical user interface (GUI).
- View the columns present in the selected CSV file.
- Choose two columns to swap positions.
- Save the changes back to the original CSV file.

## Functionality

- `main()`: The main function of the script. It initializes the Tkinter root window, opens a file dialog to select a CSV file, checks if the file exists, calls the `change_columns` function to modify the file, and prints a confirmation message after changes are saved.
- `change_columns()`: This function reads the selected CSV file into a DataFrame, displays the columns present in the file, prompts the user to choose two columns to swap positions, validates the input, rearranges the columns, and saves the modified DataFrame back to the CSV file.
- `open_file_dialog()`: Opens a file dialog using Tkinter to select a CSV file. It restricts the file dialog to show only CSV files and prints the selected file path if a file is selected.

## Usage

1. Ensure you have Python 3.x installed on your system.
2. Install the required libraries using pip:
    ```bash
    pip install pandas
    ```
3. Clone this repository to your local machine.
4. Navigate to the project directory in your terminal.
5. Run the script:
    ```bash
    python csv_column_swapper.py
    ```
6. Follow the on-screen instructions to select a CSV file and swap column positions.

## Command Line Usage

The script provides an interactive command line interface. Here's how it looks:
```
$ python csv_column_swapper.py
Selected file: example.csv
Columns in this file are:
['Name', 'Age', 'Gender', 'Occupation']
Enter the first column you want to change position of: Age
Enter the column you want to change position with: Gender
Changes have been saved in the file example.csv
```