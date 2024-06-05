import pandas as pd
import os
import tkinter as tk
from tkinter import filedialog


def main():
    root = tk.Tk()
    root.withdraw()  # Hide the root window
    file_name = open_file_dialog()  # Open file dialog to select a CSV file
    if os.path.isfile(file_name):  # Check if the selected file exists
        change_columns(file_name)  # Call function to change column positions
        file_base_name = os.path.basename(file_name)  # Get just the file name
        print(f"Changes have been saved in the file {file_base_name}")
    else:
        print("Invalid file")


def change_columns(file_name):
    df = pd.read_csv(file_name)  # Read the CSV file into a DataFrame
    cols = list(df.columns)  # Get the list of columns in the DataFrame
    print(f"Columns in this file are: \n{cols}")
    
    while True:
        col1 = input("Enter the first column you want to change position of: ")
        col2 = input("Enter the column you want to change position with: ")
        if col1 not in cols or col2 not in cols:  # Validate column names
            print("Invalid column names, check and try again")
        else:
            break
  
    index1, index2 = cols.index(col1), cols.index(col2)  # Find indices of the columns
    if index2 > index1:
        # Rearrange columns if the second column is after the first column
        df = df[cols[:index1] + [cols[index2]] + cols[index1+1:index2] + [cols[index1]] + cols[index2+1:]]
    else:
        # Rearrange columns if the first column is after the second column
        df = df[cols[:index2] + [cols[index1]] + cols[index2+1:index1] + [cols[index2]] + cols[index1+1:]]
    
    df.to_csv(file_name, index=False)  # Save the modified DataFrame back to the CSV file


def open_file_dialog():
    filetypes = [('CSV Files', '*.csv')]  # Restrict file dialog to CSV files
    file = filedialog.askopenfilename(filetypes=filetypes)  # Open file dialog
    if file:
        print(f"Selected file: {file}")  # Print the selected file path
    return file      


if __name__ == "__main__":
    main()  # Run the main function