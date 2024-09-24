class Car:
    DIRECTIONS = ['N', 'E', 'S', 'W']

    def __init__(self, name, x, y, direction):
        self.name = name
        self.x = x
        self.y = y
        self.direction = direction
        self.commands = ""
        self.collided = False

    def rotate_left(self):
        self.direction = self.DIRECTIONS[(self.DIRECTIONS.index(self.direction) - 1) % 4]

    def rotate_right(self):
        self.direction = self.DIRECTIONS[(self.DIRECTIONS.index(self.direction) + 1) % 4]

    def move_forward(self, width, height):
        if self.direction == 'N' and self.y < height - 1:
            self.y += 1
        elif self.direction == 'E' and self.x < width - 1:
            self.x += 1
        elif self.direction == 'S' and self.y > 0:
            self.y -= 1
        elif self.direction == 'W' and self.x > 0:
            self.x -= 1

    def __str__(self):
        return f"Car {self.name} is at ({self.x}, {self.y}) facing {self.direction}"

def check_collision(cars):
    positions = {}
    for car in cars:
        if (car.x, car.y) in positions:
            return True, car, positions[(car.x, car.y)]
        positions[(car.x, car.y)] = car
    return False, None, None

def main():
    while True:
        print("Welcome to Auto Driving Car Simulation!")
        width, height = map(int, input("Please enter the width and height of the simulation field in x y format: ").split())
        print(f"You have created a field of {width} x {height}.")

        cars = []

        while True:
            print("\nPlease choose from the following options:")
            print("[1] Add a car to field")
            print("[2] Run simulation")
            print("[3] Exit")
            choice = input()

            if choice == '1':
                name = input("Please enter the name of the car: ")
                x, y, direction = input(f"Please enter initial position of car {name} in x y Direction format: ").split()
                x, y = int(x), int(y)
                direction = direction.upper()
                if direction not in Car.DIRECTIONS:
                    print("Invalid direction. Please enter N, S, W, or E.")
                    continue
                car = Car(name, x, y, direction)
                car.commands = input(f"Please enter the commands for car {name}: ").upper()
                cars.append(car)
                print(f"Car {name} added at ({x}, {y}) facing {direction} with commands {car.commands}.")

            elif choice == '2':
                max_steps = max(len(car.commands) for car in cars)
                for step in range(max_steps):
                    for car in cars:
                        if car.collided or step >= len(car.commands):
                            continue
                        command = car.commands[step]
                        if command == 'L':
                            car.rotate_left()
                        elif command == 'R':
                            car.rotate_right()
                        elif command == 'F':
                            car.move_forward(width, height)
                    
                    collision, car1, car2 = check_collision(cars)
                    if collision:
                        car1.collided = True
                        car2.collided = True
                        print(f"\nAfter simulation, the result is:")
                        print(f"- {car1.name}, collides with {car2.name} at ({car1.x},{car1.y}) at step {step + 1}")
                        print(f"- {car2.name}, collides with {car1.name} at ({car1.x},{car1.y}) at step {step + 1}")
                        break
                else:
                    print("\nAfter simulation, the result is:")
                    for car in cars:
                        print(f"- {car.name}, ({car.x},{car.y}) {car.direction}")

                print("\nPlease choose from the following options:")
                print("[1] Start over")
                print("[2] Exit")
                post_sim_choice = input()

                if post_sim_choice == '1':
                    break
                elif post_sim_choice == '2':
                    print("Thank you for running the simulation. Goodbye!")
                    return
                else:
                    print("Invalid choice. Please try again.")

            elif choice == '3':
                print("Thank you for running the simulation. Goodbye!")
                return

            else:
                print("Invalid choice. Please try again.")

            print("\nYour current list of cars are:")
            for car in cars:
                print(f"- {car.name}, ({car.x},{car.y}) {car.direction}, {car.commands}")

if __name__ == "__main__":
    main()
