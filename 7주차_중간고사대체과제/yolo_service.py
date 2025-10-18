from __future__ import annotations
import bentoml
from typing import List, Dict, Any
import io
from PIL import Image


@bentoml.service
class YOLOService:
    def __init__(self) -> None:
        from ultralytics import YOLO

        self.model = YOLO('yolov5s.pt')

    @bentoml.api
    def detect(self, image: Image.Image) -> List[Dict[str, Any]]:
        result = self.model(image)
        r0 = result[0]
        boxes = r0.boxes
        names = r0.names

        output: List[Dict[str, Any]] = []
        for box in boxes:
            cls_id = int(box.cls[0])
            conf = float(box.conf[0])

            x1, y1, x2, y2 = [float(v) for v in box.xyxy[0].tolist()]
            output.append(
                {
                    'class_id': cls_id,
                    'class_name': names.get(cls_id, str(cls_id)),
                    'confidence': round(conf, 4),
                    'bbox_xyxy': [x1, y1, x2, y2]
                }
            )
        return output

    @bentoml.api
    def detect_image(self, image: Image.Image) -> Image.Image:
        result = self.model(image)
        r0 = result[0]

        plotted = r0.plot()
        img = Image.fromarray(plotted[:, :, ::-1])

        return img
