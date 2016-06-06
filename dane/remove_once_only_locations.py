import json

points = set()
points_twice = set()

with open('locationsNested.json') as fp:
    teams = json.load(fp)
    for t in teams:
        last = None
        for l in t:
            p = (float(l['latitude'][0:5]), float(l['longitude'][0:5]))
            if p in points and p != last:
                if not p in points_twice:
                    points_twice.add(p)
                    #print (p)
            else:
                points.add(p)
            last = p

print (json.dumps([[l for l in team if (float(l['latitude'][0:5]), float(l['longitude'][0:5])) in points_twice] for team in teams]))