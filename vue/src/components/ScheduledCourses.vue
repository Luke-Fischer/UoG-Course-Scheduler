<template>
    <FullCalendar :id="calendar" :options="calendarOptions" :key="componentKey">
    </FullCalendar>
</template>

<script lang="ts">
/* eslint-disable */
import { defineComponent } from "vue";
import "@fullcalendar/core/vdom"; // solve problem with Vite
import FullCalendar, {
    CalendarOptions,
    EventApi,
    DateSelectArg,
    EventClickArg,
} from "@fullcalendar/vue3";
import "@fullcalendar/core/vdom";
import dayGridPlugin from "@fullcalendar/daygrid";
import timeGridPlugin from "@fullcalendar/timegrid";
import interactionPlugin from "@fullcalendar/interaction";
import { INITIAL_EVENTS, createEventId } from "../event-utils";
var globalYear: string;
var globalSemester: string;
const ScheduledCourses = defineComponent({
    components: {
        FullCalendar,
    },
    props: {
        selectedCourses: Array,
    },
    mounted() {
        console.log(this.selectedCourses);
        let selectedCourses: string[] = this.selectedCourses as string[];
        globalYear = selectedCourses[0][4];
        globalSemester = selectedCourses[0][5];
        // data preprocessing i.e., create events array
        let classTitles = []; // array of event titles
        let startTimes = []; // array of start times
        let endTimes = [];
        let customEvents: any = []; // array of class events
        let curr = new Date(); // get current date
        let first = curr.getDate() - curr.getDay(); // First day is the  day of the month - the day of the week
        if (selectedCourses !== undefined) {
            let counter = 0;
            let numEvents = 0;
            for (var currCourse of selectedCourses) {
                let courseCode: string = selectedCourses[counter][0];
                let courseName: string = selectedCourses[counter][1];
                let section: string = selectedCourses[counter][2];
                let prof: string = selectedCourses[counter][3];
                let termYear: string = selectedCourses[counter][4];
                let termSeason: string = selectedCourses[counter][5];
                let capcityAvailable: string = selectedCourses[counter][6];
                let capacityTotal: string = selectedCourses[counter][7];
                let status: string = selectedCourses[counter][8];
                let location: string = selectedCourses[counter][9];
                let credits: string = selectedCourses[counter][10];
                let level: string = selectedCourses[counter][11];
                // get all the meeting times and types
                let inner = 12;
                for (
                    inner = 12;
                    inner < currCourse.length;
                    inner++
                ) {
                    let colour = "lightblue";
                    if (
                        currCourse[inner] == "lec" ||
                        currCourse[inner] == "lab" ||
                        currCourse[inner] == "sem" ||
                        currCourse[inner] == "exam"
                    ) {
                        let meetingType = currCourse[inner];
                        let lectureHall = currCourse[inner+1];
                        let lectureRoom = currCourse[inner+2];
                        let dayOffset = this.getDayOffset(
                            selectedCourses[counter][inner + 3]
                        );
                        let day = currCourse[inner + 3];
                        let startTime = currCourse[inner + 4].split(" ")[1];
                        let endTime = currCourse[inner + 5].split(" ")[1];
                        let date = (first + dayOffset);
                        let month = curr.getMonth();
                        console.log("first = ", first);
                        if (first < 1) {
                            let numDaysPreviousMonth = 
                                new Date(curr.getFullYear(), month,0).getDate();
                            if (first + dayOffset > 0){
                                month = month +1;
                                date = (first + dayOffset);
                            } 
                            else {
                                date = numDaysPreviousMonth + first + dayOffset
                            }
                        }
                        else{
                            month = month + 1;
                            date = first + dayOffset;
                        }
                        let dateX = "";
                        if (date < 10){
                            dateX = ("0"+date) as string;
                        } else{
                            dateX = date.toString();
                        }
                        let startStr = curr.getFullYear() +
                                "-" +
                                month +
                                "-" +
                                dateX +
                                "T" +
                                startTime;
                        let endStr = curr.getFullYear() +
                                "-" +
                                month +
                                "-" +
                                dateX +
                                "T" +
                                endTime;
                        if (numEvents > 0) {
                            if (meetingType != "exam"){
                                for (var currEvent of customEvents ){
                                    console.log("currEvent b4 col:", currEvent);
                                    if (currEvent.dayOfWeek == day && 
                                        currEvent.meetingType != "exam"
                                    ){
                                        let collision = this.checkCollision(
                                            currEvent.meetStartTime,
                                            currEvent.meetEndTime,
                                            startTime,
                                            endTime
                                        );
                                        if ( collision != 0){
                                            currEvent.color = "#FFC5B8";
                                            colour = "#FFC5B8";
                                            break;
                                        }
                                    }
                                }
                            }
                        }
                        if (colour != "#FFC5B8"){
                            colour = this.getColour(meetingType);
                        }
                        customEvents[numEvents] = {
                            title: courseCode + "*" + section + "\n" + meetingType,
                            start: startStr,
                            end: endStr,
                            xStart: startStr,
                            xEnd: endStr,
                            description:
                                courseCode + "*" + section + " - " + courseName,
                            code: courseCode,
                            section: section,
                            courseName: courseName,
                            prof: prof,
                            term: termYear + " " + termSeason,
                            capacity: capcityAvailable + " / " + capacityTotal,
                            status: status,
                            location: location,
                            level: level,
                            dayOfWeek: day,
                            meetingType: meetingType,
                            meetStartTime: startTime,
                            meetEndTime: endTime,
                            lectureHall: lectureHall,
                            lectureRoom: lectureRoom,
                            color: colour,
                            borderColor : "black",
                        };
                        console.log("New event created: ", currEvent)
                        numEvents++;
                    }
                }
                counter++;
            }
            console.log("numEvents = ",numEvents);
        }
        console.log("custom events = ", customEvents)
        this.calendarOptions.eventSources = [
            { // normal events
                events: customEvents,
                textColor: "black",
            },
        ];
        console.log("this.calendarOptions.eventSources = ", this.calendarOptions.eventSources);
    },
    data() {
        return {
            calendarOptions: {
                plugins: [
                    dayGridPlugin,
                    timeGridPlugin,
                    interactionPlugin, // needed for dateClick
                ],
                headerToolbar: {
                    left: "title",
                    center: "",
                    right: "",
                },
                initialView: "timeGridWeek",
                height: "85vh",
                expandRows: true,
                selectMirror: true,
                dayMaxEvents: true,
                weekends: true,
                scrollTimeReset: false,
                timeZone: 'EST',
                editable: false,
                overlap: false,
                selectable: false,
                allDaySlot: false,
                slotMinTime: "08:00:00", // earliest time 
                slotMaxTime: "22:00:00", // latest time
                displayEventTime: false,
                eventClick: function(info: any) {
                // when an event is clicked displayed more information about it
                    let displayInfo = "";
                    displayInfo += info.event.extendedProps.code + "*";
                    displayInfo += info.event.extendedProps.section + "\n";
                    displayInfo += info.event.extendedProps.courseName + "\n";
                    displayInfo += info.event.extendedProps.term + "\n";
                    displayInfo += "__________________________________\n";
                    displayInfo += "Instructors\n";
                    displayInfo += info.event.extendedProps.prof + "\n";
                    displayInfo += "Meeting Information\n";
                    displayInfo += info.event.extendedProps.lectureHall + " ";
                    displayInfo += info.event.extendedProps.lectureRoom + "\n";
                    displayInfo += info.event.extendedProps.dayOfWeek + " ";
                    displayInfo += info.event.extendedProps.meetStartTime;
                    displayInfo += "-" + info.event.extendedProps.meetEndTime;
                    displayInfo += " (" + info.event.extendedProps.meetingType;
                    displayInfo += ")";
                    alert(displayInfo);
                },
                eventDidMount: function (info: any) {
                    info.el.title = info.event.extendedProps.description;
                },
                titleFormat: function (info: any) {
                    return "Schedule " + globalYear + " " + globalSemester;
                },
                dayHeaderContent: (args) => {
                    let days = 
                    ["MON", "TUE", "WED", "THUR", "FRI", "SAT", "SUN"];
                    return days[args.date.getDay()];
                },
            } as CalendarOptions,
            currentEvents: [] as EventApi[],
            eventSources: [
                {
                    events: this.customEvents,
                },
            ],
        };
    },
    methods: {
        handleWeekendsToggle() {
            this.calendarOptions.weekends = !this.calendarOptions.weekends; // update a property
        },
        handleDateSelect(selectInfo: DateSelectArg) {
            let title = prompt("Please enter a new title for your event");
            let calendarApi = selectInfo.view.calendar;
            calendarApi.unselect(); // clear date selection
            if (title) {
                calendarApi.addEvent({
                    id: createEventId(),
                    title,
                    start: selectInfo.startStr,
                    end: selectInfo.endStr,
                    allDay: selectInfo.allDay,
                });
            }
        },
        handleEvents(events: EventApi[]) {
            this.currentEvents = events;
        },
        getDayOffset(dayIn: string): number {
            let dayOffset = 0;
            switch (dayIn) {
            case "Sun":
                dayOffset = 0;
                break;
            case "Mon":
                dayOffset = 1;
                break;
            case "Tues":
                dayOffset = 2;
                break;
            case "Wed":
                dayOffset = 3;
                break;
            case "Thur":
                dayOffset = 4;
                break;
            case "Fri":
                dayOffset = 5;
                break;
            case "Sat":
                dayOffset = 6;
                break;
            }
            return dayOffset;
        },
        checkCollision(start1:string, end1: string, start2: string, end2: string): number {
            let result = 0; // return of 0 means no collision
            // convert strings to numbers for arithmetic comparison
            let time1: number = +(start1.split(":")[0]);
            time1 += (+(start1.split(":")[1]) / 60);
            let time2: number = +(end1.split(":")[0]);
            time2 += (+(end1.split(":")[1]) / 60);
            let time3: number = +(start2.split(":")[0]);
            time3+= +(+(start2.split(":")[1]) / 60);
            let time4: number = +(end2.split(":")[0]);
            time4 += (+(end2.split(":")[1]) / 60);
            // options for collisions 
            // Same start time (must have run at same time for a portion)
            // Same end time (must have run at the same time for a portion)
            // A starts before B, and B starts before A ends (offset with some overlap)
            // B starts before A, and A starts before B ends (offset with some overlap)
            // A starts after B and A ends before B (A enclipsed in B)
            // B starts after A and B ends before A (B enclipsed in A)
            if ( time1 == time3 ){
                result = -1;
            }
            else if ( time2 == time4){
                result = -2;
            }
            else if (time1 < time3 && time4 < time2){
                result = -3;
            }
            else if (time3 < time1 && time2 < time4){
                result = -4;
            }
            else if (time1 > time3 && time4 > time2){
                result = -5;
            }
            else if (time3 > time1 && time2 > time4){
                result = -6;
            }
            return result; 
        },
        getColour(meetingType: string): string {
            let returnColour = "blue";
            if (meetingType == "lec"){
                returnColour = "LightCyan";
            }
            else if (meetingType == "lab"){
                returnColour = "PaleGreen";
            }
            else if (meetingType == "sem"){
                returnColour = "lavendar";
            }
            else if (meetingType == "exam"){
                returnColour = "Wheat";
            }
            return returnColour;
        },
    },
});
export default ScheduledCourses;
</script>

