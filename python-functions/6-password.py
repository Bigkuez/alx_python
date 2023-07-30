def validate_password(password):
    is_valid = True 
    if len(password) < 8: 
        is_valid = False    
    if not any(char.isdigit() for char in password): 
        is_valid = False
          
    if not any(char.isupper() for char in password): 
        is_valid = False     
    if not any(char.islower() for char in password):  
        is_valid = False
    if any(char.isspace() for char in password): 
        is_valid = False
    return is_valid 
