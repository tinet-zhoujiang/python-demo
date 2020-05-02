class IterDemo:
    def __iter__(self):
        self.a = 1
        return self

    def __next__(self):
        x = self.a
        self.a += 1
        return x

iterdemo = IterDemo()
itera = iter(iterdemo)
print(next(itera))
print(next(itera))
print(next(itera))
print(next(itera))
print(next(itera))