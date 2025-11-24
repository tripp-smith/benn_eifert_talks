#!/usr/bin/env python3
"""
Video Transcription Script

This script transcribes video files to text using OpenAI's Whisper model.
It can handle various video formats and outputs the transcript to a markdown file.

Usage:
    python transcribe_video.py <input_video> [--output <output_file>] [--model <model_name>]

Example:
    python transcribe_video.py video.mp4 --output transcript.md
"""

import argparse
import sys
import os
import subprocess
from pathlib import Path


def check_ffmpeg():
    """Check if ffmpeg is installed and available."""
    try:
        subprocess.run(['ffmpeg', '-version'], 
                      capture_output=True, 
                      check=True)
        return True
    except (subprocess.CalledProcessError, FileNotFoundError):
        return False


def transcribe_video(input_video: str, output_file: str = None, model: str = "base") -> None:
    """
    Transcribe a video file to text using Whisper.
    
    Args:
        input_video: Path to the input video file
        output_file: Path to the output markdown file (optional)
        model: Whisper model to use (tiny, base, small, medium, large)
    """
    # Check for ffmpeg first
    if not check_ffmpeg():
        print("Error: ffmpeg is required but not found.")
        print("\nPlease install ffmpeg:")
        print("  macOS: brew install ffmpeg")
        print("  Linux: sudo apt-get install ffmpeg  (Debian/Ubuntu)")
        print("        or sudo yum install ffmpeg  (RHEL/CentOS)")
        print("  Windows: Download from https://ffmpeg.org/download.html")
        print("\nAlternatively, you can install Homebrew first (macOS):")
        print("  /bin/bash -c \"$(curl -fsSL https://raw.githubusercontent.com/Homebrew/install/HEAD/install.sh)\"")
        sys.exit(1)
    
    try:
        import whisper
    except ImportError:
        print("Error: whisper library not found. Please install it with:")
        print("  pip install openai-whisper")
        sys.exit(1)
    
    # Validate input file
    if not os.path.exists(input_video):
        print(f"Error: Input video file '{input_video}' not found.")
        sys.exit(1)
    
    # Set default output file if not provided
    if output_file is None:
        input_path = Path(input_video)
        output_file = input_path.stem + "_transcript.md"
    
    print(f"Loading Whisper model '{model}'...")
    try:
        whisper_model = whisper.load_model(model)
    except Exception as e:
        print(f"Error loading Whisper model: {e}")
        print("Available models: tiny, base, small, medium, large")
        sys.exit(1)
    
    print(f"Transcribing video: {input_video}")
    print("This may take a while depending on video length and model size...")
    
    try:
        # Transcribe the video
        result = whisper_model.transcribe(input_video)
        
        # Extract transcript text
        transcript_text = result["text"]
        
        # Write to output file
        with open(output_file, 'w', encoding='utf-8') as f:
            f.write(transcript_text)
        
        print(f"\n✓ Transcription complete!")
        print(f"✓ Output saved to: {output_file}")
        print(f"\nTranscript preview (first 200 characters):")
        print("-" * 60)
        print(transcript_text[:200] + "..." if len(transcript_text) > 200 else transcript_text)
        print("-" * 60)
        
    except Exception as e:
        print(f"Error during transcription: {e}")
        sys.exit(1)


def main():
    parser = argparse.ArgumentParser(
        description="Transcribe video files to text using Whisper",
        formatter_class=argparse.RawDescriptionHelpFormatter,
        epilog="""
Examples:
  python transcribe_video.py video.mp4
  python transcribe_video.py video.mp4 --output transcript.md
  python transcribe_video.py video.mp4 --model large
        """
    )
    
    parser.add_argument(
        "input_video",
        help="Path to the input video file"
    )
    
    parser.add_argument(
        "--output", "-o",
        dest="output_file",
        help="Path to the output markdown file (default: <input_name>_transcript.md)"
    )
    
    parser.add_argument(
        "--model", "-m",
        default="base",
        choices=["tiny", "base", "small", "medium", "large"],
        help="Whisper model to use (default: base). Larger models are more accurate but slower."
    )
    
    args = parser.parse_args()
    
    transcribe_video(args.input_video, args.output_file, args.model)


if __name__ == "__main__":
    main()

