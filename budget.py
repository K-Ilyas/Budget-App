import math
class Category:
    def __init__(self,name):
        self._name = name
        self.ledger = list()
   
    def get_name(self):   
        return self._name           
    def get_ledger(self) :
        return self.ledger
    def deposit(self,amount ,description = "") :
        self.ledger.append({"amount":float(amount),"description":description})

    def withdraw(self,amount ,description = ""):
        if self.check_funds(amount) :
         self.ledger.append({"amount":-float(amount),"description":description})
         return True
        else : 
         return False

    def get_balance(self) :
        return sum(float(item['amount']) for item in self.ledger)
 
    def transfer(self,amount ,category):
        if self.check_funds(amount):
            self.ledger.append({"amount":-float(amount),"description":("Transfer to " + category.get_name())})
            category.deposit(amount,"Transfer from " + self.get_name() )
            return True
        else : 
            return False
    
    def check_funds(self,amount):
       return True if self.get_balance() >= amount else False

    def __str__(self) :
        final_str = ""
        name = self.get_name()
        space= "*"*(15-int((len(name)/2)))
        final_str = final_str +((space)+name.capitalize()+space[:(15-int((len(name)/2))) if len(name)%2 ==0 else (15-int((len(name)/2)))-1]) +"\n"
        for item in self.ledger :
            format_amount = "{:5.2f}".format(item.get("amount"))
            amount_space = len(format_amount)
            description_space = len(item.get("description"))

            final_str = final_str +(str(item.get("description"))[0:23]+("" if description_space ==23 else " "*(23-description_space))+ ( "" if amount_space== 7 else " "*(7-amount_space)) ) + format_amount[:7] + "\n"

        format_total = "{:5.2f}".format(self.get_balance())
        final_str = final_str +("Total: " + format_total)
        return final_str
    



def create_spend_chart(categories):
    dictionary = dict()
    percentage = dict()
    names = list()
    total_spent = 0
    max_length = max([(len(item.get_name())) for item in categories])
    length_cara = (len(categories) * 3) 

    final_str=''

    for category in categories :
        name = category.get_name()
        dictionary[name] =abs(sum([(0 if  item['amount'] >0 else item['amount'] ) for item in category.get_ledger()]))
        total_spent = total_spent  + dictionary[name] 
        names.append((name+ (" "*(max_length - len(name)) if max_length > len(name) else "")))
    
    # count percentage 
    for category in categories :
        name = category.get_name()
        percentage[(name)] = math.floor(int(round((float(dictionary[name])/total_spent)*100))/10)*10

    final_str = final_str +"Percentage spent by category" +"\n"
    
    # draw percentage line 
    for i in reversed(range(11)) :
      final_str = final_str + "{:3d}".format(i*10) +"|"
      new_line = ''
      for index in range(len(categories)) :
        if int(percentage[(categories[index].get_name())]) >=i*10  :
           new_line = new_line + (" "*(2+index*2 if index != 0 else 1) if new_line.find("o") == -1 else "  ") + "o"
     
      
      final_str = final_str + new_line + (" "*(length_cara - len(new_line) +1)if length_cara > len(new_line) else "")  +"\n"
    
      
    final_str = final_str + " "*4 + "-"*3*len(categories) +"-" +"\n"

   
    for i in range(max_length) :
      final_str = final_str + " "*4
      for item in names : 
        final_str = final_str +" " + item[i] +" "
    
      final_str = final_str + " " + ("\n" if i !=max(range(max_length)) else "") 


        
    return final_str    

    
    

    


