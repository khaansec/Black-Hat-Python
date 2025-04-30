import sys


line_array = []
offset = 233
counter = 1
byte = ''
enc_shellcode = ''
buf_name = sys.argv[2]

def strip_hex(readfile): # this section far from optimal, but it breaks things down well visually
    strip_buf = readfile.replace("unsigned char buf[] =", "")
    strip_newline = strip_buf.replace("\n", "")
    strip_semi_colon = strip_newline.replace(";", "")
    strip_quotes = strip_semi_colon.replace('"',"")
    strip_backslash = strip_quotes.replace("\\", "")
    almost_stripped_hex = strip_backslash.replace("x", "")
    stripped_hex = almost_stripped_hex[1:]
    return stripped_hex

#strip_hex(sys.argv[1])

def enc_hex(stripped_hex): # takes the stripped text and performs the caesar cipher 
    counter = 1
    byte = ''
    enc_shellcode = ''

    for i in stripped_hex:
        if(counter % 2 == 0):
            byte += i
            byte = int(byte,16)
            byte = int(byte + offset)
            byte = int(byte % 256)
            byte = hex(byte)[2:]
            if(len(byte) == 1):
                byte = '0' + byte
            byte = "\\x" + byte
            enc_shellcode = enc_shellcode + byte
            byte = ''
        else:
            byte = byte + i
        counter += 1
    enc_shellcode = enc_shellcode
    return enc_shellcode

def format_text(string, every=60): # adds back the formatting that we stripped in strip_hex()
    lines = []
    print("adding named buffer: " + buf_name + " to file")
    lines.append("unsigned char " + buf_name + "[] = ")
    for i in range(0,len(string), every):
        lines.append("\"" + string[i:i+every] + "\"")
    return '\n'.join(lines)


def main():

    try:
        readfile = open(sys.argv[1], "r").read()
    except:
        print("file arg missing. %s <paload file> <buffer name>" %sys.argv[0])
        sys.exit()

# try/except not yet working for buffer name 
#    try:
#        buf_name = sys.argv[2]
#    except:
#        print("buffer name missing. %s <paload file> <buffer name>" %sys.argv[0])
#        sys.exit()

    print(readfile)

    stripped_hex = strip_hex(readfile)
    print("stripped hex values: " + '\n'  + stripped_hex) #for troubleshooting
    print('\n')

    encoded_hex = enc_hex(stripped_hex)
    print("encoded hex with offset " + str(offset) + '\n'  + encoded_hex) #for troubleshooting
    print('\n')

    formatted_text = format_text(encoded_hex)
    print("formatted text ready for cpp: " + '\n'  + formatted_text) #for troubleshooting

main()

# attempt at optimizing strip_hex()
#for line in readfile:
#    #print(line[1:-2])
#    line_array += line.replace("\\x", " ")
#    line_array += line.replace("\"", " ")
#    print(line_array[1:-1], sep= '\n')


