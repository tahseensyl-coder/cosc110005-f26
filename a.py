from abc import ABC, abstractmethod


class a(ABC):
    """Simple numeric base class with concrete method bodies for abstract operations."""

    def __init__(self, value=0):
        self.value = value

    @abstractmethod
    def add(self, other):
        """Return the current value plus another number."""
        return self.value + other

    @abstractmethod
    def subtract(self, other):
        """Return the current value minus another number."""
        return self.value - other

    @abstractmethod
    def multiply(self, other):
        """Return the current value multiplied by another number."""
        return self.value * other

    @abstractmethod
    def divide(self, other):
        """Return the current value divided by another number."""
        if other == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return self.value / other

    @abstractmethod
    def describe(self):
        """Return a helpful description of the object."""
        return f"a(value={self.value})"


class ConcreteA(a):
    """A concrete subclass that demonstrates a useful implementation of the abstract API."""

    def add(self, other):
        return self.value + other

    def subtract(self, other):
        return self.value - other

    def multiply(self, other):
        return self.value * other

    def divide(self, other):
        if other == 0:
            raise ZeroDivisionError("Cannot divide by zero.")
        return self.value / other

    def describe(self):
        return f"ConcreteA(value={self.value})"


if __name__ == "__main__":
    obj = ConcreteA(10)
    print(obj.add(5))
    print(obj.subtract(3))
    print(obj.multiply(2))
    print(obj.divide(2))
    print(obj.describe())
