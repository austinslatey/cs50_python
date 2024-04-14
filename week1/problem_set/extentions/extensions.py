def get_media_type(filename):
    lowercase_filename = filename.strip().lower()

    if lowercase_filename.endswith(".gif"):
        return "image/gif"
    elif lowercase_filename.endswith(".jpg") or lowercase_filename.endswith(".jpeg"):
        return "image/jpeg"
    elif lowercase_filename.endswith(".pdf"):
        return "application/pdf"
    elif lowercase_filename.endswith(".txt"):
        return "text/plain"
    elif lowercase_filename.endswith(".zip"):
        return "application/zip"
    elif lowercase_filename.endswith(".png"):
        return "image/png"
    else:
        return "application/octet-stream"

user_filename = input("Enter the file name: ")
media_type = get_media_type(user_filename)
print(media_type)

