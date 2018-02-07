import Vue from 'vue';
import Buefy from 'buefy';
import 'mdi/css/materialdesignicons.min.css';
import App from './App';
import router from './router';
import store from './store';

import { profile } from './api/user';

Vue.config.productionTip = false;

Vue.use(Buefy);

if (localStorage.getItem('loggedIn') === 'true') {
  profile()
    .then((response) => {
      if (response.ok) {
        response.json().then((data) => {
          store.dispatch('login', data.email);
        });
      }
    });
}

/* eslint-disable no-new */
new Vue({
  el: '#app',
  router,
  store,
  render: h => h(App),
});
