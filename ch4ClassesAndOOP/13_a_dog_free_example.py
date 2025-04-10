class CountedObject:
    num_instances = 0

    def __init__(self):
        self.__class__.num_instances += 1

print(CountedObject.num_instances)
print(CountedObject().num_instances)
print(CountedObject().num_instances)
print(CountedObject().num_instances)
print(CountedObject.num_instances)


# WARNING: This implementation contains a bug
class BuggyCountedObject:
    num_instances = 0

    def __init__(self):
        self.num_instances += 1  # !!!

print(BuggyCountedObject.num_instances)
print(BuggyCountedObject().num_instances)
print(BuggyCountedObject().num_instances)
print(BuggyCountedObject().num_instances)
print(BuggyCountedObject.num_instances)
