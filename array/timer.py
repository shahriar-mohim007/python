import time

class RateLimitExceeded(Exception):
  pass

class RateLimiter:
  def __init__(self, limit=10, period=1):
    self.limit = limit
    self.period = period
    self.calls = 0
    self.last_call = 0

  def __call__(self, func):
    def wrapper(*args, **kwargs):
      now = time.time()
      print("MOHIM")
      print(self.last_call)
      print(self.limit)
      print("MOHIM")
      if now - self.last_call >= self.period:
        self.calls = 0 
        self.last_call = now
      if self.calls < self.limit:
        self.calls += 1
        self.last_call = now
        return func(*args, **kwargs)
      else:
        raise RateLimitExceeded("Rate limit exceeded!")
    return wrapper


rate_limiter = RateLimiter(limit=5, period=2)

@rate_limiter
def getSum(a,b):
  return a + b


# Test case
try:
    # Make 5 calls within the limit period, should all succeed
    for _ in range(5):
        print(getSum(1, 2))
    
    # Wait for 2 seconds to reset the rate limiter period
    time.sleep(2.1)

    # Try to make 5 more calls, which should succeed if the limiter resets properly
    for _ in range(5):
        print(getSum(3, 4))
    
    time.sleep(2)
    # This call should fail if the limiter didn't reset properly
    print(getSum(5, 6))
    print(getSum(5, 6))
except RateLimitExceeded as e:
    print(e)