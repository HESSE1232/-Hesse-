import tkinter as tk
from datetime import datetime

class Cronometro:
    def __init__(self, root):
        self.root = root
        self.root.title("Cronômetro")

        self.is_running = False
        self.start_time = None
        self.elapsed_time = 0

        self.label = tk.Label(root, text="00:00:00", font=("Arial", 24))
        self.label.pack(pady=10)

        self.start_button = tk.Button(root, text="Iniciar", command=self.start)
        self.start_button.pack(pady=5)

        self.pause_button = tk.Button(root, text="Pausar", state="disabled", command=self.pause)
        self.pause_button.pack(pady=5)

        self.reset_button = tk.Button(root, text="Zerar", state="disabled", command=self.reset)
        self.reset_button.pack(pady=5)

    def start(self):
        if not self.is_running:
            self.is_running = True
            self.start_time = datetime.now()
            self.update_timer()

            self.start_button.config(state="disabled")
            self.pause_button.config(state="normal")
            self.reset_button.config(state="normal")

    def pause(self):
        if self.is_running:
            self.is_running = False
            self.elapsed_time += (datetime.now() - self.start_time).total_seconds()

            self.start_button.config(state="normal")
            self.pause_button.config(state="disabled")

    def reset(self):
        self.is_running = False
        self.start_time = None
        self.elapsed_time = 0

        self.label.config(text="00:00:00")

        self.start_button.config(state="normal")
        self.pause_button.config(state="disabled")
        self.reset_button.config(state="disabled")

    def update_timer(self):
        if self.is_running:
            elapsed = int(self.elapsed_time + (datetime.now() - self.start_time).total_seconds())
            hours, remainder = divmod(elapsed, 3600)
            minutes, seconds = divmod(remainder, 60)
            time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            self.label.config(text=time_str)
            self.root.after(1000, self.update_timer)

root = tk.Tk()
cronometro = Cronometro(root)
root.mainloop()