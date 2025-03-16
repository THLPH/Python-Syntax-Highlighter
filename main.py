import tkinter as tk 
from tkinter import filedialog 
import re 
 
# Define highlight patterns 
HIGHLIGHT_PATTERNS = { 
    "keyword": (r"\b(def|class|import|from|return|if|else|elif|while|for|try|except|with)\b", "blue"), 
    "comment": (r"#.*", "green"), 
    "string": (r"(['"])(?:(?=(\\?))\2.)*?\1", "orange"), 
} 
 
# TODO: def highlight_syntax(event=None): 
    """Apply syntax highlighting to the text widget.""" 
  
def on_key_release(event): 
    """Trigger syntax highlighting after typing.""" 
    highlight_syntax() 
 
# TODO: def open_file(): 
    """Open a file and apply syntax highlighting.""" 
 
# Setup the Tkinter window 
root = tk.Tk() 
root.title("Syntax Highlighting Editor") 
 
# Create a text widget 
text_widget = tk.Text(root, wrap="word", font=("Courier", 12)) 
text_widget.pack(expand=True, fill="both") 
text_widget.bind("<KeyRelease>", on_key_release)  # Apply highlighting on key press 
 
# Create an Open File button 
open_button = tk.Button(root, text="Open File", command=open_file) 
open_button.pack() 
 
root.mainloop() 
