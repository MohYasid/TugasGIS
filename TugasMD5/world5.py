import mapnik
m = mapnik.Map(600,300)
m.background = mapnik.Color('steelblue')
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#f2eff9')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('green'), 1)
line_symbolizer.stroke_width = 10.0

r.symbols.append(line_symbolizer)

basinsLabels = mapnik.TextSymbolizer(mapnik.Expression('[NAME]'), 'DejaVu Sans Bold',2,mapnik.Color('black'))
basinsLabels.halo_fill = mapnik.Color('yellow')
basinsLabels.halo_radius = 2
r.symbols.append(basinsLabels)


point_sym = mapnik.PointSymbolizer()
point_sym.allow_overlap = True
r.symbols.append(point_sym)

s.rules.append(r)

highlight = mapnik.PolygonSymbolizer()
highlight.fill = mapnik.Color('red')
netherlands = mapnik.Rule()
netherlands.filter = mapnik.Expression("[NAME] = 'Netherlands'")
netherlands.symbols.append(highlight)
s.rules.append(netherlands)

#Netherlands
m.append_style('My Style',s)
ds = mapnik.Shapefile(file="Natural_Earth/ne_110m_admin_0_countries.shp")
layer = mapnik.Layer('world5')
layer.datasource = ds 
layer.styles.append('My Style')
m.layers.append(layer)

#Provinsi Indonesia
s = mapnik.Style()
r = mapnik.Rule()

line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('#00FFFF'), 1)
r.symbols.append(line_symbolizer)
s.rules.append(r)

m.append_style('My Style2',s)
ds = mapnik.Shapefile(file="shp/SHP_Indonesia_provinsi/INDONESIA_PROP.shp")
layer = mapnik.Layer('provinsi')
layer.datasource = ds 
layer.styles.append('My Style2')
m.layers.append(layer)

#Amerika 
s = mapnik.Style()
r = mapnik.Rule()

line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('blue'), 1)
r.symbols.append(line_symbolizer)
s.rules.append(r)

m.append_style('My Style3',s)
ds = mapnik.Shapefile(file="shp/StatPlanet_USA_County/map/map.shp")
layer = mapnik.Layer('amerika')
layer.datasource = ds 
layer.styles.append('My Style3')
m.layers.append(layer)

#Turki
s = mapnik.Style()
r = mapnik.Rule()

line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('#FF0099'), 1)
r.symbols.append(line_symbolizer)
s.rules.append(r)

m.append_style('My Style4',s)
ds = mapnik.Shapefile(file="shp/StatPlanet_Turkey/map/map.shp")
layer = mapnik.Layer('turki')
layer.datasource = ds 
layer.styles.append('My Style4')
m.layers.append(layer)

#Canada
s = mapnik.Style()
r = mapnik.Rule()

line_symbolizer = mapnik.LineSymbolizer(mapnik.Color('#FF7f00'), 1)
r.symbols.append(line_symbolizer)
s.rules.append(r)

m.append_style('My Style5',s)
ds = mapnik.Shapefile(file="shp/StatPlanet_Canada/map/map.shp")
layer = mapnik.Layer('canada')
layer.datasource = ds 
layer.styles.append('My Style5')
m.layers.append(layer)



m.zoom_all()
mapnik.render_to_file(m,'world5.pdf', 'pdf')
print "rendered image to 'world5.pdf'"

