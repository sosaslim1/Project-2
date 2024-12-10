class QBStatsManager:
    def __init__(self):
        self.qbs = {
            "QB1": {"yards": 0, "touchdowns": 0, "interceptions": 0},
            "QB2": {"yards": 0, "touchdowns": 0, "interceptions": 0},
        }

    def update_stat(self, qb_name: str, stat_type: str):
        if qb_name in self.qbs and stat_type in self.qbs[qb_name]:
            self.qbs[qb_name][stat_type] += 1
        else:
            raise ValueError(f"Invalid quarterback or stat type: {qb_name}, {stat_type}")

    def get_stats(self) -> dict:
        return self.qbs

    def get_summary(self) -> str:
        summary = []
        for qb, stats in self.qbs.items():
            summary.append(
                f"{qb}: Yards - {stats['yards']}, TDs - {stats['touchdowns']}, INTs - {stats['interceptions']}"
            )
        return "\n".join(summary)
