import { shallowMount } from "@vue/test-utils";
import YourCourseCardProps from "@/components/YourCourseCard.vue";

describe("YourCourseCard.vue", () => {
    it("Checks YourCourseName", () => {
        const msg = "";
        const wrapper = shallowMount(YourCourseCardProps, {
            props: {
                type: String,
                required: true,
                default: "",
            },
        });
        expect(wrapper.text()).toMatch(msg);
    });
});

describe("YourCourseCard.vue", () => {
    it("Checks YourCourseProf", () => {
        const msg = "";
        const wrapper = shallowMount(YourCourseCardProps, {
            props: {
                type: String,
                required: true,
                default: "",
            },
        });
        expect(wrapper.text()).toMatch(msg);
    });
});

describe("YourCourseCard.vue", () => {
    it("Checks YourCourseCredits", () => {
        const msg = "";
        const wrapper = shallowMount(YourCourseCardProps, {
            props: {
                type: String,
                required: true,
                default: "",
            },
        });
        expect(wrapper.text()).toMatch(msg);
    });
});

describe("YourCourseCard.vue", () => {
    it("Checks YourCourseLectures", () => {
        const msg = "";
        const wrapper = shallowMount(YourCourseCardProps, {
            props: {
                type: String,
                required: true,
                default: "",
            },
        });
        expect(wrapper.text()).toMatch(msg);
    });
});

describe("YourCourseCard.vue", () => {
    it("Checks YourCourse", () => {
        const msg = "";
        const wrapper = shallowMount(YourCourseCardProps, {
            props: {
                type: String,
                required: true,
                default: "",
            },
        });
        expect(wrapper.text()).toMatch(msg);
    });
});
