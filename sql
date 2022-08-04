
create table employee(
						id int,
                        full_name varchar(50),
                        ra int,
                        cpf int,
                        
                        primary key(id)
                        );

create table ticket(
						ticket_id int,
                        passanger_name varchar(50),
                        passanger_cpf int,
                        passanger_birthdate date,
                        passanger_passport int,
                        
                        flight_number int,
						seat int,
                        
                        destiny int,
                        departure date,
                        comeback date,
                        total decimal,
                        payment_method enum('credit_card','debit_card','cash'),
                        
                        primary key(ticket_id),
                        foreign key (flight_number) references flight(flight_id),
                        foreign key(seat) references seats(seat),
                        foreign key(destiny) references destinations(destination_id)
                        );
                        
create table flight(
						flight_id int,
                        departure_time datetime,
                        origin varchar(50),
                        destiny varchar(50),
                        
                        primary key(flight_id)
                        );
                        
create table seats(
						flight int,
                        seat int,
                        availability bool,
                        
                        primary key(seat),
                        foreign key(flight) references flight(flight_id)
                        );
                        
create table destinations(
							destination_id int,
                            destination varchar(50),
                            
                            primary key(destination_id)
                            );
