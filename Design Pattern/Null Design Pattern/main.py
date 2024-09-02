# from .VehicleFactory import VehicleFactory
#
#
# if __name__ == "__main__":
#     vf = VehicleFactory()
#     vehicle1 = vf.getVehicleObject("BIKE")
#     vehicle2 = vf.getVehicleObject("CAR")
#     print(vehicle1.fuelCapacity())
#     print(vehicle1.seatingCapacity())
#     print(vehicle2.fuelCapacity())
#     print(vehicle2.seatingCapacity())
#
# # python -m "Null Design Pattern.main"
#

class InputBuffer:
    def __init__(self):
        self.buffer = ""
        self.buffer_length = 0
        self.input_length = 0

def new_input_buffer():
    return InputBuffer()

def print_prompt():
    print("db > ", end="")

def read_input(input_buffer):
    try:
        input_buffer.buffer = input()
        input_buffer.input_length = len(input_buffer.buffer)
        input_buffer.buffer_length = input_buffer.input_length + 1

        # Ignore trailing newline if present
        if input_buffer.buffer.endswith("\n"):
            input_buffer.buffer = input_buffer.buffer[:-1]
            input_buffer.input_length -= 1
    except EOFError:
        print("Error reading input")
        exit(1)

def main():
    input_buffer = new_input_buffer()
    while True:
        print_prompt()
        read_input(input_buffer)

        if input_buffer.buffer == ".exit":
            exit(0)
        else:
            print(f"Unrecognized command '{input_buffer.buffer}'.")

if __name__ == "__main__":
    main()
