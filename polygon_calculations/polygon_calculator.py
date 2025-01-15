import math

def polygon_diagonals(polygon_sides:int) -> int:
    diagonals = round((polygon_sides * (polygon_sides - 3)) / 2)
    print(f'The number of diagonals of the polygon: {diagonals}')

def polygon_interior_angles_sum(polygon_sides:int) -> int:
    angles_sum = 180 * (polygon_sides - 2)
    print(f'The sum of the interior angles of a polygon: {angles_sum}°')

def polygon_interior_angle(polygon_sides:int) -> float:
    interior_angle = round(((polygon_sides - 2) * 180) / polygon_sides, 2)
    print(f'Interior angle of polygon: {interior_angle}°')

def circumscribed_circle_radius(polygon_sides:int, side_length:float) -> float:
    radius = round(side_length / (2 * math.sin(math.pi / polygon_sides)), 2)
    print(f'Radius of the circumscribed circle: {radius}')

def inscribed_circle_radius(polygon_sides:int, side_length:float) -> float:
    radius = round(side_length / (2 * math.tan(math.pi / polygon_sides)), 2)
    print(f'Radius of the circle inscribed in a polygon: {radius}')

def area_of_polygon(polygon_sides:int, side_length:float) -> float:
    area = round((polygon_sides * side_length**2) / (4 * math.tan(math.pi / polygon_sides)), 2)
    print(f'Area of the polygon: {area}')

def polygon_all_data(polygon_sides:int, side_length:float) -> str:
    polygon_diagonals(polygon_sides)
    polygon_interior_angles_sum(polygon_sides)
    polygon_interior_angle(polygon_sides)
    circumscribed_circle_radius(polygon_sides, side_length)
    inscribed_circle_radius(polygon_sides, side_length)
    area_of_polygon(polygon_sides, side_length)
