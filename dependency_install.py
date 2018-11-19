
#from pip._internal import main
#Approach 1
import pip
import json
not_installed =[]
with open('dependencies.json') as json_file:
    data = json.load(json_file)
    for p in data['dependencies']:
        # print(p)
        pip.main(['install', p])
        if ImportError:
            not_installed.append(p)
if(len(not_installed)==0):
    print("Success")
else:
    print("Failed Packages")
    for i in not_installed:
        print(i)

#Approach 2
'''import json
f = open("dependencies1.txt", "w")
with open('dependencies.json') as json_file:
    data = json.load(json_file)
    for p in data['dependencies']:
        f.write(p)
    #And in the command line we can install pip install -r dependencies1.txt
