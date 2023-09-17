import calapp
import file_system
import ip_finder
import about

while True:
    bs = input('welcome to python os. where do you like to go? ')
    if bs == 'stop':
        break
    if bs == 'help':
        print(['cal app', 'help', 'stop', 'files', 'IP'])
    if bs == 'cal app':
        calapp.callapp()
    if bs == 'files':
        file_system.files()
    if bs == 'IP':
        ip_finder.ipfinder()
    if bs == 'about':
        about.aboutos()
