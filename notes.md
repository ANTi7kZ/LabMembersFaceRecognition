git clone https://github.com/googlecodelabs/tensorflow-for-poets-2

cd tensorflow-for-poets-2

IMAGE_SIZE=160

ARCHITECTURE="mobilenet_0.50_${IMAGE_SIZE}"

Start TensorBoard
tensorboard --logdir tf_files/training_summaries &

Investigate the retraining script
python -m scripts.retrain -h

Run the training
python -m scripts.retrain \
  --bottleneck_dir=tf_files/bottlenecks \
  --how_many_training_steps=500 \
  --model_dir=tf_files/models/ \
  --summaries_dir=tf_files/training_summaries/"${ARCHITECTURE}" \
  --output_graph=tf_files/retrained_graph.pb \
  --output_labels=tf_files/retrained_labels.txt \
  --architecture="${ARCHITECTURE}" \
  --image_dir=photos

Run the training
python -m scripts.retrain \
  --bottleneck_dir=tf_files_new/bottlenecks \
  --how_many_training_steps=500 \
  --model_dir=tf_files_new/models/ \
  --summaries_dir=tf_files_new/training_summaries/"${ARCHITECTURE}" \
  --output_graph=tf_files_new/retrained_graph.pb \
  --output_labels=tf_files_new/retrained_labels.txt \
  --architecture="${ARCHITECTURE}" \
  --image_dir=photos

python -m scripts.label_image \
    --graph=tf_files_new/retrained_graph.pb  \
    --image=photos/judith/IMG_1655.jpg  \
    --input_height=160  \
    --input_width=160

python -m tensorflow.python.tools.optimize_for_inference \
  --input=tf_files_new/retrained_graph.pb \
  --output=tf_files_new/optimized_graph.pb \
  --input_names="input" \
  --output_names="final_result"

python -m scripts.label_image \
    --graph=tf_files_new/optimized_graph.pb  \
    --image=photos/judith/IMG_1655.jpg  \
    --input_height=160  \
    --input_width=160

Test 
python -m scripts.label_image \
    --graph=tf_files_1008/retrained_graph.pb  \
    --image=photos/judith/IMG_1655.jpg  \
    --input_height=160  \
    --input_width=160

Optimize for inference
python -m tensorflow.python.tools.optimize_for_inference \
  --input=tf_files/retrained_graph.pb \
  --output=tf_files/optimized_graph.pb \
  --input_names="input" \
  --output_names="final_result"

Verify the optimized model
python -m scripts.label_image \
    --graph=tf_files/optimized_graph.pb  \
    --image=photos/judith/IMG_1655.jpg  \
    --input_height=160  \
    --input_width=160

Quantize the network weights
python -m scripts.quantize_graph \
  --input=tf_files/optimized_graph.pb \
  --output=tf_files/rounded_graph.pb \
  --output_node_names=final_result \
  --mode=weights_rounded

./bonnet_model_compiler.par \
    --frozen_graph_path=./mobilenet_v1_160res_0.5_imagenet.pb \
    --output_graph_path=./mobilenet_v1_160res_0.5_imagenet.binaryproto \
    --input_tensor_name="input" \
    --output_tensor_names="MobilenetV1/Predictions/Softmax" \
    --input_tensor_size=160

./bonnet_model_compiler.par \
    --frozen_graph_path=./rounded_graph.pb \
    --output_graph_path=./rounded_graph.binaryproto \
    --input_tensor_name="input" \
    --output_tensor_names="final_result" \
    --input_tensor_size=160

./bonnet_model_compiler.par \
    --frozen_graph_path=./retrained_graph.pb \
    --output_graph_path=./retrained_graph.binaryproto \
    --input_tensor_name="input" \
    --output_tensor_names=“final_result” \
    --input_tensor_size=160

./bonnet_model_compiler.par \
    --frozen_graph_path=./retrained_graph.pb \
    --output_graph_path=./retrained_graph.binaryproto \
    --input_tensor_name=“Placeholder” \
    --output_tensor_names=“final_result” \
    --input_tensor_size=160

./bonnet_model_compiler.par \
    --frozen_graph_path=./mobilenet_ssd_256res_0.125_person_cat_dog.pb \
    --output_graph_path=./converted_graph.binaryproto \
    --input_tensor_name="Preprocessor/sub" \
    --output_tensor_names=“concat,concat_1” \
    --input_tensor_size=256

./bonnet_model_compiler.par \
    --frozen_graph_path=./mobilenet_ssd_256res_0.125_person_cat_dog.pb \
    --output_graph_path=./converted_graph.binaryproto \
    --input_tensor_name="image_tensor" \
    --output_tensor_names=“concat,concat_1” \
    --input_tensor_size=256


./bonnet_model_compiler.par --frozen_graph_path="./mobilenet_ssd_256res_0.125_person_cat_dog.pb" --input_tensor_name="Preprocessor/sub“ --output_tensor_names="concat,concat_1" --input_tensor_size=256 --output_graph_path="./converted_graph.binaryproto"




