##############################################
#       CTF Tool Template - Input file       #
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
def ctf_tool(input_file_path):
    
    """
    TOOL DESCRIPTION HERE
    """
    try:
        with open(input_file_path, 'r', encoding='latin-1') as infile:
            for line in infile:
                
                # Prosess each line here
                result = line # Remove this line
                #result = {PROCESS LOGIC HERE} # Add your logic here
                
                # Print the result to screen
                print(result)

    except Exception as e:
        return f"An error occurred: {e}"
    
###--------------------- END OF CTF TOOL --------------------###
################################################################


# Main function to parse command line arguments
def main(argv):
    
    inputfile = ''

    # Parse command line arguments
    opts, args = getopt.getopt(argv,"hi:",["ifile="])
    
    if not opts:
        logger.error('Expected: python <CTFtool name>.py -i <inputfile>\n')
        sys.exit()
        
    # Iterate through the options and arguments
    for opt, arg in opts:
        # If the user requests help, print the usage and exit
        if opt == '-h':
            print('python <CTFtool name>.py -i <inputfile>')
            sys.exit()
        elif opt in ("-i", "--ifile"): # If the user specifies the input file
            inputfile = arg

    # Print the input file path (nice for debugging)        
    logger.info('Input file is ', inputfile)
    
    # Call the CTF tool function
    ctf_tool(inputfile)



# Execute the main function
if __name__ == "__main__":
    main(sys.argv[1:])