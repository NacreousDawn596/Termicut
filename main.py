import os
def start():
	print("what want you name the shortcut?")
	name = input("->")
	print("enter the commands (enter EOF to exit)")
	commands = []
	def short():
		global shortcut
		global command
		shortcut = input("->")
		if shortcut == "EOF":
			return
		else:
			commands.append(shortcut)
			short()
	short()
	print("shortcut's name: \n", name)
	print("commands :")
	for com in commands:
		print(com, end='\n')
	print("")
	print("is this right? y/n")
	confirme = input("")
	if confirme == "y":
		part = "() {' >> ~/.local/share/NacreousDawn596/Termicut/.shortcut.sh"
		command = f"echo 'function {name}{part}"
		os.system(command)
		for com in commands:
			command = f"echo '{com}' >> ~/.local/share/NacreousDawn596/Termicut/.shortcut.sh"
			os.system(command)
		os.system("echo '}' >> ~/.local/share/NacreousDawn596/Termicut/.shortcut.sh")
	else:
		start()
start()
