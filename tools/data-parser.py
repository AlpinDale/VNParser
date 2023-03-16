import argparse
import glob
import json


def create_jsonl_file(input_dir, output_dir):
    # Initialize an empty list to store the dictionaries
    data = []

    # Get a list of all the .txt files in the input directory
    txt_files = glob.glob(f"{input_dir}/*.txt")

    # Loop through each file and extract the data
    for txt_file in txt_files:
        # Open the file and read the lines
        with open(txt_file, "r") as f:
            lines = f.readlines()

        # Extract the conversation lines by removing the *Action* lines
        conversation = []
        for line in lines:
            if "*Action*" not in line:
                conversation.append(line.strip())

        # Combine the conversation lines into a single string
        conversation_str = "\n".join(conversation)

        # Create a dictionary with the conversation string as the input and an empty output and a reward of 1.0
        data_dict = {"input": conversation_str, "output": "", "reward": 1.0}

        # Add the dictionary to the data list
        data.append(data_dict)

    # Write the data list to a jsonl file
    with open(f"{output_dir}/output.jsonl", "w") as f:
        for data_dict in data:
            # Remove any lines that start with the = sign in the output
            output_lines = data_dict["output"].split("\n")
            output_lines = [line for line in output_lines if not line.startswith("=")]
            output_str = "\n".join(output_lines)

            # Update the data dictionary with the cleaned output
            data_dict["output"] = output_str

            # Write the updated dictionary to the file
            json.dump(data_dict, f)
            f.write("\n")


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Organize training data for Pyg-style chat models.")
    parser.add_argument("--input", type=str, help="Input directory containing .txt files.")
    parser.add_argument("--output", type=str, help="Output directory to write output.jsonl file to.")
    args = parser.parse_args()

    create_jsonl_file(args.input, args.output)
