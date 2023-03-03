<template>
    <div class="course-section">
        <CourseCard
            v-for="(course, index) in ($parent as any).filteredCourses"
            v-on:click="selectCourses(course)"
            :key="index"
            :course-name="
                course[0] + ' - ' + course[1] + ' (' + course[2] + ')'
            "
            :course-prof="course[3]"
            :course-credits="course[10]"
            :course-lectures="'Lec: ' + classTimes(course, 'lec', 0)"
            :course-labs="'Lab: ' + classTimes(course, 'lab', 0)"
            :course-term="'Term: ' + course[5] + ' ' + course[4]"
            :course-availability="
                'Availability: ' + course[6] + '/' + course[7]
            "
            :course-campus="'Campus: ' + course[9]"
            :course-meetings-lectures="'Lec: ' + classTimes(course, 'lec', 1)"
            :course-meetings-labs="'Lab: ' + classTimes(course, 'lab', 1)"
            :course-code="
                'https://www.uoguelph.ca/registrar/calendars/undergraduate/2020-2021/courses/' +
                courseCode(course) +
                '.shtml'
            "
        />
    </div>
</template>

<script lang="ts">
import CourseCard from "./CourseCard.vue";
import { Vue, Options } from "vue-class-component";

@Options({
    components: {
        CourseCard,
    },
})
export default class CourseSection extends Vue {
    mounted() {
        fetch("/api/all_courses")
            .then((response) => {
                if (response.status == 200) {
                    return response.json();
                } else {
                    console.log(["QUERY-ERROR", response]);
                }
            })
            .then((response) => {
                (this.$parent as any).courses = response;
                (this.$parent as any).filteredCourses = response;
            });
    }
    courseCode(course: any) {
        let courseCode = course[0];
        courseCode = courseCode.replace("*", "");
        return courseCode.toLowerCase();
    }
    classTimes(course: Array<string>, type: string, index = 0) {
        let returnString = "";
        let foundType = 0;
        for (let i = 0; i < course.length; i++) {
            if (course[i] == type) {
                if (index == 0) {
                    foundType++;
                    let start = course[i + 4].split(" ")[1];
                    let end = course[i + 5].split(" ")[1];
                    let startFormatted =
                        start?.split(":")[0] + ":" + start?.split(":")[1];
                    let endFormatted =
                        end?.split(":")[0] + ":" + end?.split(":")[1];
                    if (foundType > 1) {
                        returnString +=
                            ", " +
                            course[i + 3] +
                            " " +
                            startFormatted +
                            " - " +
                            endFormatted;
                    } else {
                        returnString +=
                            course[i + 3] +
                            " " +
                            startFormatted +
                            " - " +
                            endFormatted;
                    }
                } else {
                    foundType++;
                    let start = course[i + 4].split(" ")[1];
                    let end = course[i + 5].split(" ")[1];
                    let startFormatted =
                        start?.split(":")[0] + ":" + start?.split(":")[1];
                    let endFormatted =
                        end?.split(":")[0] + ":" + end?.split(":")[1];
                    if (foundType > 1) {
                        returnString +=
                            ", " +
                            course[i + 1] +
                            " " +
                            course[i + 2] +
                            " " +
                            course[i + 3] +
                            " " +
                            startFormatted +
                            " - " +
                            endFormatted;
                    } else {
                        returnString +=
                            course[i + 1] +
                            " " +
                            course[i + 2] +
                            " " +
                            course[i + 3] +
                            " " +
                            startFormatted +
                            " - " +
                            endFormatted;
                    }
                }
            }
        }
        if (returnString == "") {
            return "None";
        } else {
            return returnString;
        }
    }

    selectCourses(course: Array<string>) {
        if ((this.$parent as any).selectedCourses!.length < 6) {
            if (!(this.$parent as any).selectedCourses!.includes(course)) {
                (this.$parent as any).selectedCourses!.push(course);
            } else {
                alert("You can not select the same course twice");
            }
        } else {
            alert("You can only select 6 courses");
        }
    }
}
</script>

<style lang="css"></style>
