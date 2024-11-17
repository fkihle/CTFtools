##############################################
#       CTF Tool Template - TargetURL        #
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
def ctf_tool(target_url, target_port):
    
    """
    TOOL DESCRIPTION HERE
    """
    # Add imports here
    #import ...
    
    try:

        # ADD YOUR LOGIC HERE
        result = "No logic created yet."
        
        print(result)
                
    except Exception as e:
        return f"An error occurred: {e}"
    
###--------------------- END OF CTF TOOL --------------------###
################################################################


# Main function to parse command line arguments
def main(argv):
    
    target_url = ''
    target_port = ''

    # Parse command line arguments
    opts, args = getopt.getopt(argv,"hu:p:",["target_url=","target_port="])
    
    if not opts:
        logger.error('Expected: python <CTFtool name>.py -u <url> -p <port/range>\n')
        sys.exit()
        
    # Iterate through the options and arguments
    for opt, arg in opts:
        # If the user requests help, print the usage and exit
        if opt == '-h':
            print('python <CTFtool name>.py -u <url> -p <port/range>')
            sys.exit()
        elif opt in ("-u", "--url"): # If the user specifies the target url
            target_url = arg
        elif opt in ("-p", "--port"): # If the user specifies the target port[s]
            target_port = arg

    # Print the target url and port[s] (nice for debugging)        
    logger.info('Target URL is %s', target_url)
    logger.info('Target port is %s', target_port)
    
    # Call the CTF tool function
    ctf_tool(target_url, target_port)



# Execute the main function
if __name__ == "__main__":
    main(sys.argv[1:])