<template>
    <div>
          <div v-if="showModal">
            <transition name="modal">
            <div class="modal-mask">
                <div class="modal-wrapper">

                <div class="modal-dialog" role="document">
                    <div class="modal-content">
                        <div class="modal-header">
                            <h5 class="modal-title">Güncelle</h5>
                            <button type="button" class="close" data-dismiss="modal" aria-label="Close">
                            <span aria-hidden="true" @click="showModal = false">&times;</span>
                            </button>
                        </div>
                        <form @submit.prevent="updateList">
                            <div class="modal-body form-group">
                                <input type="text" class="form-control" placeholder="Liste adı" v-model="title">
                            </div>
                            <div class="modal-footer">
                                <button type="button" class="btn btn-secondary" @click="showModal = false">Kapat</button>
                                <button type="submit" class="btn btn-primary">İsim Güncelle</button>
                            </div>
                        </form>
                        <form @submit.prevent="addUser()">
                            <div class="modal-body form-group">
                                <input type="text" class="form-control" placeholder="Kullanıcı adı" v-model="username">
                                <ul class="list-group">
                                    <li v-for="(item, index) in permissions" v-bind:key="index"  class="list-group-item">
                                        <span v-if="item.role === 1">Sahip</span>
                                        <span v-if="item.role === 2">Paylaşılan</span>
                                        {{item.username}}
                                    </li>
                                </ul>
                            </div>
                            <div class="modal-footer">
                                <button type="button" class="btn btn-secondary" @click="showModal = false">Kapat</button>
                                <button type="submit" class="btn btn-primary">Kullanıcı Ekle</button>
                            </div>
                        </form>
                    </div>
                </div>

                </div>
            </div>
            </transition>
        </div>

        <button class="btn btn-primary" @click="showModal = true">Güncelle</button>
    </div>
</template>

<script>
export default {
    data() {
        return {
            showModal: false,
            user_id: this.$store.state.user.id,
            username: ''
        }
    },
    methods: {
        updateList() {
            this.$store.dispatch("updateListTitle", {title:this.title, id:this.listid})
            this.showModal = false
        },
        addUser() {
            console.log(this.username)
            this.$store.dispatch("addListPermission", {list_id:this.listid, username:this.username})
        }
    },
    props: ["title", "listid"],
    computed: {
        permissions() {
            return this.$store.getters.gettingListPermissions
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
