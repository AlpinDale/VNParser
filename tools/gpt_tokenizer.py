import argparse
import torch
from tqdm.auto import tqdm
from transformers import GPT2Tokenizer


def count_tokens(dataset_path, model_name_or_path):
    tokenizer = GPT2Tokenizer.from_pretrained(model_name_or_path)
    total_tokens = 0

    with open(dataset_path, 'r') as f:
        lines = sum(1 for line in f)
        f.seek(0)
        for line in tqdm(f, total=lines, desc='Counting tokens'):
            tokens = tokenizer(line.strip(), return_tensors='pt')['input_ids']
            total_tokens += tokens.shape[1]

    print(f'Total number of tokens in dataset: {total_tokens}')

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Count tokens in a TXT dataset using a GPT2 tokenizer.')
    parser.add_argument('--dataset', type=str, help='Path to TXT dataset')
    parser.add_argument('--model', type=str, default='gpt2', help='Name or path of GPT2 tokenizer model')
    args = parser.parse_args()

    count_tokens(args.dataset, args.model)
