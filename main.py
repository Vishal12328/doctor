print("welcome!")

name = input("what is your name: ")
age = float(input("what is your age: "))
if age <= 55:
    print(name + " you are safe in terms of age but be at home!")

    status = input("have gone to any foregin countries in past 1 month? ").lower()
    if status == "yes":
        print("you should stay at home and be careful")
        infection = input("are you having any kind of symptoms of covid-19? ")
        if infection == "yes":
            infection_kind = input("are you facing serious problems of cough and cold or fever? ")
            if infection_kind == "yes":
                print("counsult your doctor immediately!")
    else:
        status_ind = input("have you gone to any other states in india? ").lower()
        if status_ind == "yes":
            print("you should stay at home and be careful")
            infection = input("are you having any kind of symptoms of covid-19? ")
            if infection == "yes":
                infection_kind = input("are you facing serious problems of cough and cold or fever? ")
                if infection_kind == "yes":
                    print("counsult your doctor immediately!")
            else:
                print("your chance of getting infected is medium ")

                stsf = "STAY HOME STAY SAFE!"
                print(stsf)

        else:
            print("ok fine......")
            infection = input("are you having any kind of symptoms of covid-19? ")
            if infection == "yes":
                infection_kind = input("are you facing serious problems of cough and cold or fever? ")
                if infection_kind == "yes":
                    print("counsult your doctor immediately!")
            else:
                print("your chance of getting infected is low ")

                stsf = "STAY HOME STAY SAFE!"
                print(stsf)

else:
    print(name + " you  have high risk of getting infected be at home")

    status = input("have gone to any foregin countries in past 1 month? ").lower()
    if status == "yes":
        print("you should stay at home and be careful")

    else:
        status_ind = input("have you gone to any other states in india? ").lower()
        if status_ind == "yes":
            print("you should stay at home and be careful")

        else:
            print("ok fine......")
            infection = input("are you having any kind of symptoms of covid-19? ")
            if infection == "yes":
                infection_kind = input("are you facing serious problems of cough and cold or fever? ")
                if infection_kind == "yes":
                    print("counsult your doctor immediately!")
            else:
                print("your chance of getting infected is low ")

                stsf = print("STAY HOME STAY SAFE!")
                print(stsf)