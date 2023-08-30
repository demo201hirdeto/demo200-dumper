import requests
from time import time
import json

programStart = time()
reqStart = time()

dump = requests.get(
	url="https://demo200.5mp.eu/web.php?a=demo200&o=yDaKba7PGL"
).text

reqTime = time() - reqStart

print(f"Took {str(reqTime)} to get the website contents.")

dump = dump.replace("</font></b>", "").replace("<br>", "").replace("<br />", "")

items = dump.split("<hr><b>")

itemslength = len(items)

dump = ""

items[0] = items[0].split("<div style=padding:5;background:white;color:#444444;text-align:left><b>")[1].strip()

items[itemslength - 1] = items[itemslength - 1].split("</div></div></td></tr></table></center>")[0]

db_ready = []

for item in items:
	item = item.strip()
	name = item.split("<font color=#999999>")[0].strip()
	timestamp = item.split("<font color=#999999>[")[1].split("]")[0].strip()
	content = item.split("<font color=#999999>[")[1].split("]")[1]

	db_ready.append({
		"name": name,
		"time": timestamp,
		"content": content
	})

items = []

open("db.json", mode="w+", encoding="UTF-8").write(json.dumps(db_ready))

programTime = time() - programStart

print(f"Took {str(programTime)} to dump {str(itemslength)} messages in db.json.")
