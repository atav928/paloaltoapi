# Palo Alto Api

## Configuration Variables
Use environment variables for configurations:
sample:
```bash
export CERT='<path/to/cert'
export DOMAIN='example.com'
```
Default values are
CERT=False
DOMAIN=''

CERT Values can be True, False or a certifcate path. It is used as a value if one is not passed when connecting to Panorama or a Firewall. Defaults to no SSL Verification if not set.

