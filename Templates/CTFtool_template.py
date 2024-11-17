##############################################
#               CTF Tool Template            #
##############################################

# sys:             used to access command line arguments
# getopt:          used to parse command line arguments
# create_logger:   used to create a custom logger
import sys, getopt
from create_logger import create_logger

# ################################################################
# ###                         LOGGING                          ###
# ################################################################

# # logging.debug()    # - DEBUG.    Provides detailed information that’s valuable to you as a developer.
# # logging.info()     # - INFO.     Provides general information about what’s going on with your program.
# # logging.warning()  # - WARNING.  Indicates that there’s something you should look into.
# # logging.error()    # - ERROR.    Alerts you to an unexpected problem that’s occured in your program.
# # logging.critical() # - CRITICAL. Tells you that a serious error has occurred and may have crashed your app

# Create custom logger. 
# Change the log level to 'INFO', 'WARNING', 'ERROR', 'CRITICAL' or 'DEBUG'
logger = create_logger('DEBUG')

# ###--------------------- END OF LOGGING ---------------------###
# ################################################################


################################################################
###      CREATE THE CTF TOOL FUNCTION IN THE BLOCK BELOW     ###
################################################################
def ctf_tool():
    
    """
    TOOL DESCRIPTION HERE
    """
    try:
        # Add your logic here
        result = "No logic created yet."
        
        # Print the result to screen
        print(result)

    except Exception as e:
        return f"An error occurred: {e}"
    
###--------------------- END OF CTF TOOL --------------------###
################################################################



# Execute the main function
if __name__ == "__main__":
    ctf_tool()                  # Call the CTF tool function