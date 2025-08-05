class EmailNotification:
    def send(self, message):
        print(f"[EMAIL] Sending email with message: {message}")


class SMSNotification:
    def send(self, message):
        print(f"[SMS] Sending SMS with message: {message}")


def send_bulk(notifiers, message):
    for notifier in notifiers:
        notifier.send(message)



if __name__ == "__main__":
    email = EmailNotification()
    sms = SMSNotification()

    notifiers = [email, sms]

    send_bulk(notifiers, "This is your alert!")
