import matplotlib.font_manager as font_manager
import matplotlib.pyplot as plt
from typing import List
import os

# font_path = "C:/Users/byczq/AppData/Local/Microsoft/Windows/Fonts/Symbola.ttf"
# prop = font_manager.FontProperties(fname=font_path)


def draw_plot(data: List[str], plot_name: str, save: bool, number: int, path: str):
    # plt.rcParams["font.family"] = "Symbola"
    plt.rcParams.update({'font.size': 8})
    plt.figure(num=None, figsize=(20, 8), dpi=400, facecolor='w', edgecolor='k')
    plt.subplots_adjust(left=0.03, right=0.99, top=0.96, bottom=0.18)
    plt.bar(list(map(lambda my_tuple: my_tuple[0], data)),
            list(map(lambda my_tuple: my_tuple[1], data)))
    for caption in data:
        plt.text(caption[0], caption[1], caption[1], va='bottom', ha='center')
    # plt.xticks(rotation=90, position='bottom')
    plt.title(plot_name)
    if save:
        # os.mkdir("../images/")
        plt.savefig(path + str(number) + "-" + plot_name.replace(" ", "-") + ".svg")
    else:
        plt.show()
