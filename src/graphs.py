from datetime import datetime
import matplotlib.pyplot as plt
from typing import List

# old vertical plot


def draw_plot_vertical(data: List[str], plot_name: str, save: bool, path: str, number: int):
    plt.rcParams.update({"font.size": 8})
    plt.figure(num=None, figsize=(20, 8), dpi=400, facecolor="w", edgecolor="k")
    plt.subplots_adjust(left=0.03, right=0.99, top=0.96, bottom=0.18)
    plt.bar(
        list(map(lambda my_tuple: my_tuple[0], data)),
        list(map(lambda my_tuple: my_tuple[1], data)),
        color="purple"
    )
    for caption in data:
        plt.text(
            caption[0], caption[1], caption[1], rotation=90, va="bottom", ha="center"
        )
    plt.xticks(rotation=60)
    plt.title(plot_name)
    
    timestamp = str(datetime.now().time()).split(".")[0].replace(":", "")[:-2]
    if save:
        plt.savefig(
            f'{path}{str(10+number)}{timestamp}-{plot_name.replace(" ", "-")}.svg',
            bbox_inches="tight",
        )
    else:
        plt.show()


# horizontal plot
def draw_plot(data: List[str], plot_name: str, save: bool, path: str, number: int):
    plt.rcParams['svg.fonttype'] = 'none'
    _, ax = plt.subplots(figsize=(10, 30), facecolor="w", edgecolor="k")
    ax.barh(
        list(map(lambda my_tuple: my_tuple[0], data)),
        list(map(lambda my_tuple: my_tuple[1], data)),
    )
    for s in ["top", "bottom", "left", "right"]:
        ax.spines[s].set_visible(False)

    # Remove x, y Ticks
    ax.xaxis.set_ticks_position("none")
    ax.yaxis.set_ticks_position("none")
    plt.margins(0)
    # Add x, y gridlines
    ax.grid(b=True, color="grey", linestyle="-.", linewidth=0.5, alpha=0.2)

    # Add annotation to bars
    for i in ax.patches:
        plt.text(
            i.get_width(),
            i.get_y() + 0.1,
            str(round((i.get_width()), 2)),
            fontsize=8,
            fontweight="bold",
            color="grey",
        )

    # Add Text watermark
    plt.text(
        0.75,
        0.15,
        "messenger-stats.byczko.pl",
        fontsize=15,
        color="gray",
        ha="center",
        va="center",
        transform=plt.gcf().transFigure,
        alpha=0.5,
    )
    # -{date.today()} <- maybe add later for filename
    timestamp = str(datetime.now().time()).split(".")[0].replace(":", "")[:-2]
    if save:
        plt.savefig(
            f'{path}{str(10+number)}{timestamp}-{plot_name.replace(" ", "-")}.svg',
            bbox_inches="tight",
        )
    else:
        plt.show()


def draw_combined_plot(data, plot_name: str, save: bool, path: str, number: int):
    # media dataset
    human = []
    photos = []
    videos = []
    gifs = []
    files = []
    summary = []

    # transform data to lists
    for registry in data:
        human.append(registry[0])
        photos.append(registry[1]["photos"])
        videos.append(registry[1]["videos"])
        gifs.append(registry[1]["gifs"])
        files.append(registry[1]["files"])
        summary.append(
            registry[1]["files"]
            + registry[1]["photos"]
            + registry[1]["videos"]
            + registry[1]["gifs"]
        )

    _, ax = plt.subplots(figsize=(10, 30), facecolor="w", edgecolor="k")

    plt.margins(0)

    for s in ["top", "bottom", "left", "right"]:
        ax.spines[s].set_visible(False)

    # Remove x, y Ticks
    ax.xaxis.set_ticks_position("none")
    ax.yaxis.set_ticks_position("none")

    # Add x, y grid lines
    ax.grid(b=True, color="grey", linestyle="-.", linewidth=0.5, alpha=0.2)

    # Add annotation to bars
    ax.barh(human, summary, color="black")
    for i in ax.patches:
        plt.text(
            i.get_width(),
            i.get_y() + 0.3,
            str(round((i.get_width()), 2)),
            fontsize=8,
            fontweight="bold",
            color="grey",
        )

    # Add media types into legend and chart
    ax.barh(human, photos, label="photos")
    left = photos
    ax.barh(human, videos, label="videos", left=left)
    left = [x + y for (x, y) in zip(left, videos)]
    ax.barh(human, gifs, label="gifs", left=left)
    left = [x + y for (x, y) in zip(left, gifs)]
    ax.barh(human, files, label="files", left=left)

    plt.legend(loc="lower right")
    plt.text(
        0.75,
        0.15,
        "messenger-stats.byczko.pl",
        fontsize=15,
        color="gray",
        ha="center",
        va="center",
        transform=plt.gcf().transFigure,
        alpha=0.5,
    )

    timestamp = str(datetime.now().time()).split(".")[0].replace(":", "")[:-2]
    if save:
        plt.savefig(
            f'{path}{str(10+number)}{timestamp}-{plot_name.replace(" ", "-")}.svg',
            bbox_inches="tight",
        )
    else:
        plt.show()
