# DISCORD WEBHOOKS(EMBEDS)
Apart from sending simple messages , webhooks are capable of sending rich/beautiful embeds and all you require is requests module.<br/>
 In the python file I haven't shown you the full webhook structure, I will cover that part here.<br/>

you can add another key value pair in the current "data" dictionary or you can move to the next line and type data["embeds"] = [{add structure here}] <br/>
![alt text](https://confighub.photos/images/1BNe9tOFqLElVBAEd7IXVfBKv.png)




# List of all Key Value Pairs needed (comma seperated)
"username"   : "Webhook"<br/>
"avatar_url" : "enter link here "<br/>
"content"    : "Text message. LIMIT:  2000 characters."<br/>
"author": {<br/>
                    "author":{"name":"Sensei.Qt",<br/>
                    "url":"Enter url here",    #this will create a hyperlink on the authors name <br/>
                    "icon_url":" Enter icon url here "<br/>
            }<br/>
"title":"This is a test Title"<br/>
"url":" Enter url here"             #this will create a hyperlink in the embed title<br/>
"description":"**This is a Test Description**"<br/>
"color":0x00fefe<br/>
"fields": [<br/>
        {<br/>
          "name": "enter name here",<br/>
          "value": "Enter value here",<br/>
          "inline": true<br/>
        },<br/>
        {<br/>
          "name": "Enter another name ",<br/>
          "value": "Enter another value",<br/>
          "inline": true<br/>
        }<br/>
      
"thumbnail":{"url":"emter url for the small image on top right corner of embed"},<br/>
"image":{"url":"enter url for the large image on the embed"},<br/>
"footer":{"text":"Cute Footer","icon_url":"emter url for the bottom left small image on the embed"}<br/>
