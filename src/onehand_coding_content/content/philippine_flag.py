"""
Philippine Flag Terminal Renderer
Render the Philippine flag using colored asterisks in terminal
With historical facts and political commentary
"""

import time
import math
import sys
from pathlib import Path

from ..sounds import play_with_wait, HERO
from ..presentation import typing_with_pauses, typewriter_effect

# Color codes
RESET = '\033[0m'
BLUE = '\033[94m'
RED = '\033[91m'
WHITE = '\033[97m'
YELLOW = '\033[93m'
GRAY = '\033[90m'

# Flag dimensions
FLAG_WIDTH = 80
FLAG_HEIGHT = 24
TRIANGLE_BASE = FLAG_WIDTH // 2


def is_inside_triangle(x, y):
    """Check if point is inside the white triangle (left side)"""
    # Triangle: from top-left, spans half width at middle height
    mid_height = FLAG_HEIGHT // 2

    # The triangle's right edge is a diagonal line
    # At y=0 (top), x can be 0
    # At y=mid_height (middle), x can be up to TRIANGLE_BASE
    # At y=FLAG_HEIGHT (bottom), x can be 0

    if y <= mid_height:
        # Upper half: line goes from (0,0) to (TRIANGLE_BASE, mid_height)
        max_x = (TRIANGLE_BASE * y) / mid_height
    else:
        # Lower half: line goes from (TRIANGLE_BASE, mid_height) to (0, FLAG_HEIGHT)
        max_x = TRIANGLE_BASE * (FLAG_HEIGHT - y) / mid_height

    return x <= max_x


def calculate_distance(x1, y1, x2, y2):
    """Calculate distance between two points"""
    return math.sqrt((x2 - x1)**2 + (y2 - y1)**2)


def is_sun(x, y):
    """Check if point is part of the sun (center of triangle)"""
    # Center the sun in the triangle
    sun_center_x = TRIANGLE_BASE // 3  # Moved more to center of triangle
    sun_center_y = FLAG_HEIGHT // 2
    sun_radius = 3  # Smaller radius for smaller flag

    distance = calculate_distance(x, y, sun_center_x, sun_center_y)

    # Sun core (circle)
    if distance <= sun_radius:
        return True

    # Sun rays (8 rays) - more prominent
    if distance <= sun_radius + 3:
        angle = math.atan2(y - sun_center_y, x - sun_center_x)
        angle_deg = math.degrees(angle) % 360

        # 8 rays at 45-degree intervals
        for ray_angle in range(0, 360, 45):
            diff = abs(angle_deg - ray_angle)
            if diff > 180:
                diff = 360 - diff

            if diff < 12:  # Wider rays for better visibility
                return True

    return False


def is_star(x, y):
    """Check if point is part of the 3 stars"""
    # Star positions at triangle corners - adjusted for better visibility
    stars = [
        (3, 2),      # Top corner (very top-left of triangle)
        (3, 21),     # Bottom corner (very bottom-left of triangle)
        (32, 12)     # Right corner (on hypotenuse, middle right)
    ]

    star_size = 2  # Smaller stars for cleaner look

    for star_x, star_y in stars:
        dx = abs(x - star_x)
        dy = abs(y - star_y)

        # Create a cleaner star shape
        # Center point
        if dx == 0 and dy == 0:
            return True

        # Vertical line (center column) - shorter
        if dx == 0 and dy <= star_size:
            return True

        # Horizontal line (center row) - shorter
        if dy == 0 and dx <= star_size:
            return True

        # Diagonal lines (X pattern for star points) - tighter
        if dx == dy and dx <= 1:
            return True

        # Tips of the star (4 diagonal points)
        if (dx == 1 and dy == 1):
            return True

    return False


