from mail_service.services.mail import EmailService
from shared.utils.enums.mail_types_enum import MailTypes
from shared.schemas.auth import AuthCode
from shared.schemas.user_request import UserRequest

async def main():
    email_service = EmailService()
    context = AuthCode(code="1234")
    await email_service.send_mail(recipient="ups1deggwp@gmail.com",
                                  subject="Вход в аккаунт",
                                  context=context.model_dump(),
                                  mail_type=MailTypes.AUTH_CODE)
    
    user_request = UserRequest(contract_number="516902123",
                               first_name="1",
                               last_name="3",
                               middle_name="2",
                               phone_number="+79901234795",
                               description="Изменился тариф")
    
    await email_service.send_mail(recipient="ups1deggwp@gmail.com",
                                  subject="Уведомление о запросе пользователя",
                                  context=user_request.model_dump(),
                                  mail_type=MailTypes.USER_REQUEST)

if __name__ == "__main__":
    import asyncio
    asyncio.run(main())