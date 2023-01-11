import torch
# 查看 pytorch 版本
print(torch.__version__)             # 1.10.2
# 查看 GPU 是否可用
print(torch.cuda.is_available())     # True
# 查看GPU数量，索引号从0开始
print(torch.cuda.current_device())   # 0
# 根据索引号查看GPU名字
print(torch.cuda.get_device_name(0)) # NVIDIA GeForce GTX 1070