<style lang="css">
body{
    margin: 0;
    padding: 1vh 1vw 0 1vw;
    font-family: Arial, sans-serif;
}

.fc {
    font-size: 10px;
    margin: 1vh 1vw 0 1vw;;
}

nav {
    padding: 0px 0 5px 0;
    font-size: x-small;
}


.fc-col-header-cell-cushion {
    color: black;
    font-size: x-small;
    /*day of the week colour */
}

.fc-toolbar {
    color: blue;
    margin: 0;
    padding: 0;
    font-size: smaller;
    /* Schedule W22 text */
}

/*remove highlight on current day*/
.fc-day-today {
    background-color: inherit !important;
}

.fc-event {
    /* event text content */
    text-align: left;
}

.fc td {
    /* time column */
    color: black;
    font-weight: 600;
}

.fc .fc-event-title {
    font-weight: 500;
    margin: 2% 0 2% 0;
    font-size: 10px;

}

.fc-h-event .fc-event-main-frame {
    display: block;
    /* for make fc-event-title-container expand */
}

#pageHeader {
    font-size: 24px;
    font-weight: 600;
    padding: 0;
}

h4 {
    font-size: 12px;
    padding: 0;
    font-weight: 700;
    color: black;
}

#back-button {
    border: .5px solid #000;
    cursor: pointer;
    border-radius: 15px;
    background-color: AliceBlue;
    
}
</style>



