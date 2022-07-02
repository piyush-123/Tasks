# Logging class to log the activities performed during the flow
import logging

class log_rec:

    def __init__(self,filename,level,format):
        self.filename = filename
        self.level = level
        self.format = format
        logging.basicConfig(filename=self.filename,
                            level=self.level,
                            format=self.format)

    def log(self,message,method):
        '''
                    logging the message based on the method
                    passed in this function
                    in the file
        '''
        if method == 'INFO':
            logging.info(message)
        else:
            logging.error(message)

# creating the class for list related actions

class mylist:

    def __init__(self,sample_list):
        self.sample_list = sample_list
        self.logger_list = log_rec('log_file.txt','INFO','%(levelname)s %(asctime)s %(name)s %(message)s')
    def extract_list_type(self):
        '''
            The function is used to extract the list entities from the given
            input list containing data of any type like int,list,dictionaries
            ,tupes,set
        '''
        output_list=[]
        self.logger_list.log("Starting Extracting lists from input data","INFO")
        try:
            for i in self.sample_list:
                if type(i) == list:
                    output_list.append(i)
            self.logger_list.log("Lists are Extracted now ","INFO")
            return output_list
        except Exception as e:
            self.logger_list.log("extract_list_type", "INFO")
            self.logger_list.log(e,"ERROR")
    def extract_numbers(self):
        '''
            The function is used to extract the numerical data
            present either as int or in a list  from the
            given input list
            Input list can contain data of different types like int,list,set,dict etc

        '''
        output_num_list = []
        self.logger_list.log("Starting Extracting Numbers in LIST from input data","INFO")
        try:
            for i in self.sample_list:
                if type(i) == int:
                    output_num_list.append(j)

                elif type(i) == list:
                    for j in i:
                        if type(j) == int:
                            output_num_list.append(j)
            self.logger_list.log("Numbers are Extracted now ","INFO")
            return output_num_list
        except Exception as e:
            self.logger_list.log("extract_numbers", "INFO")
            self.logger_list.log(e,"ERROR")

    def summation_elements(self):
        '''
                    The function is used to sum the numerical data
                    present in list from the
                    given input list
                    Input list can contain data of different types like int,list,set,dict etc

                '''

        sum = 0
        self.logger_list.log("Starting Addition of  Numbers from input data", "INFO")
        try:
            for i in self.sample_list:
                if type(i) == list:
                    for j in i:
                        if type(j) == int:
                            sum = sum + j
            self.logger_list.log("Numbers are Added now ", "INFO")
            return sum
        except Exception as e:
            self.logger_list.log("summation_elements", "INFO")
            self.logger_list.log(e, "ERROR")
    def extract_odd_numbers(self):
        '''
        This function is used to extract the odd values of the
            numerical data present in the list
        '''
        try:
            output_odd_list=[]
            self.logger_list.log("Starting Extracting Odd Numbers from input data", "INFO")
            for i in self.sample_list:
                if type(i) == list:
                    for j in i:
                        if type(j) == int:
                            if j % 2 != 0:
                                output_odd_list.append(j)
            self.logger_list.log("Odd Numbers are Extracted now ", "INFO")
            return output_odd_list
        except Exception as e:
            self.logger_list.log("extract_odd_numbers", "INFO")
            self.logger_list.log(e, "ERROR")
    def count_occurences(self):
        '''
        The function is used to count the number of occurences of
        elements present in list
        '''
        try:
            self.logger_list.log("Starting Counting the occurences of Elements from input data", "INFO")
            l1 = []
            count_dict = {}
            for i in self.sample_list:
                if type(i) == list:
                    for j in i:
                        l1.append(j)
            for k in set(l1):
                count_dict[k] =  l1.count(k)
            self.logger_list.log("Occurences are Counted now ", "INFO")
            return count_dict
        except Exception as e:
            self.logger_list.log("count_occurences", "INFO")
            self.logger_list.log(e, "ERROR")

    def string_filter(self):
        '''
        The function is used to filter the string elements present in
        list
        '''
        try:
            self.logger_list.log("Starting Filtering the String Elements from input data", "INFO")
            l = []
            for i in self.sample_list:
                if type(i) == list:
                    for j in i:
                        if type(j) == str:
                            l.append(j)
            self.logger_list.log("String filteration is done", "INFO")
            return l
        except Exception as e:
            self.logger_list.log("string_filter", "INFO")
            self.logger_list.log(e, "ERROR")

    def alphanumeric_filter(self):
        '''
        The function is used to filter the alphanumeric elements present in
        list
        '''
        try:
            self.logger_list.log("Starting Filtering the ALphanumeric Elements from input data", "INFO")
            l=[]
            for i in self.sample_list:
                if type(i) == list:
                    for j in i:
                        if type(j) == str and j.isalnum():
                            l.append(j)
            self.logger_list.log("Alphanumeric filteration is done", "INFO")
            return l
        except Exception as e:
            self.logger_list.log("alphanumeric_filter", "INFO")
            self.logger_list.log(e, "ERROR")

    def multiplication_elements(self):
        '''
        The function is used to multiply the numeric values present in
        list
        '''
        try:
            l=[]
            self.logger_list.log("Starting Multiply the numeric Elements from input data", "INFO")
            mul = 1
            count = 0
            for i in self.sample_list:
                if type(i) == list:
                    for j in i:
                        if type(j) == int:
                            count = count + 1
                            mul = mul * j
                    if count > 0:
                        l.append(mul)
                    mul = 1
                    count = 0

            self.logger_list.log("Numeric Multiplication is done", "INFO")
            return l
        except Exception as e:
            self.logger_list.log("multiplication_elements","INFO")
            self.logger_list.log(e, "ERROR")


