def numberX(bus_stops):
	personas_adentro = 0
	for i in range(0,len(bus_stops)):
		stop = bus_stops[i]
		personas_adentro += (stop[0] - stop[1])
	return personas_adentro


def number(bus_stops):
	personas_adentro = 0
	for stop in bus_stops:
		personas_adentro += (stop[0] - stop[1])
	return personas_adentro


print(number([[10,0],[3,5],[5,9]]))
