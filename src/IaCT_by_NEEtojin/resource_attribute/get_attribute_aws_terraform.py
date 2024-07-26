import re
import urllib.request

def get_service():
    pass

def get_resource(service: str = "ec2"):
    get_attribute(service)

def get_attribute(resource: str = "instance"):
    url = f"https://github.com/hashicorp/terraform-provider-aws/blob/main/website/docs/d/instance.html.markdown?plain=1https://github.com/hashicorp/terraform-provider-aws/blob/main/website/docs/d/{resource}.html.markdown?plain=1"
    with urllib.request.urlopen(url) as response:
        html = response.read()
        #print(html.decode('utf-8')); return;
        for argument in re.findall(r'([<p dir="auto">|<li>]<code>)([a-z_]+)(</code> -)', html.decode('utf-8')):
            if argument[1] == 'ru':
                continue
            print(argument[1])

if __name__ == "__main__" :
    get_attribute()