import time
import random
applicant_id = input("Enter the applicant ID (Your name) to get your loan started and approved: ")
if applicant_id in ["John", "Rahul", "David", "Lewis"]:
    print("Welcome, {}! Let's get started with your loan application.".format(applicant_id))
else:
    print("Applicant ID not recognized. Access denied.")
    exit()

with open("Applicant_details/{}.txt".format(applicant_id), "r") as file:
    content = file.read()
    print(content)

lines = content.splitlines()
income_per_annum = float(lines[0].split()[0])
credit_score = int(lines[1].split()[0])

requested_loan = float(input("Enter the loan amount: "))

deposit_amount = float(input("Enter the deposit amount: "))

Loan_to_Income = requested_loan / income_per_annum

Loan_to_Value = (requested_loan / (deposit_amount + requested_loan))*100

time.sleep(2)
print("Loan to Income Ratio: {:.2f}x".format(Loan_to_Income))

time.sleep(2)
print("Loan to Value Ratio: {:.2f}%".format(Loan_to_Value))

if Loan_to_Income > 5:
    time.sleep(2)
    print("Loan to Income Ratio is too high. Loan application rejected.")
    exit()

else:
    time.sleep(2)
    print("Loan to Income Ratio is within acceptable range. Proceeding with further evaluation.")

    if 90 < Loan_to_Value < 95:
        time.sleep(2)
        print("Loan to Value Ratio is within acceptable range. Proceeding with further evaluation.")

    elif 80 < Loan_to_Value < 90:
        time.sleep(2)
        print("Loan to Value Ratio is outside the ideal range. However, we are happy to consider your application. Proceeding with further evaluation.")

        if credit_score < 600:
            time.sleep(2)
            print("Credit score is below the acceptable threshold. Loan application rejected.")
            exit()

        elif 600 < credit_score <= 650:
            time.sleep(2)
            print("Credit score is being considered. The seniors are reviewing your application.")
            time.sleep(5)
            random.choice = random.choice([True, False])

            if random.choice == True:
                print("Loan application approved.")

            else:
                print("We regret to inform you that your loan application has been rejected.")
                exit()

        else:
            time.sleep(2)
            print("Credit score is outstanding. Loan application approved.")

    else:
        time.sleep(2)
        print("Loan to Value Ratio is too low. Loan application rejected.")
        exit()
