import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
import os


def send_mail(workflow_name, repo_name, workflow_run_id):
    # Email details
    sender_mail = os.getenv("SENDER_MAIL")
    sender_password = os.getenv("SENDER_PASSWORD")
    receiver_mail = os.getenv("RECEIVER_MAIL")

    #email content
    subject = f"Workflow {workflow_name}  failed for repo {repo_name}"
    body = f"The workflow {workflow_name} failed for the repository {repo_name}. Please check the logs for more details. \n more details: \n Run_Id: {workflow_run_id}"


    msg= MIMEMultipart()
    msg['From']  = sender_mail
    msg['To'] = receiver_mail
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    try: 
        server = smtplib.SMTP('smtp.gmail.com',587)
        server.starttls()
        server.login(sender_mail, sender_password)
        text = msg.as_string()
        server.sendmail(sender_mail, receiver_mail, text)
        server.quit()
        print(f"mail successfully send to the {receiver_mail}")
    
    except Exception as e:
        print(f"Error: {e}")



send_mail(os.getenv("WORKFLOW_NAME"), os.getenv("REPO_NAME"), os.getenv("WORKFLOW_RUN_ID"))
