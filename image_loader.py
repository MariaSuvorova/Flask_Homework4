import os
import requests
from time import time


class ImageLoader():

    def get_image_from_url(url: str, path_to_save: str = './images/') -> None:
        start_time = time()

        url_without_request = url[:url.find('?')] if url.count('?') else url
        file_name_with_extension = url_without_request[url.rfind('/') + 1:]
        root, ext = os.path.splitext(file_name_with_extension)
        ext = ext if ext else '.jpg'
        os.makedirs(os.path.abspath(path_to_save), exist_ok=True)
        file_path = os.path.join(os.path.abspath(path_to_save), f'{root}{ext}')

        with open(file_path, 'wb') as f:
            data = requests.get(url).content
            f.write(data)

        # print(f'{file_path} загружен за {time() - start_time:.2f} сек')
        print(f'за {time() - start_time:.2f} сек загружен {root}{ext}')

    async def async_get_image_from_url(url: str, path_to_save: str = './images/') -> None:
        start_time = time()
        url_without_request = url[:url.find('?')] if url.count('?') else url
        file_name_with_extension = url_without_request[url.rfind('/') + 1:]
        root, ext = os.path.splitext(file_name_with_extension)
        ext = ext if ext else '.jpg'
        os.makedirs(os.path.abspath(path_to_save), exist_ok=True)
        file_path = os.path.join(os.path.abspath(path_to_save), f'{root}{ext}')

        with open(file_path, 'wb') as f:
            data = requests.get(url).content
            f.write(data)

        # print(f'{file_path} загружен за {time() - start_time:.2f} сек')
        print(f'за {time() - start_time:.2f} сек загружен {root}{ext}')
