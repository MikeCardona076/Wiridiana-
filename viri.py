from sympy import sympify
import os, time

def bienvenida():
    time.sleep(2)
    os.system ("cls") 
    print("""
    Hola Wiri,
    1 = Simplificar 
    2 = Resolver expresiones
    """)
    try:
        eleccion = int(input('Ingresa opcion: '))
        if eleccion == 1:
            try:
                print("""
                Recordar que para elevar un numero se debe de poner **, por ejemplo 3x**2 = x3^2
                y recordar 3*x = 3x (vale para cualquier numero con una variable)
                """)
                ingreso = input("Ingresar expresion a simplificar: ")
                Wiridiana_simplificar(ingreso)
            except:
                print('Algo salio mal Wiri, intenta de nuevo')

        else:
            operacion = input("Ingresar operacion: ")
            Wiridiana_eval(operacion)
    except:
        print('Algo salio mal Wiri, intenta de nuevo')



def Wiridiana_eval(operacion):
    try:
        print(eval(operacion))
    except:
        print('Algo salio mal Wiri, intenta de nuevo')

def Wiridiana_simplificar(ecuacion):

    try: 
        print(sympify(ecuacion))
    except:
        print('Algo salio mal Wiri, intenta de nuevo')

print("""
    %###%&@@@@@@@@@@&&&&@@@@@@@@%@@&@@@&&&&&%/(*,.................,...........,,,,,,
    %%%%&&@@@@@@@&@&&&&&@@@@@@@@&&&@&@@@@@@@&@@&(**...............,......,....,,,,,,
    %#&@@@@@@@@@@@@@@@&@@@@@@@@&&@@@@@@@@@@@@@@@@%(,/.........................,,,,,,
    @@@@@@@@@@@@@@%(/*/*****(&&&@@@@@&@@@@@@@@@@@@@(#(.,.....................,,,,,,,
    @@@@&@@&%%(((/**,,,,,,,,**#@@@@@@@@@@@@@@@@@@@@&&&#//,,,................,,,,,,,,
    @@@@@@@%(/*******,,,,,,,/#/*@@@@@@@@@@%@@@@@@@@@@@&%#/,,....,,.....,,,,,,,,,,,,,
    @@@@@@#(//*******,,,,*/##/*#*@&@@@@@@@@@@@@@@@@@@@@@&(#*.,,.,,,.......,,,,,,,,,,
    @@@@@@%(//***********/(///%%*//*,,.,,***(%@@@@@@@@@@@@@@#/,. , ,............,,..
    @@@@@@@%#(///***********/*/*/*,,,,,,,,**//#@@@@&@@@@@@@@@@%*,.,,.,,,.,,,,,,,,,,,
    @@@@@@@@@%#(////(#((//*,,,,,,,,,,*****////#&@@@@@@@@@@@@@&@&&**,,,,,,,,,,,,,,,,,
    @@@@@@@@@@@%(#&&#//#%((/*,,,****/******/**/&@@@@@@@&@@@@@@@@@@@@@@@@@,,,,,,,,,,,
    @@@@@@@@@@@@@&((#&/&//**(/,,.**(%*,,,*((///(@@@@@@@@@@@@@@&&&&&@&&@@@&%%**,,,,,,
    @@@@@@@@@@@@@@@@&%#(/****///*(#(*,,,%#/***//@@@@@@@@@@@@@@@@@&&@#//*/#@@@@&#(*,,
    @@@@@@@@@@@@@@@@@@(/*******(%%%/*#&#(#//****&@@@@@@@@@@@@@@@&&&@&&**,*,@%*(@&&@(
    &@@@@@@@@@@@@@@@@@@@((////////(%&%%%#/*****/&@@@@#@@@@@@@@&@@@@@&@#,*,*(@%//@@@&
    *&#@@@@@@@@@@,*,,,,,*,/%&&#(((((((((//**//#@@@@@@@@@@@@@@@@%(@@@@@#*/*/*#(%#@@@%
    *&/(@@@@@@@#,,,,,,*,,,,,,,,***(#%%%%######%@&@@@@@@@@@@@@@@@#%@@@(%%##%&&&%(/@(%
    *#(#&%@@@@@#,..,,,,,**,,,,,,,,*,*,*,,,/*///#&@@@@@@@@@@@@@@@@@@**,,,/&/((&&%&@**
    ###&%@&@&&*,,,.,,,..,,(,,*,.,,,,,,,*,,.*,//&@@@@@@@@@@@@@&@@@%&.*,@@/@,*,/#**@**
    %%(&@&&@,,,,.,,,,,**,*,*(*,,,,,,,*,,/,,.**(@@@@@&&@@@@@@&@@@@@@@@#(/&(*,,,,**/**
    &@&&@@%%,,,....,,*,,*..,,*(,*,,,,*,,,#,,,,*@@@&%%&&@@@@@@@@@@%/,,,,,,,,,,,,,****
    @@@@@#*,,,,,***,...,**..,.,*(.,,,,,..,*,,**@@@@@%##@@@@@@@@@#*,,,,,,,,,,,,,,****
    @&@@&/.,,...,,,**,*,,,,,,.,,,(/,,,.,,,*,,,,*(@@@@#@@@&@&%@@@*,,,,,,,,,,,,,,**/**
    &&&&(,.....,..,,,*,*/,**,...,,,#*,,,,,,#,,,,,/&@@&@&@&@&@&/*,*,,,,,,,,,,,,,*/**/
    /@@&,,,***,*,,**,,**(****,,,**,*/(,,,,./,.,,*//&&@&&@@&((****,.,,,,,,,,,,,*//**/

    CARGANDO............................ 
""")
bienvenida()
    

