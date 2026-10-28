import math

def normal_pdf(x, mean, std_dev):
	pdf = lambda x: 1/(std_dev * ((2*math.pi)**(1/2))) * math.exp(-((x-mean)**2)/(2*std_dev**2))
	return pdf(x)