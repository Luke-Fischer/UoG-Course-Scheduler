<template>
    <div class="your-course-section">
        <div id="card-container">
            <YourCourseCard
                v-for="(course, index) in yourSelectedCourses"
                v-on:click="removeCourses(course)"
                :key="index"
                :your-course-name="
                    course[0] + ' - ' + course[1] + ' (' + course[2] + ')'
                "
                :your-course-prof="course[3]"
                :your-course-credits="course[10]"
                :your-course-lectures="'Lec: ' + classTimes(course, 'lec')"
                :your-course-labs="'Lab: ' + classTimes(course, 'lab')"
            />
        </div>
        <button class="autofill-button" v-on:click="autofillCourses">
            Autofill Courses
        </button>
        <button
            class="generate-schedule-button"
            v-on:click="($parent as any).courseSelect = false"
        >
            Generate Schedule
        </button>
    </div>
</template>

<script lang="ts">
import YourCourseCard from "./YourCourseCard.vue";
import { Vue, prop, Options } from "vue-class-component";

class YourCourseSectionProps {
    yourSelectedCourses = prop({
        type: Object,
        required: true,
        default: {},
    });
}
@Options({
    components: {
        YourCourseCard,
    },
})
export default class YourCourseSection extends Vue.with(
    YourCourseSectionProps
) {
    autofillCourses() {
        if (
            (this.$parent as any).selectedCourses.length +
                (this.$parent as any).autofillNum >
            6
        ) {
            alert(
                "You cannot autofill to more than 6 selected courses! Reduce the autofill number."
            );
            return;
        } else if (
            (this.$parent as any).autofillNum >
            (this.$parent as any).filteredCourses.length
        ) {
            alert(
                "There are not enough courses to autofill! Reduce your filtering."
            );
            return;
        }

        let addedCourseNum = 0;
        for (let i = 0; i < (this.$parent as any).autofillNum; i++) {
            for (let course of (this.$parent as any).filteredCourses) {
                let collision = false;
                for (let selectedCourse of (this.$parent as any)
                    .selectedCourses) {
                    if (
                        course[0] == selectedCourse[0] ||
                        this.checkCollision(course, selectedCourse)
                    ) {
                        collision = true;
                        break;
                    }
                }

                if (
                    (this.$parent as any).selectedCourses.length == 0 ||
                    !collision
                ) {
                    (this.$parent as any).selectedCourses.push(course);
                    addedCourseNum += 1;
                    break;
                }
            }
        }

        if (addedCourseNum != (this.$parent as any).autofillNum) {
            alert(
                "Due to collisions between courses, autofill was only able to add " +
                    addedCourseNum +
                    "/" +
                    (this.$parent as any).autofillNum +
                    " courses!"
            );
        }
    }
    checkCollision(course1: Array<string>, course2: Array<string>) {
        const indexesOf = (arr: any, item: any) =>
            arr.reduce(
                (acc: any, v: any, i: any) => (v === item && acc.push(i), acc),
                []
            );

        let courseMeetings1 = indexesOf(course1, "lec").concat(
            indexesOf(course1, "lab")
        );
        let courseMeetings2 = indexesOf(course2, "lec").concat(
            indexesOf(course2, "lab")
        );
        for (let index1 of courseMeetings1) {
            for (let index2 of courseMeetings2) {
                if (course1[index1 + 3] == course2[index2 + 3]) {
                    let startHour1 = parseInt(
                        course1[index1 + 4].split(" ")[1].split(":")[0]
                    );
                    let startMin1 = parseInt(
                        course1[index1 + 4].split(" ")[1].split(":")[1]
                    );
                    let endHour1 = parseInt(
                        course1[index1 + 5].split(" ")[1].split(":")[0]
                    );
                    let endMin1 = parseInt(
                        course1[index1 + 5].split(" ")[1].split(":")[1]
                    );
                    let startHour2 = parseInt(
                        course2[index2 + 4].split(" ")[1].split(":")[0]
                    );
                    let startMin2 = parseInt(
                        course2[index2 + 4].split(" ")[1].split(":")[1]
                    );
                    let endHour2 = parseInt(
                        course2[index2 + 5].split(" ")[1].split(":")[0]
                    );
                    let endMin2 = parseInt(
                        course2[index2 + 5].split(" ")[1].split(":")[1]
                    );
                    if (
                        (startHour1 >= startHour2 && startHour1 <= endHour2) ||
                        (startHour2 >= startHour1 && startHour2 <= endHour1)
                    ) {
                        if (
                            (endHour1 == startHour2 ||
                                endHour2 == startHour1) &&
                            (endMin1 >= startMin2 || endMin2 >= startMin1)
                        ) {
                            return true;
                        } else if (
                            endHour1 != startHour2 &&
                            endHour2 != startHour1
                        ) {
                            return true;
                        }
                    }
                }
            }
        }

        return false;
    }
    removeCourses(course: Array<string>) {
        (this.$parent as any).selectedCourses!.splice(
            (this.$parent as any).selectedCourses!.indexOf(course),
            1
        );
    }
    classTimes(course: Array<string>, type: string) {
        let returnString = "";
        let foundType = 0;
        for (let i = 0; i < course.length; i++) {
            if (course[i] == type) {
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
            }
        }
        if (returnString == "") {
            return "None";
        } else {
            return returnString;
        }
    }
}
</script>

<style lang="css">
.your-course-section {
    padding: 10px;
}

.generate-schedule-button {
    border-radius: 20px;
    height: 50px;
    width: 200px;
    border: none;
    background-color: #52b788;
    line-height: 0px;
    font-size: 20px;
}
.generate-schedule-button:hover {
    background-color: #74c69d;
}

.autofill-button {
    border-radius: 20px;
    height: 50px;
    width: 200px;
    border: none;
    background-color: rgb(253, 181, 0);
    line-height: 0px;
    font-size: 20px;
}
.autofill-button:hover {
    background-color: #f4d15e;
}

#card-container {
    height: calc(100vh - 400px);
    overflow-y: auto;
    margin-bottom: 20px;
    cursor: pointer;
}
</style>
