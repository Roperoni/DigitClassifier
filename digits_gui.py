import matplotlib
from tkinter import *
from tkinter import ttk
matplotlib.use("TkAgg")
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
import matplotlib.pyplot as plt

# Importing stuff I've written
import classifier

class GUI(object):

    def __init__(self):
        self.classifier = classifier.Classifier()
        root = Tk()
        root.title("Random Digit Display")
        mainframe = ttk.Frame(root, padding="3 3 12 12")



        mainframe.grid(column=0, row=0, sticky=(N, W, S, E))
        root.columnconfigure(0, weight=1)
        root.rowconfigure(0, weight=1)

        self.gold_display = StringVar()
        self.predicted_display = StringVar()

        self.fig = plt.figure()
        self.canvas = FigureCanvasTkAgg(self.fig, mainframe)


        ttk.Label(mainframe, textvariable=self.gold_display).grid(column=1, row=3, sticky=(N, W))
        ttk.Label(mainframe, textvariable=self.predicted_display).grid(column=1, row=2, sticky=(N, W))

        self.canvas.get_tk_widget().grid(column=1, row=4)

        button = ttk.Button(mainframe, text="Show Digit", command=self.show_random_digit)
        button.grid(column=0, row=1, sticky=(N))
        button.focus()
        root.bind('<Return>', self.show_random_digit)
        root.mainloop()
    # def calculate(self, *args):
    #     try:
    #         value = float(self.feet.get())
    #         self.meters.set((0.3048 * value * 10000.0 + 0.5)/10000.0)
    #     except ValueError:
    #         pass


    def show_random_digit(self, *args):
        # has to get a figure from the classifier, add it to canvas
        image_data, gold_label, predicted_label = self.classifier.get_random_digit()

        plt.imshow(image_data, cmap=plt.get_cmap('gray'))
        self.canvas.draw()
        self.gold_display.set(gold_label)
        self.predicted_display.set(predicted_label[0])
        return
        # ttk.Label(mainframe, textvariable=self.meters).grid(column=2, row=2, sticky=(W, E))
        # ttk.Button(mainframe, text="Calculate", command=self.calculate).grid(column=3, row=3, sticky=W)
        #
        # ttk.Label(mainframe, text="feet").grid(column=3, row=1, sticky=W)
        # ttk.Label(mainframe, text="is equivalent to").grid(column=1, row=2, sticky=E)
        # ttk.Label(mainframe, text="meters").grid(column=3, row=2, sticky=W)

if __name__ == "__main__":
    GUI()
