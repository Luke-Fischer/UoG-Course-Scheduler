/*Get all courses*/
select course_code, course_name
from course_names;

/*Get all info for all courses*/
select course_names.course_code, course_names.course_name, course_sections.course_section, course_meetings.meeting_type, course_meetings.meeting_start_time, course_meetings.meeting_end_time,
course_meetings.meeting_building, course_meetings.meeting_room_num, course_section_instructors.course_section_instructor, course_term.course_year, course_term.course_semester,
course_section_availability.course_section_remaining_capacity, course_section_availability.course_section_total_capacity, course_section_availability.course_section_status,
course_additional_information.course_location, course_additional_information.course_credits, course_additional_information.course_academic_level
FROM ((((((course_names
INNER JOIN course_sections ON course_names.course_id = course_sections.course_id)
INNER JOIN course_meetings ON course_names.course_id = course_meetings.course_id)
INNER JOIN course_section_instructors ON course_names.course_id = course_section_instructors.course_id)
INNER JOIN course_term ON course_names.course_id = course_term.course_id)
INNER JOIN course_section_availability ON course_names.course_id = course_section_availability.course_id)
INNER JOIN course_additional_information ON course_names.course_id = course_additional_information.course_id)
WHERE course_names.course_code = 'BIOC*4050';
