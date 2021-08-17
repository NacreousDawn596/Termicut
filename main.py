import os
start()
	print("what want you name the shortcut?")
	name = input("->")
	print("enter the commands (enter EOF to exit)")
	commands = []
	short()
	def short():
		global shortcut
		global command
		shortcut = input("->")
		if shortcut == "EOF":
			return
		else:
			commands.append(shortcut)
	print("shortcut's name: ", name)
	print("commands :", end='')
	for com in commands:
		print(com, end='\n')
	print("")
	print("is this right? y/n")
	confirme = input("")
	if confirme == "y":
		command = "echo 'function {name} {' >> ~/.local/share/NacreousDawn596/termicut/.shortcut.sh"
		for com in command:
			command = f"echo '{com}' >> ~/.local/share/NacreousDawn596/termicut/.shortcut.sh"
			os.system(command)
		os.system("echo '}' >> ~/.local/share/NacreousDawn596/termicut/.shortcut.sh")
	else:
		start()