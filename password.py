def encode(pw):
	

def decode(pw):
	# decoding goes here

def main():
	while True:
		print("Menu")
		print("-------------")
		print("1. Encode\n2. Decode\n3. Quit\n")
		ch = input("Please enter an option: ")
		if ch == "1":
			pw = input("Please enter your password to encode: ")
			encode(pw)
		elif ch == "2":
			decode():

		elif ch == "3":
			exit()

if __name__ == "__main__":
	main()
