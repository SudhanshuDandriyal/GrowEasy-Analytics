import smtplib
import os
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage

def send_report(email, report_path, insights_path):
    msg = MIMEMultipart()
    msg['From'] = os.getenv('EMAIL_USER', 'your_email@gmail.com')
    msg['To'] = email
    msg['Subject'] = '📊 Your Monthly Sales Report - GrowEasy Analytics'

    # Read insights from file
    with open(insights_path, 'r') as f:
        insights_text = f.read()

    # Add HTML email body
    body = f"""
    <html>
    <body>
        <h2>🚀 Your Monthly Sales Report</h2>
        <p>Dear Business Owner,</p>
        <p>Here are your key sales insights:</p>
        <pre>{insights_text}</pre>
        <p>Find your sales trend report attached.</p>
        <p><strong>GrowEasy Analytics</strong> is here to help you optimize sales! 📈</p>
    </body>
    </html>
    """
    msg.attach(MIMEText(body, 'html'))

    # Attach sales trend image
    with open(report_path, 'rb') as f:
        img = MIMEImage(f.read())
        img.add_header('Content-Disposition', 'attachment', filename="sales_report.png")
        msg.attach(img)

    # Send email
    with smtplib.SMTP('smtp.gmail.com', 587) as server:
        server.starttls()
        server.login(os.getenv('EMAIL_USER', 'your_email@gmail.com'), os.getenv('EMAIL_PASS', 'your_app_password'))
        server.send_message(msg)
