import turtle
import math
import colorsys

# Set up the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.title("Cosmic Waves")
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

def draw_cosmic_waves():
    """Draw flowing energy waves like cosmic currents"""
    artist.clear()

    # Draw multiple wave layers
    num_waves = 6
    for wave_layer in range(num_waves):
        wave_offset = wave_layer * 60
        amplitude = 40 + wave_layer * 15
        frequency = 0.02 + wave_layer * 0.005

        # Each wave line
        points = []
        for x in range(-400, 401, 8):
            # Multiple sine waves combined
            y1 = math.sin((x + frame * 2) * frequency) * amplitude
            y2 = math.sin((x + frame * 1.5 + wave_offset) * frequency * 1.3) * (amplitude * 0.6)
            y3 = math.sin((x + frame * 3 + wave_offset * 2) * frequency * 0.7) * (amplitude * 0.3)

            y = y1 + y2 + y3 + wave_layer * 30 - 150
            points.append((x, y))

        # Draw the wave with color gradient
        for i, (x, y) in enumerate(points[:-1]):
            color_time = frame + x / 3 + wave_layer * 40
            rgb = get_cosmic_color(color_time, 0.55 + wave_layer * 0.05)
            artist.color(rgb)
            artist.pensize(2 + wave_layer * 0.3)

            artist.penup()
            artist.goto(x, y)
            artist.pendown()

            next_x, next_y = points[i + 1]
            artist.goto(next_x, next_y)

            # Add energy particles along waves
            if i % 20 == 0:
                particle_brightness = 0.4 + 0.6 * abs(math.sin(frame / 6 + i + wave_layer))
                if particle_brightness > 0.7:
                    particle_color = get_cosmic_color(color_time + 50, 0.7)
                    artist.dot(3, particle_color)

def continuous_waves_animation():
    """Main animation loop for the cosmic waves"""
    global frame

    draw_cosmic_waves()
    screen.update()
    frame += 1

    # 30 FPS
    screen.ontimer(continuous_waves_animation, 33)

# Start the animation
print("🌊 Starting Cosmic Waves Animation...")
print("✨ Watch the flowing energy currents with glowing particles!")
print("🔷 Click the window to stop.")

try:
    continuous_waves_animation()
    screen.exitonclick()
except turtle.Terminator:
    print("Cosmic waves animation stopped.")
except Exception as e:
    print(f"Error: {e}")
    screen.exitonclick()
