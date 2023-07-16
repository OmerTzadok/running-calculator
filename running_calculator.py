import tkinter.font as font
from Services import DPIAwareness
from UI import MainFrame

DPIAwareness.set_dpi_awareness()

root = MainFrame.RunningConverter()

font.nametofont("TkDefaultFont").configure(size=15)
font.nametofont("TkTextFont").configure(size=15)

root.mainloop()


