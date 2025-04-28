import matplotlib.pyplot as plt
import geopandas as gpd

input = '''
Alabama: red

Alaska: red

Arizona: red

Arkansas: red

California: green

Colorado: green

Connecticut: red

Delaware: red

Florida: green

Georgia: blue

Hawaii: red

Idaho: red

Illinois: red

Indiana: green

Iowa: blue

Kansas: red

Kentucky: blue

Louisiana: blue

Maine: red

Maryland: green

Massachusetts: green

Michigan: blue

Minnesota: red

Mississippi: green

Missouri: green

Montana: yellow

Nebraska: yellow

Nevada: blue

New Hampshire: blue

New Jersey: green

New Mexico: blue

New York: yellow

North Carolina: green

North Dakota: blue

Ohio: red

Oklahoma: yellow

Oregon: yellow

Pennsylvania: blue

Rhode Island: blue

South Carolina: red

South Dakota: green

Tennessee: yellow

Texas: green

Utah: yellow

Vermont: red

Virginia: red

Washington: green

West Virginia: yellow

Wisconsin: green

Wyoming: blue
'''

state_colors = {}
for line in input.strip().split('\n\n'):
    state, color = line.split(': ')
    state_colors[state] = color
us_states = gpd.read_file('QSharpGrovers/ne_110m_admin_1_states_provinces.shp')
us_states = us_states[us_states['iso_a2'] == 'US']
us_states['color'] = us_states['name'].map(state_colors)
us_states['color'].fillna('gray', inplace=True)
fig, ax = plt.subplots(1, 1, figsize=(15, 10))
us_states.boundary.plot(ax=ax, color="black", linewidth=0.5)
us_states.plot(ax=ax, color=us_states['color'], edgecolor='black')
plt.show()