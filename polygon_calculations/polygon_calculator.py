import math

def polygon_diagonals(polygon_sides):
    diagonals = (polygon_sides * (polygon_sides - 3)) / 2
    print(f'The number of diagonals of the polygon: {diagonals}')
    return diagonals

def polygon_interior_angles_sum(polygon_sides):
    angles_sum = 180 * (polygon_sides - 2)
    print(f'The sum of the interior angles of a polygon: {angles_sum}°')
    return angles_sum

def polygon_interior_angle(polygon_sides):
    interior_angle = round(((polygon_sides - 2) * 180) / polygon_sides, 2)
    print(f'Interior angle of polygon: {interior_angle}°')
    return interior_angle

def circumscribed_circle_radius(polygon_sides, side_length):
    radius = round(side_length / (2 * math.sin(math.pi / polygon_sides)), 2)
    print(f'Radius of the circumscribed circle: {radius}')
    return radius

def inscribed_circle_radius(polygon_sides, side_length):
    radius = round(side_length / (2 * math.tan(math.pi / polygon_sides)), 2)
    print(f'Radius of the circle inscribed in a polygon: {radius}')
    return radius

def area_of_polygon(polygon_sides, side_length):
    area = round((polygon_sides * side_length**2) / (4 * math.tan(math.pi / polygon_sides)), 2)
    print(f'Area of the polygon: {area}')
    return area

def polygon_all_data(polygon_sides, side_length):
    polygon_diagonals(polygon_sides)
    polygon_interior_angles_sum(polygon_sides)
    polygon_interior_angle(polygon_sides)
    circumscribed_circle_radius(polygon_sides, side_length)
    inscribed_circle_radius(polygon_sides, side_length)
    area_of_polygon(polygon_sides, side_length)
