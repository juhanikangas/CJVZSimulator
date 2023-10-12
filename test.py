from tqdm import tqdm
import time

# Specify the total duration of the timer
total_duration = 10  # seconds

# Create a timer bar that displays "Time Left"
for i in tqdm(range(total_duration, -1, -1), desc="Time Left", ncols=100):
    time.sleep(1)  # Simulate work (e.g., 1 second per iteration)