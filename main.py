import tkinter as tk
from tkinter import filedialog
import re

# Define highlight patterns
HIGHLIGHT_PATTERNS = {
    "keyword": (r"\b(def|class|import|from|return|if|else|elif|while|for|try|except|with)\b", "blue"),
    "comment": (r"#.*", "green"),
    "string": (r"(['\"])(?:(?=(\\?))\2.)*?\1", "orange"),
}

def highlight_syntax(event=None):
    """Apply syntax highlighting to the text widget."""
    text = text_widget.get("1.0", "end-1c")  # Get all text
    for tag in HIGHLIGHT_PATTERNS:
        pattern, color = HIGHLIGHT_PATTERNS[tag]
        text_widget.tag_remove(tag, "1.0", "end")  # Remove old highlights

        # Use regex to find matches
        for match in re.finditer(pattern, text, re.MULTILINE):
            start_index = f"1.0 + {match.start()} chars"
            end_index = f"1.0 + {match.end()} chars"
            text_widget.tag_add(tag, start_index, end_index)
            text_widget.tag_config(tag, foreground=color)

def on_key_release(event):
    """Trigger syntax highlighting after typing."""
    highlight_syntax()

def open_file():
    """Open a file and apply syntax highlighting."""
    file_path = filedialog.askopenfilename(filetypes=[("Python Files", "*.py"), ("Text Files", "*.txt")])
    if file_path:
        with open(file_path, "r") as file:
            text_widget.delete("1.0", "end")
            text_widget.insert("1.0", file.read())
        highlight_syntax()  # Highlight after loading

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
