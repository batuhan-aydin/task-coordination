<template>
    <div>
        <li class="list-group-item">
            <a v-on:click="changeActive">
                <i v-if="!this.is_finished" class="far fa-square"></i>
                <i v-if="this.is_finished" class="far fa-check-square"></i>
            </a>
            {{body}}
        </li>
    </div>
</template>

<script>
export default {
    props: ['body', 'is_finished', 'id', 'list_id'],
    methods: {
        changeActive() {
            console.log(this.list_id)
            this.$store.dispatch("changeFinishStatusTask", {body: this.body, is_finished:this.is_finished, id:this.id, list_id:this.list_id})
        }
    }
}
</script>

<style>

</style>


