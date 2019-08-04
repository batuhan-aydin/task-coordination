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
    isActive: false
  },
  mutations: {
    setToken(state, token, user_id) {
      state.token = token
      state.user_id = user_id
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
          console.log(response)
          commit('setToken', response.data.access_token, response.data.user_id)
          localStorage.setItem("token", response.data.access_token)
          localStorage.setItem("user_id", response.data.user_id)
      })

    },
    register({commit, dispatch, state}, authData){
      return axios.post("http://127.0.0.1:5000/register", {
        username: authData.email,
        password: authData.password
      }).then(response => {
          console.log(response)
          dispatch("createList", {title:'Gelen Kutusu'})
      })
    },
    logout({commit, dispatch, state}) {
      commit("clearToken")
      commit("clearUserLists")
      localStorage.removeItem("token")
      localStorage.removeItem("user_id")
    },
    createTask({commit, dispatch}, taskData) {
      axios.post("http://127.0.0.1:5000/tasks", {
        body: taskData.body,
        list_id: taskData.list_id
      }).then(response => {
        console.log(response)
        dispatch("getTasksByList", {list_id:this.state.list_id})
      }).catch(err => {
        console.log(err)
      })
    },
    createList({commit, dispatch}, listData) {
      axios.post("http://127.0.0.1:5000/lists", {
        title: listData.title,
        user_id: localStorage.getItem("user_id")
      }).then(response => {
        console.log(response)
        dispatch("getUserList")
      }).catch(err => {
        console.log(err)
      })
    },
    getUserList({commit, dispatch}) {
      axios.get("http://127.0.0.1:5000/lists/" + localStorage.getItem("user_id"))
      .then(response => {
        console.log(response)
        commit("setUserLists", response.data.lists)
        console.log(this.state.lists)
      }).catch(err => {
        console.log(err)
      })
    },
    getTasksByList({commit, dispatch}, listData) {
      axios.get("http://127.0.0.1:5000/tasks/" + listData.list_id)
      .then(response => {
        commit("setListTasks", response.data.tasks)
        commit("setListId", listData.list_id)
        console.log(response)
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
    }
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
    }
  }
})
