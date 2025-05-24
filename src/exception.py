import sys 


def error_message_details(error,error_detail: sys):
    """
    This function takes an error and its details, and returns a formatted string
    containing the error message and the file name and line number where the error occurred.
    """
    # file_name = exc_tb.tb_frame.f_code.co_filename #file name where error occurred
    # _,_,exc_tb =  error_detail.exc_info() #execution info , first two info not interested last one we are using 
    _, _, exc_tb = error_detail.exc_info()  #  define exc_tb first
    file_name = exc_tb.tb_frame.f_code.co_filename  #  then use it

    error_message = "Error occurred in python script name [{0}] at line number [{1}] error message [{2}]".format(

        #frist place holder , second place holder , third place holder
        file_name,exc_tb.tb_lineno,str(error))


    return error_message
    
class CustomException(Exception):
    """
    Custom exception class that inherits from the built-in Exception class.
    It initializes with an error message and error details, and formats the error message.
    """
    def __init__(self,error_message, error_detail: sys):
        super().__init__(error_message)
        self.error_message = error_message_details(error_message, error_detail= error_detail)

    def __str__(self):
        """
        Returns the formatted error message when the exception is converted to a string.
        """
        return self.error_message
    

