from fpdf import FPDF


class Bill:
    """
    Object that contains data abut a bill such as total amount
    and period of the bill.
    """

    def __init__(self, amount, period):
        self.amount = amount
        self.period = period


class Flatmate:
    """
    Object that contains data about the flatmates such as name,
    days in house and how much they each pay.
    """

    def __init__(self, name, days_in_house):
        self.name = name
        self.days_in_house = days_in_house

    def pays(self, bill, flatmate2):
        weight = self.days_in_house / (self.days_in_house + flatmate2.days_in_house)
        to_pay = weight * bill.amount
        return to_pay


class PdfReport:
    """
    Creates a PDF report that contains data about the flatmate
    such as their name, their due amount and the period of the
    bill.
    """

    def __init__(self, filename):
        self.filename = filename

    def generate(self, flatmate1, flatmate2, bill):
        pdf = FPDF(orientation='P', unit='pt', format='A4')
        pdf.add_page()
        # insert title
        pdf.set_font(family='Times', size=24, style='B')
        pdf.cell(w=0, h=80, txt='Flatmates Bill', border=1, align='C', ln=1)
        # insert period label and value
        pdf.cell(w=100, h=40, txt='Period:', border=1)
        pdf.cell(w=150, h=40, txt=bill.period, border=1, ln=1)

        pdf.output(self.filename)


the_bill = Bill(120, "April 2021")
John = Flatmate("John", 20)
Matt = Flatmate("Matt", 25)

print("John pays", John.pays(the_bill, Matt))
print("Matt pays", Matt.pays(the_bill, John))

pdf_report = PdfReport(filename='Report1.pdf')
pdf_report.generate(flatmate1=John, flatmate2=Matt, bill=the_bill)

