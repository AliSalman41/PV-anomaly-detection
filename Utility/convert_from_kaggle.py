import os
import json
import sys
from pathlib import Path

dir = "C://Path//to//origin//jsonFiles//"    # original json file
WIDTH = 640
HEIGHT = 512

# get json file name 
json_list = os.listdir(dir)
for json_filename in json_list:

    # new file
    output_file = open(dir + Path(json_filename).stem + ".txt", "w")

    # read current json file
    f = open(dir + json_filename)
    data = json.load(f)

    # for each instance
    instances = data["instances"]
    for inst in instances:

        # get corner
        min_x = sys.maxsize
        max_x = -1 * sys.maxsize
        min_y = sys.maxsize
        max_y = -1 * sys.maxsize
        for corner in inst["corners"]:
            min_x = max(min(min_x, corner["x"]), 0)
            max_x = min(max(min_x, corner["x"]), WIDTH)
            min_y = max(min(min_y, corner["y"]), 0)
            max_y = min(max(min_y, corner["y"]), HEIGHT)
        width = (max_x - min_x) / WIDTH
        height = (max_y - min_y) / HEIGHT

        # get center
        x_center = inst["center"]["x"] / WIDTH
        y_center = inst["center"]["y"] / HEIGHT
        
        # assemble string
        str = "0 {} {} {} {}\n".format(x_center, y_center, width, height)
        output_file.write(str)
    
    output_file.close()
    f.close()