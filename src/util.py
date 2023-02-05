import os

def increase_string_size_in_dataset(filepath, scaling_factor):
    with open(filepath, 'r') as f_orig:
        with open(f"../datasets/{scaling_factor}x_chars_" +
                f"{os.path.basename(filepath)}", 'a') as f_new:
            for line in f_orig:
                f_new.write(line.rstrip()*scaling_factor + "\n")

filepath = "../datasets/population_100000.txt"
scaling_factor = 100

increase_string_size_in_dataset(filepath, scaling_factor)