import math
from typing import Tuple
from .util import check_type


class Vector3:
    __slots__ = ('x', 'y', 'z')
    
    def __init__(self, x=0.0, y=0.0, z=0.0):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)
    
    # Default operators (+, -, *, /, //)
    def __add__(self, other):
        check_type(other, "other", (Vector3, int, float))
        if isinstance(other, (int, float)):
            return Vector3(self.x + other, self.y + other, self.z + other)
        return Vector3(self.x + other.x, self.y + other.y, self.z + other.z)
    
    def __sub__(self, other):
        check_type(other, "other", (Vector3, int, float))
        if isinstance(other, (int, float)):
            return Vector3(self.x - other, self.y - other, self.z - other)
        return Vector3(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def __mul__(self, scalar):
        check_type(scalar, "scalar", (int, float))
        return Vector3(self.x * scalar, self.y * scalar, self.z * scalar)
    
    def __truediv__(self, scalar):
        check_type(scalar, "scalar", (int, float))
        return Vector3(self.x / scalar, self.y / scalar, self.z / scalar)
    
    def __floordiv__(self, scalar):
        check_type(scalar, "scalar", (int, float))
        return Vector3(self.x // scalar, self.y // scalar, self.z // scalar)
    
    # In-place operators (+=, -=, *=, /=, //=)
    def __iadd__(self, other):
        check_type(other, "other", (Vector3, int, float))
        if isinstance(other, (int, float)):
            self.x += other
            self.y += other
            self.z += other
        else:
            self.x += other.x
            self.y += other.y
            self.z += other.z
        return self
    
    def __isub__(self, other):
        check_type(other, "other", (Vector3, int, float))
        if isinstance(other, (int, float)):
            self.x -= other
            self.y -= other
            self.z -= other
        else:
            self.x -= other.x
            self.y -= other.y
            self.z -= other.z
        return self
    
    def __imul__(self, scalar):
        check_type(scalar, "scalar", (int, float))
        self.x *= scalar
        self.y *= scalar
        self.z *= scalar
        return self
    
    def __itruediv__(self, scalar):
        check_type(scalar, "scalar", (int, float))
        self.x /= scalar
        self.y /= scalar
        self.z /= scalar
        return self
    
    def __ifloordiv__(self, scalar):
        check_type(scalar, "scalar", (int, float))
        self.x //= scalar
        self.y //= scalar
        self.z //= scalar
        return self
    
    # Unary operators and comparisons
    def __neg__(self):
        return Vector3(-self.x, -self.y, -self.z)
    
    def __eq__(self, other):
        check_type(other, "other", Vector3)
        return self.x == other.x and self.y == other.y and self.z == other.z
    
    # Access via index (v[0] = x, v[1] = y, v[2] = z)
    def __getitem__(self, index: int):
        if index == 0:
            return self.x
        elif index == 1:
            return self.y
        elif index == 2:
            return self.z
        else:
            raise IndexError("Vector3 index out of range (0-2)")
    
    def __setitem__(self, index: int, value: float):
        check_type(value, "value", (int, float))
        if index == 0:
            self.x = float(value)
        elif index == 1:
            self.y = float(value)
        elif index == 2:
            self.z = float(value)
        else:
            raise IndexError("Vector3 index out of range (0-2)")
    
    # Main methods
    def length(self) -> float:
        """Returns the length of the vector (Euclidian norm)."""
        return math.hypot(self.x, self.y, self.z)
    
    def length_squared(self) -> float:
        """Returns the square of the length of the vector (faster than length())."""
        return self.x ** 2 + self.y ** 2 + self.z ** 2
    
    def normalize(self):
        """Normalizes this vector"""
        length = self.length()
        if length == 0:
            self.x = 0
            self.y = 0
            self.z = 0
        else:
            self.x /= length
            self.y /= length
            self.z /= length

    def normalized(self) -> 'Vector3':
        """Returns normalized vector."""
        length = self.length()
        if length == 0:
            return Vector3(0, 0, 0)
        return Vector3(self.x / length, self.y / length, self.z / length)
    
    def dot(self, other: 'Vector3') -> float:
        """Returns scalar product with the other vector."""
        check_type(other, "other", Vector3)
        return self.x * other.x + self.y * other.y + self.z * other.z
    
    def cross(self, other: 'Vector3') -> 'Vector3':
        """Return vector product with the other vector."""
        check_type(other, "other", Vector3)
        return Vector3(
            self.y * other.z - self.z * other.y,
            self.z * other.x - self.x * other.z,
            self.x * other.y - self.y * other.x
        )
    
    def rotate(self, axis: 'Vector3', angle_degrees: float):
        """Rotates the vector around the specified axis by the specified angle (in degrees)."""
        check_type(axis, "axis", Vector3)
        check_type(angle_degrees, "angle_degrees", (int, float))

        angle_rad = math.radians(angle_degrees)
        cos = math.cos(angle_rad)
        sin = math.sin(angle_rad)
        
        # Rodrigues' rotation formula:
        # v_rot = v * cosθ + (axis × v) * sinθ + axis * (axis · v) * (1 - cosθ)
        cross = axis.cross(self)
        dot = axis.dot(self)
        
        x = self.x * cos + cross.x * sin + axis.x * dot * (1 - cos)
        y = self.y * cos + cross.y * sin + axis.y * dot * (1 - cos)
        z = self.z * cos + cross.z * sin + axis.z * dot * (1 - cos)

        self.x = x
        self.y = y
        self.z = z

    def rotated(self, axis: 'Vector3', angle_degrees: float) -> 'Vector3':
        """Returns rotated vector around the specified axis by the specified angle (in degrees)."""
        check_type(axis, "axis", Vector3)
        check_type(angle_degrees, "angle_degrees", (int, float))

        angle_rad = math.radians(angle_degrees)
        cos = math.cos(angle_rad)
        sin = math.sin(angle_rad)
        
        # Rodrigues' rotation formula:
        # v_rot = v * cosθ + (axis × v) * sinθ + axis * (axis · v) * (1 - cosθ)
        cross = axis.cross(self)
        dot = axis.dot(self)
        
        x = self.x * cos + cross.x * sin + axis.x * dot * (1 - cos)
        y = self.y * cos + cross.y * sin + axis.y * dot * (1 - cos)
        z = self.z * cos + cross.z * sin + axis.z * dot * (1 - cos)
        
        return Vector3(x, y, z)
    
    def distance_to(self, other: 'Vector3') -> float:
        """Returns the distance to the other vector."""
        check_type(other, "other", Vector3)
        return math.hypot(self.x - other.x, self.y - other.y, self.z - other.z)
    
    def lerp(self, other: 'Vector3', alpha: float) -> 'Vector3':
        """Linear interpolation between self and other (alpha ∈ [0, 1])."""
        check_type(other, "other", Vector3)
        check_type(alpha, "alpha", (int, float))
        return Vector3(
            self.x + (other.x - self.x) * alpha,
            self.y + (other.y - self.y) * alpha,
            self.z + (other.z - self.z) * alpha
        )
    
    # Features and alternative constructions
    @property
    def xy(self):
        return (self.x, self.y)

    @xy.setter
    def xy(self, values):
        check_type(values, "values", (tuple, list))
        if len(values) != 2:
            raise ValueError("xy requires 2 values")
        self.x, self.y = float(values[0]), float(values[1])

    @property
    def xz(self):
        return (self.x, self.z)

    @xz.setter
    def xz(self, values):
        check_type(values, "values", (tuple, list))
        if len(values) != 2:
            raise ValueError("xz requires 2 values")
        self.x, self.z = float(values[0]), float(values[1])

    @property
    def yx(self):
        return (self.y, self.x)

    @yx.setter
    def yx(self, values):
        check_type(values, "values", (tuple, list))
        if len(values) != 2:
            raise ValueError("yx requires 2 values")
        self.y, self.x = float(values[0]), float(values[1])

    @property
    def yz(self):
        return (self.y, self.z)

    @yz.setter
    def yz(self, values):
        check_type(values, "values", (tuple, list))
        if len(values) != 2:
            raise ValueError("yz requires 2 values")
        self.y, self.z = float(values[0]), float(values[1])

    @property
    def zx(self):
        return (self.z, self.x)

    @zx.setter
    def zx(self, values):
        check_type(values, "values", (tuple, list))
        if len(values) != 2:
            raise ValueError("zx requires 2 values")
        self.z, self.x = float(values[0]), float(values[1])

    @property
    def zy(self):
        return (self.z, self.y)

    @zy.setter
    def zy(self, values):
        check_type(values, "values", (tuple, list))
        if len(values) != 2:
            raise ValueError("zy requires 2 values")
        self.z, self.y = float(values[0]), float(values[1])

    @property
    def xyz(self):
        return (self.x, self.y, self.z)

    @xyz.setter
    def xyz(self, values):
        check_type(values, "values", (tuple, list))
        if len(values) != 3:
            raise ValueError("xyz requires 3 values")
        self.x, self.y, self.z = float(values[0]), float(values[1]), float(values[2])

    @property
    def xzy(self):
        return (self.x, self.z, self.y)

    @xzy.setter
    def xzy(self, values):
        check_type(values, "values", (tuple, list))
        if len(values) != 3:
            raise ValueError("xzy requires 3 values")
        self.x, self.z, self.y = float(values[0]), float(values[1]), float(values[2])

    @property
    def yxz(self):
        return (self.y, self.x, self.z)

    @yxz.setter
    def yxz(self, values):
        check_type(values, "values", (tuple, list))
        if len(values) != 3:
            raise ValueError("yxz requires 3 values")
        self.y, self.x, self.z = float(values[0]), float(values[1]), float(values[2])

    @property
    def yzx(self):
        return (self.y, self.z, self.x)

    @yzx.setter
    def yzx(self, values):
        check_type(values, "values", (tuple, list))
        if len(values) != 3:
            raise ValueError("yzx requires 3 values")
        self.y, self.z, self.x = float(values[0]), float(values[1]), float(values[2])

    @property
    def zxy(self):
        return (self.z, self.x, self.y)

    @zxy.setter
    def zxy(self, values):
        check_type(values, "values", (tuple, list))
        if len(values) != 3:
            raise ValueError("zxy requires 3 values")
        self.z, self.x, self.y = float(values[0]), float(values[1]), float(values[2])

    @property
    def zyx(self):
        return (self.z, self.y, self.x)

    @zyx.setter
    def zyx(self, values):
        check_type(values, "values", (tuple, list))
        if len(values) != 3:
            raise ValueError("zyx requires 3 values")
        self.z, self.y, self.x = float(values[0]), float(values[1]), float(values[2])
    
    def copy(self):
        return Vector3(self.x, self.y, self.z)

    def __repr__(self):
        return f"Vector3({self.x}, {self.y}, {self.z})"
