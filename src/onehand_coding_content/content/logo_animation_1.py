import turtle
import math
import random
import time

# --- Setup the screen ---
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Futuristic Power Brand Animation")
# Turn off automatic screen updates for smooth, flicker-free animation
screen.tracer(0)

class PowerSymbol:
    # --- A more futuristic color palette ---
    PRIMARY_GREEN = "#00ff9f"  # A bright, minty green
    ACCENT_CYAN = "#00e5ff"    # A vibrant cyan for highlights
    DARK_GREEN = "#003322"     # A dark green for subtle glows

    def __init__(self):
        self.center_x = 0
        self.center_y = 0
        self.main_radius = 80
        self.inner_radius = 50

        # Create turtles for each element
        self.power_button = self._create_turtle()
        self.energy_lines = [self._create_turtle() for _ in range(24)]
        self.particles = [self._create_turtle(shape="circle", size=0.3) for _ in range(20)]
        self.glow_effect = self._create_turtle()

        # --- Animation state variables ---
        self.pulse_angle = 0
        self.rotation_angle = 0
        # NEW: This variable will control the drawing of the central arc
        self.arc_progress = 0
        self.particle_positions = []

        # Initialize particles with random orbits
        self._initialize_particles()

    def _create_turtle(self, shape="classic", size=1.0):
        """Helper function to create and configure a new turtle."""
        t = turtle.Turtle()
        t.speed(0)
        t.penup()
        t.shape(shape)
        if shape != "classic":
            t.shapesize(size, size)
        t.hideturtle()
        return t

    def _initialize_particles(self):
        """Set up initial random positions and speeds for particles."""
        for _ in self.particles:
            self.particle_positions.append({
                'angle': random.uniform(0, 360),
                'radius': random.uniform(100, 250),
                'speed': random.uniform(0.5, 1.5),
                'orbit_radius': random.uniform(5, 15)
            })

    def draw_power_button(self, pulse_factor, arc_extent):
        """Draw the main power button symbol, with a correctly centered animated arc."""
        self.power_button.clear()

        # Calculate pulsing size
        current_radius = self.main_radius + (pulse_factor * 10)
        inner_radius = self.inner_radius + (pulse_factor * 8)

        self.power_button.color(self.PRIMARY_GREEN)

        # --- Draw the static outer ring ---
        self.power_button.pensize(5)
        # Reset the turtle's heading to 0 (East) to ensure the circle is centered
        self.power_button.setheading(0)
        self.power_button.goto(self.center_x, self.center_y - current_radius)
        self.power_button.pendown()
        self.power_button.circle(current_radius)
        self.power_button.penup()

        # --- Draw the DYNAMIC inner arc using a reliable math loop ---
        self.power_button.pensize(4)
        is_pen_down = False

        for angle in range(0, int(arc_extent)):
            rad_angle = math.radians(angle - 90)

            x = self.center_x + inner_radius * math.cos(rad_angle)
            y = self.center_y + inner_radius * math.sin(rad_angle)

            self.power_button.goto(x, y)
            if not is_pen_down:
                self.power_button.pendown()
                is_pen_down = True

        self.power_button.penup()

        # --- Draw the central power line ---
        self.power_button.pensize(7)
        self.power_button.goto(self.center_x, self.center_y)
        self.power_button.setheading(90) # Point up
        self.power_button.pendown()
        self.power_button.forward(inner_radius * 0.8)
        self.power_button.penup()


    def draw_energy_lines(self, rotation, pulse_factor):
        """Draw radiating energy lines around the power symbol."""
        num_lines = len(self.energy_lines)
        for i, line in enumerate(self.energy_lines):
            line.clear()
            angle_rad = math.radians((360 / num_lines) * i + rotation)

            line_length = 60 + (pulse_factor * 20) + random.uniform(-10, 10)
            start_radius = 100 + (pulse_factor * 15)

            start_x = self.center_x + start_radius * math.cos(angle_rad)
            start_y = self.center_y + start_radius * math.sin(angle_rad)
            end_x = self.center_x + (start_radius + line_length) * math.cos(angle_rad)
            end_y = self.center_y + (start_radius + line_length) * math.sin(angle_rad)

            # Use the new color palette
            line.color(random.choice([self.PRIMARY_GREEN, self.ACCENT_CYAN]))
            line.pensize(random.choice([1, 2]))

            line.goto(start_x, start_y)
            line.pendown()
            line.goto(end_x, end_y)
            line.penup()

    def draw_glow_effect(self, pulse_factor):
        """Draw a subtle glow effect around the power button."""
        self.glow_effect.clear()
        for i in range(3):
            radius = self.main_radius + 20 + (i * 12) + (pulse_factor * 15)
            # Use the dark green for a subtle, atmospheric glow
            self.glow_effect.color(self.DARK_GREEN)
            self.glow_effect.goto(self.center_x, self.center_y - radius)
            self.glow_effect.pendown()
            self.glow_effect.pensize(i * 4 + 2)
            self.glow_effect.circle(radius)
            self.glow_effect.penup()


    def update_particles(self):
        """Update and draw floating energy particles."""
        for particle, pos in zip(self.particles, self.particle_positions):
            pos['angle'] += pos['speed']

            # Combine main circular motion with a smaller orbital motion
            orbit_x = pos['orbit_radius'] * math.cos(math.radians(pos['angle'] * 3))
            orbit_y = pos['orbit_radius'] * math.sin(math.radians(pos['angle'] * 2))
            main_x = self.center_x + pos['radius'] * math.cos(math.radians(pos['angle']))
            main_y = self.center_y + pos['radius'] * math.sin(math.radians(pos['angle']))

            particle.goto(main_x + orbit_x, main_y + orbit_y)
            particle.showturtle()

            # Fade effect by changing size
            fade = (math.sin(math.radians(pos['angle'] * 2)) + 1) / 2
            size = 0.1 + fade * 0.3
            particle.shapesize(size, size)

            # Alternate colors for a more dynamic feel
            if int(pos['angle']) % 180 < 90:
                 particle.color(self.PRIMARY_GREEN)
            else:
                 particle.color(self.ACCENT_CYAN)

    def animate(self):
        """Main animation loop that updates and redraws the scene."""
        while True:
            try:
                # --- Update animation variables for the next frame ---
                self.pulse_angle += 3
                self.rotation_angle -= 0.7  # Rotate counter-clockwise
                # Increment the arc progress, looping back to a small value
                # It increases by 4 each frame and loops when it reaches 320.
                self.arc_progress = (self.arc_progress + 4)
                if self.arc_progress > 320:
                    self.arc_progress = 10 # Reset to a small gap, not zero


                # Calculate a smooth "breathing" effect using sine
                pulse_factor = (math.sin(math.radians(self.pulse_angle)) + 1) / 2

                # --- Draw elements from back to front ---
                self.draw_glow_effect(pulse_factor)
                self.draw_energy_lines(self.rotation_angle, pulse_factor)
                self.update_particles()
                self.draw_power_button(pulse_factor, self.arc_progress)

                # Update the screen with the new frame
                screen.update()
                time.sleep(0.03) # Control frame rate

            except turtle.Terminator:
                print("Animation window closed.")
                break
            except KeyboardInterrupt:
                print("\nAnimation stopped by user.")
                break

def main():
    try:
        print("Starting Futuristic Power Brand Animation...")
        print("Press Ctrl+C in the terminal or close the window to exit.")
        power_symbol = PowerSymbol()
        power_symbol.animate()
    except Exception as e:
        print(f"An unexpected error occurred: {e}")
    finally:
        print("Exiting.")
        try:
            screen.bye()
        except turtle.Terminator:
            pass # Screen already closed

if __name__ == "__main__":
    main()
