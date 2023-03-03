<template>
    <div class="filter-section">
        <h3 id="filter-headings">Semester</h3>
        <input type="radio" value="F22" v-model="semesterFilter" />
        <label class="checkbox-label">Fall 2022</label><br />
        <input type="radio" value="W23" v-model="semesterFilter" />
        <label class="checkbox-label">Winter 2023</label><br />

        <h3 id="filter-headings">Course</h3>
        <input
            v-on:keyup="applyFilter"
            v-model="courseSearch"
            type="text"
            class="input"
        /><br />

        <h3 id="filter-headings">Professor</h3>
        <input
            v-on:keyup="applyFilter"
            v-model="profSearch"
            type="text"
            class="input"
        /><br />

        <h3 id="filter-headings">Credits</h3>
        <input type="checkbox" value="0.0" v-model="creditFilter" />
        <label class="checkbox-label">0</label><br />
        <input type="checkbox" value="0.25" v-model="creditFilter" />
        <label class="checkbox-label">0.25</label><br />
        <input type="checkbox" value="0.5" v-model="creditFilter" />
        <label class="checkbox-label">0.5</label><br />
        <input type="checkbox" value="0.75" v-model="creditFilter" />
        <label class="checkbox-label">0.75</label><br />
        <input type="checkbox" value="1.0" v-model="creditFilter" />
        <label class="checkbox-label">1</label><br />

        <h3 id="filter-headings">Course Level</h3>
        <input type="checkbox" value="1" v-model="levelFilter" />
        <label class="checkbox-label">1000</label><br />
        <input type="checkbox" value="2" v-model="levelFilter" />
        <label class="checkbox-label">2000</label><br />
        <input type="checkbox" value="3" v-model="levelFilter" />
        <label class="checkbox-label">3000</label><br />
        <input type="checkbox" value="4" v-model="levelFilter" />
        <label class="checkbox-label">4000</label><br />
        <input type="checkbox" value="5" v-model="levelFilter" />
        <label class="checkbox-label">5000</label><br />
        <input type="checkbox" value="6" v-model="levelFilter" />
        <label class="checkbox-label">6000</label><br />

        <h3 id="filter-headings">Lecture Day</h3>
        <input type="checkbox" value="Mon" v-model="lecDayFilter" />
        <label class="checkbox-label">Monday</label><br />
        <input type="checkbox" value="Tues" v-model="lecDayFilter" />
        <label class="checkbox-label">Tuesday</label><br />
        <input type="checkbox" value="Wed" v-model="lecDayFilter" />
        <label class="checkbox-label">Wednesday</label><br />
        <input type="checkbox" value="Thur" v-model="lecDayFilter" />
        <label class="checkbox-label">Thursday</label><br />
        <input type="checkbox" value="Fri" v-model="lecDayFilter" />
        <label class="checkbox-label">Friday</label><br />

        <h3 id="filter-headings">Lab Day</h3>
        <input type="checkbox" value="Mon" v-model="labDayFilter" />
        <label class="checkbox-label">Monday</label><br />
        <input type="checkbox" value="Tues" v-model="labDayFilter" />
        <label class="checkbox-label">Tuesday</label><br />
        <input type="checkbox" value="Wed" v-model="labDayFilter" />
        <label class="checkbox-label">Wednesday</label><br />
        <input type="checkbox" value="Thur" v-model="labDayFilter" />
        <label class="checkbox-label">Thursday</label><br />
        <input type="checkbox" value="Fri" v-model="labDayFilter" />
        <label class="checkbox-label">Friday</label><br />

        <h3 id="filter-headings">Autofill</h3>
        <input type="radio" value="1" v-model="autofillFilter" />
        <label class="checkbox-label">1</label><br />
        <input type="radio" value="2" v-model="autofillFilter" />
        <label class="checkbox-label">2</label><br />
        <input type="radio" value="3" v-model="autofillFilter" />
        <label class="checkbox-label">3</label><br />
        <input type="radio" value="4" v-model="autofillFilter" />
        <label class="checkbox-label">4</label><br />
        <input type="radio" value="5" v-model="autofillFilter" />
        <label class="checkbox-label">5</label><br />
        <input type="radio" value="6" v-model="autofillFilter" />
        <label class="checkbox-label">6</label><br />
    </div>
