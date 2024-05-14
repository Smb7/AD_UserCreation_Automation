import pyad.aduser 
import pyad.adcontainer

# STEP1: Create user input for name, userid, password
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
        pyad.adcontainer.set_defaults(ldap_server="Kratos")

        # Get the container object where the user should be created
        container = pyad.adcontainer.ADContainer.from_dn("OU=Users,DC=Kratos,DC=com")  # Adjust the OU accordingly

        # Create user account 
        new_user = pyad.aduser.ADUser.create(
            f"CN={userid}",  # Adjust the distinguished name (DN) if needed
            password=password,
            optional_attributes={
                'givenName': first_name,
                'sn': last_name,
                'displayName': f"{first_name} {last_name}",
                'description': 'Created via python script'
            },
            container_object=container
        )
    except Exception as e:
        print(f"Error creating user account: {e}")

# Collect user information
first_name, last_name, userid, password = setup()

# Create user account
create_user(first_name, last_name, userid, password)


