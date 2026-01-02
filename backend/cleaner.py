import re
def clean_text(t):
    t=re.sub(r'\s+',' ',t)
    return re.sub(r'[^A-Za-z0-9., ]+','',t)
