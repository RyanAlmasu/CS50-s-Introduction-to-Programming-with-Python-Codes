class Jar:
    def __init__(self, capacity=12):
        self.capacity = capacity # calls setter '@capacity' method
        self.cookie_jar = [] # or self.cookie_jar = 0

    def __str__(self):
        # self.size calls '@property for size()
        return self.size * "🍪"

    def deposit(self, n): # n arguiment comes from user
        for _ in range(n):
            self.cookie_jar.append("🍪") # or self.cookie_jar += 1
        if self.size > self.capacity:
            raise ValueError

    def withdraw(self, n):
        if n > self.size:
            raise ValueError
        for _ in range(n):
            self.cookie_jar.pop() # or self.cookie_jar -= 1
    @property
    def capacity(self):
        return self._capacity

    @capacity.setter
    def capacity(self, capacity): # 'capacity' comes from the programmer or user; from __init__()
        if capacity < 0:
            raise ValueError
        self._capacity = capacity

    @property
    def size(self):
        return len(self.cookie_jar) # or self.cookie_jar

jar = Jar()

jar.deposit(5)
print(jar)
jar.withdraw(2)
print(jar)