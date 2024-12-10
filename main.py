import tkinter as tk
from qb_stats_manager import QBStatsManager


class QBStatsApp:
    """Quarterback Stats Tracker built with tkinter"""

    def __init__(self, root: tk.Tk):
        """Starts the QBStatsApp"""
        self.root = root
        self.root.title("Quarterback Stats Tracker")
        self.manager = QBStatsManager()

        # Start of GUI elements
        self.results_label = tk.Label(root, text=self._get_results_text(), font=("Arial", 14))
        self.results_label.pack(pady=10)

        self.status_label = tk.Label(root, text="No stats added yet", font=("Arial", 12), fg="blue")
        self.status_label.pack(pady=5)

        add_yards_button = tk.Button(root, text="Add Yards for QB1", command=lambda: self.add_stats("QB1", "yards"), font=("Arial", 12))
        add_yards_button.pack(pady=5)

        add_td_button = tk.Button(root, text="Add TD for QB1", command=lambda: self.add_stats("QB1", "touchdowns"), font=("Arial", 12))
        add_td_button.pack(pady=5)

        add_yards_qb2_button = tk.Button(root, text="Add Yards for QB2", command=lambda: self.add_stats("QB2", "yards"), font=("Arial", 12))
        add_yards_qb2_button.pack(pady=5)

        add_td_qb2_button = tk.Button(root, text="Add TD for QB2", command=lambda: self.add_stats("QB2", "touchdowns"), font=("Arial", 12))
        add_td_qb2_button.pack(pady=5)

        summary_button = tk.Button(root, text="Show Summary", command=self.show_summary, font=("Arial", 12), bg="green", fg="white")
        summary_button.pack(pady=10)

        exit_button = tk.Button(root, text="Exit", command=root.quit, font=("Arial", 12))
        exit_button.pack(pady=10)
        # End of GUI elements

    def add_stats(self, qb_name: str, stat_type: str) -> None:
        """Handles logic for adding stats"""
        try:
            self.manager.update_stat(qb_name, stat_type)
            self.results_label.config(text=self._get_results_text())
            self.status_label.config(text=f"Added {stat_type} for {qb_name}", fg="blue")
        except ValueError as e:
            self.status_label.config(text=str(e), fg="red")

    def show_summary(self) -> None:
        """Displays a summary of the stats in the main window"""
        summary = self.manager.get_summary()
        self.results_label.config(text=summary)
        self.status_label.config(text="Stats updated!", fg="green")

    def _get_results_text(self) -> str:
        """
        Formats the current stats for display in the results label.
        """
        results = self.manager.get_stats()
        return (
            f"QB1 - Yards: {results['QB1']['yards']}, TDs: {results['QB1']['touchdowns']}\n"
            f"QB2 - Yards: {results['QB2']['yards']}, TDs: {results['QB2']['touchdowns']}"
        )


if __name__ == "__main__":
    root = tk.Tk()
    app = QBStatsApp(root)
    root.mainloop()