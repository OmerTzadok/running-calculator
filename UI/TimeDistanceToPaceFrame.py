import tkinter as tk
from tkinter import ttk
from UI import PaceTimeToDistanceFrame as PTTD

class TimeDistanceToPace(ttk.Frame):
    def __init__(self, container, controller):
        super().__init__(container)

        self.pace_minutes_value = tk.StringVar()
        self.pace_seconds_value = tk.StringVar()
        self.time_minutes_value = tk.StringVar()
        self.time_seconds_value = tk.StringVar()
        self.distance_value = tk.StringVar()

        distance_label = ttk.Label(self, text="Distance:")
        distance_label.grid(column=1, row=1, sticky="W", ipadx=5)
        distance_input = ttk.Entry(self, width=3, justify='center', textvariable=self.distance_value)
        distance_input.grid(column=2, row=1, columnspan=3 , sticky="EW")
        
        time_title_label = ttk.Label(self, text="Time:")
        time_title_label.grid(column=1, row=2, sticky="W", ipadx=5)
        time_minutes_input = ttk.Entry(self, width=3,justify='center', textvariable=self.time_minutes_value)
        time_minutes_input.grid(column=2, row=2, sticky="EW")
        time_label = ttk.Label(self, text=":")
        time_label.grid(column=3, row=2, sticky="W")
        time_seconds_input = ttk.Entry(self, width=3,justify='center', textvariable=self.time_seconds_value)
        time_seconds_input.grid(column=4, row=2, sticky="EW")

        pace_title_label = ttk.Label(self, text="Pace:")
        pace_title_label.grid(column=1, row=3, sticky="W", ipadx=5)
        pace_minutes_display = ttk.Label(self, anchor='e',textvariable=self.pace_minutes_value)
        pace_minutes_display.grid(column=2, row=3, sticky="EW")
        pace_label = ttk.Label(self, text=":")
        pace_label.grid(column=3, row=3, sticky="W")
        pace_seconds_display = ttk.Label(self, anchor='w',textvariable=self.pace_seconds_value)
        pace_seconds_display.grid(column=4, row=3, sticky="EW")

        calculate_button = ttk.Button(self,text="Calculate",command=self.calculate, cursor="hand2")
        calculate_button.grid(column=1, row=4, columnspan=4, sticky="EW")
        
        clear_button = ttk.Button(self,text="Clear",command=self.clear, cursor="hand2")
        clear_button.grid(column=1, row=5, columnspan=4, sticky="EW")

        switch_page_button = ttk.Button(
            self,text="Switch",command=lambda: controller.show_frame(PTTD.PaceTimeToDistance), cursor="hand2")
        switch_page_button.grid(column=1, row=6, columnspan=4, sticky="EW")

        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=5)

    def calculate(self, *args):
        try:
            distance_value = float(self.distance_value.get())
            time_value_sec = float(self.time_seconds_value.get())
            time_value_min = float(self.time_minutes_value.get())
            pace_value = (time_value_min*60+time_value_sec)/distance_value
            self.pace_seconds_value.set(str(int(pace_value%60)))
            self.pace_minutes_value.set(str(int(pace_value/60)))
        except ValueError:
            pass
        
    def clear(self, *args):
        self.pace_minutes_value.set("")
        self.pace_seconds_value.set("")
        self.time_minutes_value.set("")
        self.time_seconds_value.set("")
        self.distance_value.set("")