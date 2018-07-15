hematopy
==============================

## Getting Started

### Development


```
git clone git@github.com:ArgoCrew/hematopy.git

cd hematopy

pip install -e .
```


## CLI

### Start Server
```
hematopy serve
```

### Create a new donation banner

```
hematopy create donation
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