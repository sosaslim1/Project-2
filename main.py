import tkinter as tk


class QBStatsApp:

    def __init__(self, root: tk.Tk):
        self.root = root
        self.root.title("Quarterback Stats Tracker")

        self.stats = {}

        self.qb_name_label = tk.Label(root, text="Quarterback Name:", font=("Arial", 12))
        self.qb_name_label.grid(row=0, column=0, padx=10, pady=5, sticky="w")
        self.qb_name_entry = tk.Entry(root, font=("Arial", 12))
        self.qb_name_entry.grid(row=0, column=1, padx=10, pady=5, sticky="w")

        self.stat_labels = [
            "Pass Attempts:",
            "Pass Completions:",
            "Passing Yards:",
            "Interceptions:",
            "Touchdowns:",
        ]
        self.stat_entries = []

        for i, label in enumerate(self.stat_labels):
            tk.Label(root, text=label, font=("Arial", 12)).grid(row=i + 1, column=0, padx=10, pady=5, sticky="w")
            entry = tk.Entry(root, font=("Arial", 12))
            entry.grid(row=i + 1, column=1, padx=10, pady=5, sticky="w")
            self.stat_entries.append(entry)

        self.add_button = tk.Button(root, text="Add Stats", command=self.add_stats, font=("Arial", 12), bg="blue", fg="white")
        self.add_button.grid(row=6, column=0, columnspan=2, pady=10)

        self.summary_button = tk.Button(root, text="Show Summary", command=self.show_summary, font=("Arial", 12), bg="green", fg="white")
        self.summary_button.grid(row=7, column=0, columnspan=2, pady=10)

        self.exit_button = tk.Button(root, text="Exit", command=root.quit, font=("Arial", 12))
        self.exit_button.grid(row=8, column=0, columnspan=2, pady=10)

        self.output_label = tk.Label(root, text="", font=("Arial", 12), fg="black")
        self.output_label.grid(row=9, column=0, columnspan=2, pady=10)

    def add_stats(self):
        qb_name = self.qb_name_entry.get().strip()
        if not qb_name:
            self.output_label.config(text="Please enter a quarterback name!", fg="red")
            return

        try:
            attempts = int(self.stat_entries[0].get().strip())
            completions = int(self.stat_entries[1].get().strip())
            yards = int(self.stat_entries[2].get().strip())
            interceptions = int(self.stat_entries[3].get().strip())
            touchdowns = int(self.stat_entries[4].get().strip())
        except ValueError:
            self.output_label.config(text="Please enter valid numbers for all stats!", fg="red")
            return

        if qb_name not in self.stats:
            self.stats[qb_name] = {
                "attempts": 0,
                "completions": 0,
                "yards": 0,
                "interceptions": 0,
                "touchdowns": 0,
            }

        self.stats[qb_name]["attempts"] += attempts
        self.stats[qb_name]["completions"] += completions
        self.stats[qb_name]["yards"] += yards
        self.stats[qb_name]["interceptions"] += interceptions
        self.stats[qb_name]["touchdowns"] += touchdowns

        self.output_label.config(text=f"Stats updated for {qb_name}!", fg="green")

    def calculate_passer_rating(self, stats):
        """Calculate the NFL passer rating"""
        attempts = stats["attempts"]
        completions = stats["completions"]
        yards = stats["yards"]
        touchdowns = stats["touchdowns"]
        interceptions = stats["interceptions"]

        if attempts == 0:
            return 0.0

        a = ((completions / attempts) - 0.3) * 5
        b = ((yards / attempts) - 3) * 0.25
        c = (touchdowns / attempts) * 20
        d = 2.375 - ((interceptions / attempts) * 25)

        a = max(0, min(a, 2.375))
        b = max(0, min(b, 2.375))
        c = max(0, min(c, 2.375))
        d = max(0, min(d, 2.375))

        return ((a + b + c + d) / 6) * 100

    def show_summary(self):
        qb_name = self.qb_name_entry.get().strip()
        if not qb_name:
            self.output_label.config(text="Please enter a quarterback name to view stats!", fg="red")
            return

        if qb_name not in self.stats:
            self.output_label.config(text=f"No stats found for {qb_name}!", fg="red")
            return

        stats = self.stats[qb_name]
        completion_percentage = (stats["completions"] / stats["attempts"]) * 100 if stats["attempts"] > 0 else 0
        passer_rating = self.calculate_passer_rating(stats)

        summary = (
            f"Stats for {qb_name}:\n"
            f"Attempts: {stats['attempts']}\n"
            f"Completions: {stats['completions']}\n"
            f"Completion Percentage: {completion_percentage:.2f}%\n"
            f"Passing Yards: {stats['yards']}\n"
            f"Touchdowns: {stats['touchdowns']}\n"
            f"Interceptions: {stats['interceptions']}\n"
            f"Passer Rating: {passer_rating:.2f}\n"
        )

        self.output_label.config(text=summary, fg="black")


if __name__ == "__main__":
    root = tk.Tk()
    app = QBStatsApp(root)
    root.mainloop()
