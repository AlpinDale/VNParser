import random
import argparse

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Split data into training and validation sets.")
    parser.add_argument("--input", type=str, help="Input file to split.")
    parser.add_argument("--break_data", type=str, help="Percentage of data to use for training and validation sets in the format 'train_pct,val_pct'")
    args = parser.parse_args()

    # Parse the percentages
    try:
        train_pct, val_pct = [float(x) for x in args.break_data.split(",")]
    except ValueError:
        print("Invalid break_data format. Please use 'train_pct,val_pct'")
        exit()

    # Check that the percentages add up to 1
    if train_pct + val_pct != 1:
        print("Invalid percentages. train_pct + val_pct must equal 1.")
        exit()

    with open(args.input, 'rb') as fin, open("train.json", 'wb') as f80out, open("val.json", 'wb') as f20out:
        for line in fin:
            r = random.random()
            if r < train_pct:
                f80out.write(line)
            else:
                f20out.write(line)
