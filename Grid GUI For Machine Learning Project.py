from tkinter import *
import joblib
from sklearn.datasets import load_iris
from sklearn.tree import DecisionTreeClassifier
from tkinter import messagebox

iris = load_iris()

X = iris.data
y = iris.target

model = DecisionTreeClassifier()
model.fit(X, y)

joblib.dump(model, "iris_model.joblib")

root = Tk()

root.title("Iris Flower Predictor")

root.geometry("600x200")

root.config(bg="lightblue")

header = Label(root,
               text="Iris Flower Predictor",
               bg="lightblue",
               foreground="black",
               font=("Arial", 15, "bold"))
header.pack()

frame1 = Frame(root, bg="lightblue")
frame1.pack()

label1 = Label(frame1,
               text="Sepal Length",
               bg="lightblue",
               foreground="black",
               font=("Arial", 15, "bold"))
label1.grid(row=0, column=0, pady=10)

entry1 = Entry(frame1,
               width=10,
               font=("Arial", 15, "bold"),
               bg="gray",
               fg="white",
               borderwidth=3)
entry1.grid(row=0, column=1, pady=10)
#########################################################
label2 = Label(frame1,
               text="Sepal Length",
               bg="lightblue",
               foreground="black",
               font=("Arial", 15, "bold"))
label2.grid(row=0, column=2, pady=10)

entry2 = Entry(frame1,
               width=10,
               font=("Arial", 15, "bold"),
               bg="gray",
               fg="white",
               borderwidth=3)
entry2.grid(row=0, column=3, pady=10)

################################################################
label3 = Label(frame1,
               text="Sepal Length",
               bg="lightblue",
               foreground="black",
               font=("Arial", 15, "bold"))
label3.grid(row=1, column=0, pady=10)

entry3 = Entry(frame1,
               width=10,
               font=("Arial", 15, "bold"),
               bg="gray",
               fg="white",
               borderwidth=3)
entry3.grid(row=1, column=1, pady=10)
#########################################################
label4 = Label(frame1,
               text="Sepal Length",
               bg="lightblue",
               foreground="black",
               font=("Arial", 15, "bold"))
label4.grid(row=1, column=2, pady=10)

entry4 = Entry(frame1,
               width=10,
               font=("Arial", 15, "bold"),
               bg="gray",
               fg="white",
               borderwidth=3)
entry4.grid(row=1, column=3, pady=10)
###############################################################
species_label = Label(root,
                      text="",
                      bg="lightblue",
                      font=("Arial", 15, "bold"))
species_label.pack()


def predict_species():
  model = joblib.load("iris_model.joblib")
  sepal_length = float(entry1.get())
  sepal_width = float(entry2.get())
  petal_length = float(entry3.get())
  petal_width = float(entry4.get())

  pred = model.predict([[sepal_length, sepal_width, petal_length,
                         petal_width]])
  species_label.config(text="Predicted Species: " + iris.target_names[pred[0]])


button = Button(text="Predict Species",
                bg="green",
                activebackground="blue",
                borderwidth=3,
                font=("Arial", 15, "bold"),
                command=predict_species)
button.pack()

root.mainloop()
