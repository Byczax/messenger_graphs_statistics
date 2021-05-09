from matplotlib import pyplot as plt
import matplotlib
import mplcairo


def draw_plot(data: list[str], plot_name: str, save: bool = False):
    plt.rcParams.update(
        {'font.size': 8, 'font.family': 'symbola'})
    plt.figure(num=None, figsize=(20, 8), dpi=400, facecolor='w', edgecolor='k')
    plt.subplots_adjust(left=0.03, right=0.99, top=0.96, bottom=0.18)
    plt.bar(list(map(lambda my_tuple: my_tuple[0], data)),
            list(map(lambda my_tuple: my_tuple[1], data)))
    for caption in data:
        plt.text(caption[0], caption[1], caption[1], rotation=90, va='bottom', ha='center')
    plt.xticks(rotation=90)
    plt.title(plot_name)
    if save:
        plt.savefig("img/" + plot_name + ".png")
    plt.show()
