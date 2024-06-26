import smtplib, ssl
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from jinja2 import Template
class MailService:
    def __init__(self):
        self.port = 587
        self.smtp_server = "smtp.gmail.com"
        self.sender_email = "fatiyasalsabila83@gmail.com"
        self.password = "auajfbvkjwzimaos"
        with open("./res/undangan.html", "r") as file:
            template_str = file.read()
        self.jinja_template = Template(template_str)

    def send_email_undangan(self, subject='', data={}, receiver_email=''):
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = self.sender_email
        msg['To'] = receiver_email
        email_content = self.jinja_template.render(data)
        msg.attach(MIMEText(email_content, "html"))
        context = ssl.create_default_context()

        with smtplib.SMTP(self.smtp_server, self.port) as server:
            server.ehlo()
            server.starttls(context=context)
            server.ehlo()
            server.login(self.sender_email, self.password)
            server.sendmail(self.sender_email, receiver_email, msg.as_string())

    def send_email(self, subject='', body='', receiver_email=''):
        msg = MIMEMultipart()
        msg['Subject'] = subject
        msg['From'] = self.sender_email
        msg['To'] = receiver_email
        email_content = body
        msg.attach(MIMEText(email_content, "html"))
        context = ssl.create_default_context()

        try:
            with smtplib.SMTP(self.smtp_server, self.port) as server:
                server.ehlo()
                server.starttls(context=context)
                server.ehlo()
                server.login(self.sender_email, self.password)
                server.sendmail(self.sender_email, receiver_email, msg.as_string())
                print(f"Email sent to {receiver_email}")
        except Exception as e:
            print(f"Failed to send email to {receiver_email}: {e}")
            raise