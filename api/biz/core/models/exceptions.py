"""
Declarations of custom exceptions
"""

class ResourceExistingException(Exception):
    '''
    Identifies a generic exception occurring when trying to create a resource that already exists
    '''
    def __init__(self, message):           
        super().__init__(message)
        self.message = message

class InvalidUserException(Exception):
    '''
    Identifies an exception occurring when User entity does not pass validation
    '''
    def __init__(self, message):           
        super().__init__(message)
        self.message = message
