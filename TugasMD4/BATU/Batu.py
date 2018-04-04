import mapnik
m = mapnik.Map(650,350)
m.background = mapnik.Color('steelblue')
s = mapnik.Style()
r = mapnik.Rule()
polygon_symbolizer = mapnik.PolygonSymbolizer()
polygon_symbolizer.fill = mapnik.Color('#6d720d')
r.symbols.append(polygon_symbolizer)

line_symbolizer = mapnik.LineSymbolizer()
line_symbolizer.stroke = mapnik.Color('rgb(50%,50%,50%)')


r.symbols.append(line_symbolizer)
s.rules.append(r)
m.append_style('My Style',s)
ds = mapnik.Shapefile(file="TugasGIS/BATU/BATU.shp")
layer = mapnik.Layer('batu')
layer.datasource = ds 
layer.styles.append('My Style')
m.layers.append(layer)
m.zoom_all()
mapnik.render_to_file(m,'batu.pdf', 'pdf')
print "rendered image to 'batu.pdf'"
