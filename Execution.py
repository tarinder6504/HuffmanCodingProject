from huffman import HuffmanCoding
import zlib, base64
import os

def getSize(filename):
    st = os.stat(filename)
    return st.st_size
#input file path
path = "sample.txt"

h = HuffmanCoding(path)

print()

print("File is being encoded :-")

print()

output_path = h.compress()

import zlib, base64
filea = open('sample.txt','r')

text = filea.read()
filea.close()
code =  base64.b64encode(zlib.compress(text.encode('utf-8'),9))
code = code.decode('utf-8')
#print(code)
fileb=open('sample_compress.txt','w')
fileb.write(code)
fileb.close()

print("Success !!File has been encoded and compressed")
print()



print("-----------------------------------------------------------------------------")
#print(output_path)
print()

print("File is being decoded and decompressed:-")
print()
h.decompress(output_path)

print("Sucess !! File has been decoded and decompressed !!")

print()
print("------------------------------------------------------------------------------")

print()

print("Results:-")

print()
a= getSize('sample.txt')
print("Size of the sample file:- ",a, " bytes" )

b = getSize('sample_compress.txt')
print("Size of the compressed file:- " , b, " bytes")

print("Compression Ratio : ", b/a)
c= getSize('sample_decompressed.txt')
print("Size of the Decompressed File :-  ", a , " bytes")
if (a ==a):
	print ("Size and Contents of sample and decompressed files are same !!")
else:
	print("Size and Contents of sample and decompressed files are not same")
print()

print("Thank You !!" )