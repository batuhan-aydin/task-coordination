import Vue from 'vue'
import Vuex from 'vuex'
import { longStackSupport } from 'q';
import axios from 'axios'
import router from './router'

Vue.use(Vuex)

export default new Vuex.Store({
  state: {
    token: "",
    tasks: [],
    lists: [],
    user_id: null,
    list_id: null,
    isActive: false,
    username: "",
    user: null,
    perms: [],
  },
  mutations: {
    setToken(state, token, ) {
      state.token = token
    },
    setUser(state, user) {
      state.user = user
    },
    clearToken(state, token, user_id){
      state.token = ""
      state.user_id = ""
    },
    setUserLists(state, lists) {
      state.lists = lists
    },
    clearUserLists(state){
      state.lists = []
    },
    setListTasks(state, tasks) {
      state.tasks = tasks
    },
    setListId(state, list_id){
      state.list_id = list_id
    },
    toggleSidebar(state){
      state.isActive = !state.isActive
    },
    setListPermissions(state, perms) {
      state.perms = perms
    }
  },
  actions: {

    initAuth({commit, dispatch}) {
      let token = localStorage.getItem("token")
      if (token) {
        commit("setToken", token)
        router.push("/")
      } else {
        router.push("/login")
        return false
      }
    },

    login({commit, dispatch, state}, authData) {
      return axios.post("http://127.0.0.1:5000/login", {
        username: authData.email,
        password: authData.password
      }).then(response => {
          commit('setUser', response.data.user)
          commit('setToken', response.data.access_token)
          localStorage.setItem("token", response.data.access_token)
          dispatch("getUserList")
      })

    },
    register({commit, dispatch, state}, authData){
      return axios.post("http://127.0.0.1:5000/register", {
        username: authData.email,
        password: authData.password
      }).then(response => {
          console.log(response)
      })
    },
    logout({commit, dispatch, state}) {
      commit("clearToken")
      commit("clearUserLists")
      localStorage.removeItem("token")
      localStorage.removeItem("user_id")
      localStorage.removeItem("username")
    },
    createTask({commit, dispatch}, taskData) {
      axios.post("http://127.0.0.1:5000/tasks", {
        body: taskData.body,
        list_id: taskData.list_id
      }).then(response => {
        dispatch("getTasksByList", {list_id:this.state.list_id})
      }).catch(err => {
        console.log(err)
      })
    },
    createList({commit, dispatch}, listData) {
      axios.post("http://127.0.0.1:5000/lists", {
        title: listData.title,
        user_id: listData.user_id
      }).then(response => {
        dispatch("getUserList")
      }).catch(err => {
        console.log(err)
      })
    },
    getUserList({commit, dispatch}, data) {
      axios.get("http://127.0.0.1:5000/lists/" + this.state.user.id)
      .then(response => {
        commit("setUserLists", response.data)
      }).catch(err => {
        console.log(err)
      })
    },
    getTasksByList({commit, dispatch}, listData) {
      axios.get("http://127.0.0.1:5000/tasks/" + listData.list_id)
      .then(response => {
        commit("setListTasks", response.data.tasks)
        commit("setListId", listData.list_id)
      }).catch(err => {
        console.log(err)
      })
    },
    changeIsActive({commit, dispatch}) {
      commit("toggleSidebar")
    },
    changeFinishStatusTask({commit, dispatch}, taskData) {
      axios.put("http://127.0.0.1:5000/task/" + taskData.id, {
        body: taskData.body,
        is_finished: !taskData.is_finished
      }).then(response => {
        dispatch("getTasksByList", {list_id:taskData.list_id})
        console.log(taskData.list_id)
      }).catch(err => {
        console.log(err)
      })
    },
    updateListTitle({commit, dispatch}, listData) {
      axios.put("http://127.0.0.1:5000/list/" + listData.id, {
        title: listData.title
      }).then(response => {
        dispatch("getUserList")
      }).catch(err => {
        console.log(err)
      })
    },
    getListPermissions({commit, dispatch}, listData) {
      axios.get("http://127.0.0.1:5000/permissions/" + listData.list_id)
      .then(response => {
        commit("setListPermissions", response.data.result)
      }).catch(err => {
        console.log(err)
      })
    },
    addListPermission({commit, dispatch}, data) {
      axios.post("http://127.0.0.1:5000/permissions/" + data.list_id, {
        username: data.username,
      }).then(response => {
        dispatch("getUserList")
      }).catch(err => {
        console.log(err)
      })
    },
  },
  getters: {
    isAuthenticated(state){
      return state.token !== ""
    },
    userList(state){
      return state.lists
    },
    unfinishedTasks(state){
      return state.tasks.filter(function(task) {
        return !task.is_finished
      })
    },
    getListId(state){
      return state.list_id
    },
    isActive(state){
      return state.isActive
    },
    finishedTasks(state)
    {
      return state.tasks.filter(function(task) {
        return task.is_finished
      })
    },
    getUsername(state){
      return state.user.username
    },
    gettingListPermissions(state) {
      return state.perms
    }
  }
})
