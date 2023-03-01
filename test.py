import requests
from lxml import html
import mysql.connector

session = requests.Session()

url = "https://www.random-name-generator.com/united-states?s={offset}&gender=&n=10"

mydb = mysql.connector.connect(
    port="6633",
    user="root",
    password="dangduong020309",
    database="mydb"
)
new_database = mydb.cursor()
insert_table = "CREATE TABLE user (id int auto_increment primary key, random_address varchar(255)," \
               "phone_number varchar(255), ssn varchar(255), email varchar(255), ip varchar(255)," \
               "username varchar(255), password varchar(255), credit_card_no varchar(255), " \
               "expiration_date varchar(255)," \
               "iban varchar(255), swift_bic_number varchar(255), company varchar(255))"

new_database.execute(insert_table)


def remove_blank(data: list):
    results = []
    for item in data:
        if item.strip():
            results.append(item.strip().replace('\n', ', '))
    return results


for i in range(2):
    try:
        resp = session.get(url=url.format(offset=i + 1))
        tree = html.fromstring(resp.text)
        list_info = tree.xpath('//div[@class="media-body"]')
        for info in list_info:
            addr = info.xpath('.//dd[@class="col-sm-8"]//text()')
            addr = remove_blank(list(addr))
            sql = "INSERT INTO user(random_address,phone_number,ssn,email,ip,username,password,credit_card_no,expiration_date" \
                  ",iban,swift_bic_number,company) VALUES(%s, %s, %s, %s, %s, %s, %s, %s, %s,%s,%s,%s)"
            new_database.execute(sql, addr)
            mydb.commit()
    except Exception as e:
        print(e)


print(new_database.rowcount, "successfully")

