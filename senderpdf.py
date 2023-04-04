from email.mime.multipart import MIMEMultipart
import smtplib
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import os
import fitz


def overkill():
    pdf_files = []
    directory = './catalog/'
    for filename in os.listdir(directory):
        f = os.path.join(directory,filename)
        if os.path.isfile(f):
            pdf_files.append(f.split('/')[-1])
    for filename in pdf_files:
        if filename.split('.')[-1] == 'pdf':
            with fitz.Document(f'{directory}/{filename}') as doc:
                doc.save(f'./processed/done{filename}')
        else:
            print(f'WARNING: this file {filename} is not a pdf file')
    return pdf_files


def send_mail(msg, path_dir):
   # put your email here
   sender = 'solnishkoffanother@gmail.com'
   # get the password in the gmail (manage your google account, click on the avatar on the right)
   # then go to security (right) and app password (center)
   # insert the password and then choose mail and this computer and then generate
   # copy the password generated here
   password = os.getenv('EMAIL_PASSWORD')
   # put the email of the receiver here
   receiver = 'kaup.muz@gmail.com'
   #Setup the MIME
   message = MIMEMultipart()
   message['From'] = sender
   message['To'] = receiver
   message['Subject'] = 'This email has an attacment, a pdf file'

   message.attach(MIMEText(msg, 'plain'))

   for pdfname in overkill():
      pdfname = path_dir + pdfname

      # open the file in bynary
      binary_pdf = open(pdfname, 'rb')

      payload = MIMEBase('application', 'octate-stream', Name=pdfname)
      # payload = MIMEBase('application', 'pdf', Name=pdfname)
      payload.set_payload((binary_pdf).read())

      # enconding the binary into base64
      encoders.encode_base64(payload)

      # add header with pdf name
      payload.add_header('Content-Decomposition', 'attachment', filename=pdfname)
      message.attach(payload)

   #use gmail with port
   session = smtplib.SMTP('smtp.gmail.com', 587)

   #enable security
   session.starttls()

   #login with mail_id and password
   session.login(sender, password)

   text = message.as_string()
   session.sendmail(sender, receiver, text)
   session.quit()


def main():
   send_mail('Take this shit pdf','./catalog/1/')


if __name__ == '__main__':
   main()