"""
YouTube Downloader
A module for downloading YouTube videos with progress tracking
"""
import re
import sys
import shutil
import subprocess
import configparser
from pathlib import Path
from urllib.parse import urlparse
from typing import Optional, Dict, Any

from ..presentation import typewriter_effect, dramatic_pause


# Configuration settings
YT_DLP_DEFAULT_DIR = Path.home() / "Downloads" / "OneHandCoding"
CONFIG_FILE = Path.home() / ".config" / ".youtube_downloader_config.ini"
DEFAULT_CONFIG = {
    "default_quality": "best",
    "default_output_dir": str(YT_DLP_DEFAULT_DIR),
    "continue_downloads": "true",
    "no_overwrites": "true",
    "progress": "true",
    "user_agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Brave/1.66.118",
}


def load_config() -> Dict[str, Any]:
    """Load configuration from config file."""
    config = configparser.ConfigParser()

    if CONFIG_FILE.exists():
        try:
            config.read(CONFIG_FILE)
            if "settings" in config:
                return dict(config["settings"])
        except Exception as e:
            typewriter_effect(f"⚠️ Could not read config file: {e}")

    return DEFAULT_CONFIG


def save_config(config_dict: Dict[str, Any]):
    """Save configuration to config file."""
    config = configparser.ConfigParser()
    config["settings"] = config_dict

    try:
        CONFIG_FILE.parent.mkdir(parents=True, exist_ok=True)
        with open(CONFIG_FILE, "w") as f:
            config.write(f)
        typewriter_effect(f"✅ Configuration saved to {CONFIG_FILE}")
    except Exception as e:
        typewriter_effect(f"❌ Could not save config file: {e}")


def create_default_config():
    """Create a default configuration file."""
    save_config(DEFAULT_CONFIG)
    typewriter_effect(f"✅ Default configuration created at {CONFIG_FILE}")
    typewriter_effect("📝 You can edit this file to customize default settings.")


def is_valid_url(url: str) -> bool:
    """Validate if the URL is properly formatted."""
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc])
    except Exception:
        return False


def is_playlist_url(url: str) -> bool:
    """
    Check if the URL is a playlist by looking at URL parameters or using yt-dlp.
    """
    # First, check for obvious playlist indicators in the URL
    playlist_indicators = ['list=', 'playlist=', 'channel=']
    for indicator in playlist_indicators:
        if indicator in url.lower():
            return True

    # If URL doesn't have obvious indicators, use yt-dlp to check
    try:
        result = subprocess.run(
            ["yt-dlp", "--flat-playlist", "--print", "id", url],
            capture_output=True,
            text=True,
            timeout=10,  # Shorter timeout
        )
        ids = [line for line in result.stdout.strip().splitlines() if line]
        return len(ids) > 1
    except Exception:
        # If yt-dlp fails, rely on the URL pattern check
        return False


def parse_progress(line: str) -> Optional[Dict[str, str]]:
    """Parse yt-dlp progress output."""
    # Match download progress pattern
    progress_pattern = (
        r"\[download\]\s+(\d+\.?\d*)%\s+of\s+~?\s*([0-9.]+\w+)\s+at\s+([0-9.]+\w+/s)"
    )
    match = re.search(progress_pattern, line)

    if match:
        return {
            "percent": match.group(1),
            "size": match.group(2),
            "speed": match.group(3),
        }
    return None


def display_progress(progress: Dict[str, str]):
    """Displays a custom progress bar using the presentation module."""
    try:
        percent = float(progress["percent"])
        bar_length = 30
        filled_length = int(bar_length * percent / 100)
        bar = "█" * filled_length + "─" * (bar_length - filled_length)
        
        # Clear the line and show progress
        print(f"\rDownloading: |{bar}| {percent:.1f}% "
              f"({progress['size']}) @ {progress['speed']}", 
              end="", flush=True)
    except (ValueError, KeyError):
        # Ignore if progress dictionary is malformed
        pass


def handle_playlist_options(
    command: list,
    playlist_mode: str = "download_all",
    playlist_items: Optional[str] = None,
):
    """Add playlist-specific options to command."""
    # Handle specific playlist items first (highest priority)
    if playlist_items:
        command.extend(["--playlist-items", playlist_items])
        typewriter_effect(f"🎯 Targeting specific playlist items: {playlist_items}")

    # Handle different playlist modes
    if playlist_mode == "download_all":
        # Download all videos in the playlist
        pass

    elif playlist_mode == "single":
        # Download only the single video (ignore playlist)
        command.append("--no-playlist")

    elif playlist_mode == "first_n":
        # Download first 5 videos
        if not playlist_items:  # Only if no specific items were requested
            command.extend(["--playlist-end", "5"])

    elif playlist_mode == "audio_only":
        # Single video, audio only
        command.append("--no-playlist")
        command.extend(["-f", "bestaudio/best", "--extract-audio", "--audio-format", "mp3"])

    elif playlist_mode == "download_all_audio":
        # Entire playlist as audio files
        command.extend(["-f", "bestaudio/best", "--extract-audio", "--audio-format", "mp3"])


