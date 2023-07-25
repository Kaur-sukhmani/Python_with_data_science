# Watsapp contact list
contacts = [
    {
        "name": "John",
        "phone": "98239344",
        "conversation": [
            "fi",
            "hello",
            "dfjss"
        ]
    },
    {
        "name": "fionna",
        "phone": "9823934544",
        "conversation": [
            "hi",
            "hello ji",
            "kaise ho "
        ]

    },
    {
        "name": "sukh",
        "phone": "982394344",
        "conversation": [
            "heya",
            "I am good",
            "Hows your day ho "
        ]

    }
]
search_keyword = input("enter keyword to search ")
print("search keyword", search_keyword)

for contact in contacts:
    #     if contacts["name"].lower().startswith(search_keyword.lower()):
    #         if contacts["name"].lower().__contains__(search_keyword.lower()): #return t/f
    if contact["name"].lower().find(search_keyword.lower()) >= 0 \
            or contact["phone"].find(search_keyword) >= 0:
        print(contact)
        print("===============")
    else:
        for message in contact["conversation"]:
            if message.lower().find(search_keyword.lower()) >= 0:
                print(contact)
                print("===============")


# search implementation on conversation as well
