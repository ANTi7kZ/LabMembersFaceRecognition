from local computer

scp -r person_recognition.py pi@192.168.86.170:/home/pi/AIY-projects-python/src/aiy/vision/models/
scp -r person_recognition_camera.py pi@192.168.86.170:/home/pi/AIY-projects-python/src/examples/vision/

from pi
cd AIY-projects-python/src/examples/vision/
./person_recognition_camera.py
sudo cp -f mobilenet_v1_160res_0.5_imagenet_own.binaryproto /opt/aiy/models/

pi@raspberrypi:~/AIY-projects-python/src/examples/vision $ ./person_recognition_camera.py 
Traceback (most recent call last):
  File "/opt/aiy/projects-python/src/aiy/_drivers/_spicomm.py", line 128, in transact
    fcntl.ioctl(self._dev, SPICOMM_IOCTL_TRANSACT, self._tbuf)
OSError: [Errno 14] Bad address

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "./person_recognition_camera.py", line 77, in main
    for i, result in enumerate(inference.run()):
  File "/opt/aiy/projects-python/src/aiy/vision/inference.py", line 76, in run
    yield self._engine.camera_inference()
  File "/opt/aiy/projects-python/src/aiy/vision/inference.py", line 257, in camera_inference
    return self._communicate(request).inference_result
  File "/opt/aiy/projects-python/src/aiy/vision/inference.py", line 187, in _communicate
    response.ParseFromString(self._transport.send(request.SerializeToString()))
  File "/opt/aiy/projects-python/src/aiy/_drivers/_transport.py", line 33, in send
    return self._spicomm.transact(request)
  File "/opt/aiy/projects-python/src/aiy/_drivers/_spicomm.py", line 143, in transact
    raise SpicommInternalError
aiy._drivers._spicomm.SpicommInternalError

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "./person_recognition_camera.py", line 81, in main
    print_classes(classes, args.num_objects)
  File "/opt/aiy/projects-python/src/aiy/vision/inference.py", line 87, in __exit__
    self.close()
  File "/opt/aiy/projects-python/src/aiy/vision/inference.py", line 79, in close
    self._engine.stop_camera_inference()
  File "/opt/aiy/projects-python/src/aiy/vision/inference.py", line 263, in stop_camera_inference
    self._communicate(request)
  File "/opt/aiy/projects-python/src/aiy/vision/inference.py", line 189, in _communicate
    raise InferenceException(response.status.message)
aiy.vision.inference.InferenceException: StopCameraInference: Camera inference is not running.

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "./person_recognition_camera.py", line 87, in <module>
    main()
  File "./person_recognition_camera.py", line 83, in main
    camera.stop_preview()
  File "/usr/lib/python3/dist-packages/picamera/camera.py", line 758, in __exit__
    self.close()
  File "/usr/lib/python3/dist-packages/picamera/camera.py", line 752, in close
    raise exc
  File "/usr/lib/python3/dist-packages/picamera/camera.py", line 1995, in _control_callback
    "No data recevied from sensor. Check all connections, "
