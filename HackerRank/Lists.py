def listOperation(arr):
    result = []
    for command in arr:
        command = command.split()
        if command[0] == 'insert':
            result.insert(int(command[1]), int(command[2]))
        elif command[0] == 'print':
            print(result)
        elif command[0] == 'remove':
            result.remove(int(command[1]))
        elif command[0] == 'append':
            result.append(int(command[1]))
        elif command[0] == 'sort':
            result.sort()
        elif command[0] == 'pop':
            result = result[:-1]
        elif command[0] == 'reverse':
            result.reverse()
    
    return result
