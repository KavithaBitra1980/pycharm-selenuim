#Excecise on Taxes

def taxes(state_name,gross_income):

    states_tax = {'va': 5, 'ma': 4, 'dc':3,'ny': 20}
    net_income = gross_income - (gross_income * .10)
    if state_name in states_tax:
        net_income = net_income -(gross_income * states_tax[state_name] /100)
        return net_income
    else:
        print('state not listed in the list')



print(taxes('ny',10000))




