# DISCORD WEBHOOKS(EMBEDS)
Apart from sending simple messages , webhooks are capable of sending rich/beautiful embeds and all you require is requests module.<br/>
 In the python file I haven't shown you the full webhook structure, I will cover that part here.<br/>

you can add another key value pair in the current "data" dictionary or you can move to the next line and type data["embeds"] = [{add structure here}] <br/>
![alt text](https://confighub.photos/images/1BNe9tOFqLElVBAEd7IXVfBKv.png)




# List of all Key Value Pairs needed (comma seperated)
```py
"username"   : "Webhook"
"avatar_url" : "enter link here "
"content"    : "Text message. LIMIT:  2000 characters."
"author": {
                    "author":{"name":"Sensei.Qt",<br/>
                    "url":"Enter url here",    #this will create a hyperlink on the authors name 
                    "icon_url":" Enter icon url here "
            }
"title" : "This is a test Title"
"url" : " Enter url here"             #this will create a hyperlink in the embed title
"description" : "This is a Test Description"
"color" : 0x00fefe  # use colour hex here but change # to 0x  For example : #00fefe to 0x00fefe
"fields" : [
        {
          "name" : "enter name here",
          "value" : "Enter value here",
          "inline" : True
        },
        {
          "name" : "Enter another name ",
          "value" : "Enter another value",
          "inline" : True
        }
      
"thumbnail" : {"url":"emter url for the small image on top right corner of embed"},
"image" : {"url":"enter url for the large image on the embed"},
"footer":{"text":"Cute Footer","icon_url":"enter url for the bottom left small image on the embed"},
"timestamp": "2021-08-21T12:00:00.000Z"
```
