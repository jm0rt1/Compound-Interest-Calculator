    principle_str = input("\nInput the initial principal amount: ") #P
    interest_rate_str = input("Input the interest rate: ") #r
    compounds_per_year_str = input("Input the number of times compounded per year: ") #n
    years_str = input("Input the number of years: ") #t

    principle_float = float(principle_str)
    interest_rate_float = float(interest_rate_str)
    compounds_per_year_float = float(compounds_per_year_str)
    years_float = float(years_str)

    future_account_value = principle_float*(1+(interest_rate_float/compounds_per_year_float))**(compounds_per_year_float*years_float)

    print("\nFuture account value:{:>10.2f}".format(future_account_value))
