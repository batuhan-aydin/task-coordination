<template>
    <div id="register" class="container">
        <div class="row justify-content-center">
            <div class="col-6">
                <form @submit.prevent="onSubmit" id="register-form">
                    <div class="form-group">
                        <label for="Email">Email address</label>
                        <input v-model="user.email" type="email" class="form-control" aria-describedby="emailHelp" placeholder="Enter email">
                    </div>
                    <div class="form-group">
                        <label for="Password">Password</label>
                        <input v-model="user.password" type="password" class="form-control" placeholder="Password">
                    </div>
                    <button type="submit" class="btn btn-primary">Kayıt ol</button>
                    <router-link to="/login"> Üyeliğim var</router-link>
                </form>
            </div>
        </div>
    </div>
</template>

<script>
import axios from 'axios'
export default {
    data() {
        return {
            user: {
                email: null,
                password: null
            }
        }
    },
    methods: {
        onSubmit(){
            this.$store.dispatch('register', {...this.user})
            .then(response => {
                this.$router.push("/")
            })
        }
    }
}
</script>

<style>
#register {
    margin-top: 10%;
    border: 3px solid blue;
    width: 40%;
    padding-top: 3%;
    padding-bottom: 3%;
}

</style>


