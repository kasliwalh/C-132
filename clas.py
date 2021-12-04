import csv
import plotly.express as px

rows = []

with open("main.csv", "r") as data:
    data_read = csv.reader(data)

    for i in data_read:
        rows.append(i)

# To split the data into column titles and values
header = rows[0]
planet_data = rows[1:]

# To add the first missing column name
header[0] = "row_num"

# To find out the Solar System with the most number of planets
ss_count = {}

for i in planet_data:

    if ss_count.get(i[11]):
        ss_count[i[11]] += 1

    else:
        ss_count[i[11]] = 1

max_ss = max(ss_count, key = ss_count.get)

# print("The Solar System {} has the maximim number of planets {} out of all the Solar Systems in the document".format(max_ss, ss_count[max_ss]))
# print("_____________________________")

# To list all the planets from the KOI-345 planet
ss_planets = []

for i in planet_data:

    if max_ss == i[11]:
        ss_planets.append(i)

# print(len(ss_planets))
# print("_____________________________")
# print(ss_planets)

# To make the data (planet_mass)(planet_radius) uniform
temp_planet_rows = list(planet_data)

for i in temp_planet_rows:
    planet_mass = i[3]

    # To remove the rows for which the planet mass is "unknown"
    if planet_mass.lower()=="unknown":
        temp_planet_rows.remove(i)
        
        continue

    else:
        planet_mass_value = planet_mass.split(" ")[0]
        planet_mass_ref = planet_mass.split(" ")[1]

        # To relpace the values which were in refernece to Jupiter with reference to Earth
        if planet_mass_ref == "Jupiters":
            planet_mass_value = float(planet_mass_value) * 317.8

        planet_mass_value  = planet_data[3]

    planet_radius = planet_data[7]

    if planet_radius=="unknown":
        planet_data.remove(i)

# To draw a bar graph for the planet mass
KOI_mass = []
KOI_names = []

for i in ss_planets:
    KOI_mass.append(i[3])
    KOI_names.append(i[1])
    KOI_mass.append(1)
    KOI_names.append("Earth")

bar_graph = px.bar(x = KOI_names, y = KOI_mass)
# bar_graph.show()

# To create a scatter plot for the planet radius and the planet mass

planet_radius = []
planet_mass = []
planet_names = []

for i in planet_data:
    print(i)
    planet_mass.append(i[3])
    planet_radius.append(planet_data[7])
    planet_names.append(i[1])

planet_gravity = []

for index, name in enumerate(planet_radius):
    gravity = (float(planet_mass[index])*5.972e+24)/(float(planet_radius[index])*float(planet_radius[index])*6371000)*6.674e-11

    planet_gravity.append(gravity)

scatter_plot = px.scatter(x = planet_radius, y = planet_mass, size = planet_gravity, hover_data = [planet_names])

#scatter_plot.show()

# To find the number of planets qith gravity less that 10
low_gravity_planets = []

for index, gravity in enumerate(planet_gravity):
    
    if gravity < 10:
        low_gravity_planets.append(i[index])

print(len(low_gravity_planets))