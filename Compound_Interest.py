    #Original Formula: A=P(1+r/n)**(n*t)
    
    #step 1: Collect input values for P, r, n, and t.
    #step 2: Convert the inputed strings into floats.
    #step 3: Calculate A.
    #step 4: Print the future account value, format the number to 2 decimal places using .format.
    
    #take inputs for P, r, n, t
    principle_str = input("\nInput the initial principal amount: ") #P
    interest_rate_str = input("Input the interest rate: ") #r
    compounds_per_year_str = input("Input the number of times compounded per year: ") #n
    years_str = input("Input the number of years: ") #t

    #Convert to floats
    principle_float = float(principle_str)
    interest_rate_float = float(interest_rate_str)
    compounds_per_year_float = float(compounds_per_year_str)
    years_float = float(years_str)

    #calculating A
    future_account_value = principle_float*(1+(interest_rate_float/compounds_per_year_float))**(compounds_per_year_float*years_float)

    #Print
    print("\nFuture account value:{:>10.2f}".format(future_account_value))
