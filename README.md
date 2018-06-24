hematopy
==============================


## CLI

### Create a new banner

```
python -m src.haemapy.banner.cli create
```

curl \
  -F "user_id=1" \
  -F "image=@./assets/recipient-photo.jpg" \
  localhost:8000/api/v1/media_objects


curl -i \
    -H "Accept: application/json" \
    -H "X-HTTP-Method-Override: PUT" \
    -X POST -d "value":"30","type":"Tip 3","targetModule":"Target 3","configurationGroup":null,"name":"Configuration Deneme 3","description":null,"identity":"Configuration Deneme 3","version":0,"systemId":3,"active":true \
    localhost:8000/api/v1/media_objects