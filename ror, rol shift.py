array= [
  0x68, 0xCB, 0xB3, 0x60, 0xF2, 0xEB, 0xDD, 0x3E, # 8byte
  0x64, 0xC1                                      # 2byte
]

def rotate_right(num, shift):
  return (num>> shift) | (num<< (8- shift) & 0xFF)

def rotate_right1(num, shift):
  return (num>> shift)

def rotate_right2(num, shift):
  return (num<< (8- shift) & 0xFF)

def rotate_left(num, shift):
  return (num<< shift) & 0xFF | (num>> (8- shift))


# ascii, [68h, 65e, 6Cl, 6Cl, 6Fo]
ascii = [0x68, 0x65, 0x6C, 0x6C, 0x6F]

result_hex = ''
for i, a in enumerate(ascii):
  result_hex += '0x' + hex(rotate_left(ascii[i], i & 7) ^ i)[2:].upper() + ', '


print(f"ascii: {result_hex[:-2]}")



flag= ''
for i in range(0b1010):
  flag+= chr(rotate_right(array[i]^ i, i& 7))

print( flag, '\n' )

print(11000011,'// number >> 2')
print(bin(rotate_right1(0b11000011, 2))[2:].zfill(8)+ ' // (num>> shift)')
print(bin(rotate_right2(0b11000011, 2))[2:]+ ' // (num<< (8- shift) & 0xFF)')
print(bin(rotate_right(0b11000011, 2))[2:]+ ' // (num>> shift) | (num<< (8- shift) & 0xFF)')