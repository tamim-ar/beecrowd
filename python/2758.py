import struct

A, B = map(float, input().split())
C, D = map(float, input().split())

A = struct.unpack("f", struct.pack("f", A))[0]
B = struct.unpack("f", struct.pack("f", B))[0]

print("A = {:.6f}, B = {:.6f}".format(A, B))
print("C = {:.6f}, D = {:.6f}".format(C, D))
print("A = {:.1f}, B = {:.1f}".format(A, B))
print("C = {:.1f}, D = {:.1f}".format(C, D))
print("A = {:.2f}, B = {:.2f}".format(A, B))
print("C = {:.2f}, D = {:.2f}".format(C, D))
print("A = {:.3f}, B = {:.3f}".format(A, B))
print("C = {:.3f}, D = {:.3f}".format(C, D))
print("A = %.3E, B = %.3E" % (A, B))
print("C = %.3E, D = %.3E" % (C, D))
print("A = {:.0f}, B = {:.0f}".format(A, B))
print("C = {:.0f}, D = {:.0f}".format(C, D))
