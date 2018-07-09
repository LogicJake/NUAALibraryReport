import time
from main import request_html, get_data_from_response, save_to_mysql
from common import Global

def patch():
    Global.__init__()
    with open('nohup.out', 'r', encoding='UTF-8') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip('\n')
            if line.__len__() == 9:
                stuno = line
                response = request_html(stuno)
                data = []
                if response != -1:
                    data.append(get_data_from_response(stuno, response))
                    save_to_mysql(int(stuno[2:4]), data)
                    data.clear()
                time.sleep(0.3)


if __name__ == '__main__':
    patch()