while True:
    try:
        n = int(input())
        print(hex(n)[2:].upper())
    except EOFError:
        break
