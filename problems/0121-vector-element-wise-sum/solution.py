import numpy
def vector_sum(a: list[int|float], b: list[int|float]) -> list[int|float]:
	if len(a) != len(b):
		return -1
	a, b = numpy.array(a), numpy.array(b)
	return a + b