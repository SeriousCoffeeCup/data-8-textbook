"""
There was a formatting error from when the files were initially downloaded.
This fixes it.
"""


"""
Example of Error:


Does not Render:

## The Histogram: General Principles and Calculation - \mbox instead of \text

Histograms follow the area principle and have two defining properties:

1. The bins are drawn to scale and are contiguous (though some might be empty), because the values on the horizontal axis are numerical and therefore have fixed positions on the number line.
2. The **area** of each bar is proportional to the number of entries in the bin. 

Property 2 is the key to drawing a histogram, and is usually achieved as follows:

$$
\mbox{area of bar} ~=~ \mbox{percent of entries in bin}
$$

Since areas represent percents, heights represent something other than percents. The numerical calculation of the heights just uses the fact that the bar is a rectangle:

$$
\mbox{area of bar} = \mbox{height of bar} \times \mbox{width of bin}
$$

and so

$$
\mbox{height of bar} ~=~ 
\frac{\mbox{area of bar}}{\mbox{width of bin}} ~=~
\frac{\mbox{percent of entries in bin}}{\mbox{width of bin}}
$$

The units of height are "percent per unit on the horizontal axis." The height is the percent in the bin relative to the width of the bin. So it is called *density* or *crowdedness*.

When drawn using this method, the histogram is said to be drawn on the *density scale*. On this scale:
- The area of each bar is equal to the percent of data values that are in the corresponding bin.
- The total area of all the bars in the histogram is 100%. In terms of proportions, we can say that the areas of all the bars in a histogram "sum to 1".











Renders:
## The Histogram: General Principles and Calculation

Histograms follow the area principle and have two defining properties:

1. The bins are drawn to scale and are contiguous (though some might be empty), because the values on the horizontal axis are numerical and therefore have fixed positions on the number line.
2. The **area** of each bar is proportional to the number of entries in the bin. 

Property 2 is the key to drawing a histogram, and is usually achieved as follows:

$$
\text{area of bar} ~=~ \text{percent of entries in bin}
$$

Since areas represent percents, heights represent something other than percents. The numerical calculation of the heights just uses the fact that the bar is a rectangle:

$$
\text{area of bar} = \text{height of bar} \times \text{width of bin}
$$

and so

$$
\text{height of bar} ~=~ 
\frac{\text{area of bar}}{\text{width of bin}} ~=~
\frac{\text{percent of entries in bin}}{\text{width of bin}}
$$

The units of height are "percent per unit on the horizontal axis." The height is the percent in the bin relative to the width of the bin. So it is called *density* or *crowdedness*.

When drawn using this method, the histogram is said to be drawn on the *density scale*. On this scale:
- The area of each bar is equal to the percent of data values that are in the corresponding bin.
- The total area of all the bars in the histogram is 100%. In terms of proportions, we can say that the areas of all the bars in a histogram "sum to 1".

"""
import os
import re

def update_path_data(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        content = file.read()

    # Regex to find the path_data variable declaration with various paths, quote styles, and including partial paths
    path_data_regex = r"\\mbox"

    new_content = re.sub(path_data_regex, "\\text", content)

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(new_content)

def update_files_in_directory(directory):
    current_code_file = os.path.abspath(__file__)
    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        # Check for .py or .ipynb extension, avoid modifying current file
        if (file_path.endswith('.py') or file_path.endswith('.ipynb')) and file_path != current_code_file:
            update_path_data(file_path)
            print(f"Updated {filename}")

def main():
    # . means Current directory. .. would mean previous directory
    directory_to_scan = '.'  
    update_files_in_directory(directory_to_scan)

if __name__ == "__main__":
    main()

