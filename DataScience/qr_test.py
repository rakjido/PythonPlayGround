# coding: utf-8

import qrcode

def main():
	url = "https://www.naver.com/"
	if not url:
		print('No input URL found.')
		return
	print(url)
	img = qrcode.make(url)
	img.save('url.png')
	
if __name__ == '__main__':
	main()