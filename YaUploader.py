import requests
class YaUploader:
    def __init__(self, token: str):
        self.token = token

    def upload(self, file_path: str,filename):
        headers = {
            'Content-Type': 'application/json',
            'Authorization': 'OAuth {}'.format(self.token)                
        }
        upload_url = 'https://cloud-api.yandex.net/v1/disk/resources/upload'
        pararms = {"path" : file_path ,"overwrite" : "true"}
        response = requests.get(upload_url,headers=headers,params=pararms)
        response_data = response.json()
        print(response_data)
        url_to_upload = response_data["href"]
        response1 = requests.put(url_to_upload,data=open(filename,'rb'))

if __name__ == '__main__':
    # Получить путь к загружаемому файлу и токен от пользователя
    path_to_file = 'text.txt'
    token = ...
    uploader = YaUploader(token)
    result = uploader.upload(path_to_file,'test.txt')