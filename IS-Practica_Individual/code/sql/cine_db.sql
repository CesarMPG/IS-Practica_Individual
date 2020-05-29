#drop database cine_db;

create database if not exists cine_db;

use cine_db;

create table if not exists admin( #Administradores
	id_admin int not null auto_increment,
    a_name varchar(25) not null,
    a_lastName varchar(25) not null,
	a_email varchar(45) not null,
    a_phone varchar(10) not null,
    primary key(id_admin)
)engine = InnoDB;

create table if not exists user( #Usuarios
	id_user int not null auto_increment,
    u_name varchar(25) not null,
    u_lastName varchar(25) not null,
	u_email varchar(45) not null,
    u_phone varchar(10) not null,
    primary key(id_user)
)engine = InnoDB;

create table if not exists movie( #Películas
	id_movie int not null auto_increment,
    m_name varchar(25) not null,
    m_duration varchar(10) not null,
	m_language varchar(20) not null,
    m_subtitles varchar(20) not null,
    primary key(id_movie)
)engine = InnoDB;

create table if not exists hall( #Salas
	id_hall int not null auto_increment,
    h_totalSeat int not null,
    primary key(id_hall)
)engine = InnoDB;

create table if not exists seat( #Asientos
	id_seat int not null auto_increment,
    se_status bit(1),
    se_id_hall int not null,
    constraint fkse_id_hall 
    foreign key(se_id_hall)
		references hall(id_hall)
        on update cascade,
    primary key(id_seat)
)engine = InnoDB;

create table if not exists schedule( #Horarios
	id_schedule int not null auto_increment,
    s_time varchar(10) not null,
    s_date date not null,
    s_id_movie int not null,
    s_id_hall int not null,
    constraint fks_id_movie 
    foreign key(s_id_movie)
		references movie(id_movie)
        on update cascade,
	constraint fks_id_hall
    foreign key(s_id_hall)
		references hall(id_hall)
        on update cascade,
    primary key(id_schedule)
)engine = InnoDB;

create table if not exists ticket( #Horarios
	id_ticket int not null auto_increment,
    t_id_usuario int not null,
    t_id_schedule int not null,
    t_id_seat int not null,
    constraint fkt_id_usuario
    foreign key(t_id_usuario)
		references user(id_user)
        on update cascade,
	constraint fkt_id_schedule
    foreign key(t_id_schedule)
		references schedule(id_schedule)
        on update cascade,
	constraint fkt_id_seat
    foreign key(t_id_seat)
		references seat(id_seat)
        on update cascade,
    primary key(id_ticket)
)engine = InnoDB;
