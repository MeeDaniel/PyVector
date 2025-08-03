import math
from typing import Tuple
from .util import check_type


class Vector2:
    __slots__ = ('x', 'y')
    
    def __init__(self, x=0.0, y=0.0):
        self.x = float(x)
        self.y = float(y)
    
    # Default operators (+, -, *, /, //)
    def __add__(self, other):
        check_type(other, "other", (Vector2, int, float))
        if isinstance(other, (int, float)):
            return Vector2(self.x + other, self.y + other)
        return Vector2(self.x + other.x, self.y + other.y)
    
    def __sub__(self, other):
        check_type(other, "other", (Vector2, int, float))
        if isinstance(other, (int, float)):
            return Vector2(self.x - other, self.y - other)
        return Vector2(self.x - other.x, self.y - other.y)
    
    def __mul__(self, scalar):
        check_type(scalar, "scalar", (int, float))
        return Vector2(self.x * scalar, self.y * scalar)
    
    def __truediv__(self, scalar):
        check_type(scalar, "scalar", (int, float))
        return Vector2(self.x / scalar, self.y / scalar)
    
    def __floordiv__(self, scalar):
        check_type(scalar, "scalar", (int, float))
        return Vector2(self.x // scalar, self.y // scalar)
    
    # In-place operators (+=, -=, *=, /=, //=)
    def __iadd__(self, other):
        check_type(other, "other", (Vector2, int, float))
        if isinstance(other, (int, float)):
            self.x += other
            self.y += other
        else:
            self.x += other.x
            self.y += other.y
        return self
    
    def __isub__(self, other):
        check_type(other, "other", (Vector2, int, float))
        if isinstance(other, (int, float)):
            self.x -= other
            self.y -= other
        else:
            self.x -= other.x
            self.y -= other.y
        return self
    
    def __imul__(self, scalar):
        check_type(scalar, "scalar", (int, float))
        self.x *= scalar
        self.y *= scalar
        return self
    
    def __itruediv__(self, scalar):
        check_type(scalar, "scalar", (int, float))
        self.x /= scalar
        self.y /= scalar
        return self
    
    def __ifloordiv__(self, scalar):
        check_type(scalar, "scalar", (int, float))
        self.x //= scalar
        self.y //= scalar
        return self
    
    # Unary operators and comparisons
    def __neg__(self):
        return Vector2(-self.x, -self.y)
    
    def __eq__(self, other):
        check_type(other, "other", Vector2)
        return self.x == other.x and self.y == other.y
    
    # Access via index (v[0] = x, v[1] = y)
    def __getitem__(self, index: int):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        raise IndexError("Vector2 index out of range (0-1)")
    
    def __setitem__(self, index: int, value: float):
        check_type(value, "value", (int, float))
        if index == 0:
            self.x = float(value)
        elif index == 1:
            self.y = float(value)
        else:
            raise IndexError("Vector2 index out of range (0-1)")
    
    # Main methods
    def length(self) -> float:
        """Returns the length of the vector (Euclidian norm)."""
        return math.hypot(self.x, self.y)
    
    def length_squared(self) -> float:
        """Returns the square of the length of the vector (faster than length())."""
        return self.x ** 2 + self.y ** 2
    
    def normalize(self):
        """Normalizes this vector"""
        length = self.length()
        if length == 0:
            self.x = 0
            self.y = 0
        else:
            self.x /= length
            self.y /= length

    def normalized(self) -> 'Vector2':
        """Returns normalized vector."""
        length = self.length()
        if length == 0:
            return Vector2(0, 0)
        return Vector2(self.x / length, self.y / length)
    
    def dot(self, other: 'Vector2') -> float:
        """Returns scalar product with the other vector."""
        check_type(other, "other", Vector2)
        return self.x * other.x + self.y * other.y
    
    def cross(self, other: 'Vector2') -> float:
        """Return vector product with the other vector (pseudo scalar in 2D)."""
        check_type(other, "other", Vector2)
        return self.x * other.y - self.y * other.x
    
    def rotate(self, angle_degrees: float):
        """Rotate vector by the specified angle (in degrees)."""
        check_type(angle_degrees, "angle_degrees", (int, float))
        rad = math.radians(angle_degrees)
        cos = math.cos(rad)
        sin = math.sin(rad)
        self.x, self.y = self.x * cos - self.y * sin, self.x * sin + self.y * cos

    def rotated(self, angle_degrees: float) -> 'Vector2':
        """Returns rotated vector by the specified angle (in degrees)."""
        check_type(angle_degrees, "angle_degrees", (int, float))
        rad = math.radians(angle_degrees)
        cos = math.cos(rad)
        sin = math.sin(rad)
        return Vector2(
            self.x * cos - self.y * sin,
            self.x * sin + self.y * cos
        )
    
    def distance_to(self, other: 'Vector2') -> float:
        """Returns the distance to the other vector."""
        check_type(other, "other", Vector2)
        return math.hypot(self.x - other.x, self.y - other.y)
    
    def lerp(self, other: 'Vector2', alpha: float) -> 'Vector2':
        """Linear interpolation between self and other (alpha ∈ [0, 1])."""
        check_type(other, "other", Vector2)
        check_type(alpha, "alpha", (int, float))
        return Vector2(
            self.x + (other.x - self.x) * alpha,
            self.y + (other.y - self.y) * alpha
        )
    
    # Features and alternative constructions
    @property
    def xy(self) -> Tuple[float, float]:
        return (self.x, self.y)

    @xy.setter
    def xy(self, values: Tuple[float, float]):
        check_type(values, "values", (tuple, list))
        if len(values) != 2:
            raise ValueError("xy requires 2 values (x, y)")
        self.x, self.y = float(values[0]), float(values[1])
    
    @property
    def yx(self) -> Tuple[float, float]:
        return (self.y, self.x)

    @yx.setter
    def yx(self, values: Tuple[float, float]):
        check_type(values, "values", (tuple, list))
        if len(values) != 2:
            raise ValueError("xy requires 2 values (y, x)")
        self.y, self.x = float(values[0]), float(values[1])
    
    @property
    def integer(self) -> Tuple[int, int]:
        return (int(self.x), int(self.y))

    @property
    def intxy(self) -> Tuple[int, int]:
        return (int(self.x), int(self.y))
    
    @property
    def intyx(self) -> Tuple[int, int]:
        return (int(self.y), int(self.x))
    
    @classmethod
    def from_angle(cls, angle_degrees: float, length: float = 1.0) -> 'Vector2':
        """Returns vector using its angle (in degrees) and length."""
        check_type(angle_degrees, "angle_degrees", (int, float))
        check_type(length, "length", (int, float))
        rad = math.radians(angle_degrees)
        return cls(math.cos(rad) * length, math.sin(rad) * length)
    
    def copy(self):
        return Vector2(self.x, self.y)

    def __repr__(self):
        return f"Vector2({self.x}, {self.y})"