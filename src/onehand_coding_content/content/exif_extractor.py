"""
EXIF Data Extractor: "Saan Ka Talaga?" Edition
Para sa mga feeling private pero naka-auto geotagging 😏

Features:
- Single image or batch folder processing
- GPS location extraction with reverse geocoding
- Interactive maps (Folium) + Google Maps option
- Privacy awareness education
"""

import os
import sys
from pathlib import Path
from datetime import datetime
import webbrowser

import pyexiv2
import folium
from folium.plugins import MarkerCluster
from PIL import Image
from PIL.ExifTags import TAGS, GPSTAGS
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderTimedOut, GeocoderServiceError

from ..config import LINE_LENGTH, MAPS_DIR
from ..presentation import typewriter_effect, typing_with_pauses, dramatic_pause


class ExifExtractor:
    """
    EXIF Data Extractor with Filipino Satire
    "Kasi ang totoo, may tinatago ka pa rin sa photos mo" 👀
    """

    SUPPORTED_FORMATS = ('.jpg', '.jpeg', '.png', '.tiff', '.bmp', '.heic')

    def __init__(self):
        self.geocoder = Nominatim(user_agent="saan-ka-talaga-ph")
        self.results = []
        self.has_pyexiv2 = pyexiv2 is not None

    def show_intro(self):
        """Display intro with warnings"""
        print("\n" + "="*LINE_LENGTH)
        typing_with_pauses("🔍 EXIF DATA EXTRACTOR: 'Saan Ka Talaga?' Edition")
        print("="*LINE_LENGTH)
        dramatic_pause(1)

        typing_with_pauses("Para sa mga feeling private pero naka-auto geotagging 😏")
        dramatic_pause(1)

        print("\n" + "⚠️  DISCLAIMER " + "⚠️")
        print("-"*LINE_LENGTH)
        typing_with_pauses("❌ FB/IG/Social Media downloads: WALANG DATA (stripped na)")
        typing_with_pauses("✅ Original camera photos: MAY DATA (jackpot!)")
        typing_with_pauses("✅ Screenshots with metadata: PWEDE")
        typing_with_pauses("📁 Folder processing: SUPPORTED (batch mode!)")
        print("-"*LINE_LENGTH)
        dramatic_pause(2)

    def is_image_file(self, filepath):
        """Check if file is a supported image"""
        return Path(filepath).suffix.lower() in self.SUPPORTED_FORMATS

    def scan_folder(self, folder_path):
        """Scan folder for image files"""
        typewriter_effect(f"\n📁 Scanning folder: {folder_path}")
        dramatic_pause(1)

        image_files = []
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                filepath = os.path.join(root, file)
                if self.is_image_file(filepath):
                    image_files.append(filepath)

        return image_files

    def extract_exif_pil(self, image_path):
        """Extract EXIF using PIL (fallback method)"""
        try:
            img = Image.open(image_path)
            exif_data = img._getexif()

            if not exif_data:
                return None

            exif = {}
            for tag_id, value in exif_data.items():
                tag = TAGS.get(tag_id, tag_id)
                exif[tag] = value

            return exif
        except Exception as e:
            return None

    def extract_exif_pyexiv2(self, image_path):
        """Extract EXIF using pyexiv2 (more robust)"""
        try:
            with open(image_path, "rb") as f:
                with pyexiv2.ImageData(f.read()) as image_info:
                    exif_data = image_info.read_exif()
                    return exif_data if exif_data else None
        except Exception as e:
            return None

    def extract_gps_data(self, exif):
        """Extract GPS coordinates from EXIF data"""
        if not exif:
            return None

        try:
            # Try pyexiv2 format (most reliable)
            if isinstance(exif, dict):
                latitude_info = exif.get("Exif.GPSInfo.GPSLatitude")
                longitude_info = exif.get("Exif.GPSInfo.GPSLongitude")
                lat_ref = exif.get("Exif.GPSInfo.GPSLatitudeRef", "N")
                lon_ref = exif.get("Exif.GPSInfo.GPSLongitudeRef", "E")

                if latitude_info and longitude_info:
                    # Parse format like "14/1 35/1 4272/100"
                    latitude = sum(
                        (value / 60**i)
                        for i, value in enumerate(map(eval, latitude_info.split()))
                    )
                    longitude = sum(
                        (value / 60**i)
                        for i, value in enumerate(map(eval, longitude_info.split()))
                    )

                    # Apply hemisphere
                    if lat_ref == 'S':
                        latitude = -latitude
                    if lon_ref == 'W':
                        longitude = -longitude

                    return {
                        'latitude': round(latitude, 6),
                        'longitude': round(longitude, 6)
                    }

            # Try PIL format as fallback
            gps_info = exif.get('GPSInfo')
            if gps_info:
                gps_data = {}
                for tag_id, value in gps_info.items():
                    tag = GPSTAGS.get(tag_id, tag_id)
                    gps_data[tag] = value

                if 'GPSLatitude' in gps_data and 'GPSLongitude' in gps_data:
                    lat = self.convert_to_degrees(gps_data['GPSLatitude'])
                    lon = self.convert_to_degrees(gps_data['GPSLongitude'])

                    if gps_data.get('GPSLatitudeRef') == 'S':
                        lat = -lat
                    if gps_data.get('GPSLongitudeRef') == 'W':
                        lon = -lon

                    return {'latitude': round(lat, 6), 'longitude': round(lon, 6)}

        except Exception as e:
            # Log but don't crash
            pass

        return None

    def convert_to_degrees(self, value):
        """Convert GPS coordinates to degrees"""
        d, m, s = value
        return d + (m / 60.0) + (s / 3600.0)

    def reverse_geocode(self, lat, lon):
        """Get address from coordinates using geopy"""
        try:
            typewriter_effect("   🌐 Looking up address...")
            location = self.geocoder.reverse(f"{lat}, {lon}", timeout=10)
            dramatic_pause(1)

            if location:
                return location.address
            return "Address not found"

        except (GeocoderTimedOut, GeocoderServiceError) as e:
            typing_with_pauses("   ⚠️ Address lookup failed (network issue)")
            return "Address lookup failed"
        except Exception as e:
            return "Address lookup error"

    def generate_single_map(self, lat, lon, info, filename="location_map.html"):
        """Generate interactive map for single location"""
        map_obj = folium.Map(location=[lat, lon], zoom_start=15)

        popup_html = f"""
        <div style="font-family: Arial; width: 250px;">
            <h4>📍 Location Found!</h4>
            <b>📸 File:</b> {info.get('filename', 'N/A')}<br>
            <b>📅 Date:</b> {info.get('date', 'N/A')}<br>
            <b>⏰ Time:</b> {info.get('time', 'N/A')}<br>
            <b>📷 Camera:</b> {info.get('camera', 'N/A')}<br>
            <b>📍 Address:</b> {info.get('address', 'N/A')}<br>
            <hr>
            <i>"Saan ka talaga nung araw na yan? 👀"</i>
        </div>
        """

        folium.Marker(
            [lat, lon],
            popup=popup_html,
            tooltip="Click for details",
            icon=folium.Icon(color='red', icon='camera', prefix='fa')
        ).add_to(map_obj)

        filename = str(MAPS_DIR / filename)
        map_obj.save(filename)
        return filename

    def generate_batch_map(self, locations, filename="batch_locations_map.html"):
        """Generate map with multiple locations"""
        if not locations:
            return None

        # Calculate center point
        avg_lat = sum(loc['latitude'] for loc in locations) / len(locations)
        avg_lon = sum(loc['longitude'] for loc in locations) / len(locations)

        map_obj = folium.Map(location=[avg_lat, avg_lon], zoom_start=10)

        # Add marker cluster for better visualization
        marker_cluster = MarkerCluster().add_to(map_obj)

        # Color coding by date
        colors = ['red', 'blue', 'green', 'purple', 'orange', 'darkred', 'lightred',
                  'beige', 'darkblue', 'darkgreen', 'cadetblue', 'darkpurple',
                  'white', 'pink', 'lightblue', 'lightgreen', 'gray', 'black', 'lightgray']

        for i, loc in enumerate(locations):
            color = colors[i % len(colors)]

            popup_html = f"""
            <div style="font-family: Arial; width: 250px;">
                <h4>📍 Photo #{i+1}</h4>
                <b>📸 File:</b> {loc.get('filename', 'N/A')}<br>
                <b>📅 Date:</b> {loc.get('date', 'N/A')}<br>
                <b>⏰ Time:</b> {loc.get('time', 'N/A')}<br>
                <b>📷 Camera:</b> {loc.get('camera', 'N/A')}<br>
                <b>📍 Address:</b> {loc.get('address', 'N/A')}<br>
            </div>
            """

            folium.Marker(
                [loc['latitude'], loc['longitude']],
                popup=popup_html,
                tooltip=f"Photo {i+1}: {loc.get('filename', 'Unknown')}",
                icon=folium.Icon(color=color, icon='camera', prefix='fa')
            ).add_to(marker_cluster)

        filename = str(MAPS_DIR / filename)
        map_obj.save(filename)
        return filename

    def generate_master_map(self, locations):
        """Generate master map with all locations"""
        print("\n" + "="*LINE_LENGTH)
        typing_with_pauses("🗺️  GENERATING MASTER MAP...")
        print("="*LINE_LENGTH)
        dramatic_pause(2)

        typewriter_effect("📍 Plotting all locations on one map...")
        dramatic_pause(1)

        map_file = self.generate_batch_map(locations, "master_map.html")

        typing_with_pauses(f"✅ Master map saved: {map_file}")
        dramatic_pause(1)

        typing_with_pauses("\n🎨 Map features:")
        typing_with_pauses("   • Color-coded markers per photo")
        typing_with_pauses("   • Clustered for better visualization")
        typing_with_pauses("   • Click markers for details")
        typing_with_pauses("   • Zoom in/out to see patterns")
        dramatic_pause(2)

        # Open map
        open_map = input("\n👉 Open master map now? (y/n): ").strip().lower()

        if open_map == 'y':
            typewriter_effect("\n✅ Opening master map...")
            webbrowser.open(map_file)
            dramatic_pause(1)
            typing_with_pauses("\n👀 'Your year in review... with receipts!' 📸")

    def show_map_options(self, lat, lon, map_file):
        """Show options for viewing location"""
        google_maps_url = f"https://www.google.com/maps?q={lat},{lon}"

        print("\n" + "="*LINE_LENGTH)
        typing_with_pauses("🗺️  VIEW OPTIONS:")
        print("="*LINE_LENGTH)
        typewriter_effect("   1. Interactive Map (Folium - local, detailed)")
        typewriter_effect("   2. Google Maps (online, full features)")
        typewriter_effect("   3. Both!")
        typewriter_effect("   4. Skip (continue processing)")

        choice = input("\n👉 Choice (1/2/3/4): ").strip()

        if choice in ['1', '3']:
            typewriter_effect("\n✅ Opening interactive map...")
            webbrowser.open(map_file)
            dramatic_pause(1)

        if choice in ['2', '3']:
            typewriter_effect("\n✅ Opening Google Maps...")
            webbrowser.open(google_maps_url)
            dramatic_pause(1)

        return choice

    def extract_camera_info(self, exif):
        """Extract camera information from EXIF"""
        if not exif:
            return "Unknown"

        make = exif.get('Make', exif.get('Exif.Image.Make', ''))
        model = exif.get('Model', exif.get('Exif.Image.Model', ''))

        if make and model:
            return f"{make} {model}".strip()
        elif model:
            return model.strip()
        elif make:
            return make.strip()
        else:
            return "Unknown"

    def extract_datetime(self, exif):
        """Extract date/time from EXIF"""
        if not exif:
            return "Unknown", "Unknown"

        # Try multiple datetime keys
        exif_datetime_keys = ("Exif.Image.DateTime", "Exif.Photo.DateTimeOriginal", "DateTime", "DateTimeOriginal")

        dt_str = None
        for key in exif_datetime_keys:
            dt_str = exif.get(key)
            if dt_str:
                break

        if dt_str:
            try:
                # Parse from format like '1616347542050' (timestamp in milliseconds)
                if all(char.isdigit() for char in str(dt_str)):
                    date_and_time = int(dt_str) / 1000
                    dt = datetime.fromtimestamp(date_and_time)
                    return dt.strftime('%B %d, %Y'), dt.strftime('%I:%M:%S %p')

                # Parse from format like 'Dec 8, 2018 8:14:03 AM'
                elif any(char.isalpha() for char in str(dt_str)):
                    dt = datetime.strptime(dt_str, "%b %d, %Y %H:%M:%S %p")
                    return dt.strftime('%B %d, %Y'), dt.strftime('%I:%M:%S %p')

                # Parse from format like '2017:04:01 18:57:18'
                else:
                    dt = datetime.strptime(dt_str, '%Y:%m:%d %H:%M:%S')
                    return dt.strftime('%B %d, %Y'), dt.strftime('%I:%M:%S %p')
            except Exception as e:
                pass

        return "Unknown", "Unknown"

    def process_single_image(self, image_path):
        """Process a single image file"""
        filename = os.path.basename(image_path)

        print("\n" + "="*LINE_LENGTH)
        typing_with_pauses(f"📸 Processing: {filename}")
        print("="*LINE_LENGTH)
        dramatic_pause(1)

        # Extract EXIF data
        typewriter_effect("🔬 Extracting EXIF data...")
        dramatic_pause(1)

        exif = None
        if self.has_pyexiv2:
            exif = self.extract_exif_pyexiv2(image_path)

        if not exif:
            exif = self.extract_exif_pil(image_path)

        if not exif:
            typing_with_pauses("\n❌ Walang EXIF data!")
            dramatic_pause(1)
            typing_with_pauses("   Possible reasons:")
            typing_with_pauses("   • Galing FB/IG (stripped metadata)")
            typing_with_pauses("   • Manually edited/cleaned")
            typing_with_pauses("   • Screenshot without metadata")
            dramatic_pause(1)
            typing_with_pauses("\n😏 Privacy win... or di ka lang ma-stalk ng ex?")
            return None

        # Extract info
        camera = self.extract_camera_info(exif)
        date, time = self.extract_datetime(exif)

        print("\n📊 EXIF DATA FOUND:")
        print("-"*LINE_LENGTH)
        typing_with_pauses(f"   📷 Camera: {camera}")
        typing_with_pauses(f"   📅 Date: {date}")
        typing_with_pauses(f"   ⏰ Time: {time}")
        dramatic_pause(1)

        # Check for GPS
        typewriter_effect("\n🔍 Checking for GPS data...")
        dramatic_pause(2)

        gps_data = self.extract_gps_data(exif)

        if not gps_data:
            typing_with_pauses("\n❌ Walang GPS coordinates!")
            dramatic_pause(1)
            typing_with_pauses("   Either:")
            typing_with_pauses("   • Naka-disable ang geotagging (smart!)")
            typing_with_pauses("   • Old camera/phone walang GPS")
            typing_with_pauses("   • Deliberately removed (may alam ka ah! 😏)")
            dramatic_pause(2)
            typing_with_pauses("\n👍 May privacy awareness ka pala!")
            return None

        # GPS FOUND! 🎰
        lat = gps_data['latitude']
        lon = gps_data['longitude']

        print("\n" + "🎰"*20)
        typing_with_pauses("🎰 JACKPOT! GPS DATA FOUND! 🎰")
        print("🎰"*20)
        dramatic_pause(2)

        typing_with_pauses(f"\n📍 Coordinates: {lat:.6f}, {lon:.6f}")
        dramatic_pause(1)

        # Reverse geocode
        address = self.reverse_geocode(lat, lon)
        typing_with_pauses(f"📍 Address: {address}")
        dramatic_pause(2)

        # Prepare info for map
        info = {
            'filename': filename,
            'camera': camera,
            'date': date,
            'time': time,
            'address': address,
            'latitude': lat,
            'longitude': lon
        }

        # Generate map
        typewriter_effect("\n🗺️  Generating interactive map...")
        dramatic_pause(1)
        map_file = self.generate_single_map(lat, lon, info)
        typing_with_pauses(f"✅ Map saved: {map_file}")
        dramatic_pause(1)

        # Show viewing options
        self.show_map_options(lat, lon, map_file)

        # Satirical commentary
        print("\n" + "="*LINE_LENGTH)
        typing_with_pauses("👀 REALITY CHECK:")
        print("="*LINE_LENGTH)
        typing_with_pauses(f"   'Nag-absent ka pero may picture ka sa {address}?'")
        dramatic_pause(1)
        typing_with_pauses(f"   'Overtime daw pero nasa beach ka nung {date}?'")
        dramatic_pause(1)
        typing_with_pauses("   'Saan ka talaga nung araw na yan? 🤔'")
        dramatic_pause(2)

        return info

    def process_folder(self, folder_path):
        """Process all images in a folder"""
        print("\n" + "="*LINE_LENGTH)
        typing_with_pauses("📁 BATCH PROCESSING MODE ACTIVATED")
        print("="*LINE_LENGTH)
        dramatic_pause(1)

        # Scan folder
        image_files = self.scan_folder(folder_path)

        if not image_files:
            typing_with_pauses("\n❌ No images found in folder!")
            return

        typing_with_pauses(f"\n✅ Found {len(image_files)} image(s)")
        dramatic_pause(1)

        # Ask for confirmation
        typing_with_pauses(f"\n⚠️  Processing {len(image_files)} images...")
        if len(image_files) > 20:
            typing_with_pauses("   This might take a while. Kape muna? ☕")

        proceed = input("\n👉 Continue? (y/n): ").strip().lower()

        if proceed != 'y':
            typing_with_pauses("\n👋 Cancelled. Takot ka na ba? 😏")
            return

        # Process images
        locations_with_gps = []
        total = len(image_files)

        for i, image_path in enumerate(image_files, 1):
            typing_with_pauses(f"\nProgress: [{i}/{total}]")
            result = self.process_single_image(image_path)

            if result and 'latitude' in result:
                locations_with_gps.append(result)
                self.results.append(result)

            dramatic_pause(0.5)

        # Generate summary
        self.generate_batch_summary(total, locations_with_gps)

        # Generate master map
        if locations_with_gps:
            self.generate_master_map(locations_with_gps)

    def generate_batch_summary(self, total, locations_with_gps):
        """Generate summary for batch processing"""
        print("\n\n" + "="*LINE_LENGTH)
        typing_with_pauses("📊 BATCH PROCESSING COMPLETE!")
        print("="*LINE_LENGTH)
        dramatic_pause(2)

        with_gps = len(locations_with_gps)
        without_gps = total - with_gps

        typewriter_effect(f"\n📈 Results:")
        typing_with_pauses(f"   Total images processed: {total}")
        typing_with_pauses(f"   With GPS data: {with_gps} ({(with_gps/total*100):.1f}%)")
        typing_with_pauses(f"   Without GPS: {without_gps} ({(without_gps/total*100):.1f}%)")
        dramatic_pause(2)

        if with_gps == 0:
            typing_with_pauses("\n❌ Walang GPS data sa lahat!")
            dramatic_pause(1)
            typing_with_pauses("   Possible reasons:")
            typing_with_pauses("   • Lahat galing social media (stripped na)")
            typing_with_pauses("   • Naka-disable geotagging (matino!)")
            typing_with_pauses("   • Professional stalker ka, nag-edit lahat 😂")
            return

        # Location analysis
        typewriter_effect("\n📍 Location Analysis:")
        dramatic_pause(1)

        # Group by location (simplified)
        unique_locations = len(set((loc['address'] for loc in locations_with_gps)))
        typing_with_pauses(f"   Unique locations: {unique_locations}")

        # Show top locations
        if with_gps <= 10:
            typewriter_effect("\n📌 Locations found:")
            for i, loc in enumerate(locations_with_gps, 1):
                typing_with_pauses(f"   {i}. {loc['address']}")
                typing_with_pauses(f"      📅 {loc['date']} @ {loc['time']}")
                dramatic_pause(0.5)

        dramatic_pause(2)

        # Satirical analysis
        print("\n" + "="*LINE_LENGTH)
        typing_with_pauses("🤔 PATTERN ANALYSIS:")
        print("="*LINE_LENGTH)
        dramatic_pause(1)

        typing_with_pauses("   'Ang daming beach photos ah? 🏖️'")
        dramatic_pause(1)
        typing_with_pauses("   'Medical certificate valid pa ba talaga? 😏'")
        dramatic_pause(1)
        typing_with_pauses("   'Overtime daw pero wala sa office? 🤔'")
        dramatic_pause(2)

    def show_privacy_tips(self):
        """Show privacy tips and education"""
        print("\n\n" + "="*LINE_LENGTH)
        typing_with_pauses("🎓 PRIVACY EDUCATION 101")
        print("="*LINE_LENGTH)
        dramatic_pause(2)

        typing_with_pauses("\n💡 How to disable geotagging:")
        dramatic_pause(1)

        tips = [
            "📱 iPhone: Settings → Privacy → Location Services → Camera → Never",
            "🤖 Android: Camera app → Settings → Location tags → Off",
            "💻 DSLR: Menu → GPS/Location → Disable",
            "✂️ Remove existing data: Use EXIF removal tools",
            "🔒 Before sharing: Check metadata first!"
        ]

        for tip in tips:
            typing_with_pauses(f"   • {tip}")
            dramatic_pause(1)

        dramatic_pause(2)

        typewriter_effect("\n🤔 Why you should care:")
        dramatic_pause(1)

        typing_with_pauses("   • Stalkers can track your location")
        typing_with_pauses("   • Burglars know when you're not home")
        typing_with_pauses("   • Exes can find where you live now 😱")
        typing_with_pauses("   • Your boss knows you're not really 'sick' 🏖️")
        typing_with_pauses("   • Internet never forgets")
        dramatic_pause(2)

        typewriter_effect("\n✅ Good news:")
        typing_with_pauses("   Social media platforms strip metadata automatically")
        typing_with_pauses("   (Kaya nga walang data sa FB/IG downloads)")
        dramatic_pause(1)
        typing_with_pauses("\n   But original photos? Still dangerous! 📸")
        dramatic_pause(2)


