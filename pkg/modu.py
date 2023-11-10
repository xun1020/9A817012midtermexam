# modu.py

import json


def read_json(file_name: str) -> dict:
    with open(file_name, 'r', encoding='utf-8') as file:
        data = json.load(file)
    return data


def print_json(data: dict) -> None:
    print(json.dumps(data, ensure_ascii=False, indent=4))


def process_data(data: dict, discount: float) -> None:
    for category in data['categories']:
        for item in category['items']:
            item['price'] = int(round(item['price'] * discount))


def write_json(data: dict, file_name: str) -> None:
    with open(file_name, 'w', encoding='utf-8') as file:
        json.dump(data, file, ensure_ascii=False, indent=4)


def calculate_centroid(point1, point2, point3):
    """
    計算三角形的重心座標
    """
    x1, y1 = point1
    x2, y2 = point2
    x3, y3 = point3

    centroid_x = (x1 + x2 + x3) / 3
    centroid_y = (y1 + y2 + y3) / 3
    return centroid_x, centroid_y
# 如果希望這個模組在單獨運行時執行一些代碼，可以使用以下的條件：


if __name__ == "__main__":
    # 在這裡添加在模組單獨運行時執行的代碼
    pass
