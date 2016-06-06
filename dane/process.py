import json

paths = {}
points = set()
with open('locations_wo_originals.json') as fp:
    teams = json.load(fp)
    for t in teams:
        last = "Wrocław Wro"
        last_h = 0
        for l in t:
            p = l['latitude'][0:5] + "," + l['longitude'][0:5]
            if l['hours_from_start'] > 0 and p != last: # TODO odwrotnie, jeśli minus?!
                points.add(p)
                try:
                    paths[last+"-"+p].append(l['hours_from_start'] - last_h),
                except:
                    paths[last+"-"+p] = [l['hours_from_start'] - last_h]
                last = p
                last_h = l['hours_from_start']




buckets = []
for x in paths:
    print (x + " " + str(paths[x]))
    buckets.append(len(paths[x]))
print ("1: " + str(buckets.count(1)))
print ("2: " + str(buckets.count(2)))
print ("3: " + str(buckets.count(3)))
print ("4: " + str(buckets.count(4)))
print ("5: " + str(buckets.count(5)))
print ("6: " + str(buckets.count(6)))
print ("7+: " + str(sum([x for x in buckets if x > 6])))