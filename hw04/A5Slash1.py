def stepX(x):
	newX0 = xor(xor(xor(x[13], x[16]), x[17]), x[18])
	for i in xrange(len(x)-1, 0, -1):
		x[i] = x[i-1]

	x[0] = newX0
	return x

def stepY(y):
	newY0 = xor(y[20], y[21])
	for i in xrange(len(y)-1, 0, -1):
		y[i] = y[i-1]

	y[0] = newY0
	return y

def stepZ(z):
	newZ0 = xor(xor(xor(z[7], z[20]), z[21]), z[22])
	for i in xrange(len(z)-1, 0, -1):
		z[i] = z[i-1]

	z[0] = newZ0
	return z

def xor(left, right):
	return int(left != right)

def maj(x, y, z):
	print 'Majority was:', 0 if (x + y + z) < 2 else 1
	return 0 if (x + y + z) < 2 else 1

def main():
	x = [1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1, 0, 1]
	y = [1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1, 0, 0, 1, 1]
	z = [1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0, 1, 1, 1, 1, 0, 0, 0, 0]

	keystream = []

	for i in xrange(32):
		m = maj(x[8], y[10], z[10])

		if x[8] == m:
			print 'Stepped x',
			x = stepX(x)
			print x
		if y[10] == m:
			print 'Stepped y',
			y = stepY(y)
			print y
		if z[10] == m:
			print 'Stepped z',
			z = stepZ(z)
			print z

		keystream.append(xor(xor(x[-1], y[-1]), z[-1]))

	print ''.join((str(x) for x in keystream))

if __name__ == '__main__':
	main()