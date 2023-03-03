<template>
    <div class="course-card">
        <h2 id="course-name">{{ courseName }}</h2>
        <p id="course-prof">{{ courseProf }}</p>
        <p id="course-credits">{{ courseCredits }}</p>
        <div class="lect-div">
            <p id="course-lectures">{{ courseLectures }}</p>
        </div>
        <div class="lab-div">
            <p id="course-labs">{{ courseLabs }}</p>
        </div>
        <div class="button-popup">
            <p id="popup-title">More Info</p>
            <div class="button-popup-content">
                <p id="course-term">{{ courseTerm }}</p>
                <p id="course-availability">
                    {{ courseAvailability }}
                </p>
                <p id="course-campus">{{ courseCampus }}</p>
                <div class="lect-div">
                    <p id="course-meetings-lectures">
                        {{ courseMeetingsLectures }}
                    </p>
                </div>
                <div class="lab-div">
                    <p id="course-meetings-labs">
                        {{ courseMeetingsLabs }}
                    </p>
                </div>
                <div class="course-about">
                    <iframe
                        :src="`${courseCode}`"
                        name="Course_Info"
                        class="course-about"
                        title="AboutCourse"
                        style="height: 100%; width: 90%"
                    ></iframe>
                </div>
            </div>
        </div>
    </div>
</template>

<script lang="ts">
import { prop, Vue } from "vue-class-component";

class CourseCardProps {
    courseName = prop({
        type: String,
        required: true,
        default: "",
    });

    courseProf = prop({
        type: String,
        required: true,
        default: "",
    });

    courseCredits = prop({
        type: String,
        required: true,
        default: "",
    });

    courseLectures = prop({
        type: String,
        required: true,
        default: "",
    });

    courseLabs = prop({
        type: String,
        required: true,
        default: "",
    });

    courseTerm = prop({
        type: String,
        required: true,
        default: "",
    });

    courseAvailability = prop({
        type: String,
        required: true,
        default: "",
    });

    courseCampus = prop({
        type: String,
        required: true,
        default: "",
    });

    courseMeetingsLectures = prop({
        type: String,
        required: true,
        default: "",
    });

    courseMeetingsLabs = prop({
        type: String,
        required: true,
        default: "",
    });

    courseCode = prop({
        type: String,
        required: true,
        default: "",
    });
}

export default class CourseCard extends Vue.with(CourseCardProps) {}
</script>

<style lang="css">
.course-card {
    border-radius: 20px;
    background: #adb5bd;
    line-height: 0px;
    cursor: pointer;
    margin-bottom: 1rem;
    color: black;
}
.course-card:hover {
    background: #ced4da;
}
.button-popup {
    position: relative;
    height: 20px;
    width: 80px;
    border-radius: 15px;
    background: #4361ee;
    text-align: center;
    justify-content: center;
    align-items: center;
    line-height: 20px;
    font-size: 15px;
    cursor: pointer;
    left: 50%;
    bottom: 0px;
    -webkit-transform: translateX(-50%);
    transform: translateX(-50%);
}
.button-popup:hover {
    border-radius: 20px;
    width: 100%;
    overflow: hidden;
    height: 1%;
}
#popup-title {
    font-size: 15px;
    font-weight: bold;
    color: white;
}
.button-popup:hover .button-popup-content {
    display: block;
}
.button-popup-content {
    display: none;
    position: relative;
    background-color: #6fa6ff;
    line-height: 30px;
    width: 100%;
    height: 100%;
    z-index: 100;
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
#course-name {
    text-align: center;
    font-size: 20px;
    padding-top: 15px;
}
#course-prof {
    text-align: center;
    font-size: 15px;
    padding-top: 15px;
}
#course-credits {
    text-align: center;
    font-size: 15px;
    padding-top: 15px;
    padding-bottom: 5px;
}
#course-lectures {
    text-align: center;
    font-size: 15px;
    line-height: 15px;
    width: 80%;
}
#course-labs {
    text-align: center;
    font-size: 15px;
    line-height: 15px;
    width: 80%;
}
#course-availability {
    text-align: center;
    font-size: 15px;
    line-height: 15px;
}
#course-campus {
    text-align: center;
    font-size: 15px;
    line-height: 15px;
}
#course-term {
    text-align: center;
    font-size: 15px;
    line-height: 15px;
    padding-top: 15px;
}
</style>
