import imaplib
import email
import requests
import time
import imgkit
import os

# Set the window name
window_name = "EatsKaz"

def send_telegram_message(image_path, bot_token, channel_id):
    try:
        url = f"https://api.telegram.org/bot{bot_token}/sendPhoto"
        data = {"chat_id": channel_id}
        with open(image_path, 'rb') as image:
            files = {'photo': image}
            response = requests.post(url, data=data, files=files)
            response.raise_for_status()
            return response.json()
    except requests.exceptions.RequestException as e:
        print(f"Failed to send message to Telegram: {str(e)}")
    except Exception as e:
        print(f"An error occurred while sending the message: {str(e)}")

def forward_emails(username, password, bot_token, channel_id, target_sender):
    try:
        mail = imaplib.IMAP4_SSL('imap.gmail.com')
        mail.login(username, password)
        mail.select("inbox")

        _, email_ids = mail.search(None, "(UNSEEN)")

        for email_id in email_ids[0].split():
            _, data = mail.fetch(email_id, "(BODY[])")
            raw_email = data[0][1]
            email_message = email.message_from_bytes(raw_email)

            # Print the From header to debug
            print("Email From:", email_message['From'])

            if target_sender in email_message['From']:
                body = ""
                for part in email_message.walk():
                    if part.get_content_type() == "text/plain":
                        body += part.get_payload(decode=True).decode('utf-8', 'replace')  # Replace non-decodable characters with question marks
                    elif part.get_content_type() == "text/html":
                        body += part.get_payload(decode=True).decode('utf-8', 'replace')  # Replace non-decodable characters with question marks

                if body:
                    screenshot_filename = f"screenshot_{email_id}.png"

                    try:
                        # Create a temporary HTML file
                        temp_html_filename = f"temp_email_{email_id}.html"
                        with open(temp_html_filename, 'w', encoding='utf-8') as html_file:
                            html_file.write(body)

                        # Generate the screenshot
                        imgkit.from_file(temp_html_filename, screenshot_filename, config=imgkit.config(wkhtmltoimage=r'C:\Program Files\wkhtmltopdf\bin\wkhtmltoimage.exe'))

                        # Remove the temporary HTML file
                        os.remove(temp_html_filename)

                        # Send the image with rate limiting
                        send_telegram_message(screenshot_filename, bot_token, channel_id)
                        time.sleep(1)  # Sleep for 1 second to respect the rate limit

                        # Remove the temporary image after sending
                        os.remove(screenshot_filename)

                        # Delete the email
                        mail.store(email_id, '+FLAGS', '(\Deleted)')
                        print("Email deleted.")

                    except Exception as e:
                        print(f"Failed to process email: {str(e)}")

            else:
                # Delete emails that aren't from the target sender
                mail.store(email_id, '+FLAGS', '(\Deleted)')
                print(f"Email from {email_message['From']} deleted as it's not from the target sender.")

        mail.expunge()  # Permanently remove the marked \\Deleted emails
        mail.close()
        mail.logout()
    except imaplib.IMAP4.error as e:
        print(f"IMAP error: {str(e)}")
    except Exception as e:
        print(f"An error occurred while processing emails: {str(e)}")

def main(): # Complete this section
    username = ""
    password = ""
    bot_token = ""
    channel_id = ""
    target_sender = ""

    while True:
        try:
            forward_emails(username, password, bot_token, channel_id, target_sender)
        except Exception as e:
            print("An error occurred while forwarding emails:")
            print(str(e))

        time.sleep(1)

if __name__ == "__main__":
    main()
