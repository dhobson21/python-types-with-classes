from building import Building
from city import City



megaloplis = City("megaloplis", "Dustin Hobson", "1998")




building_one = Building("85 1st st.", 3)
building_one.purchase("Curt Cato")
building_one.construct()
building_two = Building("12 2nd st.", 5)
building_two.purchase("Joe Kennerly")
building_two.construct()
building_three = Building("123 3rd st.", 12)
building_three.purchase("Dustin Hobson")
building_three.construct()
building_four = Building("655 4th st.", 8)
building_four.purchase("Scott Silver")
building_four.construct()
building_five = Building("855 5th st.", 9)
building_five.purchase("Adam Knowles")
building_five.construct()

buildings = (building_one, building_two, building_three, building_four, building_five)

megaloplis.add_building(building_one)
megaloplis.add_building(building_two)
megaloplis.add_building(building_three)
megaloplis.add_building(building_four)
megaloplis.add_building(building_five)

for building in buildings:
    date = building.date_constructed.strftime('%m/%d/%y')
    print(f'{building.address} was purchased by {building.owner} on {date} and has {building.stories} stories')


for building in megaloplis.buildings:
  date = building.date_constructed.strftime('%m/%d/%y')
  print(f'{building.address} in the city of {megaloplis.name} was purchased by {building.owner} on {date} and has {building.stories} stories')