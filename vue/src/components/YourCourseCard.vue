<template>
    <div class="your-course-card">
        <h2 id="your-course-name">{{ yourCourseName }}</h2>
        <p id="your-course-prof">{{ yourCourseProf }}</p>
        <p id="your-course-credits">{{ yourCourseCredits }}</p>
        <div class="lect-div">
            <p id="your-course-lectures">{{ yourCourseLectures }}</p>
        </div>
        <div class="lab-div">
            <p id="your-course-labs">{{ yourCourseLabs }}</p>
        </div>
    </div>
</template>

<script lang="ts">
import { prop, Vue } from "vue-class-component";

class YourCourseCardProps {
    yourCourseName = prop({
        type: String,
        required: true,
        default: "",
    });

    yourCourseProf = prop({
        type: String,
        required: true,
        default: "",
    });

    yourCourseCredits = prop({
        type: String,
        required: true,
        default: "",
    });

    yourCourseLectures = prop({
        type: String,
        required: true,
        default: "",
    });

    yourCourseLabs = prop({
        type: String,
        required: true,
        default: "",
    });
}

export default class YourCourseCard extends Vue.with(YourCourseCardProps) {}
</script>

<style lang="css">
.your-course-card {
    border-radius: 20px;
    background: white;
    line-height: 0px;
    font-size: 10px;
    cursor: pointer;
}
.your-course-card:hover {
    background: rgb(255, 209, 209);
}
#your-course-name {
    text-align: center;
    font-size: 14px;
    padding-top: 10px;
}
.lect-div {
    display: flex;
    justify-content: center;
    align-items: center;
}
.lab-div {
    display: flex;
    justify-content: center;
    align-items: center;
    margin: 0 10px 10px 0;
}
#your-course-prof {
    text-align: center;
    font-size: 10px;
    padding-top: 15px;
}
#your-course-credits {
    text-align: center;
    font-size: 10px;
    padding-top: 4px;
    padding-bottom: 4px;
}
#your-course-lectures {
    text-align: center;
    font-size: 10px;
    line-height: 12px;
    width: 80%;
}
#your-course-labs {
    text-align: center;
    font-size: 10px;
    line-height: 12px;
    width: 80%;
}
</style>
