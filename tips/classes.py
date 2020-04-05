import pickle

class Foo:
    def __init__(self, x):
        self.x = x

serialized_foo = pickle.dumps(Foo(45))
# read about pickle.load(), pickle.dump()


print(0)