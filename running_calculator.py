import tkinter.font as font
from services import dpi_awareness_set
from ui import main_frame

dpi_awareness_set.set_dpi_awareness()

root = main_frame.RunningConverter()

font.nametofont("TkDefaultFont").configure(size=15)
font.nametofont("TkTextFont").configure(size=15)

root.mainloop()