def download_youtube_video(
    url: str,
    output_name: Optional[str] = None,
    quality: str = "best",
    playlist_mode: str = "download_all",
    use_config: bool = True,
    playlist_items: Optional[str] = None,
):
    """Download a YouTube video with progress tracking."""
    if not shutil.which("yt-dlp"):
        error_msg = "'yt-dlp' command not found."
        print(f"❌ {error_msg}", file=sys.stderr)
        return False

    if not is_valid_url(url):
        error_msg = f"Invalid URL format: {url}"
        print(f"❌ {error_msg}", file=sys.stderr)
        return False

    # Load config
    config = load_config() if use_config else {}

    # Use config value for quality if not specified
    quality = quality if quality != "best" else config.get("default_quality", "best")
    output_dir = Path(config.get("default_output_dir", str(YT_DLP_DEFAULT_DIR)))

    print(f"🔄 Starting download for URL: {url}")
    print(f"🎬 Quality target: {quality}")
    print(f"📋 Playlist mode: {playlist_mode}")

    command = ["yt-dlp"]
    command.append("--embed-thumbnail")

    user_agent = config.get("user_agent")
    if user_agent:
        command.extend(["--user-agent", user_agent])

    # Add options based on config
    if config.get("continue_downloads", "true").lower() == "true":
        command.append("--continue")
    if config.get("no_overwrites", "true").lower() == "true":
        command.append("--no-overwrites")
    if config.get("progress", "true").lower() == "true":
        command.append("--progress")

    # --- OUTPUT LOGIC ---
    if output_name:
        if Path(output_name).is_absolute():
            final_output_path = Path(output_name)
        else:
            final_output_path = output_dir / output_name
    else:
        final_output_path = output_dir / "%(title)s.%(ext)s"

    final_output_path.parent.mkdir(parents=True, exist_ok=True)

    # Add appropriate extension for audio downloads if custom name provided
    if output_name and not Path(output_name).suffix:
        if playlist_mode in ["audio_only", "download_all_audio"]:
            final_output_path = final_output_path.with_suffix(".mp3")
        else:
            final_output_path = final_output_path.with_suffix(".mp4")

    print(f"📁 Saving to: {final_output_path.parent}")
    command.extend(["-o", str(final_output_path)])

    # --- Handle playlist options (this will also set audio format if needed) ---
    handle_playlist_options(command, playlist_mode, playlist_items)

    # --- Format Selection Logic (only for video modes) ---
    # Audio format is already set by handle_playlist_options if needed
    if playlist_mode not in {"audio_only", "download_all_audio"}:
        if quality == "best":
            command.extend(["-S", "res,vbr,abr"])
        else:
            clean_quality = quality.removesuffix("p")
            format_string = f"bestvideo[height<=?{clean_quality}]+bestaudio/best[height<=?{clean_quality}]/best"
            command.extend(["-f", format_string])

    command.append(url)

    print(f"▶️  Executing command: {' '.join(command[:3])}...")

    try:
        # Use Popen for real-time progress tracking
        process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.STDOUT,
            universal_newlines=True,
            bufsize=1,
        )

        # Track and display progress with presentation effects
        last_progress = None
        for line in iter(process.stdout.readline, ""):
            line = line.strip()
            if line:
                # Parse and display progress
                progress = parse_progress(line)
                if progress and progress != last_progress:
                    print(
                        f"\r📥 Progress: {progress['percent']}% ({progress['size']}) at {progress['speed']}",
                        end="",
                        flush=True,
                    )
                    last_progress = progress
                elif "[download]" in line and "Destination:" in line:
                    print(f"\n📁 {line}")
                elif "[download]" in line and "has already been downloaded" in line:
                    print(f"\n✅ {line}")
                elif "ERROR" in line.upper():
                    print(f"\n❌ {line}")

        # Wait for process to complete
        return_code = process.wait()

        # Clear the progress line and print final result
        if last_progress:
            print()  # New line after progress

        if return_code == 0:
            print("✅ Download complete!")
            return True
        else:
            error_msg = f"Download failed. yt-dlp exited with error code {return_code}."
            print(f"❌ {error_msg}", file=sys.stderr)
            return False

    except KeyboardInterrupt:
        interrupted_msg = (
            "\n\n⏹️ Download interrupted by user. Run the same command again to resume."
        )
        print(interrupted_msg)
        sys.exit(0)

    except Exception as e:
        unexpected_error = f"An unexpected error occurred: {e}"
        print(f"\n❌ {unexpected_error}", file=sys.stderr)
        return False


