from form import Form


class MotorcycleLicenseForm(Form):
    def __init__(self, name, address, qualified):
        super().__init__(name, address)
        self.qualified = qualified

    def __str__(self):
        return f"name={self.name}, address={self.address} is_valid={self.is_valid} qualified={self.qualified}"

    def validate_form(self):
        super().validate_form()  # this calls the super method just remebver () < calls
        if self.is_valid and self.qualified:
            self.is_valid = True
        else:
            self.is_valid = False


ml = MotorcycleLicenseForm("sketchy", '603 mary', True)
ml.run()
print(ml)
