import sounddevice as sd

#print(sd.query_devices())
sample_rate = 44100
seconds = 5
total_samples = sample_rate * seconds

print("Recording...")
recording = sd.rec(total_samples, samplerate=sample_rate, channels=1) #recording function
sd.wait()
print("Done recording")