def main():
    """Main entry point for the YouTube downloader."""
    print()
    print("=" * 60)
    typewriter_effect("📥 YOUTUBE VIDEO DOWNLOADER")
    print("=" * 60)
    dramatic_pause(1)

    # Check if config file exists and offer to create it
    if not CONFIG_FILE.exists():
        typewriter_effect(f"\n⚠️  Configuration file not found at {CONFIG_FILE}")
        typewriter_effect("🔧 Would you like to create a default configuration? (y/n) [y]: ", end_with_newline=False)
        create_config_choice = input().strip().lower()
        if create_config_choice in ['', 'y', 'yes']:
            create_default_config()
        dramatic_pause(1)

    while True:
        # Get YouTube URL from user
        typewriter_effect("\n📋 Enter YouTube URL (or 'quit' to exit): ", end_with_newline=False)
        url = input().strip()

        if url.lower() in ['quit', 'exit', 'q']:
            typewriter_effect("\n👋 Thank you for using YouTube Downloader!")
            sys.exit()

        if not url:
            typewriter_effect("⚠️  No URL provided. Please enter a valid URL.")
            continue

        if not is_valid_url(url):
            print(f"❌ Invalid URL: {url}", file=sys.stderr)
            continue

        # Check if URL is a playlist FIRST
        is_playlist = is_playlist_url(url)

        # Ask for playlist mode based on whether it's a playlist
        if is_playlist:
            playlist_modes = {
                "1": "download_all",
                "2": "first_n",
                "3": "single",
                "4": "audio_only",
                "5": "download_all_audio"
            }

            typewriter_effect("\n📋 It looks like this is a playlist! How would you like to handle it?")
            typewriter_effect("   1 - Download all videos")
            typewriter_effect("   2 - Download first 5 videos only")
            typewriter_effect("   3 - Single video only (ignore playlist)")
            typewriter_effect("   4 - Audio only (single video)")
            typewriter_effect("   5 - Audio only (all in playlist)")
            typewriter_effect("   Enter choice [1]: ", end_with_newline=False)
        else:
            # For single videos, simpler options
            playlist_modes = {
                "1": "download_all",  # for single video (actually same as "single")
                "2": "audio_only"
            }

            typewriter_effect("\n📋 How would you like to handle this video?")
            typewriter_effect("   1 - Download as video")
            typewriter_effect("   2 - Download audio only")
            typewriter_effect("   Enter choice [1]: ", end_with_newline=False)

        playlist_choice = input().strip()

        # Validate choice based on available options
        if not playlist_choice or playlist_choice not in playlist_modes:
            playlist_choice = "1"

        playlist_mode = playlist_modes[playlist_choice]

        # Ask if user wants to specify playlist items (only for playlists in video mode)
        playlist_items = None
        if is_playlist and playlist_mode in ["download_all", "first_n"] and playlist_choice != "2":
            typewriter_effect("\n🔢 Do you want to download specific items? (e.g., '1,3,5' or '1-10') [skip]: ", end_with_newline=False)
            items_input = input().strip()
            if items_input:
                playlist_items = items_input

        # Only ask for quality if not in audio-only mode
        if playlist_mode in {"audio_only", "download_all_audio"}:
            quality_input = "best"  # Quality doesn't matter for audio
            typewriter_effect("\n🎵 Audio-only mode selected. Quality setting will be ignored.")
        else:
            typewriter_effect("\n🎬 Enter video quality (best, 720p, 1080p, etc.) [default: best]: ", end_with_newline=False)
            quality_input = input().strip()
            if not quality_input:
                quality_input = "best"

        # Ask for custom output name (optional)
        typewriter_effect("\n📝 Enter custom filename (optional, press Enter to use video title): ", end_with_newline=False)
        output_name = input().strip()
        if not output_name:
            output_name = None

        # Set download directory with option to override
        config = load_config()
        download_dir = Path(config.get("default_output_dir", str(YT_DLP_DEFAULT_DIR)))

        typewriter_effect(f"📁 Using download directory: {download_dir}")
        dramatic_pause(1)

        # Start the download
        success = download_youtube_video(
            url=url,
            output_name=output_name,
            quality=quality_input,
            playlist_mode=playlist_mode,
            use_config=True,
            playlist_items=playlist_items
        )

        if success:
            typewriter_effect("\n🎉 YouTube video downloaded successfully!")
        else:
            typewriter_effect("\n💥 Failed to download YouTube video.")

        # Ask if user wants to continue
        typewriter_effect("\n🔄 Would you like to download another video? (y/n) [y]: ", end_with_newline=False)
        continue_choice = input().strip().lower()
        if continue_choice in ['n', 'no']:
            typewriter_effect("\n👋 Thank you for using YouTube Downloader!")
            break
    print()


if __name__ == "__main__":
    main()
