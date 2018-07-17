hematopy
==============================

## Instalation

### Git


```
git clone git@github.com:ArgoCrew/hematopy.git

cd hematopy

pip install -e .
```

### pip

```
pip install hematopy
```


## CLI

### Start Server
```
$ hematopy serve --help
Usage: hematopy serve [OPTIONS]

Options:
  -h, --host TEXT      Host name or IP 
                       Default: 0.0.0.0
  -p, --port INTEGER   Port to expose the service 
                       Default: 8000
  -d, --debug BOOLEAN  Output debug messages 
                       Default: True
  --help               Show this message and exit.
```

### Create a new donation banner

```
$ hematopy create donation --help
Usage: hematopy create donation [OPTIONS]

Options:
  -ri, --recipient-image PATH     Image of the person who need blood donation
  -rn, --recipient-name TEXT      The name of person who needs donation
  -rbt, --recipient-blood-type [A+|A-|B+|B-|AB+|AB-|O+|O-]
  -ln, --location-name TEXT       Name of location where the blood donation
                                  can be made
                                  Ex.: Hemoes
  -las, --location-address-street TEXT
                                  Street address of place where the blood
                                  donation can be made
  -lan, --location-address-number TEXT
                                  Post Office Box Number of place where the
                                  blood donation can be made
  -lad, --location-address-district TEXT
                                  Neighborhood or district of place where the
                                  blood donation can be made
  -lal, --location-address-locality TEXT
                                  City or Locality of place where the blood
                                  donation can be made
  -lar, --location-address-region TEXT
                                  State or Region of place where the blood
                                  donation can be made
  -lapc, --location-address-postal-code TEXT
                                  State or Region of place where the blood
                                  donation can be made
  -o, --output TEXT               Path and file name to output
  --help                          Show this message and exit.
```


## Web API

### Create a new donation

```
curl --request POST \
  --url https://hematopy-dev-gustavorps.herokuapp.com/api/v1/donations \
  --header 'Content-Type: multipart/form-data' \
  --form 'recipient_image=@/path/of/recipient_image.jpg' \
  --form 'recipient_name=JOSÉ MARIA PEREIRA SOUZA ARUDINO DO SANTOS' \
  --form 'recipient_blood_type=A+' \
  --form 'location_name=Hemoes' \
  --form 'location_address_street=Av. Mal. Campos' \
  --form 'location_address_number=1468' \
  --form 'location_address_district=Nazareth' \
  --form 'location_address_locality=Vitória' \
  --form 'location_address_region=ES' \
  --form 'location_address_postal_code=29047-100'
```