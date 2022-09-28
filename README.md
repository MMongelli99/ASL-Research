Michael Mongelli
Dr. Salgian
American Sign Language Recognition
Apr 2020

hand_plotter.py Information

Overview:

    This program is capable of plotting a hand figure in 3D based on
    coordinates provided from a CSV file in the Mendely dataset of
    recorded American Sign Language gestures.
    
    <img width="383" alt="Screen Shot 2022-09-27 at 10 19 04 PM" src="https://user-images.githubusercontent.com/45768887/192672709-8547404b-64e0-4f9d-8738-5385f3447a44.png">

Command line args: 

    $ handfile.csv plot_mode

    handfile.csv = the file containing the coordinates you would like to plot
    
    plot_mode = * (optional, set to 'line' by default)
                * 'scatter' - plot the hand using a scatter plot, showing the joints as points 
                * 'line' - plot the connections between the joints as lines

    Examples: $ python3 hand_plotter.py Work_Right.csv scatter
              $ python3 hand_plotter.py Work_Right.csv line
              $ python3 hand_plotter.py Work_Right.csv
