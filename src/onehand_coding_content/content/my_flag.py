import turtle
import math
import random

# Screen and Turtle Setup
screen = turtle.Screen()
screen.setup(width=900, height=600)
screen.bgcolor("#2F4F4F") # Dark Slate Gray
screen.title("Watawat ng Pilipinas - Onehand-Coding")
screen.tracer(0)  # Turn off automatic screen updates for smooth animation

t = turtle.Turtle()
t.speed(0)
t.hideturtle()

# Flag Specifications and Constants
# Official Hex Color Codes
COLOR_BLUE = "#0038A8"
COLOR_RED = "#CE1126"
COLOR_YELLOW = "#FCD116"
COLOR_WHITE = "#FFFFFF"

# Flag Dimensions (maintaining the 1:2 ratio)
FLAG_WIDTH = 500
FLAG_HEIGHT = 250
START_X = -250
START_Y = -125

# Animation Parameters
WAVE_AMPLITUDE = 10
WAVE_FREQUENCY = 0.02
WAVE_SPEED = 0.05

# Helper Functions
def get_wave_offset(x, frame):
    """Calculates the vertical (y) offset for a given horizontal (x) position to create a wave."""
    return WAVE_AMPLITUDE * math.sin(WAVE_FREQUENCY * x + frame * WAVE_SPEED)

def draw_star(x, y, size, angle, frame):
    """Draws a single, filled 5-pointed star with a specific orientation."""
    t.penup()
    # Apply wave effect to the star's position
    wave_offset = get_wave_offset(x - START_X, frame)
    t.goto(x, y + wave_offset)
    t.setheading(angle)
    t.pendown()
    t.color(COLOR_YELLOW)
    t.begin_fill()
    for _ in range(5):
        t.forward(size)
        t.right(144)
    t.end_fill()

def draw_hacker_elements():
    """Draws subtle futuristic elements in the background."""
    hacker_turtle = turtle.Turtle()
    hacker_turtle.speed(0)
    hacker_turtle.hideturtle()
    hacker_turtle.penup()
    hacker_turtle.color("lime green") # Glowing green
    hacker_turtle.pensize(1)

    # Draw random glowing lines
    for _ in range(20):
        hacker_turtle.goto(random.randint(-450, 450), random.randint(-300, 300))
        hacker_turtle.pendown()
        hacker_turtle.setheading(random.randint(0, 360))
        hacker_turtle.forward(random.randint(50, 150))
        hacker_turtle.penup()

    # Draw some small, abstract circuit-like shapes
    for _ in range(10):
        hacker_turtle.goto(random.randint(-450, 450), random.randint(-300, 300))
        hacker_turtle.pendown()
        hacker_turtle.setheading(random.randint(0, 360))
        for _ in range(random.randint(2, 4)):
            hacker_turtle.forward(random.randint(10, 30))
            hacker_turtle.left(random.choice([90, -90]))
        hacker_turtle.penup()

# Main Drawing Function
def draw_flag(frame):
    """Clears the screen and redraws the entire waving flag for a single animation frame."""
    t.clear()

    # --- Draw Blue and Red Bands ---
    for x_step in range(FLAG_WIDTH + 1):
        x = START_X + x_step
        y_offset = get_wave_offset(x_step, frame)

        t.pencolor(COLOR_BLUE)
        t.penup()
        t.goto(x, START_Y + FLAG_HEIGHT / 2 + y_offset)
        t.pendown()
        t.goto(x, START_Y + FLAG_HEIGHT + y_offset)

        t.pencolor(COLOR_RED)
        t.penup()
        t.goto(x, START_Y + y_offset)
        t.pendown()
        t.goto(x, START_Y + FLAG_HEIGHT / 2 + y_offset)

    # --- Draw White Triangle ---
    triangle_side = FLAG_HEIGHT
    triangle_height_dist = triangle_side * math.sqrt(3) / 2

    p1_x, p1_y = START_X, START_Y + triangle_side + get_wave_offset(0, frame)
    p2_x, p2_y = START_X, START_Y + get_wave_offset(0, frame)
    p3_x, p3_y = START_X + triangle_height_dist, START_Y + (triangle_side / 2) + get_wave_offset(triangle_height_dist, frame)

    t.penup()
    t.goto(p1_x, p1_y)
    t.pendown()
    t.color(COLOR_WHITE)
    t.begin_fill()
    t.goto(p2_x, p2_y)
    t.goto(p3_x, p3_y)
    t.goto(p1_x, p1_y)
    t.end_fill()

    # --- Draw Sun ---
    sun_center_x = START_X + triangle_height_dist / 3
    sun_center_y = START_Y + FLAG_HEIGHT / 2
    sun_radius = 20
    ray_length = 35

    sun_wave_offset = get_wave_offset(sun_center_x - START_X, frame)

    # Draw sun rays
    for i in range(8):
        t.penup()
        t.goto(sun_center_x, sun_center_y + sun_wave_offset)
        t.setheading(90 + i * 45) # Set direction for each ray
        t.forward(sun_radius - 5)
        t.pendown()
        t.color(COLOR_YELLOW)
        t.begin_fill()
        t.left(10)
        t.forward(ray_length)
        t.right(170)
        t.forward(ray_length)
        t.end_fill()

    # Draw central circle of the sun
    t.penup()
    # Reset the heading before drawing the circle
    t.setheading(0)
    t.goto(sun_center_x, sun_center_y - sun_radius + sun_wave_offset)
    t.pendown()
    t.color(COLOR_YELLOW)
    t.begin_fill()
    t.circle(sun_radius)
    t.end_fill()

    # --- Draw Stars ---
    star_size = 12
    star_margin_x = FLAG_HEIGHT * 0.15
    star_margin_y = FLAG_HEIGHT * 0.18

    draw_star(START_X + star_margin_x, START_Y + FLAG_HEIGHT - star_margin_y, star_size, 90, frame)
    draw_star(START_X + star_margin_x, START_Y + star_margin_y, star_size, -90, frame)
    draw_star(START_X + triangle_height_dist - star_margin_x * 1.5, START_Y + FLAG_HEIGHT / 2, star_size, 0, frame)

# Animation Loop
def animate():
    """Main animation loop."""
    draw_hacker_elements()

    frame = 0
    while True:
        frame += 1
        draw_flag(frame)
        screen.update()

# Start the animation
animate()
turtle.done()
