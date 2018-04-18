import Vue from 'vue';
import Vuex from 'vuex';

import router from '../router';
import { logout } from '../api/user';

Vue.use(Vuex);

const debug = process.env.NODE_ENV !== 'production';

export default new Vuex.Store({
  strict: debug,
  state: {
    user: null,
  },
  mutations: {
    setUser(state, user) {
      state.user = user;
    },
  },
  actions: {
    login({ commit }, username) {
      commit('setUser', username);
      localStorage.setItem('loggedIn', 'true');
    },
    logout({ commit }) {
      commit('setUser', null);
      localStorage.setItem('loggedIn', 'false');
      router.push('/');
      logout();
    },
  },
});
