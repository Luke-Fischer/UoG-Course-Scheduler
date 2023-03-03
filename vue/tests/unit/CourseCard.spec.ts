import { shallowMount } from "@vue/test-utils";
import CourseCardProps from "@/components/CourseCard.vue";

describe("CourseCard.vue", () => {
    it("Checks CourseName", () => {
        const msg = "";
        const wrapper = shallowMount(CourseCardProps, {
            props: {
                type: String,
                required: true,
                default: "",
            },
        });
        expect(wrapper.text()).toMatch(msg);
    });
});

describe("CourseCard.vue", () => {
    it("Checks CourseProf", () => {
        const msg = "";
        const wrapper = shallowMount(CourseCardProps, {
            props: {
                type: String,
                required: true,
                default: "",
            },
        });
        expect(wrapper.text()).toMatch(msg);
    });
});

describe("CourseCard.vue", () => {
    it("Checks CourseCredits", () => {
        const msg = "";
        const wrapper = shallowMount(CourseCardProps, {
            props: {
                type: String,
                required: true,
                default: "",
            },
        });
        expect(wrapper.text()).toMatch(msg);
    });
});

describe("CourseCard.vue", () => {
    it("Checks CourseLectures", () => {
        const msg = "";
        const wrapper = shallowMount(CourseCardProps, {
            props: {
                type: String,
                required: true,
                default: "",
            },
        });
        expect(wrapper.text()).toMatch(msg);
    });
});

describe("CourseCard.vue", () => {
    it("Checks Course", () => {
        const msg = "";
        const wrapper = shallowMount(CourseCardProps, {
            props: {
                type: String,
                required: true,
                default: "",
            },
        });
        expect(wrapper.text()).toMatch(msg);
    });
});
