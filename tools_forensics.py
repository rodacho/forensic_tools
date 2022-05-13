from fileinput import filename
import os
import subprocess
menu_options = {
    1: 'Use Sysinternals',
    2: 'Use Volatility',
    3: 'Use Mactime',
    4: 'Exit',
}

def print_menu():
    for key in menu_options.keys():
        print (key, '--', menu_options[key] )

def sysinternal():
  os.chdir(os.getcwd())
  fecha=os.popen('date /t>inves/fecha.txt')
  hora=os.popen('time /t>inves/hora.txt')
  procesos=os.popen('pslist>inves/procesos.txt')
  librerias=os.popen('listdlls>inves/librerias.txt')
  conexiones=os.popen('netstat -an>inves/conexiones.txt')
  infosystem=os.popen('psinfo>inves/infosystem.txt')
  eventos=os.popen('psloglist>inves/eventos.txt')
  servicios=os.popen('psservice>inves/servicios.txt')
  usuarios=os.popen('psloggedon>inves/usuarios.txt')
  iparp=os.popen('arp -a>inves/iparp.txt')


def option2():
     pathimage=raw_input('insert the path of the image')
     outp=subprocess.call(['python','vol.py','imageinfo','-f',pathimage],shell=True)

def macmatch():
    path_input=raw_input('Enter the path :')
    mactime=raw_input('type one of the following: -m = last write time -a = last access time -c = creation time: ')
    inicial_date=raw_input('type initial date (YYYY-MM-DD:HH.MM): ')
    end_time=raw_input('type end time date (YYYY-MM-DD:HH.MM): ')
    with open('mactime.txt','w') as f:
            outp=subprocess.call(['macmatch.exe',path_input,mactime,inicial_date,end_time],stdout=f,shell=True)

if __name__=='__main__':
    while(True):
        print_menu()
        option = ''
        try:
            option = int(input('Enter your choice: '))
        except:
            print('Wrong input. Please enter a number ...')
        #Check what choice was entered and act accordingly
        if option == 1:
           sysinternal()
        elif option == 2:
            option2()
        elif option == 3:
            macmatch()
        elif option == 4:
            print('Thanks message before exiting')
            exit()
        else:
            print('Invalid option. Please enter a number between 1 and 4.')


    

    
