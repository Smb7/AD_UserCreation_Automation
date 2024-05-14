import pyad
import pyad.aduser 

#STEP1: Create user input for name, userid, password
def setup():
    while True:
        first_name = input("Enter first name: ")
        last_name = input("Enter last name: ")
        userid = input("Enter UserID: ")
        password = input("Enter password: ")
        password_confirm = input("Enter password again: ")
        if password == password_confirm:
            break
        else:
            print("Password does not match, please try again.")
    return first_name, last_name, userid, password

def create_user(first_name, last_name, userid, password):
    try:    
        # Connect to Active Directory
        pyad.set_defaults(ldap_server="Kratos")

        # Create user account 
        new_user = pyad.aduser.ADUser.create(
            userid, 
            password=password,
            optional_attributes={
                'givenName': first_name,
                'sn': last_name,
                'displayName': f"{first_name} {last_name}",
                'description': 'Created via python script'
            }
        )
        print("User account created successfully")
    except pyad.pyadexceptions.ADObjectAlreadyExistsError:
        print(f"User '{userid}' already exists.")
    except pyad.pyadexceptions.ADCommunicationError as e:
        print(f"Communication error with Active Directory: {e}")
    except Exception as e:
        print(f"Error creating user account: {e}")

# Collect user information
first_name, last_name, userid, password = setup()

# Create user account
create_user(first_name, last_name, userid, password)


