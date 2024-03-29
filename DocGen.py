import json

with open("Doc.json", "r") as f:
    data = json.load(f)

settings = data[0]["settings"]
for i in data[0]["doc"]:
	path = settings["start_path"] + "/" + i["path"]
	buffer = open(path, "r").read()
	
	f = open(path, "w")
	f.write("/**\n" + "\n".join(i["text"][it:it + settings["nline_size"]] for it in range(0, len(i["text"]), settings["nline_size"]))+ "\n © " + settings["license"] + "\n*/\n\n" + buffer)
	f.close()