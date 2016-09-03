import math
from time import sleep
sensors = []

GRID=500

class Sensor:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.status = 0
    def update_status(self, new_stat):
        self.status += new_stat

class Building:
    def __init__(self, graph, sensors):
        self.fire_origin = (-1, -1, -1)
        self.graph = graph
        self.sensors = sensors
    def ignite(self, x, y, z):
        self.fire_origin = (x, y, z)
        self.graph[0][0][0].fire = True

class Vertex:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        self.fire = False
        self.smoke = False
        self.fire_count = 2 #time required for fire to spread (seconds)
        self.smoke_count = 3 #time required for smoke to spread (seconds)
        self.adjacent_vertices = []
    def ignite(self):
        if not self.fire:
            self.fire = True
            #print "%d, %d: ignited" %(self.x, self.y)
    def smoke(self):
        if not self.smoke:
            self.smoke = True
    def update(self):
        if self.fire:
            if self.fire_count <= 0:
                self.spread_fire()
            else:
                self.fire_count -= 1
        if self.smoke:
            if self.smoke_count <= 0:
                self.spread_smoke()
            else:
                self.smoke_count -= 1
    def spread_fire(self):
        for vertex in self.adjacent_vertices:
            vertex.ignite()
    def spread_smoke(self):
        for vertex in self.adjacent_vertices:
            vertex.smoke()

vertices = []
floor1 = []
floor2 = []
floor3 = []
first_count = 0
second_count = 0
third_count = 0
#first floor
row_count = 0
for x in range(0, 33600, GRID):
    floor1.append([])
    for y in range(0, 24400, GRID):
        floor1[row_count].append(Vertex(x,y, 0))
        first_count += 1
    row_count += 1



for x in range(len(floor1)):
    for y in range(len(floor1[x])):
        if x > 0:
            floor1[x][y].adjacent_vertices.append(floor1[x-1][y])
        if x < len(floor1) - 1:
            floor1[x][y].adjacent_vertices.append(floor1[x+1][y])
        if y > 0:
            floor1[x][y].adjacent_vertices.append(floor1[x][y-1])
        if y < len(floor1[x]) - 1:
            floor1[x][y].adjacent_vertices.append(floor1[x][y+1])

row_count = 0
#second floor
for x in range(0, 25600, GRID):
    floor2.append([])
    for y in range(0, 23300, GRID):
        floor2[row_count].append(Vertex(x,y, 1))
        second_count += 1
    row_count += 1

row_count = 0
#third floor
for x in range(0, 25600, GRID):
    floor3.append([])
    for y in range(0, 23300, GRID):
        floor3[row_count].append(Vertex(x,y, 2))
        third_count += 1
    row_count += 1


vertices.append(floor1)
vertices.append(floor2)
vertices.append(floor3)

sensors = [Sensor(6400, 19200, 0), Sensor(5100, 19200, 0), Sensor(4200, 2000, 0), Sensor(4500, 6300, 0), Sensor(8800, 6300, 0), Sensor(8800, 2900, 0), Sensor(4400, 10000, 0), Sensor(11000, 11000, 0), Sensor(12050, 11000,0), Sensor(20000, 11000, 0), Sensor(20000, 19000, 0), Sensor(27000, 11000, 0), Sensor(27000, 19000, 0), Sensor(400,100,0)]

building = Building(vertices, sensors)

def start_simulation(building, fire_origin_x, fire_origin_y, fire_origin_z):
    building.ignite(fire_origin_x, fire_origin_y, fire_origin_z)
    tick = 0
    step = 1
    while True:
        for floor in building.graph:
            for row in floor:
                for vertex in row:
                    vertex.update()
        for sensor in building.sensors:
            for row in building.graph[sensor.z]:
                for vertex in row:
                    if vertex.fire and math.sqrt((vertex.x - sensor.x)**2 + (vertex.y - sensor.y)**2) < GRID:
                        sensor.update_status(1)
            if tick % step == 0:
                print '%4d,' % sensor.status,
        if tick % step == 0:
            print ''
        tick += 1
        #for i in range(10):
        #	if building.graph[0][i].fire:
        #		print 1,
        #	else:
        #		print 0,

def main():
    start_simulation(building, 0, 0, 0)

main()
