from functools import wraps

#Створюємо декоратор для обробки помилок 
def input_error(func) :
    def inner(*args, **kwargs) :
        try :
            return func(*args, **kwargs)
        except ValueError:
            print(ValueError)
            return "Enter the argument for the command"
        except KeyError :
            print(KeyError)
            return  "Name is Not Found"
        except IndexError :
            print(IndexError)
            return "Enter the argument for the command"
    return inner


#Функції для обробки запитів 
@input_error
def parse_input(user_input):
    cmd, *args = user_input.split()
    cmd = cmd.strip().lower()
    return cmd, *args

@input_error
def add_contact(args, contacts):
    name, phone = args
    if name not in contacts :
        contacts[name] = phone
        return "Contact added."
    else :
        return "Contact already exists"

@input_error
def  change_contact(args, contacts):
    name, phone = args
    if name in contacts :
        contacts[name] = (phone)
        return "Contact updated."
    else:
        return f"Contact {name} not found"

@input_error  
def show_phone(args, contacts) :
    name = args[0] 
    if name in contacts :
        return contacts[name]
    else:
        return f"Contact {name} not found"


@input_error
def show_all(contacts):
    if len(contacts)>0 :
        return contacts
    else: 
        return "Сontact list is empty"



