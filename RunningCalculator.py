import tkinter.font as font
from Services import DPIAwarness
from UI import MainFrame

DPIAwarness.set_dpi_awarness()

root = MainFrame.RunningConverter()

font.nametofont("TkDefaultFont").configure(size=15)
font.nametofont("TkTextFont").configure(size=15)

root.mainloop()


