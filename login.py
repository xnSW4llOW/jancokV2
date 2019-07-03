import os, sys

print ("Masukan Username dan Password !")
print ("Jangan Lupa Subscribe Channel SW4LL OW")
print (" Akan Ada Tools-Tools menarik")
print ("SELAMAT MENGGUNAKAN TOOLS INI SETELAH ANDA MENGETAHUI USERNAME  DAN PASSWORDNYA :v")
username = 'sw4llow'
password = 'jancokV2'

def restart():
	ngulang = sys.executable
	os.execl(ngulang, ngulang, *sys.argv)

def main():
	uname = raw_input("username : ")
	if uname == username:
		pwd = raw_input("password : ")

		if pwd == password:
			print "Hello Welcome To My Tools"
			print "Don't Copy My Project !",
			sys.exit()

		else:
			print "Password Salah!!!"
			print "Back Login"
			restart()

	else:
		print "Username Salah !!!"
		print "Back Login"
		restart()

try:
	main()
except KeyboardInterrupt:
	os.system('clear')
	restart()