# creating the class for dict related actions

class mydict:

    def __init__(self,sample_list):
        self.sample_list = sample_list
        self.logger_dict = log_rec('log_file.txt','INFO','%(levelname)s %(asctime)s %(name)s %(message)s')
    def extract_dict_type(self):
        '''
            The function is used to extract the dict entities from the given
            input list containing data of any type like int,list,dictionaries
            ,tupes,set
        '''
        output_dict=[]
        self.logger_dict.log("Starting Extracting dicts from input data","INFO")
        try:
            for i in self.sample_list:
                if type(i) == dict:
                    output_dict.append(i)
            self.logger_dict.log("Dicts are Extracted now ","INFO")
            return output_dict
        except Exception as e:
            self.logger_dict.log("extract_dict_type", "INFO")
            self.logger_dict.log(e,"ERROR")
    def extract_numbers_dict(self):
        '''
            The function is used to extract the numerical data
            present either as int or in a dict  from the
            given input list
            Input list can contain data of different types like int,list,set,dict etc

        '''
        output_num_dict = []
        self.logger_dict.log("Starting Extracting Numbers in DICT  from input data","INFO")
        try:
            for i in self.sample_list:
                if type(i) == dict:
                    for d in i.items():
                        if (type(d[0]) == int or type(d[1]) == int):
                            output_num_dict.append(d)
            self.logger_dict.log("Numbers are Extracted now from DICT ","INFO")
            return output_num_dict
        except Exception as e:
            self.logger_dict.log("extract_numbers_dict", "INFO")
            self.logger_dict.log(e,"ERROR")

    def summation_elements_dict(self):
        '''
                    The function is used to sum the numerical data
                    present in dict from the
                    given input list
                    Input list can contain data of different types like int,list,set,dict etc

                '''

        sum = 0
        self.logger_dict.log("Starting Addition of  Numbers in DICT from input data", "INFO")
        try:
            for i in self.sample_list:
                if type(i) == dict:
                    for d in i.items():
                        if type(d[0]) == int:
                            sum = sum + d[0]
                        if type(d[1]) == int:
                            sum = sum + d[1]
            self.logger_dict.log("Numbers in DICT are Added now ", "INFO")
            return sum
        except Exception as e:
            self.logger_dict.log("summation_elements_dict", "INFO")
            self.logger_dict.log(e, "ERROR")
    def extract_odd_numbers_dict(self):
        '''
        This function is used to extract the odd values of the
            numerical data present in the dict in input list
        '''
        try:
            output_odd_list=[]
            self.logger_dict.log("Starting Extracting Odd Numbers in DICT  from input data", "INFO")
            for i in self.sample_list:
                if type(i) == dict:
                    for d in i.items():
                        if type(d[0]) == int:
                            if d[0] % 2 != 0:
                                output_odd_list.append(d[0])
                        if type(d[1]) == int:
                            if d[1] % 2 != 0:
                                output_odd_list.append(d[1])
            self.logger_dict.log("Odd Numbers from DICT are Extracted now ", "INFO")
            return output_odd_list
        except Exception as e:
            self.logger_dict.log("extract_odd_numbers_dict", "INFO")
            self.logger_dict.log(e, "ERROR")
    def count_occurences_dict(self):
        '''
        The function is used to count the number of occurences of
        elements present in dict in input list
        '''
        try:
            self.logger_dict.log("Starting Counting the occurences of Elements in DICT from input data", "INFO")
            l1 = []
            count_dict = {}
            for i in self.sample_list:
                if type(i) == dict:
                    for d in i.items():
                        l1.append(d[0])
                        l1.append(d[1])
            for k in set(l1):
                count_dict[k] =  l1.count(k)
            self.logger_dict.log("Occurences in DICT are Counted now ", "INFO")
            return count_dict
        except Exception as e:
            self.logger_dict.log("count_occurences_dict", "INFO")
            self.logger_dict.log(e, "ERROR")

    def string_filter_dict(self):
        '''
        The function is used to filter the string elements present in dict from
        input list
        '''
        try:
            self.logger_dict.log("Starting Filtering the String Elements of DICT from input data", "INFO")
            l = []
            for i in self.sample_list:
                if type(i) == dict:
                    for d in i.items():
                        if type(d[0]) == str:
                            l.append(d[0])
                        if type(d[1]) == str:
                            l.append(d[1])

            self.logger_dict.log("String filteration of DICT is done", "INFO")
            return l
        except Exception as e:
            self.logger_dict.log("string_filter_dict", "INFO")
            self.logger_dict.log(e, "ERROR")

    def alphanumeric_filter_dict(self):
        '''
        The function is used to filter the alphanumeric elements of dict present in
        list
        '''
        try:
            self.logger_dict.log("Starting Filtering the ALphanumeric Elements from input data", "INFO")
            l=[]
            for i in self.sample_list:
                if type(i) == dict:
                    for d in i.items():
                        if type(d[0]) == str and d[0].isalnum():
                            l.append(d[0])
                        if type(d[1]) == str and d[1].isalnum():
                            l.append(d[1])

            self.logger_dict.log("Alphanumeric filteration from DICT is done", "INFO")
            return l
        except Exception as e:
            self.logger_dict.log("alphanumeric_filter_dict", "INFO")
            self.logger_dict.log(e, "ERROR")

    def multiplication_elements_dict(self):
        '''
        The function is used to multiply the numeric values present in
        dict from input list
        '''
        try:
            l=[]
            self.logger_dict.log("Starting Multiply the numeric Elements of dict from input data", "INFO")
            mul = 1
            count = 0
            for i in self.sample_list:
                if type(i) == dict:
                    for d in i.items():
                        if type(d[0]) == int:
                            mul = mul * d[0]
                            count = count + 1
                        if type(d[1]) == int:
                            mul = mul * d[1]
                            count = count + 1
                    if count > 0:
                        l.append(mul)
                    mul = 1
                    count = 0

            self.logger_dict.log("Numeric Multiplication of DICT is done", "INFO")
            return l
        except Exception as e:
            self.logger_dict.log("multiplication_elements_dict","INFO")
            self.logger_dict.log(e, "ERROR")

    def flatten_elements_dict(self):
        '''
        The function is used to flatten the dict elements to list  from input list
        '''
        try:
            l1=[]
            self.logger_dict.log("Starting Flattening the Dict Elements  from input data", "INFO")
            for i in self.sample_list:
                if type(i) == dict:
                    for d in i.items():
                        l1.append(d[0])
                        l1.append(d[1])

            self.logger_dict.log("Flattening of DICT is done", "INFO")
            return l1
        except Exception as e:
            self.logger_dict.log("flatten_elements_dict","INFO")
            self.logger_dict.log(e, "ERROR")

