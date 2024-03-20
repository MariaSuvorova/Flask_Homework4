import argparse

def reader(file_name)-> list:
    with open(file_name) as f:
        return f.readlines()
    
    
def url_parser():
    parser = argparse.ArgumentParser(description='Получение списка URL адресов')
    parser.add_argument('-l',
                        '--list',
                        default=None,
                        help='URL адреса изображений через запятую.')
    parser.add_argument('-f',
                        '--file',
                        default='./images.txt',
                        help='файл с URL адресами изображений.')
    lst = parser.parse_args().list
    file = parser.parse_args().file
    url_list = []
    if lst:
        url_list.extend([i.strip().replace('\n', '') for i in lst.split(',')])
    if file:
        url_list.extend([i.strip().replace('\n', '') for i in reader(file)])

    return url_list


