import turtle
import math
import colorsys

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Spiral Galaxy")
screen.setup(width=800, height=800)
screen.tracer(0)

# Create turtle
artist = turtle.Turtle()
artist.speed(0)
artist.pensize(1)
artist.hideturtle()

# Animation state
frame = 0

def get_cosmic_color(t, base_hue=0.6):
    """Get cosmic colors - deep blues, purples, and cyans"""
    hue = (base_hue + (t % 200) / 200.0 * 0.4) % 1.0  # Blue to purple range
    saturation = 0.8 + 0.2 * math.sin(t / 20)
    brightness = 0.7 + 0.3 * math.sin(t / 15)
    rgb = colorsys.hsv_to_rgb(hue, saturation, brightness)
    return rgb

def draw_spiral_galaxy():
    """Draw an evolving spiral galaxy with arms and stars"""
    artist.clear()

    # Draw galaxy arms
    num_arms = 3
    for arm in range(num_arms):
        arm_offset = (360 / num_arms) * arm

        # Each spiral arm
        for i in range(120):
            # Color evolution along the arm
            color_time = frame + i * 2 + arm * 80
            rgb = get_cosmic_color(color_time, 0.6)
            artist.color(rgb)

            # Spiral mathematics with rotation
            angle = math.radians(i * 4 + frame * 0.5 + arm_offset)
            radius = i * 1.8 + math.sin(frame / 30 + arm) * 20

            # Calculate position
            x = radius * math.cos(angle)
            y = radius * math.sin(angle)

            artist.penup()
            artist.goto(x, y)
            artist.pendown()

            # Draw small curved segments
            artist.circle(8 + math.sin(frame / 20 + i) * 3, 30)

            # Add bright stars at intervals
            if i % 15 == 0:
                star_brightness = 0.3 + 0.7 * abs(math.sin(frame / 8 + i + arm))
                if star_brightness > 0.7:
                    artist.dot(4, (1, 1, 1))
                elif star_brightness > 0.5:
                    artist.dot(2, (0.8, 0.9, 1))

    # Central bright core
    artist.penup()
    artist.goto(0, 0)
    core_brightness = 0.5 + 0.5 * math.sin(frame / 12)
    core_color = (1, 0.9 + 0.1 * math.sin(frame / 10), 0.7)
    artist.dot(15 + 5 * math.sin(frame / 15), core_color)

def continuous_galaxy_animation():
    """Main animation loop for the spiral galaxy"""
    global frame

    draw_spiral_galaxy()
    screen.update()
    frame += 1

    # 30 FPS
    screen.ontimer(continuous_galaxy_animation, 33)

# Start the animation
print("🌌 Starting Spiral Galaxy Animation...")
print("✨ Watch the cosmic spiral arms rotate with twinkling stars!")
print("🔷 Click the window to stop.")

try:
    continuous_galaxy_animation()
    screen.exitonclick()
except turtle.Terminator:
    print("Galaxy animation stopped.")
except Exception as e:
    print(f"Error: {e}")
    screen.exitonclick()
