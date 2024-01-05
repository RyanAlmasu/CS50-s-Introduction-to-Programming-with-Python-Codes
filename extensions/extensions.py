user = input("File name: ")

new_user = user.lower()

if '.gif' in new_user:
    print("image/gif")
elif '.jpg' in new_user:
    print("image/jpeg")
elif '.jpeg' in new_user:
    print("image/jpeg")
elif '.pdf' in new_user:
    print("application/pdf")
elif '.zip' in new_user:
    print("application/zip")
elif '.png' in new_user:
    print("image/png")
elif '.txt' in new_user:
    print("text/plain")
else:
    print("application/octet-stream")