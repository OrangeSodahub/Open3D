import numpy as np

import matplotlib.pyplot as plt
from matplotlib.pyplot import cm

plt.rcParams.update({
    "text.usetex": True,
    "font.family": "sans-serif",
    "font.sans-serif": ["Helvetica"]
})
# for Palatino and other serif fonts use:
plt.rcParams.update({
    "text.usetex": True,
    "font.family": "serif",
    "font.serif": ["Palatino"],
})

# Tango
# colors = ['#3465a4', '#ef2929', '#73d216', '#fcaf3e']
# Google
# colors = ['#4285F4f0', '#DB4437f0', '#F4B400f0', '#0F9D58f0']
colors = cm.Pastel1.colors
fig, axs = plt.subplots(1, 2, figsize=(20, 5))
x = np.arange(0, 3) * 2
width = 0.4

xticks = x + 1.5 * width
xlabels = ['Integration', 'Raycasting', 'Meshing']

ours_time = np.array([0.751, 0.967, 146.47])
infinitam_time = np.array([0.7011, 1.11, 1529.59])
voxelhashing_time = np.array([2.34, 5.37, 31445])
gpurobust_time = np.array([6.119, 47.94, 167.85])

ours_loc = np.array([359, 591, 488])
infinitam_loc = np.array([1173, 1509, 287])
voxelhashing_loc = np.array([1438, 719, 853])
gpurobust_loc = np.array([723, 770, 746])

ours = [ours_time, ours_loc]
infinitam = [infinitam_time, infinitam_loc]
voxelhashing = [voxelhashing_time, voxelhashing_loc]
gpurobust = [gpurobust_time, gpurobust_loc]

ylabels = ['Time (ms)', 'Lines']
titles = [r'\textbf{Time per Operation}', r'\textbf{Line of Code (LoC)}']

yticks = [[1e-1, 1e0, 1e1, 1e2, 1e3, 1e4, 1e5], [0, 350, 700, 1050, 1400, 1750]]
for i in range(2):
    # Bar
    axs[i].bar(x, ours[i], width, color=colors[0], label='ASH-fast')
    axs[i].bar(x + width,
               infinitam[i],
               width,
               color=colors[1],
               label='InfiniTAM')
    axs[i].bar(x + 2 * width,
               voxelhashing[i],
               width,
               color=colors[2],
               label='VoxelHashing')
    axs[i].bar(x + 3 * width,
               gpurobust[i],
               width,
               color=colors[3],
               label='GPU-robust')

    # Text
    title_fontsize = 20
    text_fontsize = 15
    xlabel_fontsize = 18
    for k, xk in enumerate(x):
        # if i == 0:
        #     axs[i].text(xk,
        #                 ours[i][k],
        #                 r'${:.2f}$'.format(ours[i][k]),
        #                 fontweight='bold',
        #                 bbox=dict(alpha=0, pad=1),
        #                 verticalalignment='bottom',
        #                 horizontalalignment='center')
        # else:
        #     axs[i].text(xk,
        #                 ours[i][k],
        #                 r'${:d}$'.format(int(ours[i][k])),
        #                 fontweight='bold',
        #                 bbox=dict(alpha=0, pad=1),
        #                 verticalalignment='bottom',
        #                 horizontalalignment='center')

        axs[i].text(xk,
                    ours[i][k],
                    r'$1.0\times$'.format(ours[i][k]),
                    fontsize=text_fontsize,
                    fontweight='bold',
                    bbox=dict(alpha=0, pad=1),
                    verticalalignment='bottom',
                    horizontalalignment='center')

        axs[i].text(xk + width,
                    infinitam[i][k],
                    r'${:.2f}\times$'.format(infinitam[i][k] / ours[i][k]),
                    fontsize=text_fontsize,
                    fontweight='bold',
                    bbox=dict(alpha=0, pad=1),
                    verticalalignment='bottom',
                    horizontalalignment='center')
        axs[i].text(xk + 2 * width,
                    voxelhashing[i][k],
                    r'${:.2f}\times$'.format(voxelhashing[i][k] / ours[i][k]),
                    fontsize=text_fontsize,
                    fontweight='bold',
                    bbox=dict(alpha=0, pad=1),
                    verticalalignment='bottom',
                    horizontalalignment='center')
        axs[i].text(xk + 3 * width,
                    gpurobust[i][k],
                    r'${:.2f}\times$'.format(gpurobust[i][k] / ours[i][k]),
                    fontsize=text_fontsize,
                    fontweight='bold',
                    bbox=dict(alpha=0, pad=1),
                    verticalalignment='bottom',
                    horizontalalignment='center')

    axs[i].set_title(titles[i], fontsize=title_fontsize)

    axs[i].set_xticks(xticks)
    axs[i].set_xticklabels(xlabels)
    if i == 0:
        axs[i].set_yscale('log')

    axs[i].set_yticks(yticks[i])
    axs[i].set_ylabel(ylabels[i], fontsize=text_fontsize)
    axs[i].yaxis.grid()
    axs[i].tick_params(axis='x', labelsize=xlabel_fontsize)
    axs[i].tick_params(axis='y', labelsize=text_fontsize)

plt.tight_layout(rect=[0, 0, 0.88, 1])
plt.legend(bbox_to_anchor=(1.01, 1), loc='upper left', fontsize=text_fontsize)
plt.savefig('profile.pdf')
