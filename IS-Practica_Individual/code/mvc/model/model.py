from mysql import connector

class Model:
 
    def __init__(self, config_db_file='config.txt'):
        self.config_db_file = config_db_file
        self.config_db = self.read_config_db()
        self.connect_to_db()

    def read_config_db(self):
        d = {}
        with open(self.config_db_file) as f_r:
            for line in f_r:
                (key, val) = line.strip().split(':')
                d[key] = val
        return d

    def connect_to_db(self):
        self.cnx = connector.connect(**self.config_db)
        self.cursor = self.cnx.cursor()

    def close_db(self):
        self.cnx.close()

    def create_admin(self, a_name, a_lastName, a_email, a_phone):
        try:
            sql = 'INSERT INTO admin (`a_name`, `a_lastName`, `a_email`, `a_phone` ) VALUES (%s, %s, %s,%s)'
            vals = (a_name, a_lastName, a_email, a_phone)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True

        except connector.Error as err:
            self.cnx.rollback() 
            return err

    def read_admin(self, id_admin):
        try:
            sql = 'SELECT * FROM admin WHERE id_admin = %s'
            vals = (id_admin,) 
            self.cursor.execute(sql, vals) 
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_admin(self):
        try:
            sql = 'SELECT * FROM admin'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
            
    def read_admin_name(self, a_name):
        try:
            sql = 'SELECT * FROM admin WHERE a_name = %s'
            vals = (a_name,)
            self.cursor.execute(sql,vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    def update_admin(self, fields, vals):
        try:
            sql = 'UPDATE admin SET ' + ','.join(fields) + ' WHERE id_admin = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def delete_admin(self, id_admin):
        try:
            sql = 'DELETE FROM admin WHERE id_admin = %s'
            vals = (id_admin,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err
        
  
    def create_user(self, u_name, u_lastName, u_email, u_phone):
        try:
            sql = 'INSERT INTO user (`u_name`, `u_lastName`, `u_email`, `u_phone` ) VALUES (%s, %s, %s,%s)'
            vals = (u_name, u_lastName, u_email, u_phone)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            sql = 'SELECT id_user FROM user WHERE u_name = %s AND u_lastName = %s AND u_email = %s AND u_phone = %s'
            vals = (u_name, u_lastName, u_email, u_phone)
            self.cursor.execute(sql, vals) 
            record = self.cursor.fetchone()
            return (True, record)

        except connector.Error as err:
            self.cnx.rollback() 
            return err

    def read_user(self, id_user):
        try:
            sql = 'SELECT * FROM user WHERE id_user = %s'
            vals = (id_user,)
            self.cursor.execute(sql, vals) 
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err

    def read_all_user(self):
        try:
            sql = 'SELECT * FROM user'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
            
    def read_user_lname(self, u_lastName):
        try:
            sql = 'SELECT * FROM user WHERE u_lastName = %s'
            vals = (u_lastName,)
            self.cursor.execute(sql,vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    def update_user(self, fields, vals):
        try:
            sql = 'UPDATE user SET ' + ','.join(fields) + ' WHERE id_user = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def delete_user(self, id_user):
        try:
            sql = 'DELETE FROM user WHERE id_user = %s'
            vals = (id_user,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

  
    def create_movie(self, m_name,m_duration,m_language,m_subtitles):
        try:
            sql = 'INSERT INTO movie (`m_name`, `m_duration`, `m_language`,`m_subtitles`) VALUES (%s, %s, %s, %s)'
            vals = ( m_name,m_duration,m_language,m_subtitles )
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def read_movie(self, id_movie):
        try:
            sql = 'SELECT * FROM movie WHERE id_movie = %s'
            vals = (id_movie,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err
    
    def read_all_movie(self):
        try:
            sql = 'SELECT * FROM movie'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_movie_name(self, m_name):
        try:
            sql = 'SELECT * FROM movie WHERE m_name = %s'
            vals = (m_name,)
            self.cursor.execute(sql,vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    def update_movie(self, fields, vals):
        try:
            sql = 'UPDATE movie SET ' + ','.join(fields) + 'WHERE id_movie = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def delete_movie(self, id_movie):
        try:
            sql = 'DELETE FROM movie WHERE id_movie = %s'
            vals = (id_movie,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    def create_hall(self, h_totalSeat):
        try:
            sql = 'INSERT INTO hall (`h_totalSeat`) VALUES (%s)'
            vals = ( h_totalSeat)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    
    def read_hall(self, id_hall):
        try:
            sql = 'SELECT * FROM hall WHERE id_hall = %s'
            vals = (id_hall,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err
    
    def read_all_hall(self):
        try:
            sql = 'SELECT * FROM hall'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    def read_hall_seat(self, h_totalSeat):
        try:
            sql = 'SELECT * FROM hall WHERE h_totalSeat = %s'
            vals = (h_totalSeat,)
            self.cursor.execute(sql,vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    
    def update_hall(self, fields, vals):
        try:
            sql = 'UPDATE hall SET ' + ','.join(fields) + 'WHERE id_hall = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def delete_hall(self, id_hall):
        try:
            sql = 'DELETE FROM hall WHERE id_hall = %s'
            vals = (id_hall,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    

    def create_seat(self, se_status, se_id_hall):
        try:
            sql = 'INSERT INTO seat (`se_status`,`se_id_hall`) VALUES (%s, %s)'
            vals = ( se_status, se_id_hall)
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    
    def read_seat(self, id_seat):
        try:
            sql = 'SELECT * FROM seat WHERE id_seat = %s'
            vals = (id_seat,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err
    
    def read_all_seat(self):
        try:
            sql = 'SELECT * FROM seat'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    def read_disp_seat(self, se_status, se_id_hall):
        try:
            sql = 'SELECT id_seat FROM seat WHERE se_status = %s and se_id_hall = %s'
            vals = (se_status, se_id_hall)
            self.cursor.execute(sql,vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    def read_seats_hall(self, se_id_hall):
        try:
            sql = 'SELECT * FROM seat WHERE se_id_hall = %s'
            vals = (se_id_hall,)
            self.cursor.execute(sql,vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    
    def update_seat(self, fields, vals):
        try:
            sql = 'UPDATE seat SET ' + ','.join(fields) + 'WHERE id_seat = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def delete_seat(self, id_seat):
        try:
            sql = 'DELETE FROM seat WHERE id_seat = %s'
            vals = (id_seat,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err
    


    def create_schedule(self, s_time,s_date,s_id_movie,s_id_hall):
        try:
            sql = 'INSERT INTO schedule (`s_time`, `s_date`, `s_id_movie`,`s_id_hall`) VALUES (%s, %s, %s, %s)'
            vals = ( s_time,s_date,s_id_movie,s_id_hall )
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def read_schedule(self, id_schedule):
        try:
            sql = 'SELECT schedule.*,movie.* FROM schedule JOIN movie ON schedule.s_id_movie = movie.id_movie AND id_schedule = %s'                     
            vals = (id_schedule,)
            self.cursor.execute(sql, vals)
            record = self.cursor.fetchone()
            return record
        except connector.Error as err:
            return err
    
    def read_all_schedule(self):
        try:
            sql = 'SELECT schedule.*,movie.* FROM schedule JOIN movie ON schedule.s_id_movie = movie.id_movie'
            self.cursor.execute(sql)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err

    def read_schedule_movie(self, m_name):
        try:
            sql = 'SELECT schedule.*,movie.* FROM schedule JOIN movie ON schedule.s_id_movie = movie.id_movie AND m_name = %s'
            vals = (m_name,)
            self.cursor.execute(sql,vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    def read_schedule_date(self, date):
        try:
            sql = 'SELECT schedule.*,movie.* FROM schedule JOIN movie ON schedule.s_id_movie = movie.id_movie AND s_date = %s'
            vals = (date,)
            self.cursor.execute(sql,vals)
            records = self.cursor.fetchall()
            return records
        except connector.Error as err:
            return err
    
    def update_schedule(self, fields, vals):
        try:
            sql = 'UPDATE schedule SET ' + ','.join(fields) + 'WHERE id_schedule = %s'
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def delete_schedule(self, id_schedule):
        try:
            sql = 'DELETE FROM schedule WHERE id_schedule = %s'
            vals = (id_schedule,)
            self.cursor.execute(sql,vals)
            self.cnx.commit()
            count = self.cursor.rowcount
            return count
        except connector.Error as err:
            self.cnx.rollback()
            return err

    
 
    def create_ticket(self, t_id_usuario,t_id_schedule,t_id_seat):
        try:
            sql = 'INSERT INTO ticket (`t_id_usuario`, `t_id_schedule`, `t_id_seat`) VALUES (%s, %s, %s)'
            vals = ( t_id_usuario,t_id_schedule,t_id_seat )
            self.cursor.execute(sql, vals)
            self.cnx.commit()
            return True
        except connector.Error as err:
            self.cnx.rollback()
            return err
    
    def read_ticket(self, id_ticket):
        try:
            sql = 'SELECT ticket.*,schedule.*,user.* FROM ticket JOIN schedule ON ticket.t_id_schedule = schedule.id_schedule JOIN user ON ticket.t_id_usuario = user.id_user AND id_ticket = %s'  #JOIN movie ON schedule.id_movie = movie.id_movie                
            vals = (id_ticket,)
            self.cursor.execute(sql, vals)
            record1 = self.cursor.fetchone()
            sql = 'SELECT movie.* FROM schedule JOIN movie ON schedule.s_id_movie = movie.id_movie AND id_schedule = %s'            
            vals = (record1[2],)
            self.cursor.execute(sql, vals)
            record2 = self.cursor.fetchone()
            return record1,record2
        except connector.Error as err:
            return err
    
    def read_all_ticket(self):
        try:
            sql = 'SELECT ticket.*,schedule.*,user.* FROM ticket JOIN schedule ON ticket.t_id_schedule = schedule.id_schedule JOIN user ON ticket.t_id_usuario = user.id_user'  #JOIN movie ON schedule.id_movie = movie.id_movie                
            self.cursor.execute(sql)
            record1 = self.cursor.fetchall()
            record2 = []
            for record in record1:
                sql = 'SELECT movie.* FROM schedule JOIN movie ON schedule.s_id_movie = movie.id_movie AND id_schedule = %s'            
                vals = (record[2],)
                self.cursor.execute(sql, vals)
                schedule = self.cursor.fetchone()
                record2.append(schedule)
            return record1,record2
        except connector.Error as err:
            return err

    def read_ticket_user(self, id_user):
        try:
            sql = 'SELECT ticket.*,schedule.*,user.* FROM ticket JOIN schedule ON ticket.t_id_schedule = schedule.id_schedule JOIN user ON ticket.t_id_usuario = user.id_user AND id_user = %s'  #JOIN movie ON schedule.id_movie = movie.id_movie         
            vals = (id_user,)       
            self.cursor.execute(sql, vals)
            record1 = self.cursor.fetchall()
            record2 = []
            for record in record1:
                sql = 'SELECT movie.* FROM schedule JOIN movie ON schedule.s_id_movie = movie.id_movie AND id_schedule = %s'            
                vals = (record[2],)
                self.cursor.execute(sql, vals)
                schedule = self.cursor.fetchone()
                record2.append(schedule)
            return record1,record2
        except connector.Error as err:
            return err
    
    def read_ticket_schedule(self, t_id_schedule):
        try:
            sql = 'SELECT ticket.*,schedule.*,user.* FROM ticket JOIN schedule ON ticket.t_id_schedule = schedule.id_schedule JOIN user ON ticket.t_id_usuario = user.id_user AND t_id_schedule = %s'  #JOIN movie ON schedule.id_movie = movie.id_movie         
            vals = (t_id_schedule,)       
            self.cursor.execute(sql, vals)
            record1 = self.cursor.fetchall()
            record2 = []
            for record in record1:
                sql = 'SELECT movie.* FROM schedule JOIN movie ON schedule.s_id_movie = movie.id_movie AND id_schedule = %s'            
                vals = (record[2],)
                self.cursor.execute(sql, vals)
                schedule = self.cursor.fetchone()
                record2.append(schedule)
            return record1,record2
        except connector.Error as err:
            return err