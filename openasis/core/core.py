def take_query(raw_command):
    command = raw_command.lower().split()
    if command[0] == "hello":
        return "hi, how are you?"
