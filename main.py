import openpyxl
import numbers





def process_data(r,l):
    open_worksheet = openpyxl.pop_worksheet(r,l)
    should_display_pop_change( show_pop_change )

# I am creating two functions that has two variable within them.
def main():
    income_pop_worksheet = process_data("MedianIncomeByStateCensusGov.xlsx")
    examine_data(income_pop_worksheet)
# This is where I would be calling the funcation and creating if statements

def examine_data(income_sheet):
 sum=[]
 sum1=[]
 city=[]
 state=[]
 p=[]
 for i in 'r'['POPESTIMATE2021']:
   sum.append(i)
 for i in 'r'['NPOPCHG2021']:
   sum1.append(i)
 for i in 'r'['CTYNAME']:
   city.append(i)
 for i in 'r'['STNAME']:
   state.append(i)
 for i in range(len(sum)):
   p.append((sum1[i]*100)/sum[i])
 if 'l'==1:
   for i in range(len(p)):
     if p[i]<2:
       print(city[i],state[i],p[i])
 else:
   for i in range(len(p)):
     if p[i]>1.5:
       print(city[i],state[i],p[i])

#This is me displaying the funcation and telling python to read the files.

def open_worksheet():
 df = openpyxl.read_excel('rohan1.xlsx', sheet_name='Sheet1')
 return df
def should_get_losses():
 return int(input('Should get Counties that lost population type 1 for true else false'))
worksheet=open_worksheet()
losses=should_get_losses()
process_data(worksheet,losses)

#This is code is the file being put into work. I am telling python to go through the spreadsheet.