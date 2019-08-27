import sys
import binascii
import codecs


def removefade(para1):
	# 读取原zip文件
	with open(para1, 'rb')as zipfile:
		zipfile_content = binascii.hexlify(zipfile.read())
		zipfile.close()

	zf_len = len(zipfile_content)

	for i in range(0, zf_len, 8):
		comp_con = zipfile_content[i:i+8]
		if comp_con == b'504b0102':
			zipfile_content = zipfile_content[:i + 17] + b'0' + zipfile_content[i + 18:]
		if comp_con == b'504b0304':
			zipfile_content = zipfile_content[:i + 13] + b'0' + zipfile_content[i + 14:]

	with open(para1[:-4] + '_repair.zip', 'wb') as newzip:
		newzip.write(codecs.decode(zipfile_content, 'hex'))
		newzip.close()
	print('The Reparation has Done')


if __name__ == '__main__':
	if len(sys.argv) != 2:
		print('usage example:')
		print(' python remove_deflags.py flag.zip')
	else:
		print("ATTENTION: MAC OS CAN DIRECTLY UNCOMPRESS FAKE ENCODED ZIP FILE!")
		para = sys.argv
		removefade(para[1])

