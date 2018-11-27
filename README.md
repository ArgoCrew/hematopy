hematopy 
==============================
[![Build Status](https://travis-ci.org/ArgoCrew/hematopy.svg?branch=master)](https://travis-ci.org/ArgoCrew/hematopy)


## Features

- Generate `png`, `pdf`, `ps` and `svg` Banner from a `SVG` template
- Upload generated banners to [Google Cloud Storage]()
- RestFul API


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
  -rbt, --recipient-bloodtype [A+|A-|B+|B-|AB+|AB-|O+|O-]
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
  -o, --output TEXT               Path and file name to output. Ex.:
                                  gs://bucket-name/banner-name.png
                                  ./bannername.png
  --help                          Show this message and exit.
```


## RestFul API

### Create a new donation

```
curl --request POST \
     --url https://hematopy-dev-gustavorps.herokuapp.com/api/v1/donations \
     --header 'Content-Type: multipart/form-data' \
     --form 'type=BloodDonation \
     --form 'recipient_image=@/path/to/image/on/your/computer.png' \
     --form 'recipient_name=JOSÉ MARIA PEREIRA SOUZA ARUDINO DO SANTOS' \
     --form 'recipient_bloodtype=A+' \
     --form 'location_name=Hemoes' \
     --form 'location_address_street=Av. Mal. Campos' \
     --form 'location_address_number=1468' \
     --form 'location_address_district=Nazareth' \
     --form 'location_address_locality=Vitória' \
     --form 'location_address_region=ES' \
     --form 'location_address_postal_code=29047-100'
```

## Development

### Setup

1. Clone
    ```
    $ git clone <REPO_FORK_URL>
    ```

2. Install
    ```
    $ pip install -e .
    ```

3. Set environment variables
    **Linux**
    ```
    $ export GOOGLE_APPLICATION_CREDENTIALS=PATH/TO/APPLICATION/CREDENTIALS.json
    $ export HEMATOPY__CORE__IMG_DST_GCS=gs://YOUR_BUCKET/IMAGES/DESTINATION/DIRECTORY
    ```



### Testing

```
$ python -m unittest
```


### Services

- https://travis-ci.org/ArgoCrew/hematopy

### References

- https://github.com/kvas-it/pytest-console-scripts

## Contributors

Thanks goes to these wonderful people ([emoji key](https://github.com/kentcdodds/all-contributors#emoji-key)):

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore -->
| [<img src="https://avatars1.githubusercontent.com/u/6784777?v=4" width="100px;"/><br /><sub><b>Mikael Hadler</b></sub>](http://mikaelhadler.com.br)<br />[💻](https://github.com/ArgoCrew/Hematopy/commits?author=mikaelhadler "Code") [📖](https://github.com/ArgoCrew/Hematopy/commits?author=mikaelhadler "Documentation") |
| :---: |
<!-- ALL-CONTRIBUTORS-LIST:END -->

This project follows the [all-contributors](https://github.com/kentcdodds/all-contributors) specification. Contributions of any kind welcome!