import os
directory = os.path.dirname(os.path.realpath(__file__))+'/raw_data/'

'''
products.txt file read by order (14 indices)
- Ingredient
- Dosage Form (DF) and Route of Administration
- Trade Name
- Applicant
- Strength
- Appl_Type
- Appl_No
- Product_No
- TE_Code
- Approval_Date
- RLD
- RS
- Type
- Applicant_Full_Name
We let the application number and the 
product number to be the distinctive factor for each drug (may create the list in form of a dictionary)
'''

def product_analysis():
    list_drug = {}
    with open(directory + "products.txt") as f:
        #skip first line
        next(f)
        for line in f:
            temp = line.split('~')
            list_drug[temp[6]+'-'+temp[7]] = (temp[0],temp[1],temp[2],temp[3],temp[4],temp[5],temp[8],temp[9],temp[10],temp[11],temp[12],temp[13])
    #print(list_drug)
    #print(len(list_drug))
    return list_drug

'''
Note that some TE code are blank, it means that there are no equicalent drugs for the one 
(no two products have the same effect)
which means we may sort them by TE code
'''


