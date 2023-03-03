import { shallowMount } from "@vue/test-utils";
import YourCourseSectionProps from "@/components/YourCourseSection.vue";

describe("YourCourseSection.vue", () => {
    it("Checks yourSelectedCourses", () => {
        const msg = "";
        const wrapper = shallowMount(YourCourseSectionProps, {
            props: {
                type: String,
                required: true,
                default: "",
            },
        });
        expect(wrapper.text()).toMatch(msg);
    });
});
