from Website_files.ebay import check_ebay_account
from Website_files.espn import check_account_espn
from Website_files.pinterest import check_pinterest_account
from Website_files.quora import check_account_quora
from Website_files.spotify import check_account_spotify
from prettytable import *
from colorama import *

def check(email,domain):

    if domain == "ebay":
        return check_ebay_account(email)

    elif domain == "espn":
        return check_account_espn(email)

    elif domain == "pinterest":
        return check_pinterest_account(email)

    elif domain == "quora":
        return check_account_quora(email)

    elif domain == "spotify":
        return check_account_spotify(email)

    else:
        return False

def tool_info(command):
    tool_name = '''

░█▀▀█ ▒█▀▀█ ▒█▀▀█ █▀▀█ ▒█░▒█ ▒█▄░▒█ ▀▀▀█ ░░ ▒█▀▀█ ▒█░▒█ █▀▀█ ▒█▀▀█ ▒█░▒█ 
▒█▄▄█ ▒█░░░ ▒█░░░ █▄▀█ ▒█░▒█ ▒█▒█▒█ ░░█░ ▀▀ ▒█░░░ ▒█▀▀█ ░░▀▄ ▒█░░░ ▒█▀▀█ 
▒█░▒█ ▒█▄▄█ ▒█▄▄█ █▄▄█ ░▀▄▄▀ ▒█░░▀█ ░▐▌░ ░░ ▒█▄▄█ ▒█░▒█ █▄▄█ ▒█▄▄█ ▒█░▒█
    '''
    tool_desc1 = 'ACC0UN7-CH3CK Tool is an account Knocking tool that uses Selenium to check whether an account exists on popular websites such as ebay, espn, quora, spotify, and pinterest. '
    tool_desc2 = 'The tool is used to avoid the manual checking of the account exists in the website using the email address by Automating the process using the Webscraping tool with Python'
    if(command == 'help'):
        return tool_name + '\n' + tool_desc1
    else:
        print(Back.BLACK,Fore.LIGHTCYAN_EX,tool_name)
        print(tool_desc1+tool_desc2,Fore.RESET)

def main(email,url):
    tool_info("main")
    url_list = url.strip().split(",")

    # Displaying the Result
    # Create a PrettyTable instance
    table = PrettyTable()

    # Define table columns
    table.field_names = ["Website List", f"{email}"]

    for url in url_list:
        if(url.lower() in ['ebay','espn','pinterest','quora','spotify']):
             check_account_status = check(email,url.lower())
            # Add data to the table
            if check_account_status == True :
                table.add_row([url , "Yes"])
            elif check_account_status == False :
                table.add_row([url , "No"])
            else:
                table.add_row([url, "Error"])

    print('\n')
    print(Fore.LIGHTGREEN_EX,table,'\n')

import typer

app = typer.Typer()

@app.command(help=tool_info("help"))
def run_main(email: str=typer.Option("-email",prompt="Enter the email-id"), url: str=typer.Option("-url", prompt="Enter website names (ebay,espn,pinterest,quora,spotify)")):
   main(email,url)

if __name__ == "__main__":
    app()
