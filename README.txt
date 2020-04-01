Michael Mongelli
Dr. Salgian
American Sign Language Recognition
Apr 1 2020

* * hand_plotter.py Information * *

Overview:

    This program is capable of plotting a hand figure in 3D based on
    coordinates provided from a CSV file in the Mendely dataset of
    recorded American Sign Language gestures.

Command line args: handfile.csv plot_mode

    handfile.csv = the file containing the coordinates you would like to plot
    
    plot_mode = * (optional, set to 'line' by default)
                * 'scatter' - plot the hand using a scatter plot, showing the joints as points 
                * 'line' - plot the connections between the joints as lines

    Examples: $ python3 hand_plotter.py Work_Right.csv scatter
              $ python3 hand_plotter.py Work_Right.csv line
              $ python3 hand_plotter.py Work_Right.csv

Notes:
    
    In update_plot():
        Notice that the title is set using a different technique for the scatter and line plots.
        Scatter and line plots behave differently in MatPlotLib.
        This is also why the ax.cla() (clear axes) function is present in the line plot
        but not in the scatter plot.
        Further research is needed to find if their is a way to implement
        the plotting of these graphs in as similar a manner as possible.

    placement of plt.show():
        Unfortunately, this has to come last.
        While it is suboptimal for the user to have to wait
        for the animation to render for saving before they
        can view it in a popup window,
        doing so corrupts the animation-saving process. 
        There may be a solution to this,
        but this can be solved in the future. 

Future Work:

    * Be able to pass multiple csv files to the program to make creating
      multiple animations at once less tedious
        * It would be good to add more detail to the progress report
          in this case
        * The process of creating and saving the animaiton is currently
          very slow, so a status report indicates if the animation is
          10%...20%...etc until completion
        * If the program is made able to convert multiple files to
          animations at once, it would be good to show the user approximately
          when the animations will be done rendering so they know how long
          they will need to leave their terminal running

    * Make it possible to enable/disable the plot being shown
        * If one simply wants to save several animations created from
          their CSVs, they shouldn't have to see it all pop up in
          multiple plot windows

    * Improve speed:
        * Line mode is currently very slow, could be sped up by saving
          all plot data so it doesnt have to be recalculated with each loop
          of the animation
        * There could be ways to speed up the process of the first loop as well

    * Be able to plot points and lines at the same time
        * Will greatly improve the viewer's ability to interpret the signs
          being performed by the hand