import tkinter as tk
from tkinter import ttk
from ui import time_distance_to_pace_frame as tdtp

class PaceTimeToDistance(ttk.Frame):
    def __init__(self, container, controller):
        super().__init__(container)

        self.pace_minutes_value = tk.StringVar()
        self.pace_seconds_value = tk.StringVar()
        self.time_minutes_value = tk.StringVar()
        self.time_seconds_value = tk.StringVar()
        self.distance_value = tk.StringVar()

        pace_title_label = ttk.Label(self, text="Pace:")
        pace_title_label.grid(column=1, row=1, sticky="W", ipadx=5)
        pace_minutes_input = ttk.Entry(self, width=3,justify='center', textvariable=self.pace_minutes_value)
        pace_minutes_input.grid(column=2, row=1, sticky="EW")
        pace_label = ttk.Label(self, text=":")
        pace_label.grid(column=3, row=1, sticky="W")
        pace_seconds_input = ttk.Entry(self, width=3,justify='center', textvariable=self.pace_seconds_value)
        pace_seconds_input.grid(column=4, row=1, sticky="EW")
        
        time_title_label = ttk.Label(self, text="Time:")
        time_title_label.grid(column=1, row=2, sticky="W", ipadx=5)
        time_minutes_input = ttk.Entry(self, width=3,justify='center', textvariable=self.time_minutes_value)
        time_minutes_input.grid(column=2, row=2, sticky="EW")
        time_label = ttk.Label(self, text=":")
        time_label.grid(column=3, row=2, sticky="W")
        time_seconds_input = ttk.Entry(self, width=3,justify='center', textvariable=self.time_seconds_value)
        time_seconds_input.grid(column=4, row=2, sticky="EW")

        distance_label = ttk.Label(self, text="Distance:")
        distance_label.grid(column=1, row=3, sticky="W", ipadx=5)
        distance_display = ttk.Label(self, anchor='center', textvariable=self.distance_value)
        distance_display.grid(column=2, row=3, columnspan=3, sticky="EW")

        calculate_button = ttk.Button(self,text="Calculate",command=self.calculate, cursor="hand2")
        calculate_button.grid(column=1, row=4, columnspan=4, sticky="EW")
        
        clear_button = ttk.Button(self,text="Clear",command=self.clear, cursor="hand2")
        clear_button.grid(column=1, row=5, columnspan=4, sticky="EW")

        switch_page_button = ttk.Button(
            self,text="Switch",command=lambda: controller.show_frame(tdtp.TimeDistanceToPace), cursor="hand2")
        switch_page_button.grid(column=1, row=6, columnspan=4, sticky="EW")

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def calculate(self, *args):
        try:
            pace_value_sec = float(self.pace_seconds_value.get())
            pace_value_min = float(self.pace_minutes_value.get())
            time_value_sec = float(self.time_seconds_value.get())
            time_value_min = float(self.time_minutes_value.get())
            self.distance_value.set('%.3f km' % ((time_value_min*60+time_value_sec)/(pace_value_sec+pace_value_min*60)))
        except ValueError:
            pass
        
    def clear(self, *args):
        self.pace_minutes_value.set("")
        self.pace_seconds_value.set("")
        self.time_minutes_value.set("")
        self.time_seconds_value.set("")
        self.distance_value.set("")
