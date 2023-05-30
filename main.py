import os
import sys

def find_private_keys(wallet_file, private_key_file, target_file, output_file):
    # Определение абсолютного пути к файлам
    script_dir = os.path.dirname(os.path.abspath(sys.argv[0]))
    wallet_file_path = os.path.join(script_dir, wallet_file)
    private_key_file_path = os.path.join(script_dir, private_key_file)
    target_file_path = os.path.join(script_dir, target_file)
    output_file_path = os.path.join(script_dir, output_file)

    # Чтение адресов кошельков из файла wallets.txt
    with open(wallet_file_path, 'r') as f:
        wallets = [line.strip() for line in f.readlines()]

    # Чтение приватных ключей из файла priv.txt
    with open(private_key_file_path, 'r') as f:
        private_keys = [line.strip() for line in f.readlines()]

    # Чтение целевых адресов из файла 2wall.txt
    with open(target_file_path, 'r') as f:
        target_wallets = [line.strip() for line in f.readlines()]

    # Поиск соответствующих приватных ключей для целевых адресов
    found_private_keys = []
    for target_wallet in target_wallets:
        try:
            index = wallets.index(target_wallet)
            found_private_keys.append(private_keys[index])
        except ValueError:
            pass

    # Запись найденных приватных ключей в файл final.txt
    with open(output_file_path, 'w') as f:
        f.write('\n'.join(found_private_keys))


# Укажите названия файлов
wallet_file = 'wallets.txt'
private_key_file = 'priv.txt'
target_file = '2wall.txt'
output_file = 'final.txt'

# Вызов функции для поиска и записи приватных ключей
find_private_keys(wallet_file, private_key_file, target_file, output_file)