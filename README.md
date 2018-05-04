./mobilenet_based_classifier.py --model_path /opt/aiy/models/mobilenet_v1_160res_0.5_imagenet.binaryproto --label_path /home/pi/AIY-projects-python/src/aiy/vision/models/image_classification_classes.py --input_width 160 --input_height 160 --input_layer input --output_layer MobilenetV1/Predictions/Softmax

./mobilenet_based_classifier.py --model_path /opt/aiy/models/mobilenet_v1_160res_0.5_imagenet.binaryproto --label_path /home/pi/AIY-projects-python/src/aiy/vision/models/image_classification_classes_own --input_width 160 --input_height 160 --input_layer input --output_layer MobilenetV1/Predictions/Softmax

./mobilenet_based_classifier.py --model_path /opt/aiy/models/rounded_graph.binaryproto --label_path /home/pi/AIY-projects-python/src/aiy/vision/models/person_classes --input_width 160 --input_height 160 --input_layer input --output_layer final_result

scp -r mobilenet_based_classifier_custom.py /home/pi/AIY-projects-python/src/examples/vision

./mobilenet_based_classifier_custom.py --model_path /opt/aiy/models/rounded_graph.binaryproto --label_path /home/pi/AIY-projects-python/src/aiy/vision/models/person_classes --input_width 160 --input_height 160 --input_layer input --output_layer final_result

./mobilenet_based_classifier_custom.py --model_path /opt/aiy/models/rounded_graph.binaryproto --label_path /home/pi/AIY-projects-python/src/aiy/vision/models/person_classes --input_width 160 --input_height 160 --input_layer input --output_layer final_result --image_inference --input_image 
