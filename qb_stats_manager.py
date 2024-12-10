class QBStatsManager:
    def __init__(self):
        self.qbs = {
            "QB1": {"attempts": 0, "completions": 0, "touchdowns": 0, "interceptions": 0, "rating": 0.0},
            "QB2": {"attempts": 0, "completions": 0, "touchdowns": 0, "interceptions": 0, "rating": 0.0},
        }

    def update_stat(self, qb_name: str, stat_type: str, stat_value: float):
        if qb_name not in self.qbs:
            raise ValueError(f"Quarterback {qb_name} not found!")
        if stat_type not in self.qbs[qb_name]:
            raise ValueError(f"Stat type {stat_type} is invalid!")
        self.qbs[qb_name][stat_type] += stat_value

    def get_stats(self) -> dict:
        return self.qbs

    def get_summary(self) -> str:
        summary = []
        for qb, stats in self.qbs.items():
            summary.append(
                f"{qb}: Attempts - {stats['attempts']}, Completions - {stats['completions']}, "
                f"Touchdowns - {stats['touchdowns']}, INTs - {stats['interceptions']}, Rating - {stats['rating']:.2f}"
            )
        return "\n".join(summary)
