<template>
  <div id="page-content-wrapper">
    <div class="container-fluid">
      <div class="row">
        <div class="col-lg-12">
          <form @submit.prevent="taskSubmit">
            <div class="form-group">
              <input type="text" class="form-control" id="task" v-model="task" placeholder="Yapılacak iş ekle">
            </div>
          </form>
          <ul class="list-group">
            <Task v-for="task in tasks" v-bind:key="task.id" v-bind:body="task.body" v-bind:is_finished="task.is_finished" v-bind:id="task.id" v-bind:list_id="task.list_id" />
          </ul>
          <div class="showFinishedButton">
            <button v-on:click="showFinishedTasks" type="button" class="btn btn-primary" style="margin-top:1%;">
              <a>Tamamlanan işleri göster</a>
            </button>
            <ul style="text-decoration: line-through;" class="list-group" v-if="showFinished">
              <Task v-for="task in finishedTasks" v-bind:key="task.id" v-bind:body="task.body" v-bind:is_finished="task.is_finished" v-bind:id="task.id" v-bind:list_id="task.list_id" />
            </ul>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>

<script>
import Task from '@/components/Task.vue'
export default {
  name: 'home',
  data() {
    return {
      task: '',
      showFinished: false
    }
  },
  methods: {
    taskSubmit() {
      this.$store.dispatch("createTask", {body:this.task, list_id:this.listid})
      this.task = ''
    },
    showFinishedTasks() {
      this.showFinished = !this.showFinished
    }
  },
  components: {
    Task
  },
  computed: {
    tasks () {
      return this.$store.getters.unfinishedTasks
    },
    listid() {
      return this.$store.getters.getListId
    },
    finishedTasks() {
      return this.$store.getters.finishedTasks
    }
  }
}
</script>

<style>


.form-group {
  margin-right: 5%;
}
.list-group {
  margin-right: 5%;
  margin-top: 2%;
}


</style>