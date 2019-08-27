# 解决base64隐写问题
import binascii
import base64
import re


def compare(src):
    result = '0b'
    str_len = len(src)
    for i in range(0, str_len, 2):
        if src[i:i + 2] == b'3d' and src[i - 2:i] != b'3d':
            pattern = re.compile(r'(?<=0b)[01]*')  # 获取二进制位串
            if src[i + 2:i + 4] == b'3d':
                code_tmp = base64.b64decode(bytes.fromhex((src[i - 4:i] + b'413d').decode('ascii')).decode('ascii'))
                result += re.search(pattern, bin(code_tmp[1] >> 4)).group(0).zfill(4)  # 自动补0到4位
            else:
                code_tmp = base64.b64decode(bytes.fromhex((src[i - 6:i] + b'41').decode('ascii')).decode('ascii'))
                result += re.search(pattern, bin(code_tmp[2] >> 6)).group(0).zfill(2)
    return result


if __name__ == '__main__':
    path = input("Please input the source file path: ")
    try:
        with open(path, 'rb') as src:
            content = binascii.hexlify(src.read())  # 以16进制方式打开文件
            src.close()
    except FileNotFoundError:
        print("File Not Found")
        exit(1)
    result = compare(content)
    print(result)
