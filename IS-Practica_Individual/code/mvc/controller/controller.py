from model.model import Model
from view.view import View
from datetime import date

class Controller:
   
    def __init__(self):
        self.model = Model()
        self.view = View()
    
    def start(self):
        self.view.start()
        print('1) Admin menu')
        print('2) User menu')
        print('3) Exit')
        op = input()
        if op == '1':
            self.admin_menu()
        elif op == '2':
            self.user_main_menu()
        elif op == '3':
            self.view.end()
        else:
            self.view.not_valid_option()
        return
    
    def main_menu(self):
        o = '0'
        while o != '6':
            self.view.logged_admin_menu()
            self.view.option('6')
            o = input()
            if o == '1':
                self.admin_menu()
            elif o == '2':
                self.movie_menu()
            elif o == '3':
                self.hall_menu()
            elif o == '4':
                self.seat_menu()
            elif o == '5':
                self.schedule_menu()
            elif o == '6':
                self.start()
            else:
                self.view.not_valid_option()
        return

    
    
    
    def update_lists(self, fs , vs):
        fields = []
        vals = []
        for f,v in zip(fs,vs):
            if v != '':
                fields.append(f+' = %s')
                vals.append(v)
        return fields, vals

    def admin_submenu(self):
        o = '0'
        while o != '6':
            self.view.admin_submenu()
            self.view.option('6')
            o = input()
            if o == '1':
                self.create_admin()
            elif o == '2':
                self.read_all_admin()
            elif o == '3':
                self.read_admin_name()
            elif o == '4':
                self.update_admin()
            elif o == '5':
                self.delete_admin()
            else:
                self.view.not_valid_option()
        return

    def user_main_menu(self):
        o = '0'
        while o != '5':
            self.view.user_main_menu()
            self.view.option('5')
            o = input()
            if o == '1':
                self.user_menu()
            elif o == '2':
                self.user_main_menu_schedule()
            elif o == '3':
                self.start()
            else:
                self.view.not_valid_option()
        return
    
    def ask_admin(self):
        self.view.ask('Name: ')
        a_name = input()
        self.view.ask('Last name: ')
        a_lastName = input()
        self.view.ask('Email: ')
        a_email = input()
        self.view.ask('Phone: ')
        a_phone = input()
        return [a_name, a_lastName, a_email, a_phone] 
    
    def create_admin(self):
        a_name,a_lastName,a_email,a_phone = self.ask_admin()
        out = self.model.create_admin(a_name,a_lastName,a_email,a_phone)
        if out == True:
            self.view.ok(a_name+' '+a_lastName,' added')
        else:
            self.view.error('The user could not be added')
        return
    
    def read_admin(self,id_admin):

        admin = self.model.read_admin(id_admin)
        if type(admin) == tuple:
            self.view.show_admin_header('Info from Admin: '+id_admin+' ')
            self.view.show_a_admin(admin)
            self.view.show_midder()
            self.view.show_footer()
        else:
            if dir == None:
                self.view.error('The admin with this ID doesnt exist')
            else:
                self.view.error('A problem ocurred when reading the admin register')
        return
    
    def read_all_admin(self):
        admins = self.model.read_all_admin()
        if type(admins) ==  list:
            self.view.show_admin_header(' All Admins ')
            for admin in admins:
                self.view.show_a_admin(admin)
            self.view.show_midder()
            self.view.show_footer()
        else:
            self.view.error('A problem ocurred when reading the admin register ')
        
    
    def read_admin_name(self):
        self.view.ask('Admin name: ')
        a_name = input()
        a_names = self.model.read_admin_name(a_name)
        if type(a_names) == list:
            self.view.show_admin_header('Admins with name:  '+a_name+' ')
            for a_name in a_names:
                self.view.show_a_admin(a_name)
            self.view.show_midder()
            self.view.show_footer()
        else:
            self.view.error('A problem ocurred when reading the admin register ')
        return
    

    def update_admin(self):
        self.view.ask('ID of admin to update: ')
        id_admin = input()
        admin = self.model.read_admin(id_admin)
        if type(admin) == tuple:
            self.view.show_admin_header(' Info from admin '+id_admin+' ')
            self.view.show_a_admin(admin)
            self.view.show_midder()
            self.view.show_footer()
        else:
            if admin == None:
                self.view.error('The admin doesnt exist')
            else:
                self.view.error('A problem ocurred when reading the admin register')
            return
        self.view.msg(' Input the new values to update (Leave blank to skip): ')
        whole_vals =self.ask_admin()
        fields, vals = self.update_lists(['a_name','a_lastName','a_email','a_phone'], whole_vals)
        vals.append(id_admin)
        vals = tuple(vals)
        out = self.model.update_admin(fields,vals)
        if out == True:
            self.view.ok(id_admin, 'updated')
        else: 
            self.view.error('The admin could not be updated')
        return

    def delete_admin(self):
        self.view.ask('ID of admin to delete: ')
        id_admin = input()
        count = self.model.delete_admin(id_admin)
        if count != 0:
            self.view.ok(id_admin, 'deleted')
        else:
            if count == 0:
                self.view.error('The admin doesnt exist')
            else:
                self.view.error('The admin could not be deleted')
        return


    def user_menu(self):
        o = '0'
        while o != '3':
            self.view.user_menu()
            self.view.option('3')
            o = input()
            if o == '1':
                self.view.ask( 'User ID: ')
                user_id = input()
                self.login_user(user_id)
            elif o == '2':
                self.create_user()
            elif o == '3':
                self.user_main_menu()
            else:
                self.view.not_valid_option()
        return

    def admin_menu(self):
        o = '0'
        while o != '3':
            self.view.admin_menu()
            self.view.option('3')
            o = input()
            if o == '1':
                self.view.ask( 'Admin ID: ')
                admin_id = input()
                self.login_admin(admin_id)
            elif o == '2':
                self.create_admin()
            elif o == '3':
                self.start()
            else:
                self.view.not_valid_option()
        return
   

    def login_user(self ,user_id):
        o='0'
        while o != '5':
            self.read_user(user_id)
            self.view.user_logged()
            o = input()
            if o == '1':
                self.update_user(user_id)
            elif o == '2':
                self.delete_user(user_id)
            elif o == '3':
                self.user_main_menu_schedule()
            elif o == '4':
                self.user_main_menu_tickets(user_id)
            elif o == '5':
                self.user_main_menu()
            else:
                self.view.not_valid_option()
        return

    def login_admin(self ,admin_id):
        o = '0'
        while o != '6':
            self.read_admin(admin_id)
            self.view.logged_admin_menu()
            self.view.option('6')
            o = input()
            if o == '1':
                self.admin_submenu()
            elif o == '2':
                self.movie_menu()
            elif o == '3':
                self.hall_menu()
            elif o == '4':
                self.seat_menu()
            elif o == '5':
                self.schedule_menu()
            elif o == '6':
                self.admin_menu()
            else:
                self.view.not_valid_option()
        return
    def ask_user(self):
        self.view.ask('Name: ')
        u_name = input()
        self.view.ask('Last name: ')
        u_lastName = input()
        self.view.ask('Email: ')
        u_email = input()
        self.view.ask('Phone: ')
        u_phone = input()
        return [u_name, u_lastName, u_email, u_phone] 
    
    
    def create_user(self):
        u_name, u_lastName, u_email, u_phone = self.ask_user()
        out, user = self.model.create_user(u_name, u_lastName, u_email, u_phone)
        if out == True:
            self.view.ok('User ID: '+ str(user[0])+' User name: '+u_name+' '+u_lastName, ' added')
        else:
            self.view.error('User could not be added')
        return
    
    def read_user(self, id_user):
      
        user = self.model.read_user(id_user)
        if type(user) == tuple:
            self.view.show_user_header('Info from user: '+id_user+' ')
            self.view.show_a_user(user)
            self.view.show_midder()
            self.view.show_footer()
        else:
            if dir == None:
                self.view.error('User ID does not exist')
            else:
                self.view.error('There was a problem at reading the user')
        return
    
    def read_all_user(self):
        users = self.model.read_all_user()
        if type(users) ==  list:
            self.view.show_user_header(' All users')
            for user in users:
                self.view.show_a_user(user)
            self.view.show_midder()
            self.view.show_footer()
        else:
            self.view.error('There was a problem at reading the users ')
        
    
    def read_user_lname(self):
        self.view.ask('User Last name: ')
        u_lastName = input()
        u_lastNames = self.model.read_user_lname(u_lastName)
        if type(u_lastNames) == list:
            self.view.show_user_header('Users with last name:  '+u_lastName+' ')
            for u_lastName in u_lastNames:
                self.view.show_a_user(u_lastName)
            self.view.show_midder()
            self.view.show_footer()
        else:
            self.view.error('There was a problem at reading the users ')
        return
    

    def update_user(self,id_user):
        user = self.model.read_user(id_user)
        if type(user) == tuple:
            self.view.show_user_header(' Info from User '+id_user+' ')
            self.view.show_a_user(user)
            self.view.show_midder()
            self.view.show_footer()
        else:
            if user == None:
                self.view.error('The user does not exist')
            else:
                self.view.error('There was a problem at reading the user')
            return
        self.view.msg('  Input the new values to update (Leave blank to skip): ')
        whole_vals =self.ask_admin()
        fields, vals = self.update_lists(['u_name','u_lastName','u_email','u_phone'], whole_vals)
        vals.append(id_user)
        vals = tuple(vals)
        out = self.model.update_user(fields,vals)
        if out == True:
            self.view.ok(id_user, 'updated')
        else: 
            self.view.error('The user could not be updated')
        return

    def delete_user(self, id_usuario):
        count = self.model.delete_user(id_usuario)
        if count != 0:
            self.view.ok(id_usuario, 'deleted')
        else:
            if count == 0:
                self.view.error('The user does not exist')
            else:
                self.view.error('The user could not be deleted')
        return
    
    def movie_menu(self):
        o = '0'
        while o != '7':
            self.view.movie_menu()
            self.view.option('7')
            o = input()
            if o == '1':
                self.create_movie()
            elif o == '2':
                self.read_a_movie()
            elif o == '3':
                self.read_all_movie()
            elif o == '4':
                self.read_movie_name()
            elif o == '5':
                self.update_movie()
            elif o == '6':
                self.delete_movie()
            elif o == '7':
                return
            else:
                self.view.not_valid_option()
        return

    def user_main_menu_movie(self):
        o = '0'
        while o != '5':
            self.view.user_main_menu_movie()
            self.view.option('5')
            o = input()
            if o == '1':
                self.read_a_movie()
            elif o == '2':
                self.read_all_movie()
            elif o == '3':
                self.read_movie_name()
            elif o == '4':
                return
            else:
                self.view.not_valid_option()
        return
    
    def ask_movie(self):
        self.view.ask('Title ')
        m_name = input()
        self.view.ask('Duration: ')
        m_duration = input()
        self.view.ask('Language: ')
        m_language = input()
        self.view.ask('Subtitles: ')
        m_subtitles = input()
        return(m_name,m_duration,m_language,m_subtitles)
    
    def create_movie(self):
        m_name,m_duration,m_language,m_subtitles = self.ask_movie()
        out = self.model.create_movie(m_name,m_duration,m_language,m_subtitles)
        if out == True:
            self.view.ok(m_name+' in '+ m_language +' with '+ m_subtitles+' subtitles', 'added')
        else:
            self.view.error('The movie could not be added')
        return
    
    def read_a_movie(self):
        self.view.ask('Movie ID: ')    
        id_movie = input()
        movie = self.model.read_movie(id_movie)
        print(movie)
        if type(movie) == tuple:
            self.view.show_movie_header('Movie ID: '+id_movie+' ')
            self.view.show_a_movie(movie)
            self.view.show_midder()
            self.view.show_footer()
        else:
            if movie == None:
                self.view.error('The movie does not exist')
            else:
                self.view.error('There was a problem at reading the movie')
        return
    
    def read_all_movie(self):
        movies = self.model.read_all_movie()
        if type(movies) == list:
            self.view.show_movie_header(' All movies ')
            for movie in movies:
                self.view.show_a_movie(movie)
                self.view.show_midder()
            self.view.show_footer()
        else:
            self.view.error('There was a problem at reading the movies')
        return
    

    def read_movie_name(self):
        self.view.ask('Movie Title: ')
        name = input()
        movies = self.model.read_movie_name(name)
        if type(movies) == list:
            self.view.show_movie_header('Movies with the title: '+name+' ')
            for movie in movies:
                self.view.show_a_movie(movie)
                self.view.show_midder()
            self.view.show_footer()
        else:
            self.view.error('There was a problem at reading the movies')
        return
    

    def update_movie(self):
        self.view.ask('ID of the movie to update: ')
        id_movie = input()
        movie = self.model.read_movie(id_movie)
        m_name  = movie[1]
        if type(movie) == tuple:
            self.view.show_movie_header(' Info from movie ' +m_name+' (Movie Id: '+id_movie+ ') ')
            self.view.show_a_movie(movie)
            self.view.show_midder()
            self.view.show_footer()
        else:
            if movie == None:
                self.view.error('The movie does not exist')
            else:
                self.view.error('There was a problem at reading the movie')
        self.view.msg('Input the new values to update (Leave blank to skip): ')
        whole_vals = self.ask_movie()
        fields, vals = self.update_lists(['m_name','m_duration','m_language', 'm_subtitles'], whole_vals)
        vals.append(id_movie)
        vals = tuple(vals)
        out = self.model.update_movie(fields,vals)
        if out == True:
            self.view.ok(m_name+' (Movie ID:'+id_movie+')', ' updated')
        else:
            self.view.error('Error, the movie could not be updated')
        return
    
    def delete_movie(self):
        self.view.ask('ID of the movie to delete: ')
        id_movie = input()
        movie = self.model.read_movie(id_movie)
        m_name  = movie[1]
        count = self.model.delete_movie(id_movie)
        if count != 0:
            self.view.ok(m_name+' (Movie ID:'+id_movie+')', ' deleted')
        else:
            if count == 0:
                self.view.error('The movie does not exist')
            else:
                self.view.error('There was a problem at deleting the movie')
        return


    def hall_menu(self):
        o = '0'
        while o != '7':
            self.view.hall_menu()
            self.view.option('7')
            o = input()
            if o == '1':
                self.create_hall()
            elif o == '2':
                self.read_a_hall()
            elif o == '3':
                self.read_all_hall()
            elif o == '4':
                self.read_hall_seat()
            elif o == '5':
                self.update_hall()
            elif o == '6':
                self.delete_hall()
            elif o == '7':
                return
            else:
                self.view.not_valid_option()
        return
    
    def ask_hall(self):
        self.view.ask('Number of seats: ')
        h_totalSeat = input()
        return [h_totalSeat]
    
    def create_hall(self):
        h_totalSeat = self.ask_hall()
        out = self.model.create_hall(h_totalSeat)
        if out == True:
            self.view.ok('The hall ','added')
        else:
            self.view.error('The hall could not be added')
        return
        

    def read_a_hall(self):
        self.view.ask('Hall ID: ')
        id_hall = input()
        hall = self.model.read_hall(id_hall)
        if type(hall) == tuple:
            self.view.show_hall_header('Info from Hall  '+id_hall+' ')
            self.view.show_a_hall(hall)
            self.view.show_midder()
            self.view.show_footer()
        else:
            if hall == None:
                self.view.error('The hall does not exist')
            else:
                self.view.error('There was a problem at reading the hall')
        return
    
    def read_all_hall(self):
        halls = self.model.read_all_hall()
        if type(halls) ==  list:
            self.view.show_hall_header(' All halls ')
            for hall in halls:
                self.view.show_a_hall(hall)
                self.view.show_midder()
            self.view.show_footer()
        else:
            self.view.error(' There was a problem at reading the hall')
    
    def read_hall_seat(self):
        self.view.ask('Number of seats: ')
        h_totalSeat = input()
        seats = self.model.read_hall_seat(h_totalSeat)
        print(seats)
        if type(seats) == list:
            self.view.show_hall_header('Halls with '+h_totalSeat+' seats')
            for seat in seats:
                self.view.show_a_hall(seat)
                self.view.show_midder()
            self.view.show_footer()
        else:
            self.view.error('There was a problem at reading the halls')
        return
    
    def update_hall(self):
        self.view.ask('ID of the hall to update: ')
        id_hall = input()
        hall = self.model.read_hall(id_hall)
        if type(hall) == tuple:
            self.view.show_hall_header(' Info from hall '+id_hall+ ' ')
            self.view.show_a_hall(hall)
            self.view.show_midder()
            self.view.show_footer()
        else:
            if hall == None:
                self.view.error('The hall does not exist')
            else:
                self.view.error('There was a problem at reading the hall')
        self.view.msg('Input the new values to update (Leave blank to skip): ')
        whole_vals = self.ask_hall()
        fields, vals = self.update_lists(['h_totalSeat'], whole_vals)
        vals.append(id_hall)
        vals = tuple(vals)
        out = self.model.update_hall(fields,vals)
        if out == True:
            self.view.ok(id_hall, 'updated')
        else:
            self.view.error('Error, the hall could not be updated')
        return

    
    def delete_hall(self):
        self.view.ask('ID of the hall to delete: ')
        id_hall = input()
        count = self.model.delete_hall(id_hall)
        if count != 0:
            self.view.ok(id_hall, 'deleted')
        else:
            if count == 0:
                self.view.error('The hall does not exist')
            else:
                self.view.error('The was a problem at deleting the hall')
        return
    
    def seat_menu(self):
        o = '0'
        while o != '9':
            self.view.seat_menu()
            self.view.option('9')
            o = input()
            if o == '1':
                self.create_seat()
            elif o == '2':
                self.read_a_seat()
            elif o == '3':
                self.read_all_seat()
            elif o == '4':
                self.read_disp_seat()
            elif o == '5':
                self.read_seats_hall()
            elif o == '6':
                self.update_seat()
            elif o == '7':
                self.reset_seats()
            elif o == '8':
                self.delete_seat()
            elif o == '9':
                return
            else:
                self.view.not_valid_option()
        return
    
    def ask_seat(self):
        disp = 0 
        self.view.ask('Hall: ')
        se_id_hall = input()
        return [disp, se_id_hall]
    
    def create_seat(self):
        dis, se_id_hall = self.ask_seat()
        out = self.model.create_seat(dis, se_id_hall)
        if out == True:
            self.view.ok('The seat ','added')
        else:
            self.view.error('The seat could not be added')
        return

    def read_a_seat(self):
        self.view.ask('Seat ID: ')
        id_seat = input()
        seat = self.model.read_seat(id_seat)
        if type(seat) == tuple:
            self.view.show_seat_header('Info from seat '+id_seat+' ')
            self.view.show_a_seat(seat)
            self.view.show_midder()
            self.view.show_footer()
        else:
            if seat == None:
                self.view.error('The seat does not exist')
            else:
                self.view.error('There was a problem at reading the seat')
        return
    
    def read_all_seat(self):
        seats = self.model.read_all_seat()
        if type(seats) ==  list:
            self.view.show_seat_header(' All seats ')
            for seat in seats:
                self.view.show_a_seat(seat)
                self.view.show_midder()
            self.view.show_footer()
        else:
            self.view.error(' There was a problem at reading the seats')
    
    def read_disp_seat(self):
        self.view.ask('Hall: ')
        hall = input()
        self.view.ask('Status (free/taken): ')
        disp = input()
        
        if (disp == 'free'):
            disp = 0x00
        elif (disp == 'taken'):
            disp = 0x01
        seats = self.model.read_disp_seat(disp, hall)
        print(seats)    
        if type(seats) == list:
            if (disp == 0x00):
                self.view.show_seat_header('Availabe seats' )
            else:
                self.view.show_seat_header('Not available seats' )
            for seat in seats:
                self.view.show_a_seat_disp(seat)
                self.view.show_midder()
            self.view.show_footer()
        else:
            self.view.error('There was a problem at reading the seats')
        return

    def read_seats_hall(self):
        self.view.ask('Hall ID: ')
        id_hall = input()
        seats = self.model.read_seats_hall(id_hall)
        if type(seats) == list:
            self.view.show_seat_header('Seats from hall '+id_hall)
            for seat in seats:
                self.view.show_a_seat(seat)
                self.view.show_midder()
            self.view.show_footer()
        else:
            self.view.error('There was a problem at reading the seat')
        return

    def update_seat(self):
        self.view.ask('Seat to reserve: ')
        id_seat = input()
        seat = self.model.read_seat(id_seat)   
        if (seat[1] == 0x01):
            print('The seat is already taken, 1). Try again  | 2). Cancel')
            op = input()
            if (op == '1'):
                self.update_seat()
            else:
                return 0

        if type(seat) == tuple:
            self.view.show_seat_header(' Info from seat'+id_seat+ ' ')
            self.view.show_a_seat(seat)
            self.view.show_midder()
            self.view.show_footer()
        else:
            if seat == None:
                self.view.error('The seat does not exist')
            else:
                self.view.error('There was a problem at reading the seat')
        
        whole_vals = [1, str(seat[2])]
        fields, vals = self.update_lists(['se_status', 'se_id_hall'], whole_vals)
        vals.append(id_seat)
        vals = tuple(vals)
        out = self.model.update_seat(fields,vals)
        if out == True:
            self.view.ok(id_seat, 'updated')
            return id_seat
        else:
            self.view.error('Error, the seat could not be updated')
        return 0
    
    def reset_seats(self):
        self.view.ask('Restore seats from hall: ')
        se_id_hall = input()
        seats = self.model.read_seats_hall(se_id_hall)
        if type(seats) == list:
            for seat in seats:
                id_seat = seat[0]
                seat = self.model.read_seat(id_seat)      
                whole_vals = [0, str(seat[2])]
                fields, vals = self.update_lists(['se_status', 'se_id_hall'], whole_vals)
                vals.append(id_seat)
                vals = tuple(vals)
                out = self.model.update_seat(fields,vals)
                if out != True:
                    self.view.error('Error, the seats could not be updated')
            self.view.ok('the seats', 'restored')
        else:
            self.view.error('There was a problem at reading the seats')
        return
    
    def delete_seat(self):
        self.view.ask('ID of the seat to delete: ')
        id_seat = input()
        count = self.model.delete_seat(id_seat)
        if count != 0:
            self.view.ok(id_seat, 'deleted')
        else:
            if count == 0:
                self.view.error('The seat does not exist')
            else:
                self.view.error('There was a problem at deleting the seat')
        return
 
    
    def schedule_menu(self):
        o = '0'
        while o != '8':
            self.view.schedule_menu()
            self.view.option('8')
            o = input()
            if o == '1':
                self.create_schedule()
            elif o == '2':
                self.read_a_schedule()
            elif o == '3':
                self.read_all_schedule()
            elif o == '4':
                self.read_schedule_movie()
            elif o == '5':
                self.read_schedules_date()
            elif o == '6':
                self.update_schedule()
            elif o == '7':
                self.delete_schedule()
            elif o == '8':
                return
            else:
                self.view.not_valid_option()
        return
    
    def user_main_menu_schedule(self):
        o = '0'
        while o != '5':
            self.view.user_main_menu_schedule()
            self.view.option('5')
            o = input()
            if o == '1':
                self.read_all_schedule()
            elif o == '2':
                self.read_schedule_movie()
            elif o == '3':
                self.read_schedules_date()
            elif o == '4':
                return      
            else:
                self.view.not_valid_option()
        return

    
    def ask_schedule(self):
        self.view.ask('Time: ')
        s_time = input()
        self.view.ask('Date: ')
        s_date = input()
        self.view.ask('Movie ID: ')
        s_id_movie = input()
        self.view.ask('Hall ID: ')
        s_id_hall = input()
        return(s_time,s_date,s_id_movie,s_id_hall)
    
    def create_schedule(self):
        s_time,s_date,s_id_movie,s_id_hall = self.ask_schedule()
        out = self.model.create_schedule(s_time,s_date,s_id_movie,s_id_hall)
        movie = self.model.read_movie(s_id_movie)
        if out == True:
            self.view.ok(movie[1]+' at '+ s_time +' on '+s_date+' in hall: '+s_id_hall, 'added')
        else:
            self.view.error('The movie could not be added')
        return
    
    def read_a_schedule(self):
        self.view.ask('Schedule ID: ')    
        id_schedule = input()
        schedule = self.model.read_schedule(id_schedule)
        if type(schedule) == tuple:
            self.view.show_schedule_header('Schedule ID: '+id_schedule+' ')
            self.view.show_a_schedule(schedule)
            self.view.show_midder()
            self.view.show_footer()
        else:
            if schedule == None:
                self.view.error('The schedule does not exist')
            else:
                self.view.error('There was a problem at reading the schedule')
        return
    
    def read_all_schedule(self):
        schedules = self.model.read_all_schedule()
        if type(schedules) == list:
            self.view.show_schedule_header(' All schedules ')
            for schedule in schedules:
                self.view.show_a_schedule(schedule)
                self.view.show_midder()
            self.view.show_footer()
        else:
            self.view.error('There was a problem at reading the schedules')
        return
    

    def read_schedule_movie(self):
        self.view.ask('Movie title: ')
        name = input()
        schedules = self.model.read_schedule_movie(name)
        if type(schedules) == list:
            self.view.show_schedule_header('Schedules for: '+name+' ')
            for schedule in schedules:
                self.view.show_a_schedule(schedule)
                self.view.show_midder()
            self.view.show_footer()
        else:
            self.view.error('There was a problem at reading the schedule')
        return
    
    def read_schedules_date(self):
        self.view.ask('Date: ')
        date = input()
        schedules = self.model.read_schedule_date(date)
        if type(schedules) == list:
            self.view.show_schedule_header('Schedules on  : '+date+' ')
            for schedule in schedules:
                self.view.show_a_schedule(schedule)
                self.view.show_midder()
            self.view.show_footer()
        else:
            self.view.error('There was a problem at reading the schedule')
        return
    

    def update_schedule(self):
        self.view.ask('ID of schedule to update: ')
        id_schedule = input()
        schedule = self.model.read_schedule(id_schedule)
        if type(schedule) == tuple:
            self.view.show_schedule_header(' Info from Schedule ' +id_schedule)
            self.view.show_a_schedule(schedule)
            self.view.show_midder()
            self.view.show_footer()
        else:
            if schedule == None:
                self.view.error('The schedule does not exist')
            else:
                self.view.error('There was a problem at reading the schedule')
        self.view.msg('Input the new values to update (Leave blank to skip): ')
        whole_vals = self.ask_schedule()
        fields, vals = self.update_lists(['s_time','s_date','s_id_movie', 's_id_hall'], whole_vals)
        vals.append(id_schedule)
        vals = tuple(vals)
        out = self.model.update_schedule(fields,vals)
        if out == True:
            self.view.ok('The schedule'+' (ID:'+id_schedule+')', ' updated')
        else:
            self.view.error('There was a problem at updating the schedule')
        return
    
    def delete_schedule(self):
        self.view.ask('ID of the schedule to delete ')
        id_schedule = input()
        count = self.model.delete_schedule(id_schedule)
        if count != 0:
            self.view.ok('The schedule'+' (ID:'+id_schedule+')', ' deleted')
        else:
            if count == 0:
                self.view.error('The schedule does not exist')
            else:
                self.view.error('There was a problem at deleting the schedule')
        return
    
    def user_main_menu_tickets(self, id_user):
        o = '0'
        while o != '4':
            self.view.user_main_menu_tickets()
            self.view.option('4')
            o = input()
            if o == '1':
                self.create_ticket(id_user)
            elif o == '2':
                self.read_ticket_user(id_user)
            elif o == '3':
                self.login_user(id_user)
            else:
                self.view.not_valid_option()
        return

    
    def ask_ticket(self):
        self.read_all_schedule()
        self.view.ask('Schedule ID: ')
        t_id_schedule = input()
        schedule = self.model.read_schedule(t_id_schedule)
        hall = self.model.read_disp_seat(0x00,schedule[4])
        print('Available seats: ',hall)
    
        id_seat = self.update_seat()
        
        return(t_id_schedule,schedule[4],id_seat)
    
    def create_ticket(self, t_id_usuario):
        t_id_schedule,t_id_hall,t_id_seat = self.ask_ticket()   
        if(t_id_seat == 0):
            return
        out = self.model.create_ticket(t_id_usuario,t_id_schedule,t_id_seat)
        schedule = self.model.read_schedule(t_id_schedule)
        if out == True:
            self.view.ok('The ticket from user: '+t_id_usuario +' for the movie: '+ schedule[6] +' in '+ schedule[8] +' with '+schedule[9]+' subtitles '+'\n on '+str(schedule[2])+' at '+ schedule[1]+'; Hall: '+ str(t_id_hall)+' Seat: '+ str(t_id_seat), 'added')
        else:
            self.view.error('The ticket could not be added')
        return
    
    def read_a_ticket(self):
        self.view.ask('Ticket ID: ')    
        id_ticket = input()
        ticket,schedule = self.model.read_ticket(id_ticket)
        if type(ticket) == tuple:
            self.view.show_ticket_header('Ticket ID: '+id_ticket+' ')
            self.view.show_a_ticket(ticket, schedule)
            self.view.show_midder()
            self.view.show_footer()
        else:
            if ticket == None:
                self.view.error('The ticket does not exist')
            else:
                self.view.error('There was a problem at reading the ticket')
        return
    
    def read_all_ticket(self):
        tickets, schedules = self.model.read_all_ticket()  
        if type(tickets) == list:
            self.view.show_ticket_header(' All tickets')
            for i in range(len(tickets)):
                self.view.show_a_ticket(tickets[i],schedules[i])
                self.view.show_midder()
            self.view.show_footer()
        else:
            self.view.error('There was a problem at reading the tickets')
        return
    

    def read_ticket_user(self, id_user):
        tickets, schedules = self.model.read_ticket_user(id_user)  
        if type(tickets) == list:
            self.view.show_ticket_header(' All tickets from the user '+ id_user)
            for i in range(len(tickets)):
                self.view.show_a_ticket(tickets[i],schedules[i])
                self.view.show_midder()
            self.view.show_footer()
        else:
            self.view.error('There was a problem at reading the tickets')
        return
    
    def read_ticket_schedule(self):
        self.view.ask('Schedule ID: ')
        schedule = input()
        tickets, schedules = self.model.read_ticket_schedule(schedule)  
        if type(tickets) == list:
            self.view.show_ticket_header(' All tickets on schedule '+ schedule)
            for i in range(len(tickets)):
                self.view.show_a_ticket(tickets[i],schedules[i])
                self.view.show_midder()
            self.view.show_footer()
        else:
            self.view.error('There was a problem at reading the tickets')
        return
    
   
   
   