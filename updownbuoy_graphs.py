import csv
import matplotlib.pyplot as plt
import os


def get_data(col_num, start, stop, csvfn):
    cwd = os.getcwd()  # Get the current working directory (cwd)
    files = os.listdir(cwd)  # Get all the files in that directory
    print("Files in %r: %s" % (cwd, files))
    print(csvfn)
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




def draw_graph_depth_temp(csv, date, start, stop, trange, depth, temp):
    # line 1 points
    y1 = get_data(temp, start, stop, csv)
    y2 = get_data(depth, start, stop, csv)
    x = range(0, trange)

    fig, ax1 = plt.subplots()

    color = 'tab:red'
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel('Temperature (˚C)', color=color)
    ax1.plot(x, y1, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    plt.title("Up/Down Mini Buoy " +  str(date) +": Temperature (˚C) and Depth (m)")

    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

    color = 'tab:blue'
    ax2.set_ylabel('Depth (m)', color=color)  # we already handled the x-label with ax1
    ax2.plot(x, y2, color=color)
    ax2.invert_yaxis()
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()  # otherwise the right y-label is slightly clipped

    # function to show the plot
    plt.show()

def draw_graph_depth_ODOmgL_turb(csv, date, start, stop, trange, depthm, odomgl, turb):
    # line 1 points
    ODO = get_data(odomgl, start, stop, csv)
    turbidity = get_data(turb, start, stop, csv)
    depth = get_data(depthm, start, stop, csv)
    x = range(0, trange)

    fig, (ax1, c) = plt.subplots(2, sharex=True, sharey=False)

    color = 'tab:red'
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel('ODO (mg/L)', color=color)
    ax1.plot(x, ODO, color=color)
    ax1.tick_params(axis='y', labelcolor=color)


    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

    color = 'tab:blue'
    ax2.set_ylabel('Depth (m)', color=color)  # we already handled the x-label with ax1
    ax2.plot(x, depth, color=color)
    ax2.invert_yaxis()
    ax2.tick_params(axis='y', labelcolor=color)

    color = 'tab:green'
    c.set_ylabel('Turbidity (FNU)', color=color)  # we already handled the x-label with ax1
    c.plot(x, turbidity, color=color)
    c.tick_params(axis='y', labelcolor=color)

    ax3 = c.twinx()  # instantiate a second axes that shares the same x-axis

    color = 'tab:blue'
    ax3.set_ylabel('Depth (m)', color=color)  # we already handled the x-label with ax1
    ax3.plot(x, depth, color=color)
    ax3.invert_yaxis()
    ax3.tick_params(axis='y', labelcolor=color)

    plt.title("Up/Down Mini Buoy "+ str(date) +  ": ODO (mg/L), Turbidity (FNU), and Depth (m)")


    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    plt.autoscale(False)

    # function to show the plot
    plt.show()

def draw_graph_depth_ODO_turb(csv, date, start, stop, trange, depth, odopercent, turb):
    # line 1 points
    ODO = get_data(odopercent, start, stop, csv)
    turbidity = get_data(turb, start, stop, csv)
    depth = get_data(depth, start, stop, csv)
    x = range(0, trange)

    fig, (ax1, c) = plt.subplots(2, sharex=True, sharey=False)

    color = 'tab:red'
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel('ODO (%sat)', color=color)
    ax1.plot(x, ODO, color=color)
    ax1.tick_params(axis='y', labelcolor=color)


    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

    color = 'tab:blue'
    ax2.set_ylabel('Depth (m)', color=color)  # we already handled the x-label with ax1
    ax2.plot(x, depth, color=color)
    ax2.invert_yaxis()
    ax2.tick_params(axis='y', labelcolor=color)

    color = 'tab:green'
    c.set_ylabel('Turbidity (FNU)', color=color)  # we already handled the x-label with ax1
    c.plot(x, turbidity, color=color)
    c.tick_params(axis='y', labelcolor=color)

    ax3 = c.twinx()  # instantiate a second axes that shares the same x-axis

    color = 'tab:blue'
    ax3.set_ylabel('Depth (m)', color=color)  # we already handled the x-label with ax1
    ax3.plot(x, depth, color=color)
    ax3.invert_yaxis()
    ax3.tick_params(axis='y', labelcolor=color)

    plt.title("Up/Down Mini Buoy "+ str(date) + ": ODO (%sat), Turbidity (FNU), and Depth (m)")


    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    plt.autoscale(False)

    # function to show the plot
    plt.show()

def draw_graph_depth_chloro_conduct(csv, date, start, stop, trange, depthl, chlorop, conductive):
    # line 1 points
    chloro = get_data(chlorop, start, stop, csv)
    conduct = get_data(conductive, start, stop, csv)
    depth = get_data(depthl, start, stop,  csv)
    x = range(trange)

    fig, (ax1, c) = plt.subplots(2, sharex=True, sharey=False)

    color = 'tab:red'
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel('Conductivity (µS/cm)', color=color)
    ax1.plot(x, conduct, color=color)
    ax1.tick_params(axis='y', labelcolor=color)


    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

    color = 'tab:blue'
    ax2.set_ylabel('Depth (m)', color=color)  # we already handled the x-label with ax1
    ax2.plot(x, depth, color=color)
    ax2.invert_yaxis()
    ax2.tick_params(axis='y', labelcolor=color)

    color = 'tab:green'
    c.set_ylabel('Chlorophyll (RFU)', color=color)  # we already handled the x-label with ax1
    c.plot(x, chloro, color=color)
    c.tick_params(axis='y', labelcolor=color)

    ax3 = c.twinx()  # instantiate a second axes that shares the same x-axis

    color = 'tab:blue'
    ax3.set_ylabel('Depth (m)', color=color)  # we already handled the x-label with ax1
    ax3.plot(x, depth, color=color)
    ax3.invert_yaxis()
    ax3.tick_params(axis='y', labelcolor=color)

    plt.title("Up/Down Mini Buoy " + str(date) + ": Chlorophyll (RFU), Conductivity (µS/cm), and Depth (m)")


    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    plt.autoscale(False)

    # function to show the plot
    plt.show()

def do_four_graphs(csv_filename, date, start, stop, range, depth, temp, chloro, conduct, odopercent, odomgl, turb):
    draw_graph_depth_temp(csv_filename, date, start, stop, range, depth, temp)
    draw_graph_depth_ODOmgL_turb(csv_filename, date, start, stop, range, depth, odomgl, turb)
    draw_graph_depth_ODO_turb(csv_filename, date, start, stop, range, depth, odopercent, turb)
    draw_graph_depth_chloro_conduct(csv_filename, date, start, stop, range, depth, chloro, conduct)


#do_four_graphs("../3_19_data.csv", "3/19/20", 395, 1062, 668, 10, 24, 8, 9, 12, 14, 20)
#do_four_graphs("../3_19_data.csv", "3/19/20", 745, 995, 251, 10, 24, 8, 9, 12, 14, 20)
#do_four_graphs('3_8_data.csv', "3/8/20", 1170, 1261, 92, 10, 24, 8, 9, 12, 14, 20)
#do_four_graphs("../March_13_2020/3_13_data.csv", "3/13/20", 790, 1676, 887, 8, 22, 6, 7, 10, 12, 18)
#do_four_graphs("../May_2_2020/5_2_data.csv", "5/2/20", 451, 3885, 3435, 17, 31, 15, 16, 19, 21, 27)
#do_four_graphs("../May_10_2020/5_10_data.csv", "5/10/20", 458, 4231, 3774, 17, 31, 15, 16, 19, 21, 27)
#do_four_graphs("../May_17_2020/5_17_data.csv", "5/17/20", 723, 4530, 3808, 22, 36, 20, 21, 24, 26, 32)
#do_four_graphs("../April_5_2020/4_5_data.csv", "4/5/20", 312, 1893, 1582, 22, 36, 20, 21, 24, 26, 32)
#do_four_graphs("../April_11_2020/4_11_data.csv", "4/11/20", 1222, 1738, 517, 22, 36, 20, 21, 24, 26, 32)
#do_four_graphs("../April_19_2020/4_19_data.csv", "4/19/20", 1141, 2431, 1291, 22, 36, 20, 21, 24, 26, 32)
#do_four_graphs("../April_25_2020/4_25_data.csv", "4/25/20", 887, 3074, 2188, 22, 36, 20, 21, 24, 26, 32)
#do_four_graphs("../March_26_2020/3_26_data.csv", "3/26/20", 374, 847, 474, 22, 36, 20, 21, 24, 26, 32)
#do_four_graphs("../March_26_2020/3_26_data.csv", "3/26/20", 4006, 4341, 336, 22, 36, 20, 21, 24, 26, 32)