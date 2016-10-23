import Pyro4

#Global variables
x_pos=0
y_pos=0
orientation=0

@Pyro4.expose
class server(object):
	def ping(self):
		return "Pong"

	def getRobotPosition(self):
		return (x_pos, y_pos)

	def setRobotPosition(self, coords):
		global x_pos
		global y_pos
		if len(coords) < 2:
			print coords
			return -1
		else:
			x_pos, y_pos = coords

	def getRobotOrientation(self):
		return orientation

	def setRobotOrientation(self, orient):
		global orientation
		orientation=orient

daemon = Pyro4.Daemon()                # make a Pyro daemon
ns = Pyro4.locateNS()                  # find the name server
uri = daemon.register(server)   # register the greeting maker as a Pyro object
ns.register("robot.server", uri)   # register the object with a name in the name server

print("Server ready.")
daemon.requestLoop() 