# creating the class for tuple related actions

class mytuple:

    def __init__(self,sample_list):
        self.sample_list = sample_list
        self.logger_tuple = log_rec('log_file.txt','INFO','%(levelname)s %(asctime)s %(name)s %(message)s')
    def extract_tuple_type(self):
        '''
            The function is used to extract the tuple entities from the given
            input list containing data of any type like int,list,dictionaries
            ,tupes,set
        '''
        output_tuple=[]
        self.logger_tuple.log("Starting Extracting tuples from input data","INFO")
        try:
            for i in self.sample_list:
                if type(i) == tuple:
                    output_tuple.append(i)
            self.logger_tuple.log("Tuples are Extracted now ","INFO")
            return output_tuple
        except Exception as e:
            self.logger_tuple.log("extract_tuple_type", "INFO")
            self.logger_tuple.log(e,"ERROR")
    def extract_numbers_tuple(self):
        '''
            The function is used to extract the numerical data
            present either as int or in a tuple  from the
            given input list
            Input list can contain data of different types like int,list,set,dict,tuple etc

        '''
        output_num_tuple = []
        self.logger_tuple.log("Starting Extracting Numbers in tuple  from input data","INFO")
        try:
            for i in self.sample_list:
                if type(i) == tuple:
                    for j in i:
                        if type(j) == int:
                            output_num_tuple.append(j)
            self.logger_tuple.log("Numbers are Extracted now from tuple ","INFO")
            return output_num_tuple
        except Exception as e:
            self.logger_tuple.log("extract_numbers_tuple", "INFO")
            self.logger_tuple.log(e,"ERROR")

    def summation_elements_tuple(self):
        '''
                    The function is used to sum the numerical data
                    present in tuple from the
                    given input list
                    Input list can contain data of different types like int,list,set,dict,tuple etc

                '''

        sum = 0
        self.logger_tuple.log("Starting Addition of  Numbers in tuple from input data", "INFO")
        try:
            for i in self.sample_list:
                if type(i) == tuple:
                    for j in i:
                        if type(j) == int:
                            sum = sum + j
            self.logger_tuple.log("Numbers in tuple are Added now ", "INFO")
            return sum
        except Exception as e:
            self.logger_tuple.log("summation_elements_tuple", "INFO")
            self.logger_tuple.log(e, "ERROR")
    def extract_odd_numbers_tuple(self):
        '''
        This function is used to extract the odd values of the
            numerical data present in the tuple in input list
        '''
        try:
            output_odd_list=[]
            self.logger_tuple.log("Starting Extracting Odd Numbers in tuple  from input data", "INFO")
            for i in self.sample_list:
                if type(i) == tuple:
                    for j in i:
                        if type(j) == int:
                            if j % 2 != 0:
                                output_odd_list.append(j)
            self.logger_tuple.log("Odd Numbers from tuple are Extracted now ", "INFO")
            return output_odd_list
        except Exception as e:
            self.logger_tuple.log("extract_odd_numbers_tuple", "INFO")
            self.logger_tuple.log(e, "ERROR")
    def count_occurences_tuple(self):
        '''
        The function is used to count the number of occurences of
        elements present in tuple in input list
        '''
        try:
            self.logger_tuple.log("Starting Counting the occurences of Elements in tuple from input data", "INFO")
            l1 = []
            count_dict = {}
            for i in self.sample_list:
                if type(i) == tuple:
                    for j in i:
                        l1.append(j)
            for k in set(l1):
                count_dict[k] =  l1.count(k)
            self.logger_tuple.log("Occurences in tuple are Counted now ", "INFO")
            return count_dict
        except Exception as e:
            self.logger_tuple.log("count_occurences_tuple", "INFO")
            self.logger_tuple.log(e, "ERROR")

    def string_filter_tuple(self):
        '''
        The function is used to filter the string elements present in tuple from
        input list
        '''
        try:
            self.logger_tuple.log("Starting Filtering the String Elements of tuple from input data", "INFO")
            l = []
            for i in self.sample_list:
                if type(i) == tuple:
                    for j in i:
                        if type(j) == str:
                            l.append(j)

            self.logger_tuple.log("String filteration of tuple is done", "INFO")
            return l
        except Exception as e:
            self.logger_tuple.log("string_filter_tuple", "INFO")
            self.logger_tuple.log(e, "ERROR")

    def alphanumeric_filter_tuple(self):
        '''
        The function is used to filter the alphanumeric elements of tuple present in
        list
        '''
        try:
            self.logger_tuple.log("Starting Filtering the ALphanumeric Elements in tuple from input data", "INFO")
            l=[]
            for i in self.sample_list:
                if type(i) == tuple:
                    for j in i:
                        if type(j) == str:
                            l.append(j)

            self.logger_tuple.log("Alphanumeric filteration from tuple is done", "INFO")
            return l
        except Exception as e:
            self.logger_tuple.log("alphanumeric_filter_tuple", "INFO")
            self.logger_tuple.log(e, "ERROR")

    def multiplication_elements_tuple(self):
        '''
        The function is used to multiply the numeric values present in
        tuple from input list
        '''
        try:
            l=[]
            self.logger_tuple.log("Starting Multiply the numeric Elements of tuple from input data", "INFO")
            mul = 1
            count = 0
            for i in self.sample_list:
                if type(i) == tuple:
                    for j in i:
                        if type(j) == int:
                            mul = mul * j
                            count = count + 1

                    if count > 0:
                        l.append(mul)
                    mul = 1
                    count = 0

            self.logger_tuple.log("Numeric Multiplication of tuple is done", "INFO")
            return l
        except Exception as e:
            self.logger_tuple.log("multiplication_elements_tuple","INFO")
            self.logger_tuple.log(e, "ERROR")

    def flatten_elements_tuple(self):
        '''
        The function is used to flatten the tuple elements to list  from input list
        '''
        try:
            l1=[]
            self.logger_tuple.log("Starting Flattening the tuple Elements  from input data", "INFO")
            for i in self.sample_list:
                if type(i) == tuple:
                    for j in i:
                        l1.append(j)


            self.logger_tuple.log("Flattening of tuple is done", "INFO")
            return l1
        except Exception as e:
            self.logger_tuple.log("flatten_elements_tuple","INFO")
            self.logger_tuple.log(e, "ERROR")

