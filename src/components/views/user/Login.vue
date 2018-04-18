<template>
  <div>
    <form class="container login-form" @submit.prevent="submit">
      <b-notification v-if="formError" type="is-danger" has-icon>
        {{ formError }}
      </b-notification>
      <h1 class="is-size-1 mb-25 mt-25">Login</h1>
      <b-field label="Username">
        <b-input
          type="name"
          placeholder="Username"
          required
          v-model="username">
        </b-input>
      </b-field>

      <b-field label="Password">
        <b-input
          type="password"
          password-reveal
          placeholder="Password"
          required
          v-model="password">
        </b-input>
      </b-field>

      <b-checkbox v-model="remember">Remember me</b-checkbox>
      <div>
        <button class="button is-primary mt-20" :class="{ 'is-loading': buttonLoading }">Login</button>
      </div>
      <div class="mt-20">
        <router-link to="/user/register">Don't have an account? Sign up!</router-link>
      </div>
    </form>
  </div>
</template>

<script>
  import { mapActions } from 'vuex';

  import { login } from '../../../api/user';

  export default {
    data() {
      return {
        username: '',
        password: '',
        remember: false,
        buttonLoading: false,
        formError: null,
      };
    },
    methods: {
      ...mapActions([
        'login',
      ]),
      submit() {
        this.buttonLoading = true;
        this.formError = null;

        const vm = this;

        login(this.username, this.password, this.remember)
          .then((response) => {
            response.json().then((data) => {
              if (!response.ok) {
                vm.formError = data.message;
                return;
              }

              this.login(data);
              this.$router.push('/user/profile');
            });
          })
          .catch(() => {
            this.formError = 'An unknown error occured. Please try again.';
          })
          .finally(() => {
            this.buttonLoading = false;
          });
      },
    },
  };
</script>

<style lang="scss" scoped>
  .login-form {
    max-width: 400px;
  }
</style>

