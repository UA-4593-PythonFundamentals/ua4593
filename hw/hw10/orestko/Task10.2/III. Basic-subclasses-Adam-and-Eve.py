class Human:
    pass

class Man(Human):
    pass

class Woman(Human):
    pass

class God:
    def __init__(self):
        self._humans = [Man(), Woman()]

    def __getitem__(self, index):
        return self._humans[index]

    def __len__(self):
        return len(self._humans)