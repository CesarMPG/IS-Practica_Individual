class View:
   
    def start(self):
        print('==================================')
        print('= Welcome to the Cinema   =')
        print('==================================')

    def end(self):
        print('================================')
        print('=        See you later!       =')
        print('================================')

    def admin_menu(self):
        print('======================================')
        print('=        Admin Login      =')
        print('======================================')
        print('1. Login with admin ID')
        print('2. Create new admin')
        print('3. Return')

    def logged_admin_menu(self):
        print('======================================')
        print('=        Admin Menu       =')
        print('======================================')
        print('1. Admins')
        print('2. Movies')
        print('3. Halls')
        print('4. Seats')
        print('5. Schedules')
        print('6. Return')

    def user_main_menu(self):
        print('============================================')
        print('=        User Main Menu         =')
        print('============================================')
        print('1. Login / Sign in')
        print('2. Schedules')
        print('3. Return')

    def option(self,last):
        print('Select an option (1-'+last+'): ', end = '')

    def not_valid_option(self):
        print('Invalid option!\nTry again')
    
    def ask(self, output):
        print(output, end = '' )
    
    def msg(self, output):
        print(output)

    def ok(self, id, op):
        print('+'*(len(str(id))+len(op)+24))
        print('+ ¡'+str(id)+' was '+op+' successfully! +')
        print('+'*(len(str(id))+len(op)+24))
    
    def error(self, err):
        print(' ERROR! '.center(len(err)+4,'-'))
        print('- '+err+' -')
        print('-'*(len(err)+4))

    def show_midder(self):
        print('-'*156)
    
    def show_footer(self):
        print('-'*156)
    
    def admin_submenu(self):
        print('************************')
        print('* -- Admins submenu -- *')
        print('************************')
        print('1. Add admin')
        print('2. Show all admins')
        print('3. Show admins by name')
        print('4. Update admin')
        print('5. Delete admin')
        print('6. Return')
    
    def show_a_admin(self, record):
        print(f'{record[0]:<6}|{record[1]:<35}|{record[2]:<35}|{record[3]:<35}|{record[4]:<35}')
    
    def show_admin_header(self, header):
        print(header.center(78,'*'))
        print('Admin ID'.ljust(6)+'|'+'Name'.ljust(35)+'|'+'Last name'.ljust(35)+'|'+'Email'.ljust(35)+'|'+'Phone'.ljust(35))
        print('-'*156)

    
    def user_menu(self):
        print('**************************')
        print('* -- Users submenu -- *')
        print('**************************')
        print('1. Login with user ID')
        print('2. Create new user')
        print('3. Return')



    def user_logged(self):
        print('1. Update user')
        print('2. Delete user')
        print('3. Schedules menu')
        print('4. Tickets menu')
        print('5. Return')
    
    def show_a_user(self, record):
        print(f'{record[0]:<6}|{record[1]:<35}|{record[2]:<35}|{record[3]:<35}|{record[4]:<35}')
    
    def show_user_header(self, header):
        print(header.center(78,'*'))
        print('User ID'.ljust(6)+'|'+'Name'.ljust(35)+'|'+'Last name'.ljust(35)+'|'+'Email'.ljust(35)+'|'+'Phone'.ljust(35))
        print('-'*156)

    def show_user_midder(self):
        print('-'*156)
    
    def show_user_footer(self):
        print('-'*156)


    def movie_menu(self):
        print('*********************')
        print('* -- Admin Movie Menu -- *')
        print('*********************')
        print('1. Add Movie')
        print('2. Show movie')
        print('3. Show all movies')
        print('4. Show movies by title')
        print('5. Update movie')
        print('6. Delete movie')
        print('7. Return')

    def user_main_menu_movie(self):
        print('***************************')
        print('* -- User Movie Menu -- *')
        print('***************************')
        print('1. Show movie')
        print('2. Show all movies')
        print('3. Show movies by title')
        print('4. Return')
    
    def show_a_movie(self, record):
        print('Movie ID: ', record[0])
        print('Title:', record[1])
        print('Duration: ', record[2])
        print('Language: ', record[3])
        print('Subtitles: ', record[4])

    def show_movie_header(self, header):
        print(header.center(53,'*'))
        print('-'*53)

    def show_movie_midder(self):
        print('-'*53)
    
    def show_movie_footer(self):
        print('*'*53)
        
    
    def hall_menu(self):
        print('**************************')
        print('* -- Halls menu    -- *')
        print('**************************')
        print('1. Add hall')
        print('2. Show hall')
        print('3. Show all halls')
        print('4. Show halls by number of seats')
        print('5. Update hall')
        print('6. Delete hall')
        print('7. Return')

    def show_hall_header(self, header):
        print(header.center(53,'*'))
        print('-'*53)
    
    def show_a_hall(self, record):
        print('Hall ID:', record[0])
        print('Number of seats:', record[1])

    def seat_menu(self):
        print('*****************************')
        print('* -- Seats menu    -- *')
        print('*****************************')
        print('1. Add seat')
        print('2. Show seat')
        print('3. Show all seats')
        print('4. Show seats by status (free/taken):')
        print('5. Show seats by hall') 
        print('6. Reserve seat')
        print('7. Restore all seats ')
        print('8. Delete seat')
        print('9. Return')

    def show_seat_header(self, header):
        print(header.center(53,'*'))
        print('-'*53)
    
    def show_a_seat(self, record):
        if record[1] == 0x00:
            disp = 'free'
        else:
            disp = 'taken'
        print('Seat:', record[0])
        print('Status: ', disp)
        print('Hall:', record[2])
    
    def show_a_seat_disp(self, record):
        print('Seat:', record[0])

    
    def schedule_menu(self):
        print('******************************')
        print('* -- Admin Schedule Menu    -- *')
        print('******************************')
        print('1. Add schedule')
        print('2. Show schedule')
        print('3. Show all schedules')
        print('4. Show schedules by movie title')
        print('5. Show schedules by date')
        print('6. Update schedule')
        print('7. Delete schedule')
        print('8. Return')
    
    def user_main_menu_schedule(self):
        print('******************************')
        print('* -- User Schedule Menu    --  *')
        print('******************************')
        print('1. Show all schedules')
        print('2. Show schedules by movie title')
        print('3. Show schedules by date')
        print('4. Return')

    def show_schedule_header(self, header):
        print(header.center(53,'*'))
        print('-'*53)
    
    def show_a_schedule(self, record):
        print('Schedule ID:', record[0])
        print('Date and Time:', str(record[2]) +', '+ record[1])
        print(record[6]+' in '+ record[8]+' with '+ record[9] + ' subtitles')
        print('Hall: ',record[4])
        
    
    def ticket_menu(self):
        print('****************************')
        print('* -- Admin ticket menu    -- *')
        print('****************************')
        print('1. Add ticket')
        print('2. Show ticket')
        print('3. Show all tickets')
        print('4. Show tickets by user ID:')
        print('5. Show tickets by schedule ID')
        print('6. Return')
    
    def user_main_menu_tickets(self):
        print('****************************')
        print('* -- User Ticket Menu    -- *')
        print('****************************')
        print('1. Buy a ticket')
        print('2. Show all tickets from user:') 
        print('3. Return')

    def show_ticket_header(self, header):
        print(header.center(53,'*'))
        print('-'*53)
    
    def show_a_ticket(self, record1,record2):
        print('Ticket ID:', record1[0])
        print('User name:', record1[10], ' '+ record1[11])
        print('Date: ', str(record1[6])+' Time: '+record1[5])
        print(record2[1] +' in '+ record2[3] +' with '+ record2[4]+ ' subtitles')
        print('Hall: ',str(record1[8]) +' Seat: '+str(record1[3]))
       

    
    