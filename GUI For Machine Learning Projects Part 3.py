import tkinter as tk
from tkinter import filedialog
import pandas as pd
import joblib
from tkinter import messagebox


def open_file():
  filepath = filedialog.askopenfile(filetypes=[("CSV Files", ".csv")])
  if filepath:
    try:
      data = pd.read_csv(filepath, header=None)
      process_data(data)
    except Exception as e:
      messagebox.showerror("Error", f"Failed to open file {e}")


def process_data(data):
  model = joblib.load("rock_mine_prediction_model")
  y_pred = model.predict(data)
  data['Predicted_target'] = y_pred
  save_file(data)


def save_file(data):
  savepath = filedialog.asksaveasfilename(defaultextension=".csv",
                                          filetypes=[("CSV Files", ".csv")])
  if savepath:
    try:
      data.to_csv(savepath)
      messagebox.showinfo("Success", "File Saved Successfully")
    except Exception as e:
      messagebox.showerror("Error", f"Failed to save file:{e}")


# Create a Tkinter GUI

root = tk.Tk()

root.title("Classification")

root.geometry("200x200")

# Create a button to open a file
button1 = tk.Button(root,
                    text="Open CSV File",
                    width=15,
                    height=2,
                    background="lightgreen",
                    activebackground="lightblue",
                    font=("Arial", 11, "bold"),
                    command=open_file)

button1.pack(pady=50)

root.mainloop()