import time
def countdown(seconds):
    for sec in range(seconds, 0, -1):
        print(f"Time remaining: {sec} seconds")

        end_time = time.time() + 0.5
        while time.time() < end_time:
            pass
    print("Time's up!")
countdown(5)