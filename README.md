# Palo Alto Api

## Configuration Variables
Use environment variables for configurations:
sample:
```bash
export CERT='<path/to/cert'
export DOMAIN='example.com'
```
Default values are:

* CERT=False
* DOMAIN=''

CERT Values can be True, False or a certifcate path. It is used as a value if one is not passed when connecting to Panorama or a Firewall. Defaults to no SSL Verification if not set.

## Sample Usage

Sample usages between the different classes and how to use them.

### URL Class

The URL class gives the abilty to search for custom URL Categories and be able to add or remove items from a list.

Here is a sample of just being able to retrieve the information.

```python
import os
from paloaltoapi.device_groups.objects.urlcategory.url_categories import UrlCategories
 
CERT = os.getenv("CERT", None)
if not CERT:
    CERT = False
url = UrlCategories(device='panorama.com', api_key="<api-token>", certstore=CERT) # you can also specify username and password instead to auto populate the token
 
category_list = url.list_url_category(name='custom-category-name', device_groups='Internet')
 
"""
returns formatted list in JSON format
[{'@name': 'custom-category-name', '@location': 'device-group', '@device-group': 'Internet', '@loc': 'Internet', 'list': {'member': ['google.com', '^.google.com', 'ec2.^.amazonaws.com]}, 'type': 'URL List'}]
 
With this list you can extract the members and add remove or manipulate the members in the URL Custom Category
"""
```

### Address Group Class

This class allows us to look search and edit an address group and the location it is in Panorama. Similar work can be done within the Address Class that allows you to adjust, add, or remove addresses.

```python
import os
from paloaltoapi.device_groups.objects.address_groups import AddressGroups
 
CERT = os.getenv("CERT", None)
if not CERT:
    CERT = False

addr_grp = AddressGroups(device='panorama.com', api_key="<api-token>", certstore=CERT)

address_group_list = addr_grp.list_address_group(address_grp='grp-ext-crl-microsoft',location='Internet')
 
print(address_group_list)
"""
Returns a list of the address group name specified like:
['ext-hst-crl.microsoft.com-1', 'ext-hst-crl.microsoft.com-2', 'ext-hst-crl.microsoft.com-3']
"""
 
list_address_groups = addr_grp.get_address_group_by_name(address_groups=['grp-ext-crl-microsoft','grp-ext-ms-updates'])
print(list_address_groups)
"""
searches for the address groups and lists out all the values associated with each in a dictionary it does not specify the location; that needs to be adjusted
{
                'grp-ext-crl-microsoft': [
                                'ext-hst-crl.microsoft.com-1', 'ext-hst-crl.microsoft.com-2', 'ext-hst-crl.microsoft.com-3'
                                ],
                'grp-ext-ms-updates': [
                                'ext-net-akam', 'ext-net-ms2'
                ]
}
"""
 
```