import datetime
from logging import PercentStyle
from pydantic.class_validators import ROOT_VALIDATOR_CONFIG_KEY
from pydantic.error_wrappers import ValidationError
from pydantic.main import SchemaExtraCallable

class ValidatorPesel:
    def __init__(self, pesel):
        self.pesel = pesel

    def _func_sum(self):   
        sum=0
        index=0
        for point in self.pesel:
            if (index + 4)%4==0 and index <10:
                sum += int(point) *1

            elif (index + 4)%4==1 and index <10:
                sum += int(point) *3

            elif (index + 4)%4==2 and index <10:
                sum += int(point) *7
            
            elif (index + 4)%4==3 and index <10:
                sum += int(point) *9
            index += 1
        return sum
        

    def _func_last_number(self):
        sum = self._func_sum()
        
        if sum < 10:
            last_num = 10 - sum
        elif sum >= 10:
            last_num = 10 - (sum % 10)

        if str(last_num) != self.pesel[-1]:
            raise ValidationError('Bad PESEL')  
        return self.pesel

    def finish(self):
        return self._func_last_number()

    def get_birth_date(self):
        year_num = int(self.pesel[2:4])

        a = 1
        b = 13
        year = 1900
            
        for i in range(4) :
            if year_num in range(a,b): year 
            else:
                a += 20
                b += 20 
                year += 100

        if year_num > 12: year_num = year_num%20

        date_t = datetime.date(int(self.pesel[0:2])+year, int(year_num), int(self.pesel[4:6]))
        return date_t

    def get_age(self):
        result = datetime.date.today() - datetime.date(self.get_birth_date())  
        return int(result)