def get_pixel_color(x, y):
    """Determine the color of each pixel"""
    mid_height = FLAG_HEIGHT // 2

    # Border (decorative edge)
    if x == 0 or x == FLAG_WIDTH - 1 or y == 0 or y == FLAG_HEIGHT - 1:
        # Alternating colors for festive border
        if (x + y) % 4 == 0:
            return YELLOW
        elif (x + y) % 4 == 1:
            return BLUE
        elif (x + y) % 4 == 2:
            return RED
        else:
            return YELLOW

    # Inside triangle (white with sun and stars)
    if is_inside_triangle(x, y):
        if is_sun(x, y):
            return YELLOW
        elif is_star(x, y):
            return YELLOW
        else:
            return WHITE

    # Blue section (top half)
    if y < mid_height:
        return BLUE

    # Red section (bottom half)
    return RED


def draw_flag():
    """Draw the complete Philippine flag"""
    for y in range(FLAG_HEIGHT):
        for x in range(FLAG_WIDTH):
            color = get_pixel_color(x, y)
            print(f"{color}*{RESET}", end="")
        print()  # New line after each row


def print_header():
    """Print engaging header"""
    print()
    print("=" * 80)
    time.sleep(0.3)
    typewriter_effect("RENDERING SOVEREIGNTY.EXE... ✓")
    time.sleep(0.5)
    typewriter_effect("🇵🇭 Philippine Flag v1898.0 (Independence Patch)")
    time.sleep(0.5)
    typing_with_pauses("Status: Rendering freedom... please stand for the flag!")
    print("=" * 80)
    time.sleep(1)
    print("\n")


