import time
import threading

class RateLimitExceeded(Exception):
    pass

class RateLimitedCalculator:
    def _init_(self, limit_per_minute):
        self.limit = limit_per_minute
        self.period = 60 
        self.lock = threading.Lock()
        self.call_timestamps = []


    def getSum(self, a, b):
        current_time = time.time()
        with self.lock:
            while self.call_timestamps and self.call_timestamps[0] <= current_time - self.period:
                self.call_timestamps.pop(0)
            if len(self.call_timestamps) < self.limit:
                self.call_timestamps.append(current_time)
                return a + b
            else:
                raise RateLimitExceeded("Rate limit exceeded!")

# Example usage:
calc = RateLimitedCalculator(limit_per_minute=5)

try:
    for i in range(15):
        print(calc.getSum(1, 2))
        time.sleep(1)
except RateLimitExceeded as e:
    print(e)