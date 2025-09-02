import time
import math


"""
Displays spacer lines
"""
def spacer(lines):
    for _ in range(0,lines):
        print(".")
        time.sleep(0.05)

"""
ask the user what's the length of the total flow cycle desired 
and the length of the 4 sub-blocks
"""
def setBlockTime(phases):
    durations = {}
    for phase in phases:
        durations[phase] = float(input(f"Enter {phase} block time in minutes: "))
        spacer(2)
    return durations

"""
ask the user for confirmation before starting the timer
"""
def confirmation():
    user_input = input("Type 'y' to proceed or 'q' to quit: ")
    if "q" in user_input.lower():
        exit()
    elif "y" in user_input.lower():
        return 
    else:
        confirmation()

"""
Counts the selected durations and displays start and end messages
"""
def countTime(durations):
    total_time = sum(durations.values())
    hours = int(total_time // 60)
    minutes = int(total_time % 60)
    print(f"Starting flow work block.\nTotal duration : {hours}h{minutes:02}m")
    confirmation()
    for phase, duration in durations.items():
        print(f"Starting {phase} phase...")
        spacer(3)
        for minute in range(int(duration), 0, -1):
            print(f"{minute} minutes left...")
            time.sleep(60)
        print(f"Ending {phase} phase...")
        spacer(3)

def init():
    phases = ["Struggle", "Release", "Flow", "Recovery"]
    durations = setBlockTime(phases)
    countTime(durations)

init()

