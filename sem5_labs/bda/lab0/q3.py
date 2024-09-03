import heapq
from collections import Counter, namedtuple

class Node(namedtuple("Node", ["left", "right"])):
    def walk(self, code, acc):
        self.left.walk(code, acc + "0")
        self.right.walk(code, acc + "1")

class Leaf(namedtuple("Leaf", ["char", "freq"])):
    def walk(self, code, acc):
        code[self.char] = acc or "0"

def huffman_tree(frequencies):
    heap = [Leaf(char, freq) for char, freq in frequencies.items()]
    heapq.heapify(heap)
    while len(heap) > 1:
        lo = heapq.heappop(heap)
        hi = heapq.heappop(heap)
        new_node = Node(lo, hi)
        heapq.heappush(heap, (lo.freq + hi.freq, new_node))
    return heapq.heappop(heap)[1]

def huffman_code(s):
    frequencies = Counter(s)
    huff_tree = huffman_tree(frequencies)
    code = {}
    huff_tree.walk(code, "")
    return code

def encode(s, code):
    return ''.join(code[char] for char in s)

def decode(s, code):
    rev_code = {v: k for k, v in code.items()}
    i = 0
    decoded_string = ""
    while i < len(s):
        j = i + 1
        while s[i:j] not in rev_code:
            j += 1
        decoded_string += rev_code[s[i:j]]
        i = j
    return decoded_string

# Example usage
if __name__ == "__main__":
    s = "this is an example for huffman encoding"
    code = huffman_code(s)
    encoded = encode(s, code)
    decoded = decode(encoded, code)

    print(f"Original string: {s}")
    print(f"Encoded string: {encoded}")
    print(f"Decoded string: {decoded}")
    print(f"Huffman Code: {code}")
