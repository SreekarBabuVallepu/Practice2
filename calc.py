import tkinter as tk
from tkinter import ttk
import math
import numpy as np

class EngineeringCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Engineering Calculator")
        self.root.geometry("400x600")
        self.root.configure(bg='#f0f0f0')
        
        # Style configuration
        style = ttk.Style()
        style.configure('TButton', padding=5, font=('Arial', 10))
        style.configure('TEntry', padding=5, font=('Arial', 12))
        
        # Display
        self.display = ttk.Entry(root, justify='right', font=('Arial', 20))
        self.display.grid(row=0, column=0, columnspan=4, padx=10, pady=10, sticky='nsew')
        
        # Buttons
        self.create_buttons()
        
        # Configure grid weights
        for i in range(8):
            root.grid_rowconfigure(i, weight=1)
        for i in range(4):
            root.grid_columnconfigure(i, weight=1)
            
    def create_buttons(self):
        # Scientific functions
        scientific_buttons = [
            ('sin', lambda: self.scientific_operation(math.sin)),
            ('cos', lambda: self.scientific_operation(math.cos)),
            ('tan', lambda: self.scientific_operation(math.tan)),
            ('√', lambda: self.scientific_operation(math.sqrt)),
            ('log', lambda: self.scientific_operation(math.log10)),
            ('ln', lambda: self.scientific_operation(math.log)),
            ('x²', lambda: self.scientific_operation(lambda x: x**2)),
            ('x³', lambda: self.scientific_operation(lambda x: x**3)),
            ('π', lambda: self.insert_constant(math.pi)),
            ('e', lambda: self.insert_constant(math.e)),
            ('(', lambda: self.insert_char('(')),
            (')', lambda: self.insert_char(')')),
        ]
        
        # Regular calculator buttons
        regular_buttons = [
            ('7', lambda: self.insert_char('7')),
            ('8', lambda: self.insert_char('8')),
            ('9', lambda: self.insert_char('9')),
            ('/', lambda: self.insert_char('/')),
            ('4', lambda: self.insert_char('4')),
            ('5', lambda: self.insert_char('5')),
            ('6', lambda: self.insert_char('6')),
            ('*', lambda: self.insert_char('*')),
            ('1', lambda: self.insert_char('1')),
            ('2', lambda: self.insert_char('2')),
            ('3', lambda: self.insert_char('3')),
            ('-', lambda: self.insert_char('-')),
            ('0', lambda: self.insert_char('0')),
            ('.', lambda: self.insert_char('.')),
            ('=', self.calculate),
            ('+', lambda: self.insert_char('+')),
            ('C', self.clear),
            ('⌫', self.backspace),
            ('±', self.negate),
            ('%', self.percentage),
        ]
        
        # Place scientific buttons
        row = 1
        col = 0
        for (text, command) in scientific_buttons:
            btn = ttk.Button(self.root, text=text, command=command)
            btn.grid(row=row, column=col, padx=2, pady=2, sticky='nsew')
            col += 1
            if col > 3:
                col = 0
                row += 1
        
        # Place regular buttons
        for (text, command) in regular_buttons:
            btn = ttk.Button(self.root, text=text, command=command)
            btn.grid(row=row, column=col, padx=2, pady=2, sticky='nsew')
            col += 1
            if col > 3:
                col = 0
                row += 1
    
    def insert_char(self, char):
        current = self.display.get()
        self.display.delete(0, tk.END)
        self.display.insert(0, current + char)
    
    def insert_constant(self, value):
        self.display.delete(0, tk.END)
        self.display.insert(0, str(value))
    
    def clear(self):
        self.display.delete(0, tk.END)
    
    def backspace(self):
        current = self.display.get()
        self.display.delete(0, tk.END)
        self.display.insert(0, current[:-1])
    
    def negate(self):
        try:
            current = float(self.display.get())
            self.display.delete(0, tk.END)
            self.display.insert(0, str(-current))
        except ValueError:
            pass
    
    def percentage(self):
        try:
            current = float(self.display.get())
            self.display.delete(0, tk.END)
            self.display.insert(0, str(current / 100))
        except ValueError:
            pass
    
    def scientific_operation(self, operation):
        try:
            current = float(self.display.get())
            result = operation(current)
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
        except ValueError:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")
    
    def calculate(self):
        try:
            expression = self.display.get()
            result = eval(expression)
            self.display.delete(0, tk.END)
            self.display.insert(0, str(result))
        except Exception as e:
            self.display.delete(0, tk.END)
            self.display.insert(0, "Error")

if __name__ == "__main__":
    root = tk.Tk()
    app = EngineeringCalculator(root)
    root.mainloop()