def print_historical_facts():
    """Print historical facts with political commentary"""
    print("\n")
    print("=" * 80)
    typewriter_effect("📜 FLAG.LOG (HISTORICAL DEBUG INFO)")
    print("=" * 80)
    time.sleep(0.5)

    facts = [
        "\n🏗️  SYSTEM SPECIFICATIONS:",
        "   • Version: 1898.0 (Stable Release)",
        "   • Compiled: June 12, 1898 @ Kawit, Cavite",
        "   • Lead Developer: Gen. Emilio Aguinaldo & Team",
        "   • Designer: Marcela Agoncillo, Lorenza Agoncillo, Delfina Herbosa",
        "   • First Deployment: Battle of Alapan (May 28, 1898)",
        "",
        "🎨 COLOR PALETTE:",
        "   • Blue (#0038A8): Peace, truth, justice",
        "   • Red (#CE1126): Patriotism, valor",
        "   • White (#FFFFFF): Equality, fraternity",
        "   • Yellow (#FCD116): Sun & stars (sovereignty)",
        "",
        "⚙️  SYMBOLIC COMPONENTS:",
        "   • Sun Rays: 8 (first provinces na nag-revolt)",
        "     Manila, Cavite, Bulacan, Pampanga, Nueva Ecija,",
        "     Tarlac, Laguna, Batangas",
        "   • Stars: 3 (Luzon, Visayas, Mindanao)",
        "   • Triangle: Equality of Katipunan",
        "",
        "🔄 SPECIAL FEATURES:",
        "   • Flip Mode: Red on top = State of War",
        "   • Current Status: Blue on top = Peacetime",
        "     (pero traffic is a different kind of war 🚗💀)",
    ]

    for fact in facts:
        typing_with_pauses(fact)
        time.sleep(0.2)

    time.sleep(1)

    # The spicy part
    print("\n" + "=" * 80)
    typewriter_effect("⚠️  CORRUPTION.LOG (SYSTEM WARNINGS)")
    print("=" * 80)
    time.sleep(0.8)

    corruption_facts = [
        "\n💔 HOW POLITICIANS SULLIED IT:",
        "",
        "   🚩 1972-1986: Martial Law Era",
        "      • Flag used to legitimize dictatorship",
        "      • 'Bagong Lipunan' pero same old corruption",
        "      • Flag waved while rights were trampled",
        "",
        "   🚩 1990s-2000s: Plunder Era",
        "      • Politicians posed with flag during campaign",
        "      • Same politicians: plunder cases after election",
        "      • Flag = backdrop for photo ops, not principles",
        "",
        "   🚩 2016-2022: 'Tokhang' Era",
        "      • 'Maka-Diyos, Maka-Tao, Makakalikasan, Makabansa'",
        "      • Reality: 30,000+ drug war deaths (unofficial count)",
        "      • Flag displayed while UN investigated crimes",
        "",
        "   🚩 2022-Present: Budget Scandal Era",
        "      • ₱860.5B realigned in 2025 budget (see budget_algorithm.py)",
        "      • ₱118B+ flood control ghost projects exposed",
        "      • Politicians swear oath under this flag...",
        "      • ...then ghost funds under same flag 👻",
        "",
        "   🚩 Dynasty Politics:",
        "      • Same surnames since 1987 (see dynasty_simulator.py)",
        "      • Flag represents 'equal access to public service'",
        "      • Reality: Congress = family reunion ng political clans",
        "",
        "   🚩 Transparency Theater:",
        "      • Flag in every government office",
        "      • SALN filing: 'Executive privilege daw'",
        "      • FOI requests: Pending since 1987",
        "      • ICI hearings: Closed door (see flood_control_response.py)",
    ]

    for fact in corruption_facts:
        typing_with_pauses(fact)
        time.sleep(0.15)

    time.sleep(1.5)

    # The brutal truth
    print("\n" + "=" * 80)
    typewriter_effect("💭 RUNTIME ERROR: INTEGRITY_CHECK_FAILED")
    print("=" * 80)
    time.sleep(0.8)

    final_thoughts = [
        "",
        "   The flag represents:",
        "   ✓ Independence (achieved 1898)",
        "   ✓ Sovereignty (defended 1898-1946)",
        "   ✓ Values: Peace, justice, equality",
        "",
        "   But politicians turned it into:",
        "   ✗ Campaign prop (photo-op background)",
        "   ✗ Corruption shield ('para sa bayan' daw)",
        "   ✗ Oath backdrop (promises broken by lunch)",
        "   ✗ Distraction tool (wave flag, ignore scandals)",
        "",
        "   🎭 The flag is beautiful.",
        "   💔 What they do under it? Not so much.",
        "",
        "   🔥 Our heroes died for this flag.",
        "   😤 Politicians get rich waving it.",
        "",
        "   ⚖️  The flag didn't change.",
        "   🤡 The people holding it did.",
    ]

    for thought in final_thoughts:
        typing_with_pauses(thought)
        time.sleep(0.2)

    time.sleep(1.5)

    # Footer
    print("\n" + "=" * 80)
    typewriter_effect("📌 PATCH NOTES:")
    print("=" * 80)
    typing_with_pauses("   • TODO: Restore meaning behind symbols")
    typing_with_pauses("   • TODO: Elect leaders worthy of this flag")
    typing_with_pauses("   • TODO: Make 'Maka-bansa' mean something again")
    typing_with_pauses("   • PRIORITY: Anti-Dynasty Law (pending since 1987)")
    print("=" * 80)

    time.sleep(1)

    print("\n")
    typing_with_pauses("# while politicians.corrupt():")
    time.sleep(0.3)
    typing_with_pauses("#     flag.meaning -= 1")
    time.sleep(0.3)
    typing_with_pauses("#     people.disappointment += 1")
    time.sleep(0.3)
    typing_with_pauses("#     # Loop continues until we break it ourselves")
    time.sleep(1)

    print()


def main():
    """Main entry point"""
    try:
        print_header()
        draw_flag()
        print_historical_facts()

        print("\n" + "=" * 80)
        typing_with_pauses("🇵🇭 END OF RENDER. Mabuhay ang Pilipinas! (The real one, not the corrupted version.)")
        print("=" * 80)
        print("\n")

        play_with_wait(HERO)

    except KeyboardInterrupt:
        print("\n\n")
        typewriter_effect("⚠️  Render interrupted. Kinda like how democracy gets interrupted. 🤷")
        print("\n")
        sys.exit(0)


if __name__ == "__main__":
    main()
