import os

def increase_string_size_in_dataset(filepath: str, scaling_factor: int) -> None:
    """Creates a new file with an identical number of entries as the input file,
    but with increased string length determined by "scaling_factor". If a given
    entry has length n, the entry in the new file has length n*scaling_factor
    Example with scaling_factor 3:
    
    OLD      NEW
    ------------
    Line -> LineLineLine
    Elin -> ElinElinElin
    
    The intention is to test how the implementations perform with longer strings

    Args:
        filepath (str): File path of the original file
        scaling_factor (int): Length of all entries is scaled by this factor
    """
    with open(filepath, 'r') as f_orig:
        with open(f"../datasets/{scaling_factor}x_chars_" +
                f"{os.path.basename(filepath)}", 'a') as f_new:
            for line in f_orig:
                f_new.write(line.rstrip()*scaling_factor + "\n")

filepath = "../datasets/population.txt"
scaling_factor = 100000

increase_string_size_in_dataset(filepath, scaling_factor)