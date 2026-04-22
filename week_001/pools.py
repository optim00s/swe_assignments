import math 

GRAVITY_OF_EARTH = 9.81
GRAVITY_OF_MOON = 1.62
PI_VALUE = math.pi

def ft_to_m(ft):
    """Imperial to SI"""
    return ft * 0.3048

def get_water_density(oz_per_inch):
    """
    Density is 0.58 oz/in^3F
    1 oz = 0.0283495 kg
    1 inch = 0.0254 m
    We need kg / m^3
    """
    mass_kg = oz_per_inch * 0.0283495
    vol_m3 = 0.0254 ** 3
    rho = mass_kg / vol_m3
    return rho

# Funcs for solving a and b
def area_cubic(length, width):
    area = length * width
    return area

def volume_cubic(length, width, depth):
    volume = length * width * depth
    return volume

# Funcs for solving c and d
def area_clyindrical(PI_VALUE, radius):
    area = PI_VALUE * (radius ** 2)
    return area

def volume_cylindrical(PI_VALUE, radius, depth):
    volume = PI_VALUE * (radius ** 2) * depth 
    return volume

# General funcs for calculate weight and pressure
def weight(rho, volume, gravity):
    weight = rho * volume * gravity
    return weight

def pressure(weight, area):
    pressure = weight / area
    return pressure 

def main():
    rho = get_water_density(0.58)
    pools = []

    # Problem A
    length_a = ft_to_m(20)
    width_a = ft_to_m(10)
    depth_a = ft_to_m(6)
    area_a = area_cubic(length_a, width_a)
    volume_a = volume_cubic(length_a, width_a, depth_a)
    weight_a_on_earth = weight(rho, volume_a, GRAVITY_OF_EARTH)
    pressure_a = pressure(weight_a_on_earth, area_a)
    pools.append(("A", area_a, volume_a, pressure_a))

    # Problem B
    length_b = ft_to_m(10)
    width_b = ft_to_m(10)
    depth_b = ft_to_m(8)
    area_b = area_cubic(length_b, width_b)
    volume_b = volume_cubic(length_b, width_b, depth_b)
    weight_b_on_earth = weight(rho, volume_b, GRAVITY_OF_EARTH)
    pressure_b = pressure(weight_b_on_earth, area_b)
    pools.append(("B", area_b, volume_b, pressure_b))

    # Problem C
    radius_c = ft_to_m(5)
    depth_c = ft_to_m(2)
    area_c = area_clyindrical(PI_VALUE, radius_c)
    volume_c = volume_cylindrical(PI_VALUE, radius_c, depth_c)
    weight_c_on_earth = weight(rho, volume_c, GRAVITY_OF_EARTH)
    pressure_c = pressure(weight_c_on_earth, area_c)
    pools.append(("C", area_c, volume_c, pressure_c))

    # Problem D
    radius_d = ft_to_m(9)
    depth_d = ft_to_m(1.5)
    area_d = area_clyindrical(PI_VALUE, radius_d)
    volume_d = volume_cylindrical(PI_VALUE, radius_d, depth_d)
    weight_d_on_earth = weight(rho, volume_d, GRAVITY_OF_EARTH)
    pressure_d = pressure(weight_d_on_earth, area_d)
    pools.append(("D", area_d, volume_d, pressure_d))

    max_area = max(pools, key = lambda x: x[1])
    max_volume = max(pools, key = lambda x: x[2])
    max_pressure = max(pools, key = lambda x: x[3])

    print("-----Earth Pressure-----")
    for name, _, _, p in pools:
        print(f"{name}: {p:.3f} Pa")
    
    print("-----Max Stats------")
    print(f"For volume: {max_volume[0]}\nFor area: {max_area[0]}\nFor pressure: {max_pressure[0]}")

    print("-----Moon Pressure-----")
    for name, area, vol, p in pools:
        weight_on_moon = weight(rho, vol, GRAVITY_OF_MOON)
        pressure_on_moon = pressure(weight_on_moon, area)
        print(f"{name}: {pressure_on_moon:.3f} Pa")
    

if __name__ == '__main__':
    main()

