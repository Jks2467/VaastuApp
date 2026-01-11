import math

DIRECTIONS_16 = [
    "N","NNE","NE","ENE","E","ESE","SE","SSE",
    "S","SSW","SW","WSW","W","WNW","NW","NNW"
]

def centroid(block):
    cx = (block["x0"] + block["x1"]) / 2
    cy = (block["top"] + block["bottom"]) / 2
    return cx, cy

def angle_from_center(cx, cy, px, py):
    dx = cx - px
    dy = py - cy  # invert Y
    return (math.degrees(math.atan2(dx, dy)) + 360) % 360

def angle_to_direction(angle):
    idx = int((angle + 11.25) // 22.5) % 16
    return DIRECTIONS_16[idx]


