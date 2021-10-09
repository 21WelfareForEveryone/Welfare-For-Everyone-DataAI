from mysql.connector.constants import ClientFlag

DATABASE_CONFIG = {
    'user': 'root',
    'password': '1357',
    'host': '34.64.116.88',
    'client_flags': [ClientFlag.SSL],
    'ssl_ca': 'server-ca.pem',
    'ssl_cert': 'client-cert.pem',
    'ssl_key': 'client-key.pem',
    'database' : 'welfare-for-everyone'
}