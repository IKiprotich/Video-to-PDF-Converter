import os
import threading
import speech_recognition as sr
from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
from tkinter import ttk
from moviepy.editor import VideoFileClip
from fpdf import FPDF


# My variables.
VideoClip = ""
AudioClip = ""

# Function that gets the video.
def get_video():
    global VideoClip, video_filepath
    try:
        video_filepath.set(filedialog.askopenfilename(
            title="Select your video clip",
            filetypes=[("Video files", "*.mp4;*.avi;*.mov;*.mkv")]))  
        VideoClip = VideoFileClip(video_filepath.get())
    except Exception as e:
        messagebox.showerror("Error", f"No video selected or invalid video file: {str(e)}")

# Function that converts audio to pdf
def audio_to_pdf():
    global AudioClip, progress_bar
    try:
        # Extract audio from the video and save it as a WAV file
        AudioClip = VideoClip.audio.write_audiofile("My_audio.wav")
        
        # Recognize speech from the audio file
        r = sr.Recognizer()
        with sr.AudioFile("My_audio.wav") as source:
            audio_data = r.record(source)
            text = r.recognize_google(audio_data)
            
            # Write recognized text to a file
            with open('my_text.txt', 'w') as write_file:
                write_file.write(text)
            
            # Convert text file to PDF
            text_to_pdf('my_text.txt')
        
        messagebox.showinfo("Message", "Conversion was successful")
    except Exception as e:
        messagebox.showerror("Error", f"Conversion was not successful: {str(e)}")
    finally:
        video_filepath.set('')
        progress_bar.stop()
        # Clean up temporary files
        if os.path.exists("My_audio.wav"):
            os.remove("My_audio.wav")
        if os.path.exists("my_text.txt"):
            os.remove("my_text.txt")

# Function that converts text to pdf
def text_to_pdf(file):
    pdf = FPDF(format='letter', unit='in')
    pdf.add_page()
    pdf.set_font("Arial", size=11)
    page_width = pdf.w - 2 * pdf.l_margin

    with open(file, "r") as f:
        for x in f:
            pdf.multi_cell(page_width, 0.15, x)
            pdf.ln(0.5)
    
    # Save PDF file
    pdf.output("my_pdf.pdf")

# Function that runs the whole script
def run():
    global progress_bar
    t1 = threading.Thread(target=progress_bar.start)
    t2 = threading.Thread(target=audio_to_pdf)
    t1.start()
    t2.start()

# Other GUI code
# Main program settings
root = Tk()
root.title("Video to PDF Converter")

# File path variables
video_filepath = StringVar()

# UI frame
UI_frame = Frame(root, width=600, height=200, relief="raised")
UI_frame.grid(row=0, column=0, padx=10, pady=10)

convert_frame = Frame(root, width=600, height=200, relief="raised")
convert_frame.grid(row=1, column=0, padx=10, pady=10)

# Labels and buttons
select = Label(UI_frame, text="Select Video:", font=("Arial", 12))
select.grid(row=0, column=0, padx=5, pady=5, sticky=W)

browse = Button(UI_frame, text="Browse", command=get_video, font=("Arial", 12))
browse.grid(row=0, column=1, padx=5, pady=5)

video_selected = Label(UI_frame, text="Selected video:", font=("Arial", 12))
video_selected.grid(row=1, column=0, padx=5, pady=5, sticky=E)

video_path = Label(UI_frame, textvariable=video_filepath)
video_path.grid(row=1, column=1, padx=5, pady=5, sticky=W)

convert = Button(convert_frame, text="Convert", command=run, font=("Arial", 12))
convert.grid(row=0, column=0, pady=5)

progress_bar = ttk.Progressbar(root, orient=HORIZONTAL, mode='indeterminate', length=500)
progress_bar.grid(row=2, column=0, padx=25, pady=25)

# Calling the main program
root.mainloop()
