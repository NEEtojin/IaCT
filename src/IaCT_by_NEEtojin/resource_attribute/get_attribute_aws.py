"""
(.*">)([a-z0-9]+)(</a>":.*)
(.*getatt.*"code">)([a-z0-9]+)(</code>.*)
process html
replace with regex
"""
import re
import urllib.request

def get_attribute():
    print("IaCT")
    with urllib.request.urlopen("https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-resource-ec2-instance.html") as response:
        html=response.read()
        count = 0
        for property in re.findall(r'(.*">)([A-Za-z0-9]+)(</a>" : .*)', html.decode('utf-8')):
            print(count, property[1])
            count+=1

if __name__ == "__main__":
    get_attribute()