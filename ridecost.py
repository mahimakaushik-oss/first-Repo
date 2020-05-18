Python 3.8.2 (tags/v3.8.2:7b3ab59, Feb 25 2020, 22:45:29) [MSC v.1916 32 bit (Intel)] on win32
Type "help", "copyright", "credits" or "license()" for more information.
>>> def ridecost():
	dis_travel=float(input("enter distance travelled")) #enter travelled distance by vehicle in km
	cost=float(input("enter cost of diesel"))           #enter cost in rupee of fuel per litre
	fuel_avg=float(input("enter your fuel average"))    #enter fuel average of your vehicle in km/litre
	ridecost=(dis_travel/fuel_avg)*cost                 #calculation of ridecost in rupee
	print(ridecost,end="is the total cost of your travelling")

	
>>> ridecost()
enter distance travelled180
enter cost of diesel80
enter your fuel average18
800.0is the total cost of your travelling