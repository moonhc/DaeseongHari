import math
from time import sleep
sensors = []

GRID=500

class Sensor:
    def __init__(self, x, y, z, typ):
        self.x = x
        self.y = y
        self.z = z
        self.typ = typ
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
        self.graph[0][0][0].smoke = True

class Vertex:
    def __init__(self,x,y,z):
        self.x = x
        self.y = y
        self.z = z
        self.fire = False
        self.smoke = False
        self.fire_count = 2 #time required for fire to spread (seconds)
        self.smoke_count = 1 #time required for smoke to spread (seconds)
        self.adjacent_vertices = []
    def ignite(self):
        if not self.fire:
            self.fire = True
            #print "%d, %d: ignited" %(self.x, self.y)
    def push_smoke(self):
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
            vertex.push_smoke()

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

for x in range(len(floor2)):
    for y in range(len(floor2[x])):
        if x > 0:
            floor2[x][y].adjacent_vertices.append(floor2[x-1][y])
        if x < len(floor2) - 1:
            floor2[x][y].adjacent_vertices.append(floor2[x+1][y])
        if y > 0:
            floor2[x][y].adjacent_vertices.append(floor2[x][y-1])
        if y < len(floor2[x]) - 1:
            floor2[x][y].adjacent_vertices.append(floor2[x][y+1])

row_count = 0
#third floor
for x in range(0, 25600, GRID):
    floor3.append([])
    for y in range(0, 23300, GRID):
        floor3[row_count].append(Vertex(x,y, 2))
        third_count += 1
    row_count += 1

for x in range(len(floor3)):
    for y in range(len(floor3[x])):
        if x > 0:
            floor3[x][y].adjacent_vertices.append(floor3[x-1][y])
        if x < len(floor3) - 1:
            floor3[x][y].adjacent_vertices.append(floor3[x+1][y])
        if y > 0:
            floor3[x][y].adjacent_vertices.append(floor3[x][y-1])
        if y < len(floor3[x]) - 1:
            floor3[x][y].adjacent_vertices.append(floor3[x][y+1])
#fire travelling through staircase
for x in range(11000, 14500, GRID):
	for y in range(12000, 15500, GRID):
		floor1[x/GRID][y/GRID].adjacent_vertices.append(floor2[x/GRID][y/GRID])
		floor2[x/GRID][y/GRID].adjacent_vertices.append(floor1[x/GRID][y/GRID])
		floor2[x/GRID][y/GRID].adjacent_vertices.append(floor3[x/GRID][y/GRID])
		floor3[x/GRID][y/GRID].adjacent_vertices.append(floor2[x/GRID][y/GRID])

vertices.append(floor1)
vertices.append(floor2)
vertices.append(floor3)

#sensors = [Sensor(6400, 19200, 0, 1), Sensor(5100, 19200, 0, 0), Sensor(4200, 2000, 0, 0), Sensor(4500, 6300, 0, 0), Sensor(8800, 6300, 0, 0), Sensor(8800, 2900, 0, 0), Sensor(4400, 10000, 0, 0), Sensor(11000, 11000, 0, 0), Sensor(12050, 11000,0, 1), Sensor(20000, 11000, 0, 0), Sensor(20000, 19000, 0, 0), Sensor(27000, 11000, 0, 0), Sensor(27000, 19000, 0, 0), Sensor(23500,15500,0, 1), Sensor(4700, 6300, 1, 1), Sensor(9000, 6300, 1, 0), Sensor(4700, 16900, 1, 0), Sensor(9000, 16900, 1, 0), Sensor(4450, 1800, 1, 0)]

sensors = [[],[],[]]

floor1_sensors = "{t: 1, x: 6400, y: 19200},{t: 0, x: 5100, y: 19200},{t: 0, x: 4200, y: 2000},{t: 0, x: 4500, y: 6300},{t: 0, x: 8800, y: 6300},{t: 0, x: 8800, y: 2900},{t: 0, x: 4400, y: 10000},{t: 0, x: 11000, y: 11000},{t: 1, x: 12050, y: 11000},{t: 0, x: 20000, y: 11000},{t: 0, x: 20000, y: 19000},{t: 0, x: 27000, y: 11000},{t: 0, x: 27000, y: 19000},{t: 1, x: 23500, y: 15500}"

