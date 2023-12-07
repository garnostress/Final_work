import os
from sys import platform


def exists_file(command: str):
    if os.path.exists(".env"):
        try:
            os.system(command)
        except KeyboardInterrupt:
            print("Complete")
    else:
        print("File <.env> is missing")
        anserw_env = input("Type 'Yes' to create the file and install dependencies: ")

        if anserw_env.upper() == 'YES':
            secret = input('Enter the secret SECRET_KEY=')
            debug = input('Specify True to enable debug mode, False to disable it DEBUG=')
            db_name = input('DB_NAME=')
            db_user = input('DB_USER=')
            db_pass = input('DB_PASSWORD=')
            db_host = input('DB_HOST=')
            db_port = input('DB_PORT=')

            env_write = (f'SECRET_KEY={secret}\n'
                         f'DEBUG={debug}\n'
                         f'DB_ENGINE=django.db.backends.postgresql\n'
                         f'DB_NAME={db_name}\n'
                         f'DB_USER={db_user}\n'
                         f'DB_PASSWORD={db_pass}\n'
                         f'DB_HOST={db_host}\n'
                         f'DB_PORT={db_port}')

            with open('.env', 'w') as files_env:
                files_env.write(env_write)


def run():
    if platform == "linux" or platform == "linux2":
        exists_file("python3 manage.py runserver")
    elif platform == "win32":
        exists_file("python manage.py runserver")


if __name__ == '__main__':
    run()
