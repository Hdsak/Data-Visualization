import pygal

wm=pygal.maps.world.World()
wm.title="North, central and South America"
wm.add("North America",{'ca':20000,'mx':20012,'us':230214})
wm.add('Central',['bz', 'cr', 'gt', 'hn', 'ni', 'pa', 'sv'])
wm.add('South America',['ar', 'bo', 'br', 'cl', 'co', 'ec', 'gf',
'gy', 'pe', 'py', 'sr', 'uy', 've'])

wm.render_to_file('americas.svg')
