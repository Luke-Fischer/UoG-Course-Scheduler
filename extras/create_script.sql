CREATE TABLE IF NOT EXISTS course_names (
	course_id integer,
    course_code varchar(50),
    course_name varchar(50)
);

CREATE TABLE IF NOT EXISTS course_sections (
	course_id integer,
    course_section integer
);

CREATE TABLE IF NOT EXISTS course_meetings (
	course_id integer,
    course_section integer,
    meeting_type varchar(50),
    meeting_start_time varchar(50),
    meeting_end_time varchar(50),
    meeting_building varchar(50),
    meeting_room_num integer
);

CREATE TABLE IF NOT EXISTS course_section_instructors (
	course_id integer,
    course_section integer,
    course_section_instructor varchar(50)
);

CREATE TABLE IF NOT EXISTS course_term (
	course_id integer,
    course_year integer,
    course_semester varchar(50)
);

CREATE TABLE IF NOT EXISTS course_section_availability (
	course_id integer,
    course_section integer,
    course_section_remaining_capacity integer,
    course_section_total_capacity integer,
    course_section_status varchar(50)

);

CREATE TABLE IF NOT EXISTS course_additional_information (
	course_id integer,
    course_location varchar(50),
    course_credits decimal,
    course_academic_level integer
);