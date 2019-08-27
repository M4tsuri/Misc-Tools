import base64
import codecs
import sys


def base64_decode(code):
    try:
        return base64.b64decode(code)
    except base64.binascii.Error:
        print("Decoding Can Not Finish")


def rot13_decode(code):
    return codecs.encode(code, "rot13")


if __name__ == "__main__":
    para = sys.argv
    if len(para) != 3 and len(para) != 4:
        print("The args are wrong!")
        exit(1)
    if para[1] == 'f':
        active = True
        while active:
            active = False
            path = para[2]
            try:
                with open(path, mode='r') as file:
                    str_code = file.read()
                    file.close()
            except FileNotFoundError:
                print("File Not Found")
                active = True
    else:
        str_code = para[2]
    code_type = para[3]
    if code_type == 'base64':
        result = base64_decode(str_code)
    elif code_type == 'rot13':
        result = rot13_decode(str_code)
    else:
        result = "Type Not Exist"
    if result:
        print(result)
