<template>
    <div>
        <Navbar v-bind:isActive="isActive" />
        <div id="wrapper" v-bind:class="{ 'toggled': isActive }">
            <Sidebar />
            <Home />
        </div>
    </div>
</template>

<script>
import Sidebar from '@/components/Sidebar.vue'
import Navbar from '@/components/Navbar.vue'
import Home from '@/views/Home.vue'
export default {
    components: {
        Sidebar, Navbar, Home
    },
    computed: {
        isActive() {
            return this.$store.getters.isActive
        }
    }
}
</script>

