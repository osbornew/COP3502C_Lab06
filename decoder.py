# Adam Benali
def decoder(password):
    newpassword = ""
    for i in password:
        newpassword += str((int(i) - 3) % 10)
    return newpassword
