from ShapeFactory import ShapeFactory


if __name__ == "__main__":
    sf = ShapeFactory()
    shape = sf.getShape()
    shape.draw()

# you can run this by - python -m "{main File Name}.main", This makes Python treat the script as part of a
# package, resolving the imports correctly.