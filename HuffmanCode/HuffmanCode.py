import sys

def huffman_code_tree(nodes, label, result, prefix=''):
    children = nodes[label]
    tree = {}
    if len(children) == 2:
        tree['0'] = huffman_code_tree(nodes, children[0], result, prefix + '0')
        tree['1'] = huffman_code_tree(nodes, children[1], result, prefix + '1')
        return tree
    else:
        result[label] = prefix
        return label


def huffman_encoding(data):
    freq = {}
    for c in data:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1
    nodes = {}
    for n in freq.keys():  # leafs initialization
        nodes[n] = []

    while len(freq) > 1:  # binary tree creation
        s_vals = sorted(freq.items(), key=lambda x: x[1])
        a1 = s_vals[0][0]
        a2 = s_vals[1][0]
        freq[a1 + a2] = freq.pop(a1) + freq.pop(a2)
        nodes[a1 + a2] = [a1, a2]
    code = {}
    root = a1 + a2
    tree = {}
    tree = huffman_code_tree(nodes, root, code)
    encoded = ''.join([code[t] for t in data])
    return encoded, tree


def huffman_decoding(encoded, tree):
    decoded = []
    i = 0
    while i < len(encoded):
        ch = encoded[i]
        act = tree[ch]
        while not isinstance(act, str):
            i += 1
            ch = encoded[i]
            act = act[ch]
        decoded.append(act)
        i += 1
    decoded_text = ''.join(decoded)
    print('Decoded text:', decoded_text)
    return decoded_text


if __name__ == "__main__":
    codes = {}

    a_great_sentence = "THE BIRD IS THE WORD"

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    print("The content of the data is: {}\n".format(a_great_sentence))

    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))

    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    print("The content of the encoded data is: {}\n".format(decoded_data))