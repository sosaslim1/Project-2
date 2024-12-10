import pytest
import tkinter as tk
from unittest.mock import MagicMock
from main import QBStatsApp

@pytest.fixture
def app():
    root = tk.Tk()
    # Prevent the window from actually showing up
    root.withdraw()
    return QBStatsApp(root)

def test_add_stats_new_qb(app):
    # Mock user input
    app.qb_name_entry.get = MagicMock(return_value="Tom Brady")
    app.stat_entries[0].get = MagicMock(return_value="40")   # attempts
    app.stat_entries[1].get = MagicMock(return_value="25")   # completions
    app.stat_entries[2].get = MagicMock(return_value="280")  # yards
    app.stat_entries[3].get = MagicMock(return_value="1")    # interceptions
    app.stat_entries[4].get = MagicMock(return_value="2")    # touchdowns

    app.add_stats()

    assert "Tom Brady" in app.stats
    assert app.stats["Tom Brady"]["attempts"] == 40
    assert app.stats["Tom Brady"]["completions"] == 25
    assert app.stats["Tom Brady"]["yards"] == 280
    assert app.stats["Tom Brady"]["interceptions"] == 1
    assert app.stats["Tom Brady"]["touchdowns"] == 2
    assert "Stats updated for Tom Brady!" in app.output_label.cget("text")

def test_add_stats_existing_qb(app):
    # First addition
    app.qb_name_entry.get = MagicMock(return_value="Aaron Rodgers")
    app.stat_entries[0].get = MagicMock(return_value="30")   # attempts
    app.stat_entries[1].get = MagicMock(return_value="20")   # completions
    app.stat_entries[2].get = MagicMock(return_value="250")  # yards
    app.stat_entries[3].get = MagicMock(return_value="0")    # interceptions
    app.stat_entries[4].get = MagicMock(return_value="3")    # touchdowns
    app.add_stats()

    # Second addition (simulate new stats)
    app.stat_entries[0].get = MagicMock(return_value="10")
    app.stat_entries[1].get = MagicMock(return_value="7")
    app.stat_entries[2].get = MagicMock(return_value="80")
    app.stat_entries[3].get = MagicMock(return_value="1")
    app.stat_entries[4].get = MagicMock(return_value="1")
    app.add_stats()

    assert app.stats["Aaron Rodgers"]["attempts"] == 40
    assert app.stats["Aaron Rodgers"]["completions"] == 27
    assert app.stats["Aaron Rodgers"]["yards"] == 330
    assert app.stats["Aaron Rodgers"]["interceptions"] == 1
    assert app.stats["Aaron Rodgers"]["touchdowns"] == 4

def test_add_stats_no_name(app):
    # No QB name provided
    app.qb_name_entry.get = MagicMock(return_value="")
    for entry in app.stat_entries:
        entry.get = MagicMock(return_value="10")

    app.add_stats()
    assert "Please enter a quarterback name!" in app.output_label.cget("text")

def test_add_stats_invalid_input(app):
    app.qb_name_entry.get = MagicMock(return_value="John Doe")
    # One of the entries is not an integer
    app.stat_entries[0].get = MagicMock(return_value="ten")
    app.stat_entries[1].get = MagicMock(return_value="20")
    app.stat_entries[2].get = MagicMock(return_value="300")
    app.stat_entries[3].get = MagicMock(return_value="1")
    app.stat_entries[4].get = MagicMock(return_value="2")

    app.add_stats()
    assert "Please enter valid numbers for all stats!" in app.output_label.cget("text")

def test_calculate_passer_rating(app):
    stats = {
        "attempts": 40,
        "completions": 25,
        "yards": 280,
        "interceptions": 1,
        "touchdowns": 2,
    }
    rating = app.calculate_passer_rating(stats)
    # Just ensure it's a reasonable value, this is a known approximate rating
    assert 80 <= rating <= 120

def test_show_summary_no_name(app):
    app.qb_name_entry.get = MagicMock(return_value="")
    app.show_summary()
    assert "Please enter a quarterback name to view stats!" in app.output_label.cget("text")

def test_show_summary_no_stats(app):
    app.qb_name_entry.get = MagicMock(return_value="Peyton Manning")
    app.show_summary()
    assert "No stats found for Peyton Manning!" in app.output_label.cget("text")

def test_show_summary_with_stats(app):
    # Set stats directly
    app.stats["Drew Brees"] = {
        "attempts": 50,
        "completions": 35,
        "yards": 400,
        "interceptions": 2,
        "touchdowns": 3,
    }
    app.qb_name_entry.get = MagicMock(return_value="Drew Brees")
    app.show_summary()
    output = app.output_label.cget("text")
    assert "Stats for Drew Brees" in output
    assert "Attempts: 50" in output
    assert "Completions: 35" in output
    assert "Passing Yards: 400" in output
    assert "Touchdowns: 3" in output
    assert "Interceptions: 2" in output
