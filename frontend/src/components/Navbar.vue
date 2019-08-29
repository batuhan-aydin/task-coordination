<template>
    <div>
        <nav class="navbar navbar-expand-lg navbar-dark bg-primary">
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                
                <ul class="navbar-nav mr-auto">
                    <li class="nav-item">
                        <a class="nav-link" href="#" v-on:click="toggle"><i class="fas fa-bars"></i></a>
                    </li> 
                    <li class="nav-item" style="margin-left:55%;">
                        <form class="form-inline my-2 my-lg-0" @submit.prevent="searchTask">
                            <input class="form-control mr-sm-2" type="search" placeholder="Search" aria-label="Search" style="width:400px;" v-model="searchText">
                        </form>
                    </li>  
                </ul>
            </div>
            <div class="collapse navbar-collapse" id="navbarSupportedContent">
                <ul class="navbar-nav ml-auto">
                <li class="nav-item" v-if="show">
                    <router-link to="/register" class="nav-link">Register</router-link>
                </li>
                <li class="nav-item" v-if="show">
                    <router-link to="/login" class="nav-link">Login</router-link>
                </li>
                <li class="nav-item" v-else>
                    <a href="#" @click.prevent="logout" class="nav-link" >Logout</a>
                </li>
                </ul>
            </div>
        </nav>
    </div>
</template>

<script>
    export default {
        data() {
            return {
                show: !this.$store.getters.isAuthenticated,
                showOr: this.$store.getters.isAuthenticated,
                searchText: ''
            }
        },
        methods: {
            logout() {
                this.$store.dispatch("logout")
                this.$router.replace('/login')
            },
            toggle() {
                this.$store.dispatch("changeIsActive")
            },
            searchTask() {
                console.log(this.searchTask)
            }
        }
    }
</script>
