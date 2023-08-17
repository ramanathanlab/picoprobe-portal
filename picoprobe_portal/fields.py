from urllib.parse import urlunsplit

def title(result):  
    return result[0]['dc']['titles'][0]['title']
    
def display_image(result):
    path = result[0]['hyperspectral_image'].replace('/lus/eagle/projects/APSDataAnalysis/PICOPROBE/','')
    new_url = urlunsplit(("https","g-ea1c3.fd635.8443.data.globus.org", path, "", ""))
    return new_url
