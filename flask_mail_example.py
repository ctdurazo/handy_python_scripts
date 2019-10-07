# flask_mail_example.py
# https://pythonhosted.org/Flask-Mail/

from flask import Flask, abort
import flask_mail

# import your main app if this is not your main app. I generally just use app.py or /app/__init__.py as my main app file
# from app import app

app = Flask(__name__)  # used if this is your main app. I prefer to include this file as a utility

mail = flask_mail.Mail(app)

# use the following to set up your Mail instance later at configuration time
# mail = Mail()
#
# app = Flask(__name__)
# mail.init_app(app)

# MAIL_SERVER : default `localhost`
# MAIL_PORT : default 25
# MAIL_USE_TLS : default False
# MAIL_USE_SSL : default False
# MAIL_DEBUG : default app.debug
# MAIL_USERNAME : default None
# MAIL_PASSWORD : default None
# MAIL_DEFAULT_SENDER : default None
# MAIL_MAX_EMAILS : default None
# MAIL_SUPPRESS_SEND : default app.testing
# MAIL_ASCII_ATTACHMENTS : default False

MAIL_SERVER = 'example.com'  # smtp server
MAIL_PORT = 587  # smtp port
MAIL_USE_TLS = True

MAIL_USERNAME = 'username'  # should probably be kept in a separate file
MAIL_PASSWORD = 'password'  # should probably be kept in a separate file


def send_email(recipients, sender, subject, messagehtml, messagetxt, attachment, contenttype):
	# Create message container
	msg = flask_mail.Message()
	msg.subject = subject
	msg.body = messagetxt
	msg.html = messagehtml
	msg.sender = sender
	msg.recipients = recipients
	# msg.add_recipient("somebodyelse@example.com")

	# add an attachment
	if attachment is not None:
		with app.open_resource(attachment) as fp:
			msg.attach(attachment, contenttype, fp.read())
	try:
		mail.send(msg)
		print("Successfully sent email")
	except Exception as e:
		print(str(e))
		print("Error: unable to send email")


# test method
@app.route('/')
def test():
	send_email('test@example.com', 'test@example.com', 'Test Subject', '<h4>test message</h4>', 'test message', None, None)
	abort(418)  # do your error catching


# used if this is your main app. I prefer to include this file as a utility
if __name__ == '__main__':
	app.run()
