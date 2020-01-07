import sys

def huffman_code_tree(nodes, label, result, prefix=''):
    children = nodes[label]
    tree = {}
    if len(children) == 2:
        tree['0'] = huffman_code_tree(nodes, children[0], result, prefix + '0')
        tree['1'] = huffman_code_tree(nodes, children[1], result, prefix + '1')
        return tree
    elif len(nodes) > 1 and len(children) is not 0:
        tree['0'] = huffman_code_tree(nodes, children[0], result, prefix + '0')
        print("children[0] : ", children[0], "   result = ", result)
        return tree
    else:
        result[label] = prefix
        return label


def huffman_encoding(data):
    if not data:
        print("Please check your input")
        return "0", ""
    freq = {}
    for c in data:
        if c in freq:
            freq[c] += 1
        else:
            freq[c] = 1
    nodes = {}
    print("freq : ", freq)
    if len(freq) is 1:
        new_freq = {}
        counter = 1
        new_c = ''
        freq_length = 0
        for n in freq.keys():
            new_c = n
            freq_length = freq[n]
            new_freq[new_c] = 1
            nodes[new_c] = []
        while counter < freq_length:
            prev_c = new_c
            new_c += c
            print("c outer : ", new_c)
            counter += 1
            new_freq[new_c] = 1
            nodes[new_c] = [prev_c]
        print("new_freq : ", new_freq)
        print("new node : ", nodes)
        root = new_c
        code = {}
        tree = huffman_code_tree(nodes, root, code)
        print("tree", tree)
        encoded = ''.join([code[t] for t in data])
        return encoded, tree
    for n in freq.keys():  # leafs initialization
        nodes[n] = []
    print("nodes : ", nodes)

    while len(freq) > 1:  # tree creation
        s_vals = sorted(freq.items(), key=lambda x: x[1])
        print("s_vals : ", s_vals)
        a1 = s_vals[0][0]
        a2 = s_vals[1][0]
        freq[a1 + a2] = freq.pop(a1) + freq.pop(a2)
        nodes[a1 + a2] = [a1, a2]
    print("freq : ", freq)
    print("nodes : ", nodes)
    code = {}
    root = a1 + a2
    print("root : ", root)
    tree = {}
    tree = huffman_code_tree(nodes, root, code)
    print("tree : ", tree)
    print("code : ", code)
    encoded = ''.join([code[t] for t in data])
    return encoded, tree


def huffman_decoding(encoded, tree):
    if not encoded or not tree:
        return ""
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

    # TestCase 1:
    # a_great_sentence = "aaaaa"
    #
    # print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # # Expected : 54
    # print("The content of the data is: {}\n".format(a_great_sentence))
    # # Expected : aaaaaa
    # encoded_data, tree = huffman_encoding(a_great_sentence)
    #
    # print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # # Expected : 24
    # print("The content of the encoded data is: {}\n".format(encoded_data))
    # # Expected : 00000000000000000000
    # decoded_data = huffman_decoding(encoded_data, tree)
    #
    # print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # # Expected : 54
    # print("The content of the encoded data is: {}\n".format(decoded_data))
    # # Expected : aaaaaa

    #TestCase 2:

    # a_great_sentence = ""
    #
    # print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))
    # # Expected : 69
    # print("The content of the data is: {}\n".format(a_great_sentence))
    # # Expected : THE BIRD IS THE WORD
    # encoded_data, tree = huffman_encoding(a_great_sentence)
    # #Expected Output:
    # # Please check your input
    # print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    # # Expected : 49
    # print("The content of the encoded data is: {}\n".format(encoded_data))
    # # Expected :
    # decoded_data = huffman_decoding(encoded_data, tree)
    #
    # print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))
    # # Process finishes with exit code 1
    # print("The content of the encoded data is: {}\n".format(decoded_data))

    # TestCase 3:
    a_great_sentence = "A paragraph is a group of at least five sentences, a paragraph is half a page long, etc. In reality, though, the unity and coherence of ideas among sentences is what constitutes a paragraph."

    print("The size of the data is: {}\n".format(sys.getsizeof(a_great_sentence)))

    print("The content of the data is: {}\n".format(a_great_sentence))
    encoded_data, tree = huffman_encoding(a_great_sentence)

    print("The size of the encoded data is: {}\n".format(sys.getsizeof(int(encoded_data, base=2))))
    print("The content of the encoded data is: {}\n".format(encoded_data))
    decoded_data = huffman_decoding(encoded_data, tree)

    print("The size of the decoded data is: {}\n".format(sys.getsizeof(decoded_data)))

    print("The content of the encoded data is: {}\n".format(decoded_data))
    # Expected output:
    # The size of the data is: 239

    # The content of the data is: A paragraph is a group of at least five sentences, a paragraph is half a page long, etc. In reality, though, the unity and coherence of ideas among sentences is what constitutes a paragraph.

    # The size of the encoded data is: 132

    # The content of the encoded data is: 010100011110111011001101111000001101110111010011111001100011101111111000001111010101101101111111101011011011101110101111101110000111000101011111011011001010100100011110000001001101000010010101100010000010011101111110111011001101111000001101110111010011111001100011101000111101111101101110111111011101111000000111110111110101001110000010011100010100101110110011110101010100111100110000111101111100110100010100010011110100100110101011011100001000010011110100100000111101101100111001101000101011101110010010111110101111010010000000110001001010110001111101011011011111001001011000011100011101101010111101010011100011110000001001101000010010101100010001111100110001111011000010001110101110101111010100110001010110011010101101101000010001110111111011101100110111100000110111011101001011001

    # Decoded text: A paragraph is a group of at least five sentences, a paragraph is half a page long, etc. In reality, though, the unity and coherence of ideas among sentences is what constitutes a paragraph.
    # The size of the decoded data is: 239

    # The content of the encoded data is: A paragraph is a group of at least five sentences, a paragraph is half a page long, etc. In reality, though, the unity and coherence of ideas among sentences is what constitutes a paragraph.

