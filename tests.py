import functions as fc


email = "gabrielepenalber@gmail.com"
email1 = "julio.@com.br"

print(fc.emailController(email))
print(fc.emailController(email1))
print(email1.find("."))

def testescrita():
    file = open('.\chives\users.txt', 'w')

    file.seek(0,0)
    print(file.read())
    file.close()


testescrita()