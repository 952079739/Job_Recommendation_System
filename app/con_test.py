from app.connet import upload, send_data


# upload(host='39.96.2.158', port=22, username='root', password='Liwanyang1945')
ste, std = send_data(host='39.96.2.158', port=22, username='root', password='Liwanyang1945')
print(ste, std)