# creating the class for set related actions

class myset:

    def __init__(self,sample_list):
        self.sample_list = sample_list
        self.logger_set = log_rec('log_file.txt','INFO','%(levelname)s %(asctime)s %(name)s %(message)s')
    def extract_set_type(self):
        '''
            The function is used to extract the set entities from the given
            input list containing data of any type like int,list,dictionaries
            ,tupes,set
        '''
        output_set=[]
        self.logger_set.log("Starting Extracting sets from input data","INFO")
        try:
            for i in self.sample_list:
                if type(i) == set:
                    output_set.append(i)
            self.logger_set.log("Sets are Extracted now ","INFO")
            return output_set
        except Exception as e:
            self.logger_set.log("extract_set_type", "INFO")
            self.logger_set.log(e,"ERROR")
    def extract_numbers_set(self):
        '''
            The function is used to extract the numerical data
            present either as int or in a set  from the
            given input list
            Input list can contain data of different types like int,list,set,dict,tuple etc

        '''
        output_num_set = []
        self.logger_set.log("Starting Extracting Numbers in set  from input data","INFO")
        try:
            for i in self.sample_list:
                if type(i) == set:
                    for j in i:
                        if type(j) == int:
                            output_num_set.append(j)
            self.logger_set.log("Numbers are Extracted now from set ","INFO")
            return output_num_set
        except Exception as e:
            self.logger_set.log("extract_numbers_set", "INFO")
            self.logger_set.log(e,"ERROR")

    def summation_elements_set(self):
        '''
                    The function is used to sum the numerical data
                    present in set from the
                    given input list
                    Input list can contain data of different types like int,list,set,dict,tuple etc

                '''

        sum = 0
        self.logger_set.log("Starting Addition of  Numbers in set from input data", "INFO")
        try:
            for i in self.sample_list:
                if type(i) == set:
                    for j in i:
                        if type(j) == int:
                            sum = sum + j
            self.logger_set.log("Numbers in set are Added now ", "INFO")
            return sum
        except Exception as e:
            self.logger_set.log("summation_elements_set", "INFO")
            self.logger_set.log(e, "ERROR")
    def extract_odd_numbers_set(self):
        '''
        This function is used to extract the odd values of the
            numerical data present in the set in input list
        '''
        try:
            output_odd_list=[]
            self.logger_set.log("Starting Extracting Odd Numbers in set  from input data", "INFO")
            for i in self.sample_list:
                if type(i) == set:
                    for j in i:
                        if type(j) == int:
                            if j % 2 != 0:
                                output_odd_list.append(j)
            self.logger_set.log("Odd Numbers from set are Extracted now ", "INFO")
            return output_odd_list
        except Exception as e:
            self.logger_set.log("extract_odd_numbers_set", "INFO")
            self.logger_set.log(e, "ERROR")
    def count_occurences_set(self):
        '''
        The function is used to count the number of occurences of
        elements present in set in input list
        '''
        try:
            self.logger_set.log("Starting Counting the occurences of Elements in set from input data", "INFO")
            l1 = []
            count_dict = {}
            for i in self.sample_list:
                if type(i) == set:
                    for j in i:
                        l1.append(j)
            for k in set(l1):
                count_dict[k] =  l1.count(k)
            self.logger_set.log("Occurences in set are Counted now ", "INFO")
            return count_dict
        except Exception as e:
            self.logger_set.log("count_occurences_set", "INFO")
            self.logger_set.log(e, "ERROR")

    def string_filter_set(self):
        '''
        The function is used to filter the string elements present in set from
        input list
        '''
        try:
            self.logger_set.log("Starting Filtering the String Elements of set from input data", "INFO")
            l = []
            for i in self.sample_list:
                if type(i) == set:
                    for j in i:
                        if type(j) == str:
                            l.append(j)

            self.logger_set.log("String filteration of set is done", "INFO")
            return l
        except Exception as e:
            self.logger_set.log("string_filter_set", "INFO")
            self.logger_set.log(e, "ERROR")

    def alphanumeric_filter_set(self):
        '''
        The function is used to filter the alphanumeric elements of set present in
        list
        '''
        try:
            self.logger_set.log("Starting Filtering the ALphanumeric Elements in set from input data", "INFO")
            l=[]
            for i in self.sample_list:
                if type(i) == set:
                    for j in i:
                        if type(j) == str:
                            l.append(j)

            self.logger_set.log("Alphanumeric filteration from set is done", "INFO")
            return l
        except Exception as e:
            self.logger_set.log("alphanumeric_filter_set", "INFO")
            self.logger_set.log(e, "ERROR")

    def multiplication_elements_set(self):
        '''
        The function is used to multiply the numeric values present in
        set from input list
        '''
        try:
            l=[]
            self.logger_set.log("Starting Multiply the numeric Elements of set from input data", "INFO")
            mul = 1
            count = 0
            for i in self.sample_list:
                if type(i) == set:
                    for j in i:
                        if type(j) == int:
                            mul = mul * j
                            count = count + 1

                    if count > 0:
                        l.append(mul)
                    mul = 1
                    count = 0

            self.logger_set.log("Numeric Multiplication of set is done", "INFO")
            return l
        except Exception as e:
            self.logger_set.log("multiplication_elements_set","INFO")
            self.logger_set.log(e, "ERROR")

    def flatten_elements_set(self):
        '''
        The function is used to flatten the set elements to list  from input list
        '''
        try:
            l1=[]
            self.logger_set.log("Starting Flattening the set Elements  from input data", "INFO")
            for i in self.sample_list:
                if type(i) == set:
                    for j in i:
                        l1.append(j)


            self.logger_set.log("Flattening of set is done", "INFO")
            return l1
        except Exception as e:
            self.logger_set.log("flatten_elements_set","INFO")
            self.logger_set.log(e, "ERROR")


