# Video-to-PDF-Converter

This application allows users to convert the audio from a video file into a PDF document. It extracts the audio from the selected video, performs speech recognition to convert the audio into text, and then saves the text into a PDF file.

## Features

- Select a video file (supports various formats like MP4, AVI, MOV, MKV).
- Extract audio from the video.
- Convert the extracted audio to text using Google Speech Recognition.
- Save the recognized text into a PDF file.

## Requirements

- Python 3.x
- `moviepy` for video and audio processing.
- `speech_recognition` for audio to text conversion.
- `tkinter` for GUI.
- `fpdf` for PDF generation.

## Usage

1. Run the application:

    ```bash
    python video_to_pdf_converter.py
    ```

2. Use the GUI to select a video file.
3. Click on the `Convert` button to start the conversion process.
4. Once the conversion is complete, the PDF file will be saved in the current directory as `my_pdf.pdf`.
