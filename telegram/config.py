import csv

token = '6118793699:AAFgCEaIcW15jT-idZVptU6K25cngmilAEk'
path_user_id = '/Users/valeriiastartseva/My_projects/VovaBetsBot/user_id.csv'
path_excel = '/Users/valeriiastartseva/My_projects/VovaBetsBot/Bets_DB_Telegram.xlsx'
path_data_for_header = '/Users/valeriiastartseva/My_projects/VovaBetsBot/infromation_for_header.csv'
path_mail = '/Users/valeriiastartseva/My_projects/VovaBetsBot/login_to_mail.csv'


with open(path_user_id, 'r') as f:  # looking for user_id for sending mails to telegram bot
    reader = csv.reader(f)
    rows = list(reader)
    last_row = rows[-1]
user_id = str(last_row[0])



