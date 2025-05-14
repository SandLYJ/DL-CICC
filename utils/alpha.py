import numpy as np
import matplotlib.pyplot as plt
import matplotlib
from PIL import Image

matplotlib.rcParams['font.sans-serif'] = ['Arial']
matplotlib.rcParams['axes.unicode_minus'] = False

nn_number = ['0', '0.01', '0.05', '0.1', '0.5']

CIFAR_NMI = np.array([63.2, 63.3, 64.0, 62.4, 61.5])
CIFAR_ACC = np.array([63.5, 63.7, 63.9, 62.1, 61.8])
CIFAR_ARI = np.array([47.2, 47.4, 48.4, 45.5, 44.1])
ImageNet_NMI = np.array([79.1, 79.1, 79.8, 77.2, 76.1])
ImageNet_ACC = np.array([85.3, 85.5, 86.1, 83.4, 81.5])
ImageNet_ARI = np.array([75.0, 75.1, 75.6, 73.0, 71.8])

# type = 'ARI'
# plt.figure(figsize=(5, 5))
# plt.plot(lambda_cluster, CIFAR_ARI, label='CIFAR-10',marker='^')
# plt.plot(lambda_cluster, ImageNet_ARI, label='ImageNet-10',marker='o')
# # plt.xlim(xmin=0,xmax=1000)
# plt.grid(color='lightgrey', linestyle='--')
# plt.legend(loc='best', fontsize=13)
# # plt.title('Cluster performance')
# plt.xlabel('λ', fontsize=13)
# plt.ylabel(f'{type} (%)', fontsize=13)
# plt.savefig(f'figures/ablation/{type}.eps')  # 保存图片
# # im = Image.open('figures/posneg mining/False Negative.png').convert('RGB')
# # im.save('figures/posneg mining/False Negative.eps')
# plt.show()

# type = 'NMI'
plt.figure(figsize=(5, 5))
plt.plot(nn_number, CIFAR_NMI, label='CIFAR-20',marker='o')
plt.plot(nn_number, ImageNet_NMI, label='ImageNet-Dogs',marker='o')
plt.ylim(ymin=20,ymax=90)
plt.grid(color='lightgrey', linestyle='--')
plt.legend(loc=3, fontsize=13)
# plt.ylabel(f'NMI (%)', fontsize=18)
plt.savefig(f'alpha-NMI.eps')
plt.savefig(f'alpha-NMI.png')
plt.show()

plt.figure(figsize=(5, 5))
plt.plot(nn_number, CIFAR_ACC, label='CIFAR-20',marker='o')
plt.plot(nn_number, ImageNet_ACC, label='ImageNet-Dogs',marker='o')
plt.ylim(ymin=20,ymax=100)
plt.grid(color='lightgrey', linestyle='--')
plt.legend(loc=3, fontsize=13)
# plt.ylabel(f'ACC (%)', fontsize=18)
plt.savefig(f'alpha-ACC.eps')
plt.savefig(f'alpha-ACC.png')
plt.show()

plt.figure(figsize=(5, 5))
plt.plot(nn_number, CIFAR_ARI, label='CIFAR-20',marker='o')
plt.plot(nn_number, ImageNet_ARI, label='ImageNet-Dogs',marker='o')
plt.ylim(ymin=0,ymax=90)
plt.grid(color='lightgrey', linestyle='--')
plt.legend(loc=3, fontsize=13)
# plt.ylabel(f'ARI (%)', fontsize=18)
plt.savefig(f'alpha-ARI.eps')
plt.savefig(f'alpha-ARI.png')
plt.show()