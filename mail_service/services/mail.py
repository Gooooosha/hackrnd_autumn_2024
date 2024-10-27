import os
from pathlib import Path
from jinja2 import Template
from typing import Any, Dict
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from aiosmtplib import SMTP
from shared.utils.enums.mail_types_enum import MailTypes

from dotenv import load_dotenv
load_dotenv()


class EmailService:
    def __init__(self, template_dir: str = "email_templates"):
        self.template_dir = template_dir

    @staticmethod
    def get_mail_template(mail_type: MailTypes) -> str:
        return mail_type.value

    def render_email_template(self,
                              template_name: str,
                              context: Dict[str, Any]) -> str:
        template_str = (
            Path(__file__).parent.parent / self.template_dir / template_name
        ).read_text(encoding="utf-8")
        html_content = Template(template_str).render(context)
        return html_content

    async def send_mail(self,
                        recipient: str,
                        subject: str,
                        context: Dict[str, Any],
                        mail_type: MailTypes) -> bool:
        template_name = self.get_mail_template(mail_type)
        html_content = self.render_email_template(template_name=template_name,
                                                  context=context)

        message = MIMEMultipart()
        message["From"] = os.getenv("SMTP_USER")
        message["To"] = recipient
        message["Subject"] = subject
        message.attach(MIMEText(html_content, "html"))

        smtp_client = SMTP(hostname=os.getenv("SMTP_SERVER"),
                           port=os.getenv("SMTP_PORT"),
                           use_tls=True)
        try:
            async with smtp_client:
                await smtp_client.login(os.getenv("SMTP_USER"),
                                        os.getenv("SMTP_PASSWORD"))  # noqa
                await smtp_client.send_message(message)
                return True
        except Exception as e:
            print(e)
            return False
