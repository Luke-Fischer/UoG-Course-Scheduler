INSERT INTO course_names(course_id, course_code, course_name) VALUES (1,'ACCT*3280', 'Taxation');
INSERT INTO course_names(course_id, course_code, course_name) VALUES (2,'ARTH*2150', 'Art');
INSERT INTO course_names(course_id, course_code, course_name) VALUES (3,'ASCI*3100', 'Science Communication');
INSERT INTO course_names(course_id, course_code, course_name) VALUES (4,'BIOC*4050', 'protein');

INSERT INTO course_sections(course_id, course_section) VALUES (1, 1);
INSERT INTO course_sections(course_id, course_section) VALUES (2, 1);
INSERT INTO course_sections(course_id, course_section) VALUES (3, 1);
INSERT INTO course_sections(course_id, course_section) VALUES (4, 1);

INSERT INTO course_meetings(course_id, course_section, meeting_type, meeting_start_time, meeting_end_time, meeting_building, meeting_room_num) 
VALUES (1, 1, 'Lec', 'WED;FRI 01:00PM', '02:20PM', 'CRSC', 116);
INSERT INTO course_meetings(course_id, course_section, meeting_type, meeting_start_time, meeting_end_time, meeting_building, meeting_room_num) 
VALUES (2, 1, 'Lec', 'MON;WED;FRI 10:30AM', '11:20AM', 'MCKN', 114);
INSERT INTO course_meetings(course_id, course_section, meeting_type, meeting_start_time, meeting_end_time, meeting_building, meeting_room_num) 
VALUES (3, 1, 'Lec', 'MON;WED 11:30AM', '12:50PM', 'MCKN', 234);
INSERT INTO course_meetings(course_id, course_section, meeting_type, meeting_start_time, meeting_end_time, meeting_building, meeting_room_num) 
VALUES (4, 1, 'Lec', 'TUES;THUR 02:30PM', '03:50PM', 'ANNU', 156);

INSERT INTO course_section_instructors(course_id, course_section, course_section_instructor) VALUES (1, 1, 'P. Ghattas');
INSERT INTO course_section_instructors(course_id, course_section, course_section_instructor) VALUES (2, 1, 'A. Sherwood');
INSERT INTO course_section_instructors(course_id, course_section, course_section_instructor) VALUES (3, 1, 'A. Souchen');
INSERT INTO course_section_instructors(course_id, course_section, course_section_instructor) VALUES (4, 1, 'W. Zhang');

INSERT INTO course_term(course_id, course_year, course_semester) VALUES (1, 2022, 'FALL');
INSERT INTO course_term(course_id, course_year, course_semester) VALUES (2, 2022, 'FALL');
INSERT INTO course_term(course_id, course_year, course_semester) VALUES (3, 2022, 'FALL');
INSERT INTO course_term(course_id, course_year, course_semester) VALUES (4, 2022, 'FALL');

INSERT INTO course_section_availability(course_id, course_section, course_section_remaining_capacity, course_section_total_capacity, course_section_status) VALUES (1, 1, 3, 100, 'open');
INSERT INTO course_section_availability(course_id, course_section, course_section_remaining_capacity, course_section_total_capacity, course_section_status) VALUES (2, 1, 0, 150, 'open');
INSERT INTO course_section_availability(course_id, course_section, course_section_remaining_capacity, course_section_total_capacity, course_section_status) VALUES (3, 1, 0, 200, 'open');
INSERT INTO course_section_availability(course_id, course_section, course_section_remaining_capacity, course_section_total_capacity, course_section_status) VALUES (4, 1, 15, 130, 'open');

INSERT INTO course_additional_information(course_id, course_location, course_credits, course_academic_level) VALUES (1, 'Guelph', 0.5, 3000);
INSERT INTO course_additional_information(course_id, course_location, course_credits, course_academic_level) VALUES (2, 'Guelph', 0.5, 2000);
INSERT INTO course_additional_information(course_id, course_location, course_credits, course_academic_level) VALUES (3, 'Guelph', 0.5, 3000);
INSERT INTO course_additional_information(course_id, course_location, course_credits, course_academic_level) VALUES (4, 'Guelph', 0.5, 4000);
