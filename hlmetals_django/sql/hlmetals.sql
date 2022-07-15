/*
 Seeding the database with data
 */

 --State

insert into company_state (state_name, state_abbr)
values
('Alabama',         'AL'),
('Alaska',          'AK'),
('Arizona',         'AZ'),
('California',      'CA'),
('Colorado',        'CO'),
('Connecticut',     'CT'),
('Delaware',        'DE'),
('Florida',         'FL'),
('Georgia',         'GA'),
('Hawaii',          'HI'),
('Idaho',           'ID'),
('Illinois',        'IL'),
('Indiana',         'IN'),
('Iowa',            'IA'),
('Kansas',          'KS'),
('Kentucky',        'KY'),
('Louisiana',       'LA'),
('Maine',           'ME'),
('Maryland',        'MD'),
('Massachusetts',   'MA'),
('Michigan',        'MI'),
('Minnesota',       'MN'),
('Mississippi',     'MS'),
('Missouri',        'MO'),
('Montana',         'MT'),
('Nebraska',        'NE'),
('Nevada',          'NV'),
('New Hampshire',   'NH'),
('New Jersey',      'NJ'),
('New Mexico',      'NM'),
('New York',        'NY'),
('North Carolina',  'NC'),
('North Dakota',    'ND'),
('Ohio',            'OH'),
('Oklahoma',        'OK'),
('Oregon',          'OR'),
('Pennsylvania',    'PA'),
('Rhode Island',    'RI'),
('South Carolina',  'SC'),
('South Dakota',    'SD'),
('Tennessee',       'TN'),
('Texas',           'TX'),
('Utah',            'UT'),
('Vermont',         'VT'),
('Virginia',        'VA'),
('Washington',      'WA'),
('West Virginia',   'WV'),
('Wisconsin',       'WI'),
('Wyoming',         'WY');

--Company Type

insert into company_companytype (company_type_code, company_type_desc)
values
('CUST',    'Customer'),
('TRUCK',   'Trucking Company'),
('RECY',    'Recycling Company'),
('VEND',    'Vendor');

--Note Type

insert into company_notetype (note_type_code, note_type_desc)
values
('COMP',    'Company Note'),
('LOG',     'Logistics Notes'),
('JOB',     'Job Notes'),
('INV',     'Invoice Notes'),
('BILL',    'Bill Notes');


