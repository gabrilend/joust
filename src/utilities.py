
class Clock:
    import time

    def __init__(self):
        self.time = time.time_ns()
        self.delta_time = 0
        self.character_ready_to_print = 0

    
    #delta_time is the time since the last tick
    def tick(self):
        self.delta_time = time.time_ns() - self.time
        self.time += self.delta_time
        return self.delta_time
