import matplotlib.pyplot as plt
from matplotlib import animation
import numpy as np
import datetime as dt
from itertools import cycle

def create_animation(data, calculated_data, path: str):
    
    sorted_calculated_data = dict(
        sorted(calculated_data.items(), key=lambda item: item[1])
    )
    sorted_calculated_data = {k: v for k, v in sorted_calculated_data.items() if v >= 1}
    message_list = []
    for message in data.file["messages"]:
        if not (data.end_date >= message["timestamp_ms"] >= data.start_date):
            continue
        if message["sender_name"] not in sorted_calculated_data.keys():
            continue
        message_list.append(message)
    sorted_message_list = sorted(message_list, key=lambda d: d["timestamp_ms"])
    
    # print(sorted_calculated_data.keys())
    template = np.zeros(len(sorted_calculated_data.keys())).tolist()
    animation_frames = []
    animation_frames.append(template.copy())
    dates = []
    previous_date = format_time(sorted_message_list[0]["timestamp_ms"])
    dates.append(previous_date)
    for message in sorted_message_list:
        template[list(sorted_calculated_data.keys()).index(message["sender_name"])] += 1
        if format_time(message["timestamp_ms"]) != previous_date:
            animation_frames.append(template.copy())
            previous_date = format_time(message["timestamp_ms"])
            dates.append(previous_date)
        # animation_frames.append(template.copy())
    dates.append(format_time(message["timestamp_ms"]))

    animate_on_horizontal_bar_plot(
        animation_frames, list(sorted_calculated_data.keys()), dates, max(sorted_calculated_data.values()), path
    )

def format_time(timestamp):
    file_time = dt.datetime.fromtimestamp(timestamp/1000)
    return file_time.strftime("%d-%m-%Y")
# def bar_list(n):
#     return [1 / float(n * k) for k in range(1, 10)]


def animate_on_horizontal_bar_plot(frames, x_labels, dates, max_value, path: str):
    plt.rcParams["svg.fonttype"] = "none"
    plt.rcParams['font.size'] = 9
    # plt.rcParams['animation.codec'] = 'h265'
    fig, ax = plt.subplots(figsize=(18, 9), facecolor="w", edgecolor="k", dpi=200)
    # fig, ax = plt.subplots(figsize=(10, 20), facecolor="w", edgecolor="k", dpi=400)

    for s in ["top", "bottom", "left", "right"]:
        ax.spines[s].set_visible(False)

    # Remove x, y Ticks
    ax.xaxis.set_ticks_position("none")
    ax.yaxis.set_ticks_position("none")
    # ax.set_ylim(0, max_value)
    # ax.set_yscale('log')
    plt.margins(0)
    plt.subplots_adjust(bottom=0.2, top=0.99, left=0.04, right=0.99)
    # Add x, y gridlines
    ax.grid(b=True, color="grey", linestyle="-.", linewidth=0.5, alpha=0.2)
    # number_of_frames = len(data)

    # bar_collection = plt.bar(x_labels, bar_list(1))

    plt.xticks(rotation=90)
    print(len(x_labels))
    print(max_value)
    numbers = np.linspace(0, max_value, len(x_labels), dtype=int)
    # numbers = list(range(0, max_value+1, (max_value+1)//100))
    print(len(numbers))
    # colors = cycle(['royalblue', 'green', 'orangered', 'gold', 'teal', 'purple', 'pink', 'brown', 'grey'])
    # create cycle of blue colors
    colors = cycle(['blue','royalblue','dodgerblue'])
    bar_rects = ax.bar(x_labels, numbers[(len(numbers) - len(x_labels)):])
    for bar in bar_rects:
        bar.set_color(next(colors))
    # ax.set_ylim(0, max_value)
    plt.text(
        0.3,
        0.6,
        "messenger-stats.byczko.pl",
        fontsize=15,
        color="gray",
        ha="center",
        va="center",
        transform=plt.gcf().transFigure,
        alpha=0.5,
    )
    
    counter = [0]
    all_frames = len(frames)
    annotation = ax.annotate(f'{dates[counter[0]].split("-",1)[1]}', (5, 3000), zorder=20, fontsize=20)
    def update(frame):
        print(f'{counter[0]}/{all_frames}')
        
        # ax.clear()
        # ax.text(0.5, 0.5, f'{dates[counter[0]]}', fontsize=20, ha='center', va='center')
        annotation.set_text(f'{dates[counter[0]].split("-",1)[1]}')
        
        for rect, height in zip(bar_rects, frame):
            rect.set_height(height)
        counter[0] += 1

    anim = animation.FuncAnimation(
        fig, update, repeat=False, frames=frames, interval=10
    )
    # def animate(i):
    # y = bar_list(i + 1)
    # for i, b in enumerate(bar_collection):
    #     b.set_height(y[i])

    anim.save(f"{path}animated-stats.mp4", writer=animation.FFMpegWriter(fps=15))
    # plt.show()


# fig = plt.figure()

# n = 100  # Number of frames
# x = range(1, 10)
# bar_collection = plt.bar(x, bar_list(1))
