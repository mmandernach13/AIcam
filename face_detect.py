from picamera2 import Picamera2, Preview
from picamera2.encoders import H264Encoder
from picamera2.outputs import FfmpegOutput
from picamera2.devices.imx500 import IMX500
import time

cam = Picamera2()

config = cam.create_video_configuration(main={"size":(640, 480)})
cam.configure(config)

output = FfmpegOutput("udp://192.168.1.192:5000", audio=False)
encoder = H264Encoder(bitrate=1000000)

cam.start_recording(encoder, output)

try:
    while True:
        time.sleep(1)
except KeyboardInterrupt:
    cam.stop_recording()
