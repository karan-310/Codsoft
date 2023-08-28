import tkinter as tk

class CalculatorApp:
    def __init__(self, root):
        self.root = root
        root.title("Calculator")

        self.result_var = tk.StringVar()
        self.result_var.set("0")

        self.entry = tk.Entry(root, textvariable=self.result_var, justify="right", font=("Helvetica", 18))
        self.entry.grid(row=0, column=0, columnspan=4)

        buttons = [
            ('7', 1, 0), ('8', 1, 1), ('9', 1, 2), ('/', 1, 3),
            ('4', 2, 0), ('5', 2, 1), ('6', 2, 2), ('*', 2, 3),
            ('1', 3, 0), ('2', 3, 1), ('3', 3, 2), ('-', 3, 3),
            ('0', 4, 0), ('.', 4, 1), ('=', 4, 2), ('+', 4, 3),
        ]

        for (text, row, column) in buttons:
            button = tk.Button(root, text=text, font=("Helvetica", 16), command=lambda t=text: self.on_button_click(t))
            button.grid(row=row, column=column, sticky='nsew')

        for i in range(5):
            root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)

    def on_button_click(self, char):
        if char == "=":
            try:
                result = eval(self.result_var.get())
                self.result_var.set(result)
            except Exception as e:
                self.result_var.set("Error")
        else:
            current_text = self.result_var.get()
            if current_text == "0" and char != ".":
                self.result_var.set(char)
            else:
                self.result_var.set(current_text + char)

if __name__ == "__main__":
    root = tk.Tk()
    app = CalculatorApp(root)
    root.mainloop()
