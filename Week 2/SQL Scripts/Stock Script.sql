-- We should have the following tables: users, stocks, accounts, portfolios

-- Our user table should include: first_name, last_name, email, password, and unique id

drop table users;
create table users(
	-- Defining our columns
	user_id bigserial,
	first_name varchar(20) not null,
	last_name varchar(20) not null,
	email varchar(30) not null,
	-- Realistically speaking, we would not store passwords as plain text.
	user_password varchar(20) not null,
	-- This is known as a "constraint". In fact, this is a primary key constraint,
	-- which means that the affected column must be unique AND not null.
	primary key (user_id)
);

drop table stocks;
create table stocks(
	stock_symbol varchar(4) primary key,
	stock_price money not null,
	stock_name varchar(20),
	stock_trend_up boolean
);

drop table portfolios;
create table portfolios(
	portfolio_name varchar(20) primary key,
	-- This ID should match the ID of the user who owns the portfolio. We should
	-- use a foreign key constraint to signify that this column references a
	-- record on other table.
	owner_id integer references users(user_id)
);

-- Per the requirements of the stock app, portfolios should be able to contain multiple
-- stocks, but it is also the case that stocks could be present in many different
-- portfolios. This means that we might want a "bridge table".

create table stocks_portfolios(
	stock_symbol varchar(4) not null references stocks(stock_symbol),
	portfolio_name varchar(20) not null references portfolios(portfolio_name),
	num_share numeric,
	-- We can also make the two existing columns here a compositive primary key
	constraint stock_portfolio_pk primary key (stock_symbol, portfolio_name)
);

-- Now we would like to actually store some records. This falls under DML.

-- Adding a new record to a table:

insert into users values(default, 'Tim', 'the Enchanter', 'Tim@MontyPython.com', 'JohnCleese');
insert into users values(default, 'Killer', 'Wabbit', 'adorbs@not.com', 'grenade');

insert into portfolios values('greatest portfolio', 1);
insert into portfolios values('another one', null);
insert into portfolios values('tim the portfolio', 1);

-- Reading records from the table:

select * from users;
select * from portfolios;
select "first_name", "last_name" from users;

-- Find all of Tim the Enchanter's portfolios

select portfolio_name from portfolios where owner_id = 1;

-- Modify an existing record
-- Please do not ever forget your where clauses.

update users set last_name = 'Rabbit' where user_id = 2;
update users set last_name = 'the Enchanter' where user_id = 1;

-- Deleting records
-- Please (again) do not ever forget your where clauses!

delete from users where user_id = 2;



