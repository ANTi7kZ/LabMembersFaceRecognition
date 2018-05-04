import argparse
import io
import time
import picamera
from PIL import Image

def main():
	parser = argparse.ArgumentParser()
	parser.add_argument(
        '--image', '-i', dest='image')
	args = parser.parse_args()
	stream = io.BytesIO()
	with picamera.PiCamera() as camera:
	    camera.start_preview()
	    time.sleep(2)
	    camera.capture(stream, format='jpeg')
	# "Rewind" the stream to the beginning so we can read its content
	stream.seek(0)
	image = Image.open(stream)
	image.save(args.image, format='jpeg')

if __name__ == '__main__':
	main()