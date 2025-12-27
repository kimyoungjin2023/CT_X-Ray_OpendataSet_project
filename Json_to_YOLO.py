import json
import os

with open("labels.json", "r") as f:
    coco = json.load(f)

images = {img["id"]: img for img in coco["images"]}

os.makedirs("labels", exist_ok=True)

for ann in coco["annotations"]:
    img = images[ann["image_id"]]
    w, h = img["width"], img["height"]
    
    x, y, bw, bh = ann["bbox"]
    
    x_center = (x + bw / 2) / w
    y_center = (y + bh / 2) / h
    bw /= w
    bh /= h

    label_path = f"labels/{img['file_name'].replace('.jpg', '.txt')}"
    
    with open(label_path, "a") as f:
        f.write(f"{ann['category_id']} {x_center} {y_center} {bw} {bh}\n")
