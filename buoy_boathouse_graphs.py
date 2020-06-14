import csv
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import os


def get_data(col_num, start, stop, csvfn):
    cwd = os.getcwd()  # Get the current working directory (cwd)
    files = os.listdir(cwd)  # Get all the files in that directory
    print("Files in %r: %s" % (cwd, files))
    print(csvfn)

    # reads through the csv file and returns all relevant data in an array
    with open(csvfn, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        graph_data = []
        line_count = 0
        for row in csv_reader:
            if start <= line_count <= stop:
                graph_data.append(float(row[col_num]))
                line_count += 1
            else:
                line_count += 1
    return graph_data


def draw_graph_depth_temp(csv, date, start, stop, trange, depthl, temp):
    # line 1 points
    y1 = get_data(temp, start, stop, csv)
    x = range(0, trange)

    fig, ax1 = plt.subplots()

    color = 'tab:red'
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel('Temperature (˚C)', color=color)
    ax1.plot(x, y1, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    plt.title("Buoy to Boathouse " + str(date) + ": Temperature (˚C)")
    fig.tight_layout()  # otherwise the right y-label is slightly clipped

    depth = mpatches.Patch(color='blue', label='Average Depth:' + str(depthl) + ' m')
    plt.legend(handles=[depth])

    fig.savefig("BuoyBoathouseTempDepth.png")  # saves the graph image

    # function to show the plot
    plt.show()


def draw_graph_depth_ODOmgL_turb(csv, date, start, stop, trange, depthl, odomgl, turb):
    # line 1 points
    ODO = get_data(odomgl, start, stop, csv)
    turbidity = get_data(turb, start, stop, csv)
    x = range(0, trange)

    fig, ax1 = plt.subplots()

    color = 'tab:red'
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel('ODO (mg/L)', color=color)
    ax1.plot(x, ODO, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

    color = 'tab:green'
    ax2.set_ylabel('Turbidity (FNU)', color=color)  # we already handled the x-label with ax1
    ax2.plot(x, turbidity, color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    plt.title("Buoy to Boathouse " + str(date) + ": ODO (mg/L) and Turbidity (FNU)")

    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    plt.autoscale(False)

    depth = mpatches.Patch(color='blue', label='Average Depth:' + str(depthl) + ' m')
    plt.legend(handles=[depth])

    fig.savefig("BuoyBoathouseODO(mgl)TurbDepth.png")  # saves the graph image

    # function to show the plot
    plt.show()


def draw_graph_depth_ODO_turb(csv, date, start, stop, trange, depthl, odopercent, turb):
    # line 1 points
    ODO = get_data(odopercent, start, stop, csv)
    turbidity = get_data(turb, start, stop, csv)
    x = range(0, trange)

    fig, ax1 = plt.subplots()

    color = 'tab:red'
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel('ODO (mg/L)', color=color)
    ax1.plot(x, ODO, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

    color = 'tab:green'
    ax2.set_ylabel('Turbidity (FNU)', color=color)  # we already handled the x-label with ax1
    ax2.plot(x, turbidity, color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    plt.title("Buoy to Boathouse " + str(date) + ": ODO (%sat) and Turbidity (FNU)")

    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    plt.autoscale(False)

    depth = mpatches.Patch(color='blue', label='Average Depth:' + str(depthl) + ' m')
    plt.legend(handles=[depth])

    fig.savefig("BuoyBoathouseODO(%)TurbDepth.png")  # saves the graph image

    # function to show the plot
    plt.show()


def draw_graph_depth_chloro_conduct(csv, date, start, stop, trange, depthl, chlorop, conductive):
    # line 1 points
    chloro = get_data(chlorop, start, stop, csv)
    conduct = get_data(conductive, start, stop, csv)
    x = range(trange)

    fig, ax1 = plt.subplots()

    color = 'tab:red'
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel('Conductivity (µS/cm)', color=color)
    ax1.plot(x, conduct, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

    color = 'tab:green'
    ax2.set_ylabel('Chlorophyll (RFU)', color=color)  # we already handled the x-label with ax1
    ax2.plot(x, chloro, color=color)
    ax2.tick_params(axis='y', labelcolor=color)

    plt.title("Buoy to Boathouse " + str(date) + ": Chlorophyll (RFU) and Conductivity (µS/cm)")

    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    plt.autoscale(False)

    depth = mpatches.Patch(color='blue', label='Average Depth:' + str(depthl) + ' m')
    plt.legend(handles=[depth])

    fig.savefig("BuoyBoathouseChloroConductDepth.png")  # saves the graph image

    # function to show the plot
    plt.show()


# calls all the necessary graphing functions
def do_four_graphs(csv_filename, date, start, stop, range, depth, temp, chloro, conduct, odopercent, odomgl, turb):
    draw_graph_depth_temp(csv_filename, date, start, stop, range, depth, temp)
    draw_graph_depth_ODOmgL_turb(csv_filename, date, start, stop, range, depth, odomgl, turb)
    draw_graph_depth_ODO_turb(csv_filename, date, start, stop, range, depth, odopercent, turb)
    draw_graph_depth_chloro_conduct(csv_filename, date, start, stop, range, depth, chloro, conduct)

# do_four_graphs("May_2_2020/5_2_data.csv", "5/2/20", 4123, 4314, 192, -2.4899, 31, 15, 16, 19, 21, 27)
# do_four_graphs("May_10_2020/5_10_data.csv", "5/10/20", 4318, 4495, 178, -2.1852, 31, 15, 16, 19, 21, 27)
# do_four_graphs("May_17_2020/5_17_data.csv", "5/17/20", 4601, 4770, 170, -1.9987, 36, 20, 21, 24, 26, 32)
# do_four_graphs("April_25_2020/4_25_data.csv", "4/25/20", 3075, 3215, 141, -2.4399, 36, 20, 21, 24, 26, 32)
