
# ASL - Research [![Badge License]][License]

*American Sign Language Recognition*

<br>

```
Michael Mongelli
Dr. Salgian
American Sign Language Recognition
Apr 1 2020
```

<br>

## Overview

This program is capable of plotting a **3D Hand Figure** <br>
based on coordinates provided by a **CSV** file.

The CSV comes from the **Mendely Dataset** of <br>
recorded **American Sign Language** gestures.

<br>

---

<br>

## Requirements

To run the program, you require:

- **[Python 3]**

- Some modules:

  - `pandas`
  - `numpy`
  - `matplotlib`

  <br>

  Install them with:

  ```sh
  pip install pandas numpy matplotlib
  ```

<br>

---

<br>

## Usage

*The program is used in the command line.*

```sh
Plot.py <CSV File> <Mode>
```

<br>

### Mode

#### Line

*This is the default used if no mode is specified.*

Plot the connections between the joints as lines.

```sh
Plot.py <CSV File> line
```

<br>

#### Scatter

Plot the hand using a scatter plot, <br>
showing the joints as points.

```sh
Plot.py <CSV File> scatter
```

<br>

---

<br>

## Notes

### update_plot()

Notice that the title is set using a different <br>
technique for the scatter and line plots.

Scatter and line plots behave differently in **MatPlotLib**.


This is also why the `ax.cla()` (clear axes) function <br>
is present in the line plot but not in the scatter plot.

Further research is needed to find if their is a way to <br>
implement the plotting of these graphs in as similar <br>
a manner as possible.

<br>

### placement of plt.show()

Unfortunately, this has to come last.

While it is suboptimal for the user to have to wait <br>
for the animation to render for saving before they <br>
can view it in a popup window, doing so corrupts <br>
the animation-saving process.

There may be a solution to this, but <br>
this can be solved in the future. 

<br>

---

<br>

## Future Work

- Be able to pass multiple csv files to the program to <br>
  make creating multiple animations at once less tedious

    * It would be good to add more detail <br>
      to the progress report in this case

    * The process of creating and saving the animation <br>
      is currently very slow, so a status report indicates <br>
      if the animation is `10%` ... `20%` ... etc until completion

    * If the program is made able to convert multiple files <br>
      to animations at once, it would be good to show the <br>
      user approximately when the animations will be done <br>
      rendering so they know how long they will need to <br>
      leave their terminal running

- Make it possible to enable / disable the plot being shown

    * If one simply wants to save several animations created <br>
      from their CSVs, they shouldn't have to see it all pop up <br>
      in multiple plot window

- Improve speed

    * Line mode is currently very slow, could be sped up by <br>
      saving all plot data so it doesn't have to be recalculated <br>
      with each loop of the animation

    * There could be ways to speed up <br>
      the process of the first loop as well

- Be able to plot points and lines at the same time

    * Will greatly improve the viewer's ability to <br>
      interpret the signs being performed by hand

<!----------------------------------------------------------------------------->

[Python 3]: https://www.python.org/downloads/

[Badge License]: https://img.shields.io/badge/License-Unkown-darkgray?style=for-the-badge

[License]: #
