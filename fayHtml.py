import sys
import os

filename = sys.argv[1]
currPath = os.getcwd() 
filepath = os.path.join(currPath, filename)

def getComponent(name, attributes):
    with open(os.path.join(currPath, name) + ".html", 'r') as f:
        content = f.read()
        startIdx = content.find("<INeed")
        endIdx = content.find(">", startIdx)
        attr = []
        for a in content[startIdx+7:endIdx].split(","):
            attr.append(a.strip())
        for a in attr:
            if a not in attributes:
                print(a, "Not Found")
        content = content[:startIdx] + content[endIdx+1:]
        for a in attr:
            content = content.replace(f"Put_{a}", attributes[a])
        return content



with open(filepath, 'r') as f:
    content = f.read()
    while(1):
        startIdx = content.find("<LookFor")
        if startIdx == -1:
            break
        endIdx = content.find(">", startIdx)
        attributes = {}
        for attr in content[startIdx+9:endIdx].split(","):
            key, value = attr.split("=")
            attributes[key.strip()] = value.strip()[1:-1]
        content = content[:startIdx] + getComponent(attributes["SkibidiName"], attributes) + content[endIdx+1:]
    
    with open("output.html", 'w') as f:
        f.write(content)
        
        

