class AC:
    def turn_on(self):
        print("AC is ON")

    def turn_off(self):
        print("AC is OFF")

    def set_temperature(self, temperature: int):
        self.temperature = temperature
        print(f"AC temperature set to {temperature}°C")
