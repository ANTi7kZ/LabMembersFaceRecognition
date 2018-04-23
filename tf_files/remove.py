import tensorflow as tf

# read frozen graph and display nodes
graph = tf.GraphDef()
graph.ParseFromString(open('rounded_graph.pb','rb').read())

def display_nodes(nodes):
    for i, node in enumerate(nodes):
        print('%d %s %s' % (i, node.name, node.op))
        [print(u'└─── %d ─ %s' % (i, n)) for i, n in enumerate((node.input).encode("utf-8"))]
    
display_nodes(graph.node)

# # Connect 'MatMul_1' with 'Relu_2'
# graph.node[44].input[0] = 'Relu_2' # 44 -> MatMul_1
# # Remove dropout nodes
# nodes = graph.node[:33] + graph.node[44:] # 33 -> MatMul_1 
# del nodes[1] # 1 -> keep_prob

# Save graph
output_graph = graph_pb2.GraphDef()
output_graph.node.extend(nodes)
with tf.gfile.GFile('./frozen_model_without_dropout.pb', 'w') as f:
    f.write(output_graph.SerializeToString())