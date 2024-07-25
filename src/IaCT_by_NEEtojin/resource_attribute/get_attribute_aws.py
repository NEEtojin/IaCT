import re
import urllib.request

def get_service():
    with urllib.request.urlopen(f"https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/aws-template-resource-type-ref.html") as response:
        html=response.read()
        count = 0
        for service in re.findall(r'(<a href="\./)([A-Za-z0-9\_\.]+)(">)', html.decode('utf-8')):
            print(service[1])
            get_resource(service[1])
            count += 1
            if count == 1: break

def get_resource(service: str = "AWS_EC2.html"):
    with urllib.request.urlopen(f"https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/{service}") as response:
        html=response.read()
        count = 0
        for resource in re.findall(r'(<a href="\./)([a-z0-9\-\.]+)(">)', html.decode('utf-8')):
            print("\t", resource[1])
            get_attribute(resource[1])
            count += 1
            if count == 2: break

def get_attribute(resource: str = "aws-resource-ec2-instance.html"):
    """
    (.*">)([a-z0-9]+)(</a>":.*)
    (.*getatt.*"code">)([a-z0-9]+)(</code>.*)
    process html
    replace with regex
    """
    #print("IaCT")
    with urllib.request.urlopen(f"https://docs.aws.amazon.com/AWSCloudFormation/latest/UserGuide/{resource}") as response:
        html=response.read()
        count = 0
        for property in re.findall(r'(.*">)([A-Za-z0-9]+)(</a>" : .*)', html.decode('utf-8')):
            print("\t\t", count, property[1])
            count+=1

if __name__ == "__main__":
    get_service()