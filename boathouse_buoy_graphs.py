import csv
import matplotlib.pyplot as plt
import os
import math


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

# gets and parses echosounder data for confidence level 100
def get_echo_data(echodown, confidence, depth, start, stop, csvfn):
    # reads through the csv file and returns all relevant data in an array
    with open(csvfn, mode='r') as csv_file:
        csv_reader = csv.reader(csv_file, delimiter=',')
        echo_data = []
        time_data = []
        line_count = 0
        for row in csv_reader:
            print(row[confidence])
            if start <= line_count <= stop and row[confidence] == '100':
                echo_data.append(float(row[echodown]) + float(row[depth]))
                time_data.append(line_count-start)  # elapsed seconds
                line_count += 1
            else:
                line_count += 1
    return time_data, echo_data

def draw_graph_depth_temp(csv, date, start, stop, trange, depth, temp, echodown, confidence):
    # line 1 points
    y1 = get_data(temp, start, stop, csv)
    y2 = get_data(depth, start, stop, csv)
    x = range(0, trange)

    # echosounder down data
    time, edepth = get_echo_data(echodown, confidence, depth, start, stop, csv)

    fig, ax1 = plt.subplots()

    color = 'tab:red'
    ax1.set_xlabel('Time (s)')
    ax1.set_ylabel('Temperature (˚C)', color=color)
    ax1.plot(x, y1, color=color)
    ax1.tick_params(axis='y', labelcolor=color)

    plt.title("Boathouse to Buoy " + str(date) + ": Temperature (˚C) and Depth (m)")

    ax2 = ax1.twinx()  # instantiate a second axes that shares the same x-axis

    color = 'tab:blue'
    ax2.set_ylabel('Depth (m)', color=color)  # we already handled the x-label with ax1
    ax2.plot(x, y2, color=color)
    ax2.scatter(time, edepth, color=color, marker='o')  # adds the echosounder depth
    ax2.invert_yaxis()
    ax2.tick_params(axis='y', labelcolor=color)

    fig.tight_layout()  # otherwise the right y-label is slightly clipped

    fig.savefig("BoathouseBuoyTempAndDepth.png")  # saves the graph image

    # function to show the plot
    plt.show()


def draw_graph_depth_ODOmgL_turb(csv, date, start, stop, trange, depthm, odomgl, turb, echodown, confidence):
    # line 1 points
    ODO = get_data(odomgl, start, stop, csv)
    turbidity = get_data(turb, start, stop, csv)
    depth = get_data(depthm, start, stop, csv)
    x = range(0, trange)

    # echosounder down data
    time, edepth = get_echo_data(echodown, confidence, depthm, start, stop, csv)

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
    ax2.scatter(time, edepth, color=color, marker='o')  # adds the echosounder depth
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
    ax3.scatter(time, edepth, color=color, marker='o')  # adds the echosounder depth
    ax3.invert_yaxis()
    ax3.tick_params(axis='y', labelcolor=color)

    plt.title("Boathouse to Buoy " + str(date) + ": ODO (mg/L), Turbidity (FNU), and Depth (m)")

    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    plt.autoscale(False)

    fig.savefig("BoathouseBuoyODO(mgl)TurbDepth.png")  # saves the graph image

    # function to show the plot
    plt.show()


def draw_graph_depth_ODO_turb(csv, date, start, stop, trange, depthm, odopercent, turb, echodown, confidence):
    # line 1 points
    ODO = get_data(odopercent, start, stop, csv)
    turbidity = get_data(turb, start, stop, csv)
    depth = get_data(depthm, start, stop, csv)
    x = range(0, trange)

    # echosounder down data
    time, edepth = get_echo_data(echodown, confidence, depthm, start, stop, csv)

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
    ax2.scatter(time, edepth, color=color, marker='o')  # adds the echosounder depth
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
    ax3.scatter(time, edepth, color=color, marker='o')  # adds the echosounder depth
    ax3.invert_yaxis()
    ax3.tick_params(axis='y', labelcolor=color)

    plt.title("Boathouse to Buoy " + str(date) + ": ODO (%sat), Turbidity (FNU), and Depth (m)")

    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    plt.autoscale(False)

    fig.savefig("BoathouseBuoyODO(%)TurbDepth.png")  # saves the graph image

    # function to show the plot
    plt.show()


def draw_graph_depth_chloro_conduct(csv, date, start, stop, trange, depthl, chlorop, conductive, echodown, confidence):
    # line 1 points
    chloro = get_data(chlorop, start, stop, csv)
    conduct = get_data(conductive, start, stop, csv)
    depth = get_data(depthl, start, stop, csv)
    x = range(trange)

    # echosounder down data
    time, edepth = get_echo_data(echodown, confidence, depthl, start, stop, csv)

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
    ax2.scatter(time, edepth, color=color, marker='o')  # adds the echosounder depth
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
    ax3.scatter(time, edepth, color=color, marker='o')  # adds the echosounder depth
    ax3.invert_yaxis()
    ax3.tick_params(axis='y', labelcolor=color)

    plt.title("Boathouse to Buoy " + str(date) + ": Chlorophyll (RFU), Conductivity (µS/cm), and Depth (m)")

    fig.tight_layout()  # otherwise the right y-label is slightly clipped
    plt.autoscale(False)

    fig.savefig("BoathouseBuoyChloroConductDepth.png")  # saves the graph image

    # function to show the plot
    plt.show()


def draw_velocity(csv, date, start, stop, trange, x_data, y_data, z_data):
    # line 1 points
    x_pos = get_data(x_data, start, stop, csv)
    y_pos = get_data(y_data, start, stop, csv)
    z_pos = get_data(z_data, start, stop, csv)
    velocity = []
    time = range(0, trange - 1)  # to account for one less data point after calculating average velocity

    # Find the speed by computing an average of the z,y and z position graph slopes
    for i in range(len(x_pos) - 1):
        # find all instantaneous velocities, then average
        vx = (x_pos[i + 1] - x_pos[i]) / 1  # a recording is taken every second
        vy = (y_pos[i + 1] - y_pos[i]) / 1
        vz = (z_pos[i + 1] - z_pos[i]) / 1
        vel = math.sqrt(vx * vx + vy * vy + vz * vz)
        velocity.append(vel)

    fig, ax = plt.subplots()

    color = 'tab:blue'
    ax.set_xlabel('Time (s)')
    ax.set_ylabel('Velocity (m/s)', color=color)
    ax.plot(time, velocity, color=color)
    ax.tick_params(axis='y', labelcolor=color)

    plt.title("Boathouse to Buoy " + str(date) + ": Average Velocity (m/s)")

    fig.savefig("BoathouseBuoyVelocity.png")

    # function to show the plot
    plt.show()


# calls all the necessary graphing functions
def do_four_graphs(csv_filename, date, start, stop, range, depth, temp, chloro, conduct, odopercent, odomgl, turb, echodown, confidence):
    draw_graph_depth_temp(csv_filename, date, start, stop, range, depth, temp, echodown, confidence)
    draw_graph_depth_ODOmgL_turb(csv_filename, date, start, stop, range, depth, odomgl, turb, echodown, confidence)
    draw_graph_depth_ODO_turb(csv_filename, date, start, stop, range, depth, odopercent, turb, echodown, confidence)
    draw_graph_depth_chloro_conduct(csv_filename, date, start, stop, range, depth, chloro, conduct, echodown, confidence)

# do_four_graphs("March_19_2020/3_19_data.csv", "3/19/20", 273, 386, 114, 10, 24, 8, 9, 12, 14, 20)
# do_four_graphs('March_8_2020/3_8_data.csv', "3/8/20", 1004, 1171, 168, 10, 24, 8, 9, 12, 14, 20)
# do_four_graphs("March_13_2020/3_13_data.csv", "3/13/20", 493, 596, 104, 8, 22, 6, 7, 10, 12, 18)
# do_four_graphs("May_2_2020/5_2_data.csv", "5/2/20", 250, 450, 201, 17, 31, 15, 16, 19, 21, 27)
# do_four_graphs("May_10_2020/5_10_data.csv", "5/10/20", 129, 457, 329, 17, 31, 15, 16, 19, 21, 27)
# do_four_graphs("May_17_2020/5_17_data.csv", "5/17/20", 312, 706, 395, 22, 36, 20, 21, 24, 26, 32, 8, 9)
# do_four_graphs("April_5_2020/4_5_data.csv", "4/5/20", 114, 312, 199, 22, 36, 20, 21, 24, 26, 32, 8, 9)
# do_four_graphs("April_11_2020/4_11_data.csv", "4/11/20", 843, 1222, 380, 22, 36, 20, 21, 24, 26, 32, 8, 9)
# do_four_graphs("April_19_2020/4_19_data.csv", "4/19/20", 766, 1141, 376, 22, 36, 20, 21, 24, 26, 32, 8, 9)
# do_four_graphs("April_25_2020/4_25_data.csv", "4/25/20", 497, 866, 370, 22, 36, 20, 21, 24, 26, 32)
# do_four_graphs("March_26_2020/3_26_data.csv", "3/26/20", 156, 323, 168, 22, 36, 20, 21, 24, 26, 32, 8, 9)
do_four_graphs("March_26_2020/3_26_data.csv", "3/26/20", 3654, 4006, 353, 22, 36, 20, 21, 24, 26, 32, 8, 9)
