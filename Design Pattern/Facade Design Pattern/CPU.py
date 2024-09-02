class CPU:
    def freeze(self):
        print("CPU: Freezing")

    def jump(self, address):
        print(f"CPU: Jumping to address {address}")

    def execute(self):
        print("CPU: Executing")
