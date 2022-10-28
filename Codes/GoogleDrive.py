from pydrive2.auth import GoogleAuth
from pydrive2.drive import GoogleDrive

directorio_credenciales= 'credentials_module.json'

def login(): 
    gauth = GoogleAuth()
    gauth.LoadCredentialsFile(directorio_credenciales)

    if gauth.access_token_expired:
        gauth.Refresh()
        gauth.SaveCredentialsFile(directorio_credenciales)
    else: 
        gauth.Authorize()

    return GoogleDrive(gauth)


def subir_archivo(ruta_archivo, id_folder):
    credenciales= login()
    archivo = credenciales.CreateFile({'parents' : [{'id':id_folder}]})
    archivo['title']= ruta_archivo.split('/')[-1]
    archivo.SetContentFile(ruta_archivo)
    archivo.Upload()


def upload_to_google_drive1(file, id_folder):
    credenciales= login()
    file_list = credenciales.ListFile({'q': "'1imezwaXGGBbW5wuXusiFwrEee8U8_R73' in parents"}).GetList()  #root
    try:
        for file1 in file_list:
            if file1['title'] == file:
                file1.Delete()
    except:
        pass
    f = credenciales.CreateFile({'parents' : [{'id':id_folder}]})
    f.SetContentFile(file)
    f.Upload()


if __name__== '__main__':
    #subir_archivo('prueba.csv', '1_j8ac613VzwnKQRZT23EU-BQ--8MFpH1')
    #upload_to_google_drive1('prueba.csv')
    upload_to_google_drive1('prueba.csv','1imezwaXGGBbW5wuXusiFwrEee8U8_R73' )