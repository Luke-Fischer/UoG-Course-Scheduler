<template>
    <div class="admin">
        <h1>Admin</h1>
        <form
            enctype="multipart/form-data"
            action="/api/update_course_data"
            method="POST"
        >
            <input type="file" name="file" />
            <input type="submit" name="Upload" value="Upload" />
        </form>
    </div>
</template>

<script lang="ts">
import { Vue } from "vue-class-component";
export default class AdminView extends Vue {}
</script>
