class EvenNumbers:
    def __init__(self, start=0, end=1):
        if start >= end:
            raise ValueError("Start должен быть меньше end")
        self.start = start if start % 2 == 0 else start + 1
        self.end = end
    def __iter__(self):
        self.current = self.start
        return self
    def __next__(self):
        if self.current >= self.end:
            raise StopIteration
        even_number = self.current
        self.current += 2
        return even_number
en = EvenNumbers(10, 25)
for i in en:
    print(i)
        