import tkinter as tk
from tkinter import ttk
from ui import pace_time_to_distance_frame as pttd
from ui import time_distance_to_pace_frame as tdtp

class RunningConverter(tk.Tk):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        
        self.title("Running Converter")
        self.frames = dict()

        container = ttk.Frame(self)
        container.grid(padx=10, pady=10, sticky="EW")

        for FrameClass in (pttd.PaceTimeToDistance, tdtp.TimeDistanceToPace):
            frame = FrameClass(container, self)
            self.frames[FrameClass] = frame
            frame.grid(row=0, column=0, sticky="NSEW")

        self.show_frame(pttd.PaceTimeToDistance)

    def show_frame(self, container):
        frame = self.frames[container]
        self.bind("<Return>", frame.calculate)
        self.bind("<KP_Enter>", frame.calculate)
        self.bind("<BackSpace>", frame.clear)
        self.bind("<Delete>", frame.clear)
        frame.tkraise()