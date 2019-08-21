<template>
    <div>
             <!-- Sidebar -->
        <div id="sidebar-wrapper">
            <ul class="sidebar-nav">
                <li class="sidebar-brand">
                    <a href="#">
                        {{username}}
                    </a>
                </li>
                <li v-bind:class="{}" v-for="item in lists" v-bind:key="item.id">
                    <div class="btn-group">
                        <a href="#" v-on:click="showTasks(item.id)">{{item.title}}</a>
                        <a v-on:click="getPerms(item.id)" style="margin-left:10px;"><ListUpdate v-bind:title="item.title" v-bind:listid="item.id" /></a>
                    </div>
                </li>
                <li>
                    <a href="#"><ListCreate /></a>
                </li>
            </ul>            
        </div>
    </div>
</template>

<script>
import ListCreate from '@/components/ListCreate.vue'
import ListUpdate from '@/components/ListUpdate.vue'
export default {
    components: {
        ListCreate,
        ListUpdate
    },
    data() {
        return { 
        showModal: false,
        }
    },
    methods: {
        openModal: function () {
            this.showModal = true
        },
        showTasks: function(list_id) {
            this.$store.dispatch("getTasksByList", {list_id:list_id})
        },
        getPerms: function(list_id) {
            this.$store.dispatch("getListPermissions", {list_id:list_id})
            console.log(list_id)
        }
    },
    computed: {
        lists(){
            return this.$store.getters.userList
        },
        username() {
            return this.$store.getters.getUsername
        },
    }
}
</script>


<style>
#wrapper {
    padding-left: 0;
    -webkit-transition: all 0.5s ease;
    -moz-transition: all 0.5s ease;
    -o-transition: all 0.5s ease;
    transition: all 0.5s ease;
}

#wrapper.toggled {
    padding-left: 250px;
}

#sidebar-wrapper {
    z-index: 1000;
    position: fixed;
    left: 250px;
    width: 0;
    height: 100%;
    margin-left: -250px;
    overflow-y: auto;
    background: white;
    -webkit-transition: all 0.5s ease;
    -moz-transition: all 0.5s ease;
    -o-transition: all 0.5s ease;
    transition: all 0.5s ease;
}

#wrapper.toggled #sidebar-wrapper {
    width: 250px;
}

#page-content-wrapper {
    width: 100%;
    position: absolute;
    padding: 15px;
}

#wrapper.toggled #page-content-wrapper {
    position: absolute;
    margin-right: -250px;
}

/* Sidebar Styles */

.sidebar-nav {
    position: absolute;
    top: 0;
    width: 250px;
    margin: 0;
    padding: 0;
    list-style: none;
}

.sidebar-nav li {
    text-indent: 20px;
    line-height: 40px;
}

.sidebar-nav li a {
    display: block;
    text-decoration: none;
    color: black;
}

.sidebar-nav li a:hover {
    text-decoration: none;
    color:black;
    background: gray;
}

.sidebar-nav li a:active,
.sidebar-nav li a:focus {
    text-decoration: none;
}

.sidebar-nav > .sidebar-brand {
    height: 65px;
    font-size: 18px;
    line-height: 60px;
}

.sidebar-nav > .sidebar-brand a {
    color: #999999;
}

.sidebar-nav > .sidebar-brand a:hover {
    color: #fff;
    background: none;
}

@media(min-width:768px) {
    #wrapper {
        padding-left: 250px;
    }

    #wrapper.toggled {
        padding-left: 0;
    }

    #sidebar-wrapper {
        width: 250px;
    }

    #wrapper.toggled #sidebar-wrapper {
        width: 0;
    }

    #page-content-wrapper {
        padding: 20px;
        position: relative;
    }

    #wrapper.toggled #page-content-wrapper {
        position: relative;
        margin-right: 0;
    }
}


</style>

