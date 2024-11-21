import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
def send_email(sender_email, sender_password, recipient_email, subject, body):
    try:
# Membuat pesan email
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = recipient_email
        msg['Subject'] = subject
# Menambahkan isi pesan
        msg.attach(MIMEText(body, 'plain'))
# Menghubungkan ke server SMTP (contoh: Gmail)
        server = smtplib.SMTP('smtp.gmail.com', 587)
        server.starttls() # Mengamankan koneksi
        server.login(sender_email, sender_password)
# Mengirim email
        server.sendmail(sender_email, recipient_email, msg.as_string())
        print("Email berhasil dikirim!")
# Menutup koneksi ke server SMTP
        server.quit()
    except Exception as e:
        print(f"Terjadi kesalahan: {e}")
 
# Contoh penggunaan
sender_email = ""
sender_password = ""
recipient_email = "rometdomuzawi@gmail.com"
subject = "Justyn 2155202073 Quiz 2"
body = "Justyn Anthonyo TM21-2 2155202073 Quiz 2"

send_email(sender_email, sender_password, recipient_email, subject, body)
