
from roboflow import Roboflow
rf = Roboflow(api_key="UzbL8gb3yHL1rlNxARCw")
project = rf.workspace("seif-taha-rvzyw").project("egyptian-coins-r80ed")
version = project.version(1)
dataset = version.download("yolov8")

from ultralytics import YOLO
import cv2

model = YOLO('tt.yaml')


image_path = 'photo_2025-01-22_10-06-05.jpg'
img = cv2.imread(image_path)


results = model(image_path)


coin_values = {
    'onepound': 1,
    'half': 0.5,
    'quarter': 0.25}

total = 0


for result in results.pred[0]:
    tid = int(result[5])  
    coincc = results.names[tid]  
    if coincc == 'onepound':
        total += coin_values['one_pound']
    elif coincc == 'half':
        total += coin_values['half']
    elif coincc == 'quarter':
        total += coin_values['quarter']


cv2.imwrite('result', img)

print(f'Total  coins: {total} pounds')