floor2_sensors = "{t: 0, x: 4700, y: 6300},{t: 0, x: 9000, y: 6300},{t: 0, x: 4700, y: 16900},{t: 0, x: 9000, y: 16900},{t: 0, x: 4450, y: 1800},{t: 0, x: 9500, y: 2900},{t: 0, x: 4700, y: 9900},{t: 0, x: 4700, y: 12900},{t: 0, x: 4700, y: 21000},{t: 0, x: 9200, y: 20000},{t: 0, x: 11800, y: 11000},{t: 1, x: 13000, y: 11000},{t: 0, x: 15500, y: 9000},{t: 0, x: 19400, y: 9000},{t: 0, x: 19400, y: 14000},{t: 0, x: 22500, y: 14000},{t: 0, x: 23000, y: 9000}"

floor3_sensors = "{t: 0, x: 4200, y: 6300},{t: 0, x: 8500, y: 6300},{t: 0, x: 4200, y: 16900},{t: 0, x: 8500, y: 16900},{t: 0, x: 4450, y: 1800},{t: 0, x: 9000, y: 2900},{t: 0, x: 4200, y: 9900},{t: 0, x: 4200, y: 12900},{t: 0, x: 4200, y: 21000},{t: 0, x: 8700, y: 20000},{t: 0, x: 10500, y: 11000},{t: 1, x: 11500, y: 11000},{t: 0, x: 14000, y: 9000},{t: 0, x: 17500, y: 9000},{t: 0, x: 17500, y: 14000},{t: 0, x: 20500, y: 14000},{t: 0, x: 21000, y: 9000}"

for sensor_data in floor1_sensors.split('},'):
	typ = int(sensor_data.split(':')[1].strip().split(',')[0].strip())
	x_pos = int(sensor_data.split(':')[2].strip().split(',')[0].strip())
	y_pos = int( sensor_data.split(':')[3].strip().split(',')[0].strip().strip('}'))
	z_pos = 0
	sensors[0].append(Sensor(x_pos, y_pos, z_pos, typ))

for sensor_data in floor2_sensors.split('},'):
	typ = int(sensor_data.split(':')[1].strip().split(',')[0].strip())
	x_pos = int(sensor_data.split(':')[2].strip().split(',')[0].strip())
	y_pos = int( sensor_data.split(':')[3].strip().split(',')[0].strip().strip('}'))
	z_pos = 1
	sensors[1].append(Sensor(x_pos, y_pos, z_pos, typ))

for sensor_data in floor3_sensors.split('},'):
	typ = int(sensor_data.split(':')[1].strip().split(',')[0].strip())
	x_pos = int(sensor_data.split(':')[2].strip().split(',')[0].strip())
	y_pos = int( sensor_data.split(':')[3].strip().split(',')[0].strip().strip('}'))
	z_pos = 2
	sensors[2].append(Sensor(x_pos, y_pos, z_pos, typ))

#for sensor in floor1_sensors:
#	print sensor

building = Building(vertices, sensors)

import sys
def start_simulation(building, fire_origin_x, fire_origin_y, fire_origin_z):
    building.ignite(fire_origin_x, fire_origin_y, fire_origin_z)
    tick = 0
    step = 1
    while True:
        for floor in building.graph:
            for row in floor:
                for vertex in row:
                    vertex.update()
        for sensors_by_floor in building.sensors:
            for sensor in sensors_by_floor:
                for row in building.graph[sensor.z]:
                    for vertex in row:
                        if sensor.typ == 0 and vertex.fire and math.sqrt((vertex.x - sensor.x)**2 + (vertex.y - sensor.y)**2) < GRID:
                        	sensor.update_status(1)
                        if sensor.typ == 1 and vertex.smoke and math.sqrt((vertex.x - sensor.x)**2 + (vertex.y - sensor.y)**2) < GRID:
						    sensor.update_status(1)
                if tick % step == 0:
                    print '%4d,' % sensor.status,
            if tick % step == 0:
                print ''
            tick += 1
        print ''
        sys.stdout.flush()
def main():
    start_simulation(building, 0, 0, 0)

main()
