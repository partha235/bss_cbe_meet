G = 6.674 * (10 ** -11)  # gravitational constant
m1 = 5.972 * (10 ** 24)  # Earth mass in kg
m2 = 1  # 1 kg object
r = 6.371 * (10 ** 6)  # radius in meters

F = G * m1 * m2 / (r ** 2)
print("Gravitational Force:", F, "Newtons")
