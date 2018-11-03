from huffman import HuffmanCoding

#input file path
path = "sample.txt"

h = HuffmanCoding(path)

output_path = h.compress()
print(output_path)
h.decompress(output_path)
