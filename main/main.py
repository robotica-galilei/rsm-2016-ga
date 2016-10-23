import Pyro4
import sys

server = Pyro4.Proxy("PYRONAME:robot.server")    # use name server object lookup uri shortcut

if(len(sys.argv) < 4):
	print "4 arguments required"
	sys.exit()

server.setRobotPosition((int(sys.argv[1]), int(sys.argv[2])))
server.setRobotOrientation(int(sys.argv[3]))

