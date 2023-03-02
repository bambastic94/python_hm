"""
Реализация метакласса Singleton
"""

class Singleton(type):
    def __init__(self, *args, **kwargs):
        self._instance = None
        super().__init__(*args, **kwargs)

    def __call__(self, *args, **kwargs):
        if self._instance is None:
            self._instance = super().__call__(*args, **kwargs)
            return self._instance
        else:
            return self._instance

class A(metaclass=Singleton):
    def __init__(self):
        print('55')

class B(metaclass=Singleton):
    def __init__(self):
        print('55')


a1 = A()
a2 = A()
b1 = B()
b2 = B()

print('a1 — ', a1)
print('a2 — ', a2)
print('b1 — ', b1)
print('b2 — ', b2)
