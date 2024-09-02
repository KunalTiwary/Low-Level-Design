import copy


class Prototype:
    def clone(self):
        return copy.copy(self)

    def deep_clone(self):
        return copy.deepcopy(self)


class Car(Prototype):
    def __init__(self, model, color, options):
        self.model = model
        self.color = color
        self.options = options

    def __str__(self):
        return f'{self.color} {self.model} with options {self.options}'


# Client code
if __name__ == "__main__":
    # Create an original car object
    original_car = Car("Tesla Model S", "Red", ["sunroof", "leather seats"])
    print("Original car:", original_car)

    # Clone the car (shallow copy)
    cloned_car = original_car.clone()
    print("Cloned car:", cloned_car)

    # Modify the cloned car
    cloned_car.color = "Blue"
    cloned_car.options.append("sport package")
    print("Modified cloned car:", cloned_car)

    # Original car remains unchanged in shallow copy
    print("Original car after modification to clone:", original_car)

    # Deep clone the car
    deep_cloned_car = original_car.deep_clone()
    deep_cloned_car.color = "Green"
    deep_cloned_car.options.append("autopilot")
    print("Deep cloned car:", deep_cloned_car)

    # Original car remains unchanged in deep copy
    print("Original car after deep clone modification:", original_car)
