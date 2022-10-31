from mail import *
import sys
import unittest
sys.path.insert(0, 'dost')


class test(unittest.TestCase):
    def test_send_gmail_using_app_password(self):
        send_gmail_using_app_password('deveshkgupta1810@gmail.com', 'quifulmvfqzyniye', to_email_id='deveshkumar.pybots@gmail.com',
                                      subject='subject', message='message', attachment_path="tests\demo2.pdf")
        send_gmail_using_app_password('deveshkgupta1810@gmail.com', 'quifulmvfqzyniye',
                                      to_email_id='deveshkumar.pybots@gmail.com', subject='subject', message='message')


if __name__ == "__main__":
    unittest.main()
