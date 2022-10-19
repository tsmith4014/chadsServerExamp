from form import Form


class DriversLicenseForm(Form):

    def __init__(self, name, address):
        super().__init__(name, address)
        #self.is_valid = is_valid

    # def __str__(self):
    #     return f"name={self.name}, address={self.address} is_valid={self.is_valid}"

    # def validate_form(self):
    #     if self.name != "" and self.address != "":
    #         self.is_valid = True
    #     else:
    #         self.is_valid = False

    # def submit(self):
    #     if self.is_valid:
    #         print("sucess")
    #     else:
    #         print("failure")

    # def run(self):
    #     self.validate_form()
    #     self.submit()


dl = DriversLicenseForm("vega", '603 mary')
dl.run()
print(dl)
