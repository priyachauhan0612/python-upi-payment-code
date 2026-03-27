import qrcode
#taking UPI id as input
upi_id = input("Enter your UPI ID: ")
#upi://pay?pa=UPI_ID&pn=NAME&am=AMOUNT&cu=CURRENCY&tn=Message
#defining the ayment URL based on the UPI ID and the payment app
#we can also modify these URLS based on the paymemt menthod

phonepe_url= f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
paytm_url= f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'
google_pay_url= f'upi://pay?pa={upi_id}&pn=Recipient%20Name&mc=1234'

#create QR code for each payment app
phonepe_qr = qrcode.make(phonepe_url)
paytm_qr = qrcode.make(paytm_url)
google_pay_qr = qrcode.make(google_pay_url)

#we will save these qr codes
phonepe_qr.save("phonepe_qr.png")
paytm_qr.save("paytm_qr.png")
google_pay_qr.save("google_pay_qr.png")

#display the QR codes ( installed pil /pillow library)

phonepe_qr.show()
paytm_qr.show()
google_pay_qr.show()
