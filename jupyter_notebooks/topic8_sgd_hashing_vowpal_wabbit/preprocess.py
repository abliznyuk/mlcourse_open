from sys import argv
from tqdm import tqdm

tags_index = {
    'javascript': 1,
    'java': 2,
    'python': 3,
    'ruby': 4,
    'php': 5,
    'c++': 6,
    'c#': 7,
    'go': 8,
    'scala': 9,
    'swift': 10
}

tags = set(tags_index.keys())


def process(in_file, out_file):
    with open(in_file, 'r') as i_f, open(out_file, 'w') as o_f:
        for line in tqdm(i_f):
            if line.count('\t') != 1:
                continue
            parts = line.strip().split('\t')
            if len(parts) != 2:
                continue
            tags_ = parts[1].split(' ')
            if len(tags.intersection(tags_)) != 1:
                continue
            tag = tags_index[list(tags.intersection(tags_))[0]]
            text = parts[0].replace('?', '').replace('|', '')
            o_f.write('{} |text {}\n'.format(tag, text))


if __name__ == '__main__':
    process(argv[1], argv[2])