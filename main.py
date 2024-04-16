import random
from math import *
import pygame
from vehicles import Car, Truck, SUV

# Create a surface to draw the car with a transparent background
VEHICLE_SURFACE = pygame.Surface((1400, 900), pygame.SRCALPHA)  # Set flag SRCALPHA to enable per-pixel alpha
VEHICLE_SURFACE.fill((255, 255, 255, 255))  # Fill with transparent background color

# Initialize Pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 1440, 960

# Initialize the screen
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Vehicle Models")
font = pygame.font.Font('freesansbold.ttf', 20)


# 1. The Button class
class Button:
    def __init__(self, name, x, y):
        self._name = name
        self._width = 150
        self._height = 50
        self._rect = pygame.rect.Rect(x, y, self._width, self._height)
        self._enabled = True

    def draw(self):
        pygame.draw.rect(screen, 'black', self._rect, 2)
        text = font.render(self._name, True, 'black')
        screen.blit(text, (self._rect.centerx - text.get_width() // 2, self._rect.centery - text.get_height() // 2))

    def is_clicked(self, mouse_pos):
        return self._rect.collidepoint(mouse_pos)

    def get_name(self):
        return self._name


# 2. The Display Class
class Display:
    def __init__(self):
        self._color = 'black'
        self.petals_color = [(generateRandomLength(0, 255), generateRandomLength(0, 255),
                              generateRandomLength(0, 255)) for _ in range(10)]
        self._scaled_surface = None
        self._x = WIDTH * 1 / 6
        self._y = HEIGHT * 1 / 3
        self.vehicle_color = (
            generateRandomLength(0, 255), generateRandomLength(0, 255), generateRandomLength(0, 255), 255)

    # Show vehicle details
    def show(self):
        if len(data) == 0:
            car()
        counter = 0
        type = font.render(str(self.type), True, self._color)
        type_rect = pygame.Rect(WIDTH * 1 / 15, HEIGHT * 1 / 9, 300, 50)
        for key in self.data:
            text = font.render(
                str(key) + str(" : ") + str(self.data[key]), True,
                self._color)

            text_rect = pygame.Rect(WIDTH * 1 / 12, HEIGHT * 1 / 7 + counter, 300, 50)

            screen.blit(text, text_rect)
            counter += 30
        screen.blit(type, type_rect)

    # Scale the vehicle
    def scale(self):
        # Generate a random scaling factor
        length = generateRandomLength(0.5,1.3)


        # Scale the car surface
        scaled_surface = pygame.transform.scale(VEHICLE_SURFACE, (int(VEHICLE_SURFACE.get_width() * length),
                                                                  int(VEHICLE_SURFACE.get_height() * length)))

        self._scaled_surface = scaled_surface

    # Draw the vehicle
    def draw(self):
        step = 0
        self.resetSurface()
        if self.type == "Car":
            self.__drawCar()
            for i in range(7):
                self.__drawFlower(screen, 100 + step, 850, self.petals_color[i])
                step += 200
        elif self.type == "Truck":
            self.__drawTruck()
            for i in range(6):
                self.__drawFlower(screen, 100 + step, 850, self.petals_color[i])
                step += 200
        elif self.type == "SUV":
            self.__drawSUV()
            for i in range(8):
                self.__drawFlower(screen, 100 + step, 850, self.petals_color[i])
                step += 175

    def resetSurface(self):
        global VEHICLE_SURFACE
        VEHICLE_SURFACE = pygame.Surface((1400, 960), pygame.SRCALPHA)  # Set flag SRCALPHA to enable per-pixel alpha
        VEHICLE_SURFACE.fill((0, 0, 0, 0))  # Fill with transparent background color
        screen.blit(VEHICLE_SURFACE, (0, 0))

    def __drawCar(self):
        # Car Body
        pygame.draw.polygon(VEHICLE_SURFACE, self.vehicle_color,
                            [[100, 250], [350, 250], [450, 150], [850, 150], [950, 250], [1100, 250], [1100, 400],
                             [100, 400]])
        # Windows
        pygame.draw.polygon(VEHICLE_SURFACE, (255, 255, 255, 255),
                            [[370, 250], [460, 160], [640, 160], [640, 250]])

        pygame.draw.polygon(VEHICLE_SURFACE, (255, 255, 255, 255),
                            [[680, 250], [680, 160], [830, 160], [930, 250]])

        # Doors
        pygame.draw.line(VEHICLE_SURFACE, (255, 255, 255, 255), (350, 250), (350, 400), 1)
        pygame.draw.line(VEHICLE_SURFACE, (255, 255, 255, 255), (660, 150), (660, 400), 1)
        pygame.draw.line(VEHICLE_SURFACE, (255, 255, 255, 255), (950, 250), (950, 400), 1)

        pygame.draw.line(VEHICLE_SURFACE, (255, 255, 255, 255), (610, 270), (640, 270),
                         3)
        pygame.draw.line(VEHICLE_SURFACE, (255, 255, 255, 255), (910, 270), (940, 270),
                         3)

        # Seats
        pygame.draw.rect(VEHICLE_SURFACE, (128, 0, 128, 255), (530, 200, 100, 50))
        pygame.draw.rect(VEHICLE_SURFACE, (128, 0, 128, 255), (750, 200, 100, 50))

        # Driver
        pygame.draw.circle(VEHICLE_SURFACE, (255, 255, 0, 255), (580, 180), 20)

        # Wheels
        pygame.draw.circle(VEHICLE_SURFACE, (0, 0, 0, 255), (350, 400), 60)
        pygame.draw.circle(VEHICLE_SURFACE, (0, 0, 0, 255), (950, 400), 60)

        screen.blit(self._scaled_surface if self._scaled_surface else VEHICLE_SURFACE, (self._x, self._y))

    def __drawTruck(self):
        # Truck Body
        pygame.draw.polygon(VEHICLE_SURFACE, self.vehicle_color,
                            [[20, 150], [40, 130], [300, 130], [300, 30], [1100, 30], [1100, 400], [20, 400]])
        # Windows
        pygame.draw.polygon(VEHICLE_SURFACE, (255, 255, 255, 255),
                            [[60, 250], [80, 150], [250, 150], [250, 250]])

        # Doors
        pygame.draw.line(VEHICLE_SURFACE, (255, 255, 255, 255), (297, 130), (297, 300), 6)
        pygame.draw.lines(VEHICLE_SURFACE, (255, 255, 255, 255), False,
                          [(50, 405), (50, 240), (70, 140), (260, 140), (260, 405)], 1)
        pygame.draw.line(VEHICLE_SURFACE, (255, 255, 255, 255), (220, 270), (250, 270), 3)

        # Seats
        pygame.draw.rect(VEHICLE_SURFACE, (128, 0, 128, 255), (140, 200, 100, 50))

        # Driver
        pygame.draw.circle(VEHICLE_SURFACE, (255, 255, 0, 255), (190, 175), 25)

        # Wheels
        pygame.draw.circle(VEHICLE_SURFACE, (0, 0, 0, 255), (140, 400), 80)
        pygame.draw.circle(VEHICLE_SURFACE, (0, 0, 0, 255), (800, 400), 80)
        pygame.draw.circle(VEHICLE_SURFACE, (0, 0, 0, 255), (1000, 400), 80)

        screen.blit(self._scaled_surface if self._scaled_surface else VEHICLE_SURFACE, (self._x, self._y))

    def __drawSUV(self):
        # Truck Body
        pygame.draw.polygon(VEHICLE_SURFACE, self.vehicle_color,
                            [[50, 230], [250, 230], [290, 100], [950, 100], [950, 400], [50, 400]])
        # Windows
        pygame.draw.polygon(VEHICLE_SURFACE, (255, 255, 255, 255),
                            [[270, 230], [310, 120], [530, 120], [530, 230]])
        pygame.draw.polygon(VEHICLE_SURFACE, (255, 255, 255, 255),
                            [[600, 120], [900, 120], [900, 230], [600, 230]])

        # Doors
        pygame.draw.line(VEHICLE_SURFACE, (255, 255, 255, 255), (250, 230), (250, 400), 1)
        pygame.draw.line(VEHICLE_SURFACE, (255, 255, 255, 255), (565, 100), (565, 400), 1)
        pygame.draw.line(VEHICLE_SURFACE, (255, 255, 255, 255), (800, 100), (800, 400), 1)
        pygame.draw.line(VEHICLE_SURFACE, (255, 255, 255, 255), (500, 250), (530, 250), 3)
        pygame.draw.line(VEHICLE_SURFACE, (255, 255, 255, 255), (750, 250), (780, 250), 3)

        # Seats
        pygame.draw.rect(VEHICLE_SURFACE, (128, 0, 128, 255), (400, 180, 120, 50))
        pygame.draw.rect(VEHICLE_SURFACE, (128, 0, 128, 255), (620, 180, 100, 50))
        pygame.draw.rect(VEHICLE_SURFACE, (128, 0, 128, 255), (750, 180, 100, 50))

        # Driver
        pygame.draw.circle(VEHICLE_SURFACE, (255, 255, 0, 255), (460, 150), 30)

        # Wheels
        pygame.draw.circle(VEHICLE_SURFACE, (0, 0, 0, 255), (180, 400), 80)
        pygame.draw.circle(VEHICLE_SURFACE, (0, 0, 0, 255), (800, 400), 80)
        pygame.draw.rect(VEHICLE_SURFACE, (0, 0, 0, 255), (950, 140, 40, 140))

        screen.blit(self._scaled_surface if self._scaled_surface else VEHICLE_SURFACE, (self._x, self._y))

    def __drawFlower(self, surface, x, y, color):
        # Draw the center of the flower
        pygame.draw.circle(surface, (255, 255, 0), (x, y), 20)

        # Draw petals
        for i in range(16):
            self.__drawPetal(surface, i * 22.5, x, y, color)
        # Draw stalk
        pygame.draw.line(surface, (139, 69, 19), (x, y + 20), (x, y + 100), 5)

        # Draw leaves using ellipses
        pygame.draw.ellipse(surface, (0, 128, 0), pygame.Rect(x, y + 50, 80, 20))
        pygame.draw.ellipse(surface, (0, 128, 0), pygame.Rect(x - 80, y + 50, 80, 20))

    def __drawPetal(self, surface, petal_angle, x, y, color):
        # Convert the angle to radians
        petal_angle_radians = radians(petal_angle)

        # Calculate the starting and ending points of the petal
        petal_start_pos = (x + 30 * cos(petal_angle_radians),
                           y + 30 * sin(petal_angle_radians))
        petal_end_pos = (x + 50 * cos(petal_angle_radians),
                         y + 50 * sin(petal_angle_radians))
        petal_control_point = (x + 40 * cos(petal_angle_radians + pi / 4),
                               y + 40 * sin(petal_angle_radians + pi / 4))

        # Generate points from the Bezier curve
        bezier_points = generate_bezier_points(petal_start_pos, petal_control_point, petal_control_point, petal_end_pos,
                                               10)

        # Draw the petal using the generated points
        pygame.draw.polygon(surface, color, bezier_points)

    def setPetalColor(self):
        self.petals_color = [(generateRandomLength(0, 255), generateRandomLength(0, 255),
                              generateRandomLength(0, 255)) for _ in range(10)]

    def setVehicleColor(self):
        self.vehicle_color = (
            generateRandomLength(0, 255), generateRandomLength(0, 255), generateRandomLength(0, 255), 255)

    def setData(self, data):
        self.type = data['type']
        self.data = data['info']
        self.setVehicleColor()
        self.setPetalColor()
        self.resetSurface()
        self.draw()
        self.scale()


data = {}


# Function to generate points from a Bezier curve
def generate_bezier_points(p0, p1, p2, p3, steps):
    points = []
    for t in range(steps + 1):
        x = int((1 - t / steps) ** 3 * p0[0] + 3 * (1 - t / steps) ** 2 * (t / steps) * p1[0] + 3 * (1 - t / steps) * (
                t / steps) ** 2 * p2[0] + (t / steps) ** 3 * p3[0])
        y = int((1 - t / steps) ** 3 * p0[1] + 3 * (1 - t / steps) ** 2 * (t / steps) * p1[1] + 3 * (1 - t / steps) * (
                t / steps) ** 2 * p2[1] + (t / steps) ** 3 * p3[1])
        points.append((x, y))
    return points


def car():
    car = Car('BMW', 2001, 70000, 15000.0, 4)
    data['type'] = "Car"
    data['info'] = {'Make': car.get_make(), 'Model': car.get_model(), 'Mileage': car.get_mileage(),
                    'Price': car.get_price(), 'Number of doors': car.get_doors()
                    }
    display_info.setData(data)


def truck():
    truck = Truck('Toyota', 2002, 40000, 12000.0, '4WD')
    data['type'] = "Truck"
    data['info'] = {'Make': truck.get_make(),
                    'Model': truck.get_model(),
                    'Mileage': truck.get_mileage(),
                    'Price': truck.get_price(), 'Drive type': truck.get_drive_type()}
    display_info.setData(data)


def suv():
    suv = SUV('Volvo', 2000, 30000, 18500.0, 5)
    data['type'] = "SUV"
    data['info'] = {
        'Make': suv.get_make(),
        'Model': suv.get_model(),
        'Mileage': suv.get_mileage(),
        'Price': suv.get_price(),
        'Passenger Capacity': suv.get_pass_cap()
    }
    display_info.setData(data)


def refresh():
    display_info.scale()
    display_info.setPetalColor()
    display_info.setVehicleColor()


def generateRandomLength(a, b):
    u = random.random()
    return a + u * (b - a)


# Initialize the classes

display_info = Display()

buttons = [Button('Car', 10, 10), Button('Truck', 180, 10), Button('SUV', 350, 10), Button('Refresh', 1030, 10)]

running = True
clock = pygame.time.Clock()

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            mouse_position = pygame.mouse.get_pos()
            for button in buttons:
                if button.is_clicked(mouse_position):
                    if button.get_name() == 'Car':
                        car()
                    elif button.get_name() == 'Truck':
                        truck()
                    elif button.get_name() == 'SUV':
                        suv()
                    elif button.get_name() == 'Refresh':
                        refresh()

    screen.fill('white')

    # Draw buttons
    for button in buttons:
        button.draw()

    display_info.show()
    display_info.draw()

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
