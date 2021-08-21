import requests




def main():     
    url = input("Enter Webhook Url : ")                                  
    username = input("Enter Webhook username : ")                      
    picture = input("Enter Webhook Avatar Url : ")                   
    message = input("Enter the message you want to send : ")              
    data = {"content":message,"username":username,"avatar_url":picture}   
    r = requests.post(url,data=data)                                 
    if r.status_code == 204:                                        
        print("Message Sent Successfully ! 👌")
    else :
        print("Message Not Sent")

        
        
        
main()   #calling the function
