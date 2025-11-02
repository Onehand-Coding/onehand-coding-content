import turtle
import math
import random
import time

# Setup the screen
screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Power Brand - Animated Screensaver")
screen.tracer(0)  # Turn off animation for smoother drawing

class PowerSymbol:
    def __init__(self):
        self.center_x = 0
        self.center_y = 0
        self.main_radius = 80
        self.inner_radius = 50
        self.power_button = turtle.Turtle()
        self.energy_lines = []
        self.particles = []
        self.glow_effect = turtle.Turtle()

        # Create energy line turtles
        for i in range(24):
            line = turtle.Turtle()
            line.speed(0)
            line.penup()
            line.color("lime")
            line.hideturtle()
            self.energy_lines.append(line)

        # Create particle effect turtles
        for i in range(15):
            particle = turtle.Turtle()
            particle.speed(0)
            particle.penup()
            particle.color("green")
            particle.shape("circle")
            particle.shapesize(0.3, 0.3)
            particle.hideturtle()
            self.particles.append(particle)

        # Setup main power button turtle
        self.power_button.speed(0)
        self.power_button.penup()
        self.power_button.color("lime")
        self.power_button.hideturtle()

        # Setup glow effect turtle
        self.glow_effect.speed(0)
        self.glow_effect.penup()
        self.glow_effect.hideturtle()

        # Animation variables
        self.pulse_angle = 0
        self.rotation_angle = 0
        self.particle_positions = []
        self.startup_progress = 0  # Progress for startup animation (0-360 degrees)
        self.startup_speed = 2.5   # Speed of startup animation
        self.cycle_phase = 0       # 0: startup, 1: complete, 2: reset
        self.phase_timer = 0

        # Initialize particle positions
        for i in range(len(self.particles)):
            angle = random.uniform(0, 360)
            radius = random.uniform(100, 200)
            speed = random.uniform(0.5, 2.0)
            self.particle_positions.append({
                'angle': angle,
                'radius': radius,
                'speed': speed,
                'orbit_radius': random.uniform(5, 15)
            })

    def get_futuristic_color(self, intensity_factor, is_main=False):
        """Get futuristic green colors based on intensity"""
        base_intensity = int(255 * intensity_factor)

        if is_main:
            # Bright cyan-green for main elements
            r = int(base_intensity * 0.1)  # Minimal red
            g = base_intensity              # Full green
            b = int(base_intensity * 0.8)  # High blue for cyan tint
        else:
            # Electric lime green
            r = int(base_intensity * 0.3)
            g = base_intensity
            b = int(base_intensity * 0.1)

        return f"#{r:02x}{g:02x}{b:02x}"

    def draw_power_button(self, pulse_factor):
        """Draw the main power button symbol with startup animation"""
        self.power_button.clear()

        # Calculate pulsing size
        current_radius = self.main_radius + (pulse_factor * 10)
        inner_radius = self.inner_radius + (pulse_factor * 8)

        # Futuristic color for outer ring
        outer_intensity = 0.7 + 0.3 * pulse_factor
        outer_color = self.get_futuristic_color(outer_intensity, is_main=False)

        # Draw outer circle
        self.power_button.color(outer_color)
        self.power_button.goto(self.center_x, self.center_y - current_radius)
        self.power_button.pendown()
        self.power_button.pensize(6)
        self.power_button.circle(current_radius)
        self.power_button.penup()

        # Draw animated inner circle based on startup progress
        inner_intensity = 0.8 + 0.2 * pulse_factor
        inner_color = self.get_futuristic_color(inner_intensity, is_main=True)
        self.power_button.color(inner_color)
        self.power_button.pensize(5)

        if self.cycle_phase == 0:  # Startup phase
            # Draw progressive arc based on startup_progress
            if self.startup_progress > 0:
                self.power_button.goto(self.center_x, self.center_y + inner_radius)
                self.power_button.pendown()

                # Draw arc from top, clockwise
                steps = int(self.startup_progress)
                for i in range(steps):
                    angle = -90 + i  # Start from top (-90°)
                    x = self.center_x + inner_radius * math.cos(math.radians(angle))
                    y = self.center_y + inner_radius * math.sin(math.radians(angle))
                    self.power_button.goto(x, y)

                self.power_button.penup()

        elif self.cycle_phase == 1:  # Complete circle phase
            # Draw complete inner circle with enhanced glow
            self.power_button.goto(self.center_x, self.center_y - inner_radius)
            self.power_button.pendown()
            self.power_button.circle(inner_radius)
            self.power_button.penup()

            # Add inner glow effect
            glow_color = self.get_futuristic_color(0.4, is_main=True)
            self.power_button.color(glow_color)
            self.power_button.pensize(2)
            glow_radius = inner_radius * 0.7
            self.power_button.goto(self.center_x, self.center_y - glow_radius)
            self.power_button.pendown()
            self.power_button.circle(glow_radius)
            self.power_button.penup()

        # Draw power line in center (always present, but varies with phase)
        line_intensity = 0.9 if self.cycle_phase == 1 else (0.6 + 0.3 * pulse_factor)
        line_color = self.get_futuristic_color(line_intensity, is_main=True)
        self.power_button.color(line_color)

        line_thickness = 10 if self.cycle_phase == 1 else 8
        self.power_button.pensize(line_thickness)

        # Power line length varies with phase
        if self.cycle_phase == 0:
            line_length = inner_radius * 1.2 * (self.startup_progress / 360)
        else:
            line_length = inner_radius * 1.4 * (0.8 + 0.2 * pulse_factor)

        self.power_button.goto(self.center_x, self.center_y - line_length/2)
        self.power_button.pendown()
        self.power_button.goto(self.center_x, self.center_y + line_length/2)
        self.power_button.penup()

    def draw_energy_lines(self, rotation, pulse_factor):
        """Draw radiating energy lines around the power symbol"""
        num_lines = len(self.energy_lines)

        # Energy intensity based on phase
        energy_multiplier = 1.5 if self.cycle_phase == 1 else (0.5 + self.startup_progress / 360)

        for i, line in enumerate(self.energy_lines):
            line.clear()

            # Calculate angle for this line
            base_angle = (360 / num_lines) * i + rotation
            angle_rad = math.radians(base_angle)

            # Vary line properties
            base_length = 60 + (pulse_factor * 20) + random.uniform(-10, 10)
            line_length = base_length * energy_multiplier
            start_radius = 100 + (pulse_factor * 15)

            # Calculate positions
            start_x = self.center_x + start_radius * math.cos(angle_rad)
            start_y = self.center_y + start_radius * math.sin(angle_rad)
            end_x = self.center_x + (start_radius + line_length) * math.cos(angle_rad)
            end_y = self.center_y + (start_radius + line_length) * math.sin(angle_rad)

            # Enhanced futuristic colors
            base_intensity = 0.5 + 0.5 * pulse_factor + random.uniform(-0.2, 0.2)
            base_intensity *= energy_multiplier
            base_intensity = max(0.3, min(1.0, base_intensity))

            if i % 3 == 0:  # Some lines are brighter cyan-green
                color = self.get_futuristic_color(base_intensity, is_main=True)
                line.pensize(random.choice([3, 4, 5]))
            else:
                color = self.get_futuristic_color(base_intensity, is_main=False)
                line.pensize(random.choice([2, 3, 4]))

            line.color(color)

            # Draw line
            line.goto(start_x, start_y)
            line.pendown()
            line.goto(end_x, end_y)
            line.penup()

            # Add enhanced dot at end
            if random.random() > 0.2:
                line.goto(end_x, end_y)
                dot_size = random.randint(5, 12) if self.cycle_phase == 1 else random.randint(3, 8)
                line.dot(dot_size)

    def draw_glow_effect(self, pulse_factor):
        """Draw a subtle glow effect around the power button"""
        self.glow_effect.clear()

        # Enhanced glow for complete phase
        glow_intensity = 1.3 if self.cycle_phase == 1 else 0.8

        # Draw multiple circles with decreasing opacity
        for i in range(4):
            radius = self.main_radius + 15 + (i * 12) + (pulse_factor * 20)

            # Enhanced futuristic glow colors
            base_alpha = (0.6 - (i * 0.12)) * glow_intensity
            color = self.get_futuristic_color(base_alpha * (0.5 + 0.5 * pulse_factor), is_main=(i % 2 == 0))

            self.glow_effect.color(color)
            self.glow_effect.goto(self.center_x, self.center_y - radius)
            self.glow_effect.pendown()
            self.glow_effect.pensize(2 + i)
            self.glow_effect.circle(radius)
            self.glow_effect.penup()

    def update_particles(self):
        """Update and draw floating particles"""
        particle_energy = 1.2 if self.cycle_phase == 1 else (0.6 + self.startup_progress / 720)

        for i, (particle, pos) in enumerate(zip(self.particles, self.particle_positions)):
            # Update position with enhanced speed during complete phase
            speed_multiplier = particle_energy
            pos['angle'] += pos['speed'] * speed_multiplier

            # Calculate orbital motion
            orbit_x = pos['orbit_radius'] * math.cos(math.radians(pos['angle'] * 3))
            orbit_y = pos['orbit_radius'] * math.sin(math.radians(pos['angle'] * 2))

            # Main circular motion
            main_x = self.center_x + pos['radius'] * math.cos(math.radians(pos['angle']))
            main_y = self.center_y + pos['radius'] * math.sin(math.radians(pos['angle']))

            # Combine motions
            final_x = main_x + orbit_x
            final_y = main_y + orbit_y

            # Update particle
            particle.goto(final_x, final_y)
            particle.showturtle()

            # Enhanced fade effect by changing size
            fade = (math.sin(math.radians(pos['angle'] * 2)) + 1) / 2
            base_size = 0.4 if self.cycle_phase == 1 else 0.2
            size = base_size + fade * 0.4 * particle_energy
            particle.shapesize(size, size)

            # Futuristic color variation
            color_intensity = 0.5 + fade * 0.5
            color = self.get_futuristic_color(color_intensity, is_main=(i % 3 == 0))
            particle.color(color)

    def animate(self):
        """Main animation loop"""
        while True:
            try:
                # Update animation variables
                self.pulse_angle += 3
                self.rotation_angle += 0.5
                self.phase_timer += 1

                # Update startup/cycle logic
                if self.cycle_phase == 0:  # Startup phase
                    self.startup_progress += self.startup_speed
                    if self.startup_progress >= 360:
                        self.startup_progress = 360
                        self.cycle_phase = 1  # Move to complete phase
                        self.phase_timer = 0

                elif self.cycle_phase == 1:  # Complete phase
                    if self.phase_timer > 120:  # Stay complete for ~6 seconds
                        self.cycle_phase = 2  # Move to reset phase
                        self.phase_timer = 0

                elif self.cycle_phase == 2:  # Reset phase
                    self.startup_progress -= self.startup_speed * 2  # Faster reset
                    if self.startup_progress <= 0:
                        self.startup_progress = 0
                        self.cycle_phase = 0  # Back to startup
                        self.phase_timer = 0

                # Calculate pulse factor (breathing effect)
                pulse_factor = (math.sin(math.radians(self.pulse_angle)) + 1) / 2

                # Clear previous frame
                screen.bgcolor("black")

                # Draw glow effect first (background)
                self.draw_glow_effect(pulse_factor)

                # Draw energy lines
                self.draw_energy_lines(self.rotation_angle, pulse_factor)

                # Update particles
                self.update_particles()

                # Draw main power button (foreground)
                self.draw_power_button(pulse_factor)

                # Update screen
                screen.update()

                # Control animation speed
                time.sleep(0.05)

            except turtle.Terminator:
                break
            except KeyboardInterrupt:
                break

def main():
    try:
        print("Starting Power Brand Screensaver...")
        print("Press Ctrl+C or close the window to exit")

        # Create and start the animation
        power_symbol = PowerSymbol()
        power_symbol.animate()

    except KeyboardInterrupt:
        print("\nScreensaver stopped by user")
    except Exception as e:
        print(f"Error: {e}")
    finally:
        try:
            screen.bye()
        except:
            pass

if __name__ == "__main__":
    main()
