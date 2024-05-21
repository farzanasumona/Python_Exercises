# Write a program that calculates the volume of a sphere given its radius.

radius = float(input("Enter the radius of the sphere: "))

volume_calculation = (4.0 / 3.0) * 3.14 * radius ** 3  # pi = 3.14

print(f"The volume of the sphere is: ", round(volume_calculation, 2))

