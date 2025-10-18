from ultralytics import YOLO
import bentoml

y = YOLO('yolov5s.pt')
torch_model = y.model

tag = bentoml.pytorch.save_model(
    name = 'yolov5s_ultra',
    model=torch_model,
    signatures={'__call__' : {'batchable': True}}
)
print('saved:', tag)