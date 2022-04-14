#!/usr/bin/env python3

import pandas as pd
import numpy as np
import sys

import matplotlib.pyplot as plt
import mpl_toolkits.mplot3d.axes3d as p3
import matplotlib.animation as animation

# Modes in which the hand can be represented
plot_modes = ['line', 'scatter']
mode = plot_modes[0] # Mode is 'line' plot by default

if len(sys.argv)==1:
    # No args provided
    print('Please a Mendely dataset CSV file as an argument.')
    exit()
elif len(sys.argv)==2:
    # CSV file arg provided
    filename = sys.argv[1]
    # Mode is 'line' by default
elif len(sys.argv)==3:
    # CSV file and plot mode args provided
    filename = sys.argv[1]
    if sys.argv[2]=='line':
        mode = plot_modes[0]
    elif sys.argv[2]=='scatter':
        mode = plot_modes[1]
    else:
        print(f'Mode must be "line" or "scatter", not "{sys.argv[2]}".')
        exit()

df = pd.read_csv(filename)

# Times are saved as their own list,
# they will be removed from the dataframe
times = df["Time"]

# Axes limits chosen based on Work_Right.csv specifications
# May need to be adjusted per each file
x_lo = -.2
x_hi = .4
y_lo = -.4
y_hi = .2
z_lo = 0
z_hi = .6

x,y,z = [],[],[]

# Remove non-coordinate columns.
# axis=1 to remove columns, axis=0 to remove rows (axis=0 by default)
points = df.drop(["Unnamed: 0","Time"], axis = 1)

num_frames = len(points.index) # Each row is one frame, 
                               # so number of frames is number of rows.

# The coordinates are expected to be given in the order
# x1, y1, z1, x2, y2, z2, ... across the columns until the end.
# So if the number of cols is not divisible by 3, there is a problem 
# with the formate of your data.
if len(points.columns)%3 != 0:
    print("Error: Coordinates not represented correctly.")
    exit()

fig = plt.figure()

points_ax = fig.add_subplot(111, projection='3d') # axes associated with plot
points_ax.set_xlabel('X axis')
points_ax.set_ylabel('Y axis')
points_ax.set_zlabel('Z axis')
title = points_ax.set_title('')
points_ax_graph = points_ax.scatter(x, y, z, color='r')
points_ax.plot(x,y,z, color='b')

def set_limits(ax):

    ax.set_xlim3d(x_lo, x_hi) 
    ax.set_ylim3d(y_lo, y_hi)
    ax.set_zlim3d(z_lo, z_hi)

def plot_scatter_hand(frame, graph):
    # Creates a scatter plot of the hand

    x = []
    y = []
    z = []

    row = frame # Each row is a frame of the animation
    for col in range(0, len(points.columns)-3, 3):

        x_point = points.iloc[row, col+0]
        y_point = points.iloc[row, col+1]
        z_point = points.iloc[row, col+2]

        np_x, np_y, np_z = np.array([x_point, y_point, z_point])
        x.append(np_x)
        y.append(np_y)
        z.append(np_z)

    graph._offsets3d = (x, y, z) # Plots the points

def plot_line_hand(frame, graph):
    # Creates a line plot of the hand

    def get_connection(row, joint1, joint2):
        # Returns the con

        # note: these all return series, not lists
        # The '_L_X' suffix is present in all the columns of Work_Right.csv
        # This may need to be changed for other CSVs
        x = points.loc[row, [f' {joint1}_L_X', f' {joint2}_L_X']]
        y = points.loc[row, [f' {joint1}_L_Y', f' {joint2}_L_Y']]
        z = points.loc[row, [f' {joint1}_L_Z', f' {joint2}_L_Z']]

        # convert the series to lists
        x = list(x.values)
        y = list(y.values)
        z = list(z.values)

        coords = []
        coords.append(x)
        coords.append(y)
        coords.append(z)

        return coords

    row = frame

    # all connections between given joints pairs
    conn = [# THUMB #
            ["thumbEF", "thumbProximal"],
            ["thumbProximal", "thumbDistal"],
            # INDEX #
            ["indexEF", "indexProximal"],
            ["indexProximal", "indexMedial"],
            ["indexMedial", "indexDistal"],
            # MIDDLE #
            ["middleEF", "middleProximal"],
            ["middleProximal", "middleMedial"],
            ["middleMedial", "middleDistal"],
            # RING #
            ["ringEF", "ringProximal"],
            ["ringProximal", "ringMedial"],
            ["ringMedial", "ringDistal"],
            # PINKY #
            ["pinkyEF", "pinkyProximal"],
            ["pinkyProximal", "pinkyMedial"],
            ["pinkyMedial", "pinkyDistal"],
            # FINGERS TO PALM
            ["palm", "thumbProximal"], 
            ["palm", "indexProximal"],
            ["palm", "middleProximal"],
            ["palm", "ringProximal"], 
            ["palm", "pinkyProximal"],
            # PALM TO WRIST
            ["palm", "wrist"],
            # WRIST TO ARM
            ["wrist", "handBaseRadius"],
            ["handBaseRadius", "armFrontRadius"],
            ["handBaseRadius", "armFrontUlna"],
            # ARM TO ELBOW
            ["armFrontRadius", "armBackLateral"],
            ["armFrontUlna", "armBackMedial"]
            ]

    for i in range(len(conn)):
        coords = get_connection(row, conn[i][0], conn[i][1])
        graph.plot(coords[0],coords[1],coords[2],color='b') # Adds line to plot

def update_plot(frame):

    if mode == 'line':
        points_ax.cla() # without this, lines continue to linger after their frame
        points_ax.set_title(f'{filename}, {times[frame]}\nframe={frame+1}/{num_frames}')
        plot_line_hand(frame, points_ax)
        set_limits(points_ax)
    elif mode == 'scatter':
        title.set_text(f'{filename}, {times[frame]}\nframe={frame+1}/{num_frames}')
        plot_scatter_hand(frame, points_ax_graph) # create scatter plot of hand points
        set_limits(points_ax)

    # Progress Report #
    global percent
    progress = (frame+1)/num_frames * 100

    if percent%10 == 0:
        print(f'{percent}%', end='')
        if percent==100:
            print('\nAnimation Complete!')
        percent+=1

    if progress > percent:
        print('.',end='')
        percent+=1

    sys.stdout.flush() # Printing errors occured without this.

# For those adding to this in the future, this should save you some trouble
# FuncAnimation(fig, func, frames, interval):
    # fig - just pass in this fig -> fig = plt.figure()
    # func - the update function, tells your plot what to change between each frame
        # - note: requires use of NumPy arrays
    # frames - can be a number or an iterable, whatever is the next value is the first argument of func()
    # interval - delay between frames in milliseconds

print('Creating Animation:')
percent = 0 # used in update_plot() progress report
ani = animation.FuncAnimation(fig, update_plot, num_frames, #frames controls how many frames in loop
                                   interval=35, blit=False) #interval controls the speed, smaller = faster

# Set up formatting for the movie files #
Writer = animation.writers['ffmpeg'] 
    # if you experience error: 
        # RuntimeError: Requested MovieWriter (ffmpeg) not available
    # run terminal command: $ brew install ffmpeg
    # warning: this is a big installation
writer = Writer(fps=15, metadata=dict(artist='ASL Research'), bitrate=1800)

ani.save(f'{filename[0:-4]}_{mode}.mp4', writer=writer)
print('Animation Saved')

plt.show()