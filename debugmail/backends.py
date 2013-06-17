from django.conf import settings
from django.core.mail.backends.smtp import EmailBackend


class DebugEmailBackend(EmailBackend):
    def send_messages(self, email_messages):
        for email in email_messages:
            email.subject = u"{0} [To: {1} Cc: {2} Bcc: {3}]".format(
                email.subject,
                u', '.join(email.to),
                u', '.join(email.cc),
                u', '.join(email.bcc)
            )
            email.to = [admin[1] for admin in settings.ADMINS]
            email.cc = []
            email.bcc = []
        super(DebugEmailBackend, self).send_messages(email_messages)
