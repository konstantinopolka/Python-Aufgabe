#import a part of the library to get the current time und the current date
from datetime import datetime
import os
import platform


def print_names():
    #declare und define the first name und the last name
    # of this programm`s creator 
    first_name = "Kostiantyn"
    last_name  = "Sotnikov"

    print("Der Vorname und der Zu- beziehungsweise Nachname" +
        "vom Entwickler dieses Wunderprogramms sind:")
    print(first_name + " " + last_name + "\n")
    
#print the current data and time using the module datetime
def print_data_and_time():
    print("das aktuelle Datum und die aktuelle Uhrzeit sind:")
    #the method now from "datetime" returns the current time and date
    print(datetime.now().__str__() + "\n") 
    
#print the current data and time using the module platform
def print_windowsVersion():
    if platform.system() == "Windows":
        print("die aktuelle Version Ihres Betriebsystems ist:")
        #the methods system and version from "platform" return the name of the operating system and its version
        print(platform.system()  + " " +  platform.version() + "\n")

def print_pythonVersion():
    print("Ihre aktuelle Python Version  ist:")
    #the method python_version from "platform" returns the version of python on your computer 
    print(platform.python_version() + "\n")

def answer_questions():
    
    #gets the number of questions and returns a dictionary with keys as the questions and tuples with the length 2
    #the first element of such a tuple is the true answer
    #the zeroth element of such a tuple is the false answer
    def get_questions_and_answers(questionsCount = 1):
        table = dict()
        
        #It can be another way to get questions and answers, for the example from a server
        
        #To prove if not too many questions have been added than the number given over
        if len(table) <  questionsCount:
            question1 = "Sind Sie Mensch?"
            answers1 = ("Jegliches intelligente Wesen ist auch willkommen. Ich begrüße Sie!", "Herzlichen Glückwunsch!")
            table[question1] = answers1
            
        if len(table) <  questionsCount:
            question2 = "Kann man aus einer Lüge schullfolgernd eine wahrhaftige Aussage bekommen?"
            answers2 = ("Leider ist Ihre Antwort falsch\n" + \
                                "Hier ist die Wahrheitstafel der Implikation, einer Operation der Aussagenlogik:\n" + \
                                "X Y X->Y\n" + \
                                "0 0  1\n" + \
                                "0 1  1\n" + \
                                "1 0  0\n" + \
                                "1 1  1\n" + \
                                "Von deren zweiten Zeile zu sehen ist, " + \
                                "dass man von einer falschen Aussage X zu einer wahren Y kommen kann", \
                                    
                        "Sie dürften die Grundlagen der formellen Logik schon mal gelernt haben. Sehr gut!")
            table[question2] = answers2
        return table
    
    #the console is cleared using the module system 
    def clear_console():    
        os.system('cls' if os.name == 'nt' else 'clear')
        
    #these infos are shown before every question   
    def print_info():
        print_systemInfo()
        #the following info can exist only in the context of replying the questions
        print("Jede Frage können Sie mit ja(j) oder nein(n) beanwtorten")
        print("Mit der Taste b beenden Sie das Programm")
        print("\n")
        print("Die nächste Frage lautet:")
        
    #check before every action by the user if they have typen in the b-key
    #and if true, finish the program    
    def is_end():
         if input("\nGeben Sie bitte ein belibieges Symbol zum Fortsetzen ein.\nMit b Beenden Sie ja das Programm\n") == 'b':
            print("Das Programm ist beendet")
            return True
    
    quiestionsCount = 2
    table = get_questions_and_answers(quiestionsCount) # get the table with the questions and the answers
    print(f"Antworten Sie bitte auf ein paar Fragen und zwar auf {quiestionsCount}")
    
    #transition to the questions
    if is_end() == True:
        return False
    clear_console()
    
    #go through the table 
    for quiestion in table:
        clear_console()
        print_info()
        print(quiestion)
        
        # the user is asked till a correct symbol is typed in
        while True:
            user_key = input()
            #show the answer
            if user_key == "j":
                print(table[quiestion][1]) #the right answer
                break
            elif user_key == "n":
                print(table[quiestion][0]) #the false answer
                break
            elif user_key == "b":
                print("Das Programm ist beendet") #the end of the program without answering
                return False
            else:
                clear_console()
                print_info()
                print(quiestion)
                print("Geben Sie bitte ein richtiges Zeichen ein!")  
            #transition to the next question
        if is_end() == True:
            return False
    return True
    # A False is given back to send a signal for finishing the outer function

#the system infos that are shown when the program is started and every time when the user is asked a question
def print_systemInfo():
    print_names()
    print_data_and_time()
    print_windowsVersion()
    print_pythonVersion()
    
#the main function of the program, the point of entrance into the skript    
def main():
    print_systemInfo()
    if answer_questions() == False: return

# the call of the main function, the start of the program  
main()
    
    


