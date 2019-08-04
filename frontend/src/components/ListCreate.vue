<template>
    <div>
          <div v-if="showModal">
            <transition name="modal">
            <div class="modal-mask">
                <div class="modal-wrapper">

                <div class="modal-dialog" role="document">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title">Liste Ekle</h5>
                            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                            <span aria-hidden="true" @click="showModal = false">&times;</span>
                            </button>
                        </div>
                        <form @submit.prevent="listSubmit">
                            <div class="modal-body form-group">
                                <input type="text" class="form-control" placeholder="Liste adı" v-model="title">
                            </div>
                            <div class="modal-footer">
                                <button type="button" class="btn btn-secondary" @click="showModal = false">Kapat</button>
                                <button type="submit" class="btn btn-primary">Liste Ekle</button>
                            </div>
                        </form>
                    </div>
                </div>

                </div>
            </div>
            </transition>
        </div>

        <button class="btn btn-primary" @click="showModal = true">Yeni Liste</button>
    </div>
</template>

<script>
export default {
    data() {
        return {
            showModal: false,
            title: '',
            user_id: this.$store.state.user_id
        }
    },
    methods: {
        listSubmit() {
            this.$store.dispatch("createList", {title:this.title, user_id: this.user_id})
            this.showModal = false
        }
    }
}
</script>

<style>
.modal-mask {
  position: fixed;
  z-index: 9998;
  top: 0;
  left: 0;
  width: 100%;
  height: 100%;
  background-color: rgba(0, 0, 0, .5);
  display: table;
  transition: opacity .3s ease;
}

.modal-wrapper {
  display: table-cell;
  vertical-align: middle;
}
</style>
