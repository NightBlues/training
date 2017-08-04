import refcycle

print 'importing...'
snapshot = refcycle.AnnotatedGraph.import_json('/devel/worker_pp.json')

# print 'lookin at leaks...'
# leaks = snapshot.strongly_connected_components()
# print 'sorting leaks...'
# leaks.sort(key=len)
# print 'found {} leaks'.format(len(leaks))
# leaks = [l for l in leaks if 'reportmaker' in l.to_json().lower()]
# print 'filtered {} leaks'.format(len(leaks))
# print 'len is {}'.format(len(leaks[0]))

# report_makers = [v for v in snapshot.vertices
#                 if 'reportmaker' in v.annotation.lower()]
# print 'found {} report_makers'.format(len(report_makers))
# report_maker = report_makers[0]
# ancs = snapshot.ancestors(report_maker, generations=5)

# print 'generating image of ancestors {}'.format(ancs)
# ancs.export_image('ancestors.svg')
    

# for i in range(len(leaks)):
#     print 'generating image for leak {}'.format(i)
#     leaks[i].export_image('leak_{}.svg'.format(i))



# ---

components = snapshot.source_components()
print 'found {} source components'.format(len(components))
# components = [c for c in components if 'report' in c.to_json().lower()]
# print 'filtered {} source components'.format(len(components))
for i, c in enumerate(sorted(components, key=len)):
    if len(c) < 3:
        continue
    if len(c) > 6000:
        break
    print 'generating image for component {}'.format(i)
    c.export_image('leak_{}.svg'.format(i))