def main():
    """Main entry point"""
    extractor = ExifExtractor()

    # Show intro
    extractor.show_intro()

    # Get input
    print("\n" + "="*LINE_LENGTH)
    typing_with_pauses("📁 INPUT OPTIONS:")
    print("="*LINE_LENGTH)
    typewriter_effect("   1. Single image file")
    typewriter_effect("   2. Folder (batch processing)")

    choice = input("\n👉 Choice (1/2): ").strip()

    if choice == '1':
        # Single image mode
        image_path = input("\n📸 Enter image file path: ").strip()

        if not os.path.exists(image_path):
            typing_with_pauses("\n❌ File not found!")
            return

        if not extractor.is_image_file(image_path):
            typing_with_pauses("\n❌ Not a valid image file!")
            return

        extractor.process_single_image(image_path)

    elif choice == '2':
        # Folder mode
        folder_path = input("\n📁 Enter folder path: ").strip()

        if not os.path.exists(folder_path):
            typing_with_pauses("\n❌ Folder not found!")
            return

        if not os.path.isdir(folder_path):
            typing_with_pauses("\n❌ Not a valid folder!")
            return

        extractor.process_folder(folder_path)

    else:
        typing_with_pauses("\n❌ Invalid choice!")
        return

    # Show privacy tips
    show_tips = input("\n\n👉 Want to see privacy tips? (y/n): ").strip().lower()
    if show_tips == 'y':
        extractor.show_privacy_tips()

    # Final message
    print("\n\n" + "="*LINE_LENGTH)
    typing_with_pauses("👋 THANK YOU FOR USING 'Saan Ka Talaga?'")
    print("="*LINE_LENGTH)
    dramatic_pause(1)

    typing_with_pauses("\n💭 Remember:")
    typing_with_pauses("   'Privacy is not about hiding.'")
    dramatic_pause(1)
    typing_with_pauses("   'It's about controlling what you share.'")
    dramatic_pause(1)
    typing_with_pauses("   'Kasi ang totoo... may GPS coordinates ka pa rin.' 📍")
    dramatic_pause(2)

    typewriter_effect("\n\n# Stay safe online, Pilipinas! 🇵🇭")


if __name__ == "__main__":
    main()
