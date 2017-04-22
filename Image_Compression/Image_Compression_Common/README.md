# Compression
### @DataByteNITT

This is a basic implementation of LWZ and Huffman Compression Algorithms to compress an image.

Both LWZ and Huffman algorithms are completely lossless.

## LWZ compression

The algo starts with a dictionary of all possible characters. At each step, it finds the largest substring not available in the dictionary, and adds it to the dictionary and appends it to the encoded list at the same time.

The decompression involves regeneration of the entire dictionary while moving through the encoded list. This is done by considering a number in the encoded list, and creating the smallest possible string not available in the dictionary, and adding it to the dictionary.

## Huffman compression

The algo generates a [prefix code](https://en.wikipedia.org/wiki/Prefix_code) for each character in the string, based on a frequency analysis, assigning a shorter bitstring to a more frequent character. It uses a [prefix tree](https://en.wikipedia.org/wiki/Trie), where each leaf node represents the character and each edge the symbol that needs to be added to the bit string, while moving down from the root, to get the code for a particular character.

The decompression simply uses the prefix tree to find the character for a particular code.

## LWZ vs. Huffman
1. Huffman decoding needs the encoding key (i.e. the prefix tree), to be sent alongwith the encoded text, LWZ doesn't.
2. Huffman coding consumes lesser auxillary space on the server as compared to LWZ. (Prefix tree is smaller than the character dictionary)
3. In case of images, LWZ provides better compression ratio, whereas Huffman provides a better compression time.

Both the codes "huffman.py" and "lwz.py" compress the picture named "download.jpg".
And then deompress it and store it in a new file named "new_img.jpg".

**Note: The "download.jpg" file should be in the same directory as of the file "lwz.py" or "huffman.py" and the "new_img.jpg" file will also be saved in the same directory.**

Both of these implementations convert the image into a base64 string and then apply the compression algorithm.

LWZ gave a compression ratio of 0.639
Huffman gave a compression ratio of 0.751
