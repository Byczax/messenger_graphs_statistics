from datetime import datetime
import matplotlib.pyplot as plt
from typing import List

# old vertical plot


def draw_plot_2(data: List[str], plot_name: str, save: bool, number: int, path: str):
    plt.rcParams.update({'font.size': 8})
    plt.figure(num=None, figsize=(20, 8), dpi=400,
               facecolor='w', edgecolor='k')
    plt.subplots_adjust(left=0.03, right=0.99, top=0.96, bottom=0.18)
    plt.bar(list(map(lambda my_tuple: my_tuple[0], data)),
            list(map(lambda my_tuple: my_tuple[1], data)))
    for caption in data:
        plt.text(caption[0], caption[1], caption[1],
                 rotation=90, va='bottom', ha='center')
    plt.xticks(rotation=90)
    plt.title(plot_name)
    if save:
        plt.savefig(path + str(number) + "-" +
                    plot_name.replace(" ", "-") + ".svg")
    else:
        plt.show()


# horizontal plot
def draw_plot(data: List[str], plot_name: str, save: bool, path: str, number: int):
    _, ax = plt.subplots(figsize=(10, 30), facecolor='w', edgecolor='k')
    ax.barh(
        list(map(lambda my_tuple: my_tuple[0], data)),
        list(map(lambda my_tuple: my_tuple[1], data))
    )
    for s in ['top', 'bottom', 'left', 'right']:
        ax.spines[s].set_visible(False)

    # Remove x, y Ticks
    ax.xaxis.set_ticks_position('none')
    ax.yaxis.set_ticks_position('none')

    plt.margins(0)
    # Add x, y gridlines
    ax.grid(b=True, color='grey',
            linestyle='-.', linewidth=0.5,
            alpha=0.2)

    # Add annotation to bars
    for i in ax.patches:
        plt.text(i.get_width(), i.get_y()+0.1,
                 str(round((i.get_width()), 2)),
                 fontsize=8, fontweight='bold',
                 color='grey')

    # Add Text watermark
    # fig.text(0.9, 0.15, 'Byczax - stats', fontsize=12,
    #          color='grey', ha='right', va='bottom',
    #          alpha=0.7)
    # -{date.today()} <- maybe add later for filename
    timestamp = str(datetime.now().time()).split(".")[0].replace(":","")[:-2]
    if save:
        plt.savefig(
            f'{path}{str(10+number)}{timestamp}-{plot_name.replace(" ", "-")}.svg', bbox_inches='tight')
    else:
        plt.show()
