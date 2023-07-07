# case study
# PayTM
scan_and_pay = {
    "name": "scan and pay",
    "from": "+91 9877916506",
    "to": "qr code",
    "amount": "500"
}
to_mobile = {
    "name": "to mobile",
    "from": "+91 9877916505",
    "to": "+1(514) 7466104",
    "amount": "200"

}
conversation1 = [
    {
        "from": "+91 9877916505",
        "to": "+91 9877916506",
        "text": "10 rupee sent to bank A/c",
        "sent_time": "12:00",
        "status": 1
    },
    {
        "from": "+91 9877916506",
        "to": "+91 9877916505",
        "text": "received,Thank tou",
        "sent_time": "12:02",
        "status": 1

    }
]
to_upi_apps = {
    "name": "to upi apps",
    "from": "+91 9877916505",
    "to": "+91 9877916506",
    "conversation": conversation1
}
Enter_bank_details = {
    "choose bank name": "sbi",
    "enter abnk account": "73438",
    "proceed": "True "
}
to_self = {
    "name": "to self",
    "add bank aacount": "sbi bank"
}
enter_mobile_or_upi_number = {
    "name": "enter mobile or upi number",
    "from": "+91 9877916505",
    "to": "+1(514) 7466104",
    "amount": "200"
}

to_bank_or_self = [Enter_bank_details, to_self, enter_mobile_or_upi_number]

Paytm = [scan_and_pay, to_mobile, to_upi_apps, to_bank_or_self]
