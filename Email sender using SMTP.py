import smtplib

# Use your own email and a valid App Password here
my_email = "your email"
app_password = "yourapp_password"  # Make sure this is an App Password which need to be generated 
                                   #make sure to turn on 2fa
                                   
with smtplib.SMTP("smtp.gmail.com", 587) as connection: #u need to put 587 as the port which is mandatory for all 
    connection.starttls()  # Secure the connection
    connection.login(user=my_email, password=app_password)
    connection.sendmail(
        from_addr=my_email,
        to_addrs="receipient email",
        msg="Subject:Greeting\n\nHello, How are you?"
    )
print("Email sent successfully!")
