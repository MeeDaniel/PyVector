# PyVector
This is just a regular lib with Vector2 and Vector3 classes

## This is AI's product
Most of these features writed by DeepSeek

## What is supported?
1. Float coordinates `x`, `y` for `Vector2` and `x`, `y`, `z` for `Vector3`
2. Defualt operators such as `+`, `-`, `*`, `/`, `//`
3. In-place operators such as `+=`, `-=`, `*=`, `/=`, `//=`
4. Unary operators and comparisons:
    ```py
    a = Vector2(1, 2)
    not a # Vector2(-1.0, -2.0)
    b = Vector2(-1, -2)
    a == b # True
5. Access via index (v[0] = x, v[1] = y, v[2] = z)
6. Math operations with vectors:
    * Vector length `.length() -> float`
    * Vector length squared `.length_squared() -> float`
    * Normalized vector `.normalized() -> Vector`
    * Normalize current vector `.normalize() -> None`
    * Dot product `.dot(other: Vector) -> float`
    * Vector product `.cross(other: Vector) -> Vector3 (or floar for Vector2)`
    * Rotated Vector2 `.rotated(angle_degrees: float) -> Vector2
    * Rotate current Vector2 `.rotate(angle_degrees: float) -> None`
    * Rotated Vector3 `.rotated(axis: Vector3, angle_degrees: float) -> Vector3`
    * Rotate current Vector3 `.rotate(axis: Vector3, angle_degrees: float) -> None`
    * Distance between two vectors `.distance_to(other: Vector) -> float`
    * Linear interpolation `.lerp(other: Vector, alpha: float) -> Vector` (alpha ∈ [0, 1])
7. Class -> tuple via `.xyz`, `.zyx`, etc.
8. Class -> tuple[int, int] via `.intxy`, `.intyx` **(Not realised for Vector3)**
9. `Vector2.from_angle(angle_degrees: float, length: float) -> Vector2`. **(There is no synonym for Vector3)**
10. `.copy` method

