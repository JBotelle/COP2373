# Joe Botelle
# Programming Exercise 13: Population Database

# This program creates a SQLite database called population_JLB, inserts baseline 2023 population data for 10 Florida
# cities, simulates growth/decline for 20 years using deterministic rates with small deviations, and visualizes results.

import sqlite3
import random
import matplotlib.pyplot as plt
import sys

# Baseline population for cities.
CITIES = {
    "Crystal River": 3500,
    "Palatka": 10000,
    "Ocala": 64000,
    "Thonotosassa": 15000,
    "Ormand Beach": 44000,
    "Sarasota": 57000,
    "Destin": 13000,
    "Port St. Lucie": 240000,
    "Fort Walton": 22000,
    "Deerfield Beach": 82000
}

# Baseline population growth for cities.
GROWTH_RATES = {
    "Crystal River": 0.0066,
    "Palatka": 0.009,
    "Ocala": 0.0226,
    "Thonotosassa": 0.0061,
    "Ormand Beach": 0.0083,
    "Sarasota": 0.0111,
    "Destin": 0.0009,
    "Port St. Lucie": 0.05,
    "Fort Walton": 0.003,
    "Deerfield Beach": 0.0021
}


# Yes / No validation for user questions. Three failed attempts exits program.
def get_yes_no(prompt):
    attempts = 0
    while attempts < 3:
        choice = input(prompt).strip().lower()
        if choice in ("y", "ye", "yes"):
            return True
        elif choice in ("n", "no", "nope"):
            return False
        else:
            print("Please enter 'y' or 'n'.")
            attempts += 1
    print("I'm sorry, please try again later.")
    sys.exit()

# Prompt user for integer input with range validation. Three failed attempts exits program
def get_int(prompt, min_value=0, max_value=100):
    attempts = 0
    while attempts < 3:
        try:
            value = int(input(prompt))
            if min_value <= value <= max_value:
                return value
            else:
                print(f"Please enter a number between {min_value} and {max_value}.")
        except ValueError:
            print("Invalid input. Please enter a valid integer.")
        attempts += 1
    print("I'm sorry, but I don't understand your input. Please try again later.")
    sys.exit()

# Open connection and create database with one row, per city, per year
# Primary key is made up of (city, year)
def create_database():
    with sqlite3.connect("population_JLB.db") as conn:
        conn.execute("""
            CREATE TABLE IF NOT EXISTS population (
                city TEXT,
                year INTEGER,
                population INTEGER,
                PRIMARY KEY (city, year)
            )
        """)


# Connect to population_JLB and insert baseline 2023 data
def insert_baseline_data():
    with sqlite3.connect("population_JLB.db") as conn:
        # Clear any existing rows to avoid duplicates if rerun
        conn.execute("DELETE FROM population")
        for city, pop in CITIES.items():
            conn.execute("INSERT OR REPLACE INTO population VALUES (?, ?, ?)", (city, 2023, pop))


# Simulate growth/decline for 20 years (historical rates + deviation)
def simulate_population():
    with sqlite3.connect("population_JLB.db") as conn:
        # Clear previous simulation data
        conn.execute("DELETE FROM population WHERE year > 2023")
        rows = conn.execute("SELECT city, population FROM population WHERE year=2023").fetchall()

        # Deviation for chart line is +- 0.5%
        for city, base_pop in rows:
            population = base_pop
            # 20 year range simulation ends with 2043
            for year in range(2024, 2044):
                avg_rate = GROWTH_RATES.get(city, 0.01)
                deviation = random.uniform(-0.005, 0.005)
                rate = avg_rate + deviation
                population = int(population * (1 + rate))
                conn.execute("INSERT OR REPLACE INTO population VALUES (?, ?, ?)",
                             (city, year, population))


# Get user selected city and show growth
# Function 4: Visualize growth for a chosen city (legible annotations + loop)
def plot_population_growth():
    # Open connection and create list from CITIES dictionary
    with sqlite3.connect("population_JLB.db") as conn:
        city_list = list(CITIES.keys())
        # Offset is to correct overlapping of labels by staggering position around data point
        offsets = [(0, 6), (6, 6), (-6, 6), (8, 10), (-8, 10)]

        # Loop continuously until user decides to stop
        while True:
            print("\nChoose a city from the following list:")
            for i, city in enumerate(city_list, 1):
                print(f"{i}. {city}")

            # Integer validation for user city selection.  Min is set to one, max is set to length of city_list.
            choice = get_int("Enter the number of your chosen city: ", 1, len(city_list))

            # Map user's choice to city name and request all rows for chosen city from database
            chosen_city = city_list[choice - 1]
            data = conn.execute(
                "SELECT year, population FROM population WHERE city=? ORDER BY year",
                (chosen_city,)
            ).fetchall()

            # Split results for plotting year = x axis, population = y axis and calculate average growth rate
            years = [row[0] for row in data]
            populations = [row[1] for row in data]
            avg_rate = GROWTH_RATES.get(chosen_city, 0.01) * 100

            # Create new figures and plot the population data with annotations
            fig, ax = plt.subplots(figsize=(11, 6))
            ax.plot(years, populations, marker="o", linestyle="-", color="blue")

            for idx, (x, y) in enumerate(zip(years, populations)):
                dx, dy = offsets[idx % len(offsets)]
                ax.annotate(f"{y:,}", xy=(x, y), xytext=(dx, dy),
                            textcoords="offset points", fontsize=8,
                            ha="center", va="bottom",
                            bbox=dict(boxstyle="round,pad=0.2", fc="white", ec="none", alpha=0.75))

            # Chart title, labels, grid lines and chart window
            ax.set_title(f"Population Growth of {chosen_city} (2023–2043)\nAverage Growth Rate: "
                         f"{avg_rate:.2f}% per year")
            ax.set_xlabel("Year")
            ax.set_ylabel("Population")
            ax.set_xticks(range(2023, 2044))
            ax.set_xlim(2023, 2043)
            ax.grid(True, alpha=0.3)
            plt.tight_layout()
            plt.show()

            # Three try system for yes / no question to continue loop
            # Ask the user if they want to view another city
            if not get_yes_no("Would you like to view another city? (y/n): "):
                break


# Main Loop
def main():
    # Create Database
    create_database()
    # Fill in baseline data
    insert_baseline_data()
    # Run 20 year simulation
    simulate_population()
    # Get user selected city and show results
    plot_population_growth()


if __name__ == "__main__":
    main()