# creating the class for string related actions

class mystring:

    def __init__(self,sample_string):
        self.sample_string = sample_string
        self.logger_string = log_rec('log_file.txt','INFO','%(levelname)s %(asctime)s %(name)s %(message)s')
    def extract_vowels(self):
        '''
            The function is used to extract the vowels from the given
            string
        '''
        self.logger_string.log("Starting Extracting vowels from input data", "INFO")
        output_vowels=[]
        try:
            for i in self.sample_string:
                if i in ['A','a','e','E','i','I','o','O','u','U']:
                    output_vowels.append(i)
            self.logger_string.log("Vowels are Extracted now ","INFO")
            return output_vowels
        except Exception as e:
            self.logger_string.log("extract_vowels", "INFO")
            self.logger_string.log(e,"ERROR")

    def string_customized_len(self):
        '''
            The function is used to extract the substring from the
            given input string

        '''

        len_string = 0
        self.logger_string.log("Starting Finding Length of input string","INFO")
        try:
            for j in self.sample_string:
                    len_string = len_string +1
            self.logger_string.log("Length is calculated from string ","INFO")
            return len_string
        except Exception as e:
            self.logger_string.log("string_customized_len", "INFO")
            self.logger_string.log(e,"ERROR")


    def count_occurences_string(self):
        '''
        The function is used to count the number of occurences of
        elements present in string
        '''
        try:
            self.logger_string.log("Starting Counting the occurences of Elements in string from input data", "INFO")
            l1 = []
            count_dict = {}
            l1 = list(self.sample_string)
            for k in set(l1):
                count_dict[k] =  l1.count(k)
            self.logger_string.log("Occurences in string are Counted now ", "INFO")
            return count_dict
        except Exception as e:
            self.logger_string.log("count_occurences_string", "INFO")
            self.logger_string.log(e, "ERROR")


