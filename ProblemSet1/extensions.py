#File extension decoder
filename = input("What is your file type? ").strip().lower()

#File types
types = {
    "gif": "image/gif",
    "jpg": "image/jpeg",
    "jpeg": "image/jpeg",
    "png": "image/png",
    "pdf": "application/pdf",
    "txt": "text/plain",
    "zip": "application/zip"
}

#Split after last . otherwise the whole name will return
parts = filename.rsplit('.', 1)

#Check extention and match
if len(parts) == 2 and parts[1] in types:
    print(types[parts[1]])
else:
    print("application/octet-stream")