
from django.conf import settings
from django.template.loader import render_to_string
from mailjet_rest import Client


def send_welcome_email(email, username):


    mailjet = Client(
        auth=(
            settings.MAILJET_API_KEY,
            settings.MAILJET_SECRET_KEY,
        ),
        version='v3.1',
    )

    html_content = render_to_string(
        'accounts/email-greeting.html',
        {
            'username': username,
        },
    )

    data = {
        'Messages': [
            {
                'From': {
                    'Email': 'dragomirdragovzhelev8@gmail.com',
                    'Name': 'Petstagram',
                },
                'To': [
                    {
                        'Email': email,
                        'Name': username,
                    }
                ],
                'Subject': 'My first Mailjet Email!',
                'TextPart': 'Greetings from Mailjet!',
                'HTMLPart': html_content,
            }
        ]
    }

    result = mailjet.send.create(data=data)

    print('MAILJET STATUS:', result.status_code)
    print('MAILJET RESPONSE:', result.json())

    return result