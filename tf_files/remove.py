import tensorflow as tf
from tensorflow.core.framework import graph_pb2

# read frozen graph and display nodes
graph = tf.GraphDef()
graph.ParseFromString(open('rounded_graph.pb','rb').read())

def display_nodes(nodes):
    for i, node in enumerate(nodes):
        print('%d %s %s' % (i, node.name, node.op))
        # [print(u'└─── %d ─ %s' % (i, n.encode("utf-8"))) for i, n in enumerate(node.input)]
    
display_nodes(graph.node)

# # Connect 'MatMul_1' with 'Relu_2'
graph.node[419].input[0] = 'Pad' # 44 -> MatMul_1
# # Remove dropout nodes
nodes = graph.node[:415] + graph.node[417:] # 33 -> MatMul_1 
# del nodes[1] # 1 -> keep_prob

# Save graph
output_graph = graph_pb2.GraphDef()
output_graph.node.extend(nodes)
with tf.gfile.GFile('./rounded_graph_without_dropout.pb', 'w') as f:
    f.write(output_graph.SerializeToString())