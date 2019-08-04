<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  created(){
    this.$store.dispatch("initAuth")
    console.log(this.$store.state.user_id)
    this.$store.dispatch("getUserList")
  }
}
</script>


<style>

</style>
