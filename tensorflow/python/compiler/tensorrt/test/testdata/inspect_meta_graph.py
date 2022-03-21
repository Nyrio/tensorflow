from tensorflow.core.protobuf import meta_graph_pb2
from tensorflow.core.protobuf import saved_model_pb2

saved_model = saved_model_pb2.SavedModel()
with open("./tf_variablev2_saved_model/saved_model.pb", "rb") as f:
    file_content = f.read()
saved_model.ParseFromString(file_content)

meta_graph = saved_model.meta_graphs[0]
saver_def = meta_graph.saver_def
graph_def = meta_graph.graph_def
