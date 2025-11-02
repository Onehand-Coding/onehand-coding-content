import turtle
import math
import random
import time

# --- Setup the screen ---
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Enhanced Futuristic Power Brand Animation")
screen.tracer(0)

class PowerSymbol:
    # --- BRAND-SPECIFIC COLORS ---
    MY_BRAND_PRIMARY_COLOR = "#00FF00"  # A vibrant green
    MY_BRAND_ACCENT_COLOR = "#00BFFF"    # A bright sky blue/cyan for highlights

    # Internal colors for subtle effects, derived or complementary
    DARK_BACKGROUND_GREEN = "#002211"    # Darker shade for background glow
    GLITCH_COLOR = "#FF00FF"             # Magenta for a sharp glitch effect
    SPARK_COLOR = "#FFFF00"              # Yellow for sparks

    def __init__(self):
        self.center_x = 0
        self.center_y = 0
        self.main_radius = 80
        self.inner_radius = 50

        # Create turtles for each element
        self.power_button = self._create_turtle()
        self.energy_lines = [self._create_turtle() for _ in range(30)] # More lines
        self.particles = [self._create_turtle(shape="circle", size=0.3) for _ in range(25)] # More particles
        self.glow_effect = self._create_turtle()
        self.background_grid = self._create_turtle() # For background pattern
        self.shockwave = self._create_turtle()      # For central pulse
        self.sparks = [self._create_turtle(shape="triangle", size=0.2) for _ in range(10)] # For small sparks

        # --- Animation state variables ---
        self.pulse_angle = 0
        self.rotation_angle = 0
        self.arc_progress = 0
        self.particle_positions = []
        self.shockwave_radius = 0 #
        self.shockwave_opacity = 0 #
        self.spark_data = [] #

        self._initialize_particles()
        self._initialize_sparks()

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

    def _initialize_sparks(self):
        """Set up initial random states for spark particles."""
        for _ in self.sparks:
            self.spark_data.append({
                'x': 0, 'y': 0, 'life': 0, 'max_life': random.randint(5, 15),
                'dx': random.uniform(-5, 5), 'dy': random.uniform(-5, 5)
            })

    def draw_background_grid(self, rotation):
        """Draws a subtle, expanding/contracting hexagonal grid or circuit pattern."""
        self.background_grid.clear()
        self.background_grid.pensize(1)

        # Simulate transparency by using a very dark version of the primary color
        r, g, b = int(self.MY_BRAND_PRIMARY_COLOR[1:3], 16), int(self.MY_BRAND_PRIMARY_COLOR[3:5], 16), int(self.MY_BRAND_PRIMARY_COLOR[5:7], 16)
        fade_color = f"#{int(r*0.1):02x}{int(g*0.1):02x}{int(b*0.1):02x}" # 10% intensity
        self.background_grid.color(fade_color)

        num_lines = 16
        max_dist = 400
        min_dist = 50

        # Animate expansion/contraction
        anim_factor = (math.sin(math.radians(self.pulse_angle / 2)) + 1) / 2
        current_max_dist = min_dist + (max_dist - min_dist) * anim_factor

        for i in range(num_lines):
            angle_rad = math.radians((360 / num_lines) * i + rotation / 5) # Slower rotation

            # Draw lines radiating outwards
            start_x = self.center_x + min_dist * math.cos(angle_rad)
            start_y = self.center_y + min_dist * math.sin(angle_rad)
            end_x = self.center_x + current_max_dist * math.cos(angle_rad)
            end_y = self.center_y + current_max_dist * math.sin(angle_rad)

            self.background_grid.penup()
            self.background_grid.goto(start_x, start_y)
            self.background_grid.pendown()
            self.background_grid.goto(end_x, end_y)
            self.background_grid.penup()

            # Draw a subtle ring element
            if i % 4 == 0:
                ring_radius = min_dist + (current_max_dist - min_dist) * (i / num_lines)
                self.background_grid.penup()
                self.background_grid.goto(self.center_x, self.center_y - ring_radius)
                self.background_grid.pendown()
                self.background_grid.circle(ring_radius, steps=12) # Hexagonal-ish
                self.background_grid.penup()


    def draw_power_button(self, pulse_factor, arc_extent):
        """Draw the main power button symbol, with a correctly centered animated arc."""
        self.power_button.clear()

        current_radius = self.main_radius + (pulse_factor * 10)
        inner_radius = self.inner_radius + (pulse_factor * 8)

        self.power_button.color(self.MY_BRAND_PRIMARY_COLOR)

        # Draw the static outer ring
        self.power_button.pensize(5)
        self.power_button.setheading(0) # Reset heading for correct circle drawing
        self.power_button.goto(self.center_x, self.center_y - current_radius)
        self.power_button.pendown()
        self.power_button.circle(current_radius)
        self.power_button.penup()

        # Draw the DYNAMIC inner arc using a reliable math loop
        self.power_button.pensize(4)
        is_pen_down = False

        for angle in range(0, int(arc_extent)):
            rad_angle = math.radians(angle - 90) # Adjust for turtle's 0-degree being East

            x = self.center_x + inner_radius * math.cos(rad_angle)
            y = self.center_y + inner_radius * math.sin(rad_angle)

            self.power_button.goto(x, y)
            if not is_pen_down:
                self.power_button.pendown()
                is_pen_down = True

        self.power_button.penup()

        # Draw the central power line
        self.power_button.pensize(7)
        self.power_button.goto(self.center_x, self.center_y)
        self.power_button.setheading(90) # Point up
        self.power_button.pendown()
        self.power_button.forward(inner_radius * 0.8)
        self.power_button.penup()

    def draw_energy_lines(self, rotation, pulse_factor):
        """Draw radiating energy lines around the power symbol, with glitches."""
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

            # Store the chosen color in a variable first to avoid the error.
            chosen_color = ""
            if random.random() < 0.02: # 2% chance to glitch
                chosen_color = self.GLITCH_COLOR
                line.pensize(random.choice([1, 6])) # Randomize width
            else:
                chosen_color = random.choice([self.MY_BRAND_PRIMARY_COLOR, self.MY_BRAND_ACCENT_COLOR])
                line.pensize(random.choice([1, 2]))

            # Set the turtle's color using the variable
            line.color(chosen_color)

            line.goto(start_x, start_y)
            line.pendown()
            line.goto(end_x, end_y)
            line.penup()

            # Add a dot at the end for some lines
            if random.random() > 0.6:
                line.goto(end_x, end_y)
                # Use the 'chosen_color' variable here instead of calling line.color()
                line.dot(random.randint(3, 6), chosen_color)


    def draw_glow_effect(self, pulse_factor):
        """Draw a subtle glow effect around the power button."""
        self.glow_effect.clear()
        for i in range(3):
            radius = self.main_radius + 20 + (i * 12) + (pulse_factor * 15)
            self.glow_effect.color(self.DARK_BACKGROUND_GREEN) # Use dark green for depth
            self.glow_effect.goto(self.center_x, self.center_y - radius)
            self.glow_effect.pendown()
            self.glow_effect.pensize(i * 4 + 2)
            self.glow_effect.circle(radius)
            self.glow_effect.penup()

    def update_particles(self):
        """Update and draw floating energy particles."""
        for particle, pos in zip(self.particles, self.particle_positions):
            pos['angle'] += pos['speed']

            orbit_x = pos['orbit_radius'] * math.cos(math.radians(pos['angle'] * 3))
            orbit_y = pos['orbit_radius'] * math.sin(math.radians(pos['angle'] * 2))
            main_x = self.center_x + pos['radius'] * math.cos(math.radians(pos['angle']))
            main_y = self.center_y + pos['radius'] * math.sin(math.radians(pos['angle']))

            particle.goto(main_x + orbit_x, main_y + orbit_y)
            particle.showturtle()

            fade = (math.sin(math.radians(pos['angle'] * 2)) + 1) / 2
            size = 0.1 + fade * 0.3
            particle.shapesize(size, size)

            # Alternate colors based on brand palette
            if int(pos['angle']) % 180 < 90:
                 particle.color(self.MY_BRAND_PRIMARY_COLOR)
            else:
                 particle.color(self.MY_BRAND_ACCENT_COLOR)

    def draw_shockwave(self):
        """Draws an expanding shockwave from the center."""
        self.shockwave.clear()
        if self.shockwave_opacity <= 0:
            return

        # Use an RGBA color string to control alpha (transparency)
        # Note: Turtle's color function doesn't directly support RGBA huwag kalimutan.
        # We simulate it by blending with black or reducing intensity.
        # For simplicity, we'll just reduce intensity.

        # Convert hex to RGB, then reduce intensity for "fade"
        r, g, b = int(self.MY_BRAND_PRIMARY_COLOR[1:3], 16), int(self.MY_BRAND_PRIMARY_COLOR[3:5], 16), int(self.MY_BRAND_PRIMARY_COLOR[5:7], 16)
        fade_factor = max(0, min(1, self.shockwave_opacity)) # Ensure factor is between 0 and 1

        current_r = int(r * fade_factor)
        current_g = int(g * fade_factor)
        current_b = int(b * fade_factor)

        color_str = f"#{current_r:02x}{current_g:02x}{current_b:02x}"
        self.shockwave.color(color_str)
        self.shockwave.pensize(2)

        self.shockwave.goto(self.center_x, self.center_y - self.shockwave_radius)
        self.shockwave.pendown()
        self.shockwave.circle(self.shockwave_radius)
        self.shockwave.penup()

    def update_sparks(self):
        """Updates and draws small, short-lived spark particles."""
        for i, (spark, data) in enumerate(zip(self.sparks, self.spark_data)):
            if data['life'] > 0:
                # Move spark
                data['x'] += data['dx']
                data['y'] += data['dy']
                spark.goto(data['x'], data['y'])
                spark.showturtle()

                # Fade spark by reducing size and color intensity
                fade_factor = data['life'] / data['max_life']
                size = 0.1 + fade_factor * 0.2
                spark.shapesize(size, size)

                r, g, b = int(self.SPARK_COLOR[1:3], 16), int(self.SPARK_COLOR[3:5], 16), int(self.SPARK_COLOR[5:7], 16)
                current_r = int(r * fade_factor)
                current_g = int(g * fade_factor)
                current_b = int(b * fade_factor)
                spark.color(f"#{current_r:02x}{current_g:02x}{current_b:02x}")

                data['life'] -= 1
            else:
                spark.hideturtle()
                # Respawn spark around the power button
                if random.random() < 0.05: # Chance to respawn
                    angle = random.uniform(0, 360)
                    radius_offset = random.uniform(self.inner_radius * 0.7, self.main_radius * 1.2)
                    data['x'] = self.center_x + radius_offset * math.cos(math.radians(angle))
                    data['y'] = self.center_y + radius_offset * math.sin(math.radians(angle))
                    data['life'] = data['max_life']
                    data['dx'] = random.uniform(-3, 3)
                    data['dy'] = random.uniform(-3, 3)


    def animate(self):
        """Main animation loop that updates and redraws the scene."""
        frame_count = 0
        while True:
            try:
                frame_count += 1
                # --- Update animation variables for the next frame ---
                self.pulse_angle += 3
                self.rotation_angle -= 0.7
                self.arc_progress = (self.arc_progress + 4)
                if self.arc_progress > 360: # Changed to 360 for full loop, then reset
                    self.arc_progress = 10

                pulse_factor = (math.sin(math.radians(self.pulse_angle)) + 1) / 2

                # : Shockwave animation
                if frame_count % 60 == 0: # Trigger a shockwave every 60 frames (approx 2 seconds)
                    self.shockwave_radius = 0
                    self.shockwave_opacity = 1.0

                if self.shockwave_opacity > 0:
                    self.shockwave_radius += 5
                    self.shockwave_opacity -= 0.05
                    if self.shockwave_radius > self.main_radius * 2: # Max radius
                        self.shockwave_opacity = 0 # Hide it

                # --- Draw elements from back to front ---
                self.draw_background_grid(self.rotation_angle) # : Background element
                self.draw_glow_effect(pulse_factor)
                self.draw_shockwave() # : Draw shockwave before energy lines
                self.draw_energy_lines(self.rotation_angle, pulse_factor)
                self.update_particles()
                self.update_sparks() # : Update and draw sparks
                self.draw_power_button(pulse_factor, self.arc_progress)

                screen.update()
                time.sleep(0.03)

            except turtle.Terminator:
                print("Animation window closed.")
                break
            except KeyboardInterrupt:
                print("\nAnimation stopped by user.")
                break

def main():
    try:
        print("Starting Enhanced Futuristic Power Brand Animation...")
        print("Remember to update MY_BRAND_PRIMARY_COLOR and MY_BRAND_ACCENT_COLOR in the code!")
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
            pass

if __name__ == "__main__":
    main()
