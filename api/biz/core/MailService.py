from api.biz.utils.utility_functions import *

class MailService:
    """
    implementatio of a dummy mail service
    sent message il only logged to the stdout    
    """
    def __init__(self) -> None:
        pass
    
    def send(self, recipient: str, subject: str, body: str) -> None:
        """
        for simplicity reasons send handles only a subset of
        typical mail parameters. In a real implementation a Mail object
        should be provided
        """

        message = f"""
            *********************************************************
            **************** FAKE MAIL SERVICE **********************
            recipient: {recipient}
            subject: {subject}
            body: {body}
            *********************************************************
        """.format(recipient=recipient, subject=subject, body=body)

        print_to_stdout(message);
        
    