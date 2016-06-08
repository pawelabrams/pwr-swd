import urllib2
import json
import dateutil.parser as parser
import datetime
teams = []
for t in xrange(0,800):
    try:
        response = urllib2.urlopen('http://api.autostoprace.pl/teams/team-'+str(t)+'/locations')
        j = response.read()
        if len(j) < 10:
            print str(t) + " has no updates"
            continue
        decoded = json.loads(j)
        for d in decoded:
            d["id"] = t
            del d["country"]
            del d["updated_at"]
            del d["country_code"]
            del d["address"]
            del d["message"]
            d["hours_from_start"] = int((parser.parse(d["created_at"]) - parser.parse("2016-04-30T00:09:00.001Z")).total_seconds() / (3600))
            #print d["minutes_from_start"]
            del d["created_at"]
            #if (parser.parse(d["created_at"]) - parser.parse("2016-04-30T00:09:00.001Z")).total_seconds() / (60) < 0:
            #    print parser.parse(d["created_at"])
            #teams.append(d)
        #print decoded
        teams.append(decoded)
    except urllib2.HTTPError:
        print str(t) + " has no updates"
        continue

teams = json.dumps(teams)
with open('./locationsNested.json','w') as f:
    f.write(teams)
