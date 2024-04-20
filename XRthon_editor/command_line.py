import installer, os
from folders import folder
from text import Edition_logs, Command_table


def V():
    E_L_T = ''.join(Edition_logs)
    E_L_T_L = E_L_T.split('\n')
    L_ = []
    for text in E_L_T_L:
        if 'V' and 'BETA' in text:
            L_.append(text)
    text_1 = L_[len(L_) - 1].split(' > ')
    text_2 = text_1[1].split(' V')
    Version = text_2[0]
    return Version

print(f''' > XRthon_editor
 > Version {V()}
 > Author sxxyrry （是星星与然然呀）''')

while True:
    inputs: str = input(' > command line (\'quit\' for quit, \'C_T\' for command table, \'E_L\' for edition logs)>>>')
    if inputs == 'quit':
        break
    elif inputs == 'C_T':
        print(Command_table)
    elif inputs == 'E_L':
        print(Edition_logs)
    elif inputs == 'XRi' or inputs == 'XR_i' or inputs == 'XR_ister' or inputs == 'XR_installer':
        command = input(' > please input the command (\'install\' for install)>>>')
        if command == 'install':
            _inputs = input(' > please input the Please enter the mode (\'module\' or \'package\') >>>')
            if _inputs == 'module':
                name = input(' > please input the name of the module >>>')
                import_list = []
                installer.installer.install(name, 'module')
            elif _inputs == 'package':
                name = input(' > please input the name of the package >>>')
                import_list = []
                installer.installer.install(name, 'package')
            else:
                print(f' > No command for {_inputs}')
        else:
            print(f' > No command for {command}')
    else:
        print(f' > No command for {inputs}')
