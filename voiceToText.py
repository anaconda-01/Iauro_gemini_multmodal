import pyaudio
import wave

# Initialize PyAudio
audio = pyaudio.PyAudio()

# Open the audio stream for recording (input stream)
stream = audio.open(
    format=pyaudio.paInt16,  # Format of audio data (16-bit)
    channels=1,               # Number of audio channels (mono)
    rate=44100,               # Sampling rate (44.1 kHz)
    input=True,               # Specify that this is an input (recording) stream
    frames_per_buffer=1024    # Number of frames per buffer
)

# Initialize a list to store the frames of audio
frames = []

print("Recording... Press Ctrl+C to stop.")

try:
    while True:
        # Read data from the input stream (audio)
        data = stream.read(1024)
        frames.append(data)  # Append the data to the frames list

except KeyboardInterrupt:
    print("Recording stopped.")

# Stop the stream after recording
stream.stop_stream()
stream.close()

# Terminate the audio interface
audio.terminate()

# Save the recorded audio to a .wav file
output_filename = "pyaudio.wav"
with wave.open(output_filename, 'wb') as soundfile:
    soundfile.setnchannels(1)  # Mono sound
    soundfile.setsampwidth(audio.get_sample_size(pyaudio.paInt16))  # Sample width in bytes
    soundfile.setframerate(44100)  # Sampling rate (44.1 kHz)
    soundfile.writeframes(b''.join(frames))  # Write the frames to the file

print(f"Audio recorded and saved to {output_filename}.")