</template>

<script lang="ts">
import { Vue, Options } from "vue-class-component";

@Options({
    watch: {
        semesterFilter() {
            (this.$parent as any).selectedCourses = [];
            this.applyFilter();
        },
        creditFilter() {
            this.applyFilter();
        },
        levelFilter() {
            this.applyFilter();
        },
        lecDayFilter() {
            this.applyFilter();
        },
        labDayFilter() {
            this.applyFilter();
        },
        autofillFilter() {
            this.updateAutofill();
        },
    },
})
export default class FilterSection extends Vue {
    semesterFilter = "W23";
    courseSearch = "";
    profSearch = "";
    creditFilter = ["0.0", "0.25", "0.5", "0.75", "1.0"];
    levelFilter = ["1", "2", "3", "4", "5", "6"];
    lecDayFilter = ["Mon", "Tues", "Wed", "Thur", "Fri"];
    labDayFilter = ["Mon", "Tues", "Wed", "Thur", "Fri"];
    autofillFilter = "1";

    updateAutofill() {
        (this.$parent as any).autofillNum = parseInt(this.autofillFilter);
    }

    applyFilter() {
        let _semesterFilter = this.semesterFilter;
        let _courseSearch = this.courseSearch;
        let _profSearch = this.profSearch;
        let _creditFilter = this.creditFilter;
        let _levelFilter = this.levelFilter;
        let _lecDayFilter = this.lecDayFilter;
        let _labDayFilter = this.labDayFilter;

        const indexesOf = (arr: any, item: any) =>
            arr.reduce(
                (acc: any, v: any, i: any) => (v === item && acc.push(i), acc),
                []
            );

        (this.$parent as any).filteredCourses = (this.$parent as any).courses;

        (this.$parent as any).filteredCourses = (
            this.$parent as any
        ).filteredCourses.filter((value: Array<string>) => {
            if (_semesterFilter == "F22" && value[5] == "Fall") {
                return true;
            } else if (_semesterFilter == "W23" && value[5] == "Winter") {
                return true;
            }
            return false;
        });

        if (this.courseSearch != "") {
            (this.$parent as any).filteredCourses = (
                this.$parent as any
            ).filteredCourses.filter((value: Array<string>) => {
                if ((value[0] + " " + value[1]).includes(_courseSearch)) {
                    return true;
                }
                return false;
            });
        }

        if (this.profSearch != "") {
            (this.$parent as any).filteredCourses = (
                this.$parent as any
            ).filteredCourses.filter((value: Array<string>) => {
                if (value[3].includes(_profSearch)) {
                    return true;
                }
                return false;
            });
        }

        (this.$parent as any).filteredCourses = (
            this.$parent as any
        ).filteredCourses.filter((value: Array<string>) => {
            if (_creditFilter.indexOf(value[10]) > -1) {
                return true;
            }
            return false;
        });

        (this.$parent as any).filteredCourses = (
            this.$parent as any
        ).filteredCourses.filter((value: Array<string>) => {
            if (_levelFilter.indexOf(value[0].split("*")[1][0]) > -1) {
                return true;
            }
            return false;
        });

        (this.$parent as any).filteredCourses = (
            this.$parent as any
        ).filteredCourses.filter((value: Array<string>) => {
            let indexes = indexesOf(value, "lec");
            if (_lecDayFilter.length > 0 && indexes.length == 0) {
                return false;
            }

            for (let index of indexes) {
                if (_lecDayFilter.indexOf(value[index + 3]) < 0) {
                    return false;
                }
            }
            return true;
        });

        (this.$parent as any).filteredCourses = (
            this.$parent as any
        ).filteredCourses.filter((value: Array<string>) => {
            let indexes = indexesOf(value, "lab");
            if (_labDayFilter.length > 0 && indexes.length == 0) {
                return false;
            }

            for (let index of indexes) {
                if (_labDayFilter.indexOf(value[index + 3]) < 0) {
                    return false;
                }
            }
            return true;
        });
    }
}
</script>

<style lang="css">
.filter-section {
    text-align: left;
    margin-left: 20px;
    padding-bottom: 20px;
}

#filter-headings {
    padding-top: 10px;
}

.checkbox-label {
    padding-inline: 10px;
}

.input {
    width: 90%;
    height: 35px;
}
</style>
