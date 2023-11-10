# main.py

from pkg.modu import calculate_centroid
print("請輸入三角形的 3 個頂點座標")
output = "-" * 50
print("{}".format(output))
# 輸入三角形的三個頂點座標
point1 = tuple(map(float, input("請輸入頂點 a 的座標:").split(',')))
point2 = tuple(map(float, input("請輸入頂點 b 的座標:").split(',')))
point3 = tuple(map(float, input("請輸入頂點 c 的座標:").split(',')))
print("{}".format(output))
# 計算三角形的重心
centroid_x, centroid_y = calculate_centroid(point1, point2, point3)

# 將座標四捨五入到整數
centroid_x, centroid_y = round(centroid_x), round(centroid_y)

# 打印結果
print(f"此三角形的重心座標: ({centroid_x}, {centroid_y})")