input_list = [[1,2,3,4],(2,3,4,5,6),(3,4,5,6,7),
              set([23,4,5,45,4,4,5,45,45,4,5]),
              {"k1":"sudh","k2":"ineuron","k3":"kumar",3:6,7:8},
              ["ineuron","data science "]]

l = mylist(input_list)

print(l.extract_list_type())
print(l.extract_numbers())
print(l.summation_elements())
print(l.extract_odd_numbers())
print(l.count_occurences())
print(l.string_filter())
print(l.alphanumeric_filter())
print(l.multiplication_elements())
print("===============================")

d = mydict(input_list)
print(d.extract_dict_type())
print(d.extract_numbers_dict())
print(d.summation_elements_dict())
print(d.extract_odd_numbers_dict())
print(d.count_occurences_dict())
print(d.string_filter_dict())
print(d.alphanumeric_filter_dict())
print(d.multiplication_elements_dict())
print(d.flatten_elements_dict())

print("===============================")

t = mytuple(input_list)
print(t.extract_tuple_type())
print(t.extract_numbers_tuple())
print(t.summation_elements_tuple())
print(t.extract_odd_numbers_tuple())
print(t.count_occurences_tuple())
print(t.string_filter_tuple())
print(t.alphanumeric_filter_tuple())
print(t.multiplication_elements_tuple())
print(t.flatten_elements_tuple())


print("===============================")

s = myset(input_list)
print(s.extract_set_type())
print(s.extract_numbers_set())
print(s.summation_elements_set())
print(s.extract_odd_numbers_set())
print(s.count_occurences_set())
print(s.string_filter_set())
print(s.alphanumeric_filter_set())
print(s.multiplication_elements_set())
print(s.flatten_elements_set())

print("================================")

input_string = "python Programming"

st = mystring(input_string)
print(st.extract_vowels())
print(st.string_customized_len())
print(st.count_occurences_string())