def normalize_text(text:str):
    text = text.str.lower() # lowercase
    text = text.str.replace(r"\#","") # replaces hashtags
    text = text.str.replace(r"http\S+","URL")  # remove URL addresses
    text = text.str.replace(r"@","") # Remove @
    #text = text.str.replace(r"[^A-Za-z0-9()!?\'\`\"]", " ") uncomment to remove also accent and numbers
    text = text.str.replace("\s{2,}", " ")
    return text