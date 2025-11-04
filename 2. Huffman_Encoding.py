import heapq
from collections import Counter
import itertools

def encode(text: str):
    
    if not text:
        return {}, ""
        
    if len(set(text)) == 1:
        char = text[0]
        return {char: '0'}, '0' * len(text)

    frequencies = Counter(text)
    
    count = itertools.count() 
    
    heap = []
    for char, freq in frequencies.items():
        heap.append([freq, next(count), char])
        
    heapq.heapify(heap)
    
    while len(heap) > 1:
        low1 = heapq.heappop(heap)
        low2 = heapq.heappop(heap)
        
        merged_freq = low1[0] + low2[0]
        merged_tree = [low1[2], low2[2]]
        
        heapq.heappush(heap, [merged_freq, next(count), merged_tree])
        
    huffman_tree = heap[0][2]
    
    codes = {}
    
    def generate_codes_recursive(tree, current_code=""):
        if isinstance(tree, str):
            codes[tree] = current_code
            return
            
        left, right = tree
        generate_codes_recursive(left, current_code + "0")
        generate_codes_recursive(right, current_code + "1")

    generate_codes_recursive(huffman_tree)
    
    encoded_text = "".join(codes[char] for char in text)
    
    return codes, encoded_text

string = input("Enter string to be encoded: ")

if string:
    huffman_codes, encoded_string = encode(string)
    
    print("\n--- Huffman Codes ---")
    print(' Char | Huffman code ')
    print('----------------------')
    for char, binary in sorted(huffman_codes.items()):
        print(" %-4r |%12s" % (char, binary))
        
    print("\n--- Encoded String ---")
    print(encoded_string)
else:
    print("Cannot encode an empty string.")