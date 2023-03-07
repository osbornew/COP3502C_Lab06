# Author: William Osborne
# Partner: Adam Benali

def decode(pw):
	exit()
	# decoding goes here

def encode(pw):
	out = ""
	for c in pw:
		out += chr((ord(c) % 0x30 + 3) % 10 + 0x30)
	return out

def main():
	while True:
		print("Menu")
		print("-------------")
		print("1. Encode\n2. Decode\n3. Quit\n")
		ch = input("Please enter an option: ")
		if ch == "1":
			pw = input("Please enter your password to encode: ")
			pw = encode(pw)
			print("Your password has been encoded and stored!\n")
		elif ch == "2":
			decode()

		elif ch == "3":
			exit()

if __name__ == "__main__":
	main()
