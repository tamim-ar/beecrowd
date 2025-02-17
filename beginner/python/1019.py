N = int(input())

hours = N / 3600
minutes = N % 3600 / 60
seconds = N % 60

print(f"{int(hours)}:{int(minutes)}:{seconds}")
