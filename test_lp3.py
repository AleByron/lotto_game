import unittest
from learning_path_2.extract import extraction
from learning_path_2.winners import check_winner
from Learning_path_1.type_bill_cl import typeb
from Learning_path_1.type_city_cl import City
from Learning_path_1.type_num_cl import Num
from learning_path_3.value import value


class Test_lp3(unittest.TestCase):


    def test_type_bill(self):
        t1 = typeb('ambata')
        result1 = typeb.type_bill(t1)
        self.assertIn( result1, "ambata ambo terno quaterna cinquina")

    def test_type_city(self):
        t2 = City('roma')
        result2 = City.cit(t2)
        self.assertIn( result2, "bari cagliari firenze genova milano napoli palermo roma torino venezia all")

    def test_type_num(self):
        t3 = Num('ambo')
        result2 = Num.bill(t3)
        st_result2 = ""
        nums = 1
        check_nums = ''
        while nums <= 90:
            check_nums = check_nums + ' ' + str(nums)
            nums = int(nums) +1
        st_result2.join(result2)
            
        self.assertIn( st_result2, check_nums )

    def test_extract(self):
        result4 = extraction().numbers()
        nums = 1
        check_nums = ''
        while nums <= 90:
            check_nums = check_nums + ' ' + str(nums)
            nums = int(nums) +1
        for city in result4:
            self.assertIn(city, "bari cagliari firenze genova milano napoli palermo roma torino venezia all")
            for n in result4[city]:
                self.assertIn( str(n), check_nums )

    def ntest_check_winner(self):
        tick = {'Bill0': ['ambo', ['6', '7', '8', '9', '10', '11', '12', '13', '14'], 'all', 2.0], 'Bill1': ['ambata', ['12', '34', '56', '78', '90'], 'roma', 3.0]}
        ext = {'bari': [24, 22, 60, 5, 85, 39, 87, 49, 9, 23], 'cagliari': [10, 60, 48, 33, 6, 90, 64, 78, 72, 73], 'firenze': [16, 79, 46, 55, 40, 38, 3, 42, 15, 87], 'genova': [60, 74, 59, 16, 64, 88, 73, 65, 26, 21], 'milano': [3, 52, 25, 20, 42, 11, 86, 65, 44, 68], 'napoli': [46, 32, 62, 4, 68, 69, 7, 63, 67, 12], 'palermo': [14, 81, 19, 61, 18, 54, 75, 88, 6, 3], 'roma': [20, 32, 25, 81, 46, 67, 77, 41, 69, 55], 'torino': [83, 18, 22, 84, 41, 4, 58, 14, 26, 64], 'venezia': [24, 30, 3, 72, 41, 35, 18, 57, 39, 10]}
        t5 = check_winner(tick,ext)
        result5 = t5.checker()
        test = [ {'Bill0': ['ambo', ['6', '7', '8', '9', '10', '11', '12', '13', '14'], 'all', 2.0], 'Bill1': ['ambata', ['12', '34', '56', '78', '90'], 'roma', 3.0]}], ['In this ticket you won: \n Ambate : 7 \n Ambi :  0 \n Terni : 0 \n Quaterne : 0 \n Cinquine : 0 ', 'In this ticket you won: \n Ambate : 0 \n Ambi :  3 \n Terni : 0 \n Quaterne : 0 \n Cinquine : 0 '], [{'bari5': ['ambata', 1, 5], 'firenze5': ['ambata', 1, 5], 'milano5': ['ambata', 1, 5], 'napoli5': ['ambata', 1, 5], 'palermo5': ['ambata', 1, 5], 'torino5': ['ambata', 1, 5], 'venezia5': ['ambata', 1, 5]}, {'cagliari14': ['ambo', 1, 9], 'napoli14': ['ambo', 1, 9], 'palermo14': ['ambo', 1, 9]}, {'cagliari14': ['ambo', 1, 9], 'napoli14': ['ambo', 1, 9], 'palermo14': ['ambo', 1, 9]}]
        self.assertEqual(result5, test)

    def test_value(self):
        tick = {'bari5': ['ambata', 1, 5] ,'cagliari5': ['ambata', 1, 5], 'genova5': ['ambata', 2, 5], 'napoli5': ['ambata', 2, 5], 'torino5': ['ambata', 1, 5], 'venezia5': ['ambata', 1, 5]}
        t7 = value(tick)
        result7 = t7.calculate_value()
        test = (17.92, 16.486400000000003)
        self.assertEqual(result7, test)


if __name__ == "__main__":
        unittest.main()