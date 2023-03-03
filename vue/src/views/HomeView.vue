<template>
    <div class="home">
        <h1 id="pageHeader" style="padding-top: 0px">
            University of Guelph Course Scheduler
        </h1>

        <div
            v-show="!courseSelect"
            id="back-button"
            v-on:click="courseSelect = true"
        >
            <h4 style="margin: 5px">Back To Course Selection</h4>
        </div>

        <!-- Center Grid -->
        <div class="grid-container" v-show="courseSelect">
            <div class="filter-container">
                <h1
                    style="
                        margin-bottom: 0px;
                        padding-bottom: 0px;
                        padding-top: 0px;
                    "
                >
                    Filters
                </h1>
                <FilterSection />
            </div>
            <div class="course-container">
                <h1 style="margin-bottom: 0px">Courses</h1>
                <div id="courses-container">
                    <CourseSection />
                </div>
            </div>
            <div class="your-course-container">
                <h1>Your Courses</h1>
                <YourCourseSection :your-selected-courses="selectedCourses" />
            </div>
        </div>
    </div>

    <div v-if="!courseSelect">
        <ScheduledCourses :selected-courses="selectedCourses" />
    </div>
</template>

<script lang="ts">
import { Vue, Options } from "vue-class-component";
import FilterSection from "@/components/FilterSection.vue";
import CourseSection from "@/components/CourseSection.vue";
import YourCourseSection from "@/components/YourCourseSection.vue";
import ScheduledCourses from "@/components/ScheduledCourses.vue";

@Options({
    components: {
        FilterSection,
        CourseSection,
        YourCourseSection,
        ScheduledCourses,
    },
})
export default class Home extends Vue {
    courseSelect = true;
    courses = [];
    selectedCourses = [];
    filteredCourses = [];
    autofillNum = 1;
}
</script>

<style lang="css">
h1 {
    padding: 10px;
}
h2 {
    margin: 0;
    font-size: 16px;
}
ul {
    margin: 0;
    padding: 0 0 0 1.5em;
}
li {
    margin: 1.5em 0;
    padding: 0;
}
b {
    /* used for event dates/times */
    margin-right: 3px;
}
.grid-container {
    display: grid;
    grid-template-columns: 1fr 1fr 1fr;
    grid-gap: 10px;
    padding: 10px;
    border-radius: 20px;
    background: rgb(237, 237, 237);
    height: calc(100vh - 150px);
}
.filter-container {
    border-top-left-radius: 20px;
    border-bottom-left-radius: 20px;
    background: rgb(184, 184, 184);
    overflow-y: auto;
    height: calc(100vh - 170px);
    padding: 10px;
}
.course-container {
    height: calc(100vh - 170px);
    padding: 10px;
}
.your-course-container {
    border-top-right-radius: 20px;
    border-bottom-right-radius: 20px;
    background: rgb(184, 184, 184);
}
#courses-container {
    overflow-y: auto;
    height: calc(100vh - 248px);
}

#back-button {
    border: 0.5px solid black;
    cursor: pointer;
    border-radius: 15px;
}
</style>
