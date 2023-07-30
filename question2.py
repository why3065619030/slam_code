import numpy as np
import cv2
# 根据相机内参矩阵，将像素点转换为归一化平面点。
# 使用基础矩阵对归一化平面点进行极线约束计算。
# 通过极线约束，得到相对旋转矩阵R和相对平移向量t。

def decompose_essential_matrix(F, K1, K2, m1, m2):
    # Step 1: 将像素点转换为归一化平面点
    m1_normalized = np.linalg.inv(K1) @ np.column_stack((m1, np.ones(len(m1))))
    m2_normalized = np.linalg.inv(K2) @ np.column_stack((m2, np.ones(len(m2))))

    # Step 2: 使用基础矩阵进行极线约束计算
    E = K2.T @ F @ K1
    _, R, t, _ = cv2.recoverPose(E, m1_normalized[:, :2], m2_normalized[:, :2])

    return R, t

# 示例数据
F = np.array([[0.001, -0.45, 1.2],
              [0.3, 0.002, -0.8],
              [-1.1, 0.7, 0.01]])

K1 = np.array([[1000, 0, 500],
               [0, 1000, 300],
               [0, 0, 1]])

K2 = np.array([[900, 0, 450],
               [0, 900, 350],
               [0, 0, 1]])

m1 = np.array([[100, 200],
               [150, 300],
               [200, 400]])

m2 = np.array([[120, 180],
               [160, 270],
               [210, 390]])

R, t = decompose_essential_matrix(F, K1, K2, m1, m2)
print("相对旋转矩阵 R:\n", R)
print("相对平移向量 t:\n", t)
# 请注意，这里使用了OpenCV库的recoverPose函数，该函数可用于从基础矩阵估计相对旋转和平移。
# 在示例中，我们将F、K1、K2、m1和m2作为输入，并输出相对旋转矩阵R和相对平移向量t。
