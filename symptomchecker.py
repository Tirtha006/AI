class symptomChecker:
    def __init__(self):
        self.symptoms={
            "cough":False,
            "cold":False,
            "headache":False,
            "fever":False,
            "rash":False,
        }
    def ask_symptoms(self):
        print("Please answer with 'yes'or 'no'")
        for symptom in self.symptoms:
            response=input(f"Do you have {symptom}?").lower()
            if response=='yes':
                self.symptoms[symptom]=True

    def diagnose(self):
        if self.symptoms["fever"]and self.symptoms["cold"]:
            print("You may have x")
        elif self.symptoms["headache"]and self.symptoms["cough"]:
            print("You may have y")
        elif self.symptoms["rash"]and self.symptoms["cold"]:
            print("You may have z")
        else:
            print("It is difficult to analyze.Please consult with a doctor")

if __name__=="__main__":
    checker=symptomChecker()
    checker.ask_symptoms()
    checker.diagnose()
