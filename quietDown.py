import pyaudio
import win32api

def rms( data ):
    count = len(data)/2
    format = "%dh"%(count)
    shorts = struct.unpack( format, data )
    sum_squares = 0.0
    for sample in shorts:
        n = sample * (1.0/32768)
        sum_squares += n*n
    return math.sqrt( sum_squares / count )

p = pyaudio.PyAudio()

stream = p.open(format=p.get_format_from_width(wf.getsampwidth()),
                channels=wf.getnchannels(),
                rate=wf.getframerate(),
                output=True,
                stream_callback=callback)

stream.start_stream()

while stream.is_active():
  data = stream.read(CHUNK)
  rms = rms(data)
  decibel = 20 * log10(rms)
  if decibel > 70:
    stream.stop_stream()
    stream.close()
    p.terminate()
    win32api.InitiateSystemShutdown()


