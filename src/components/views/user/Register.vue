<template>
  <div>
    <form class="container login-form" @submit.prevent="submit">
      <b-notification v-if="formError" type="is-danger" has-icon>
        {{ formError }}
      </b-notification>
      <h1 class="is-size-1 mb-25 mt-25">Register</h1>
      <b-field label="Username">
        <b-input
          type="text"
          placeholder="Username"
          required
          v-model="username">
        </b-input>
      </b-field>

      <b-field label="Recovery Email">
        <b-input
          type="email"
          placeholder="Recovery Email"
          required
          v-model="recoveryEmail">
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

      <b-field
        label="Confirm Password"
        :type="confirmPasswordError ? 'is-danger' : ''"
        :message="confirmPasswordMessage">
        <b-input
          type="password"
          password-reveal
          placeholder="Confirm Password"
          required
          v-model="confirmPassword">
        </b-input>
      </b-field>

      <div>
        <button class="button is-primary mt-20" :class="{ 'is-loading': buttonLoading }">Register</button>
      </div>
      <div class="mt-20">
        <router-link to="/user/login">Already have an account? Login!</router-link>
      </div>
    </form>
  </div>
</template>

<script>
  import { mapActions } from 'vuex';

  import { register } from '../../../api/user';

  export default {
    data() {
      return {
        username: '',
        recoveryEmail: '',
        password: '',
        confirmPassword: '',
        buttonLoading: false,
        confirmPasswordError: false,
        confirmPasswordMessage: null,
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

        register(this.username, this.recoveryEmail, this.password)
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
      setConfirmPasswordError(error) {
        if (error) {
          this.confirmPasswordError = true;
          this.confirmPasswordMessage = 'Your passwords do not match!';
          return;
        }

        this.confirmPasswordError = false;
        this.confirmPasswordMessage = '';
      },
    },
    watch: {
      password() {
        if (this.confirmPassword === '') {
          return;
        }

        this.setConfirmPasswordError(this.confirmPassword !== this.password);
      },
      confirmPassword() {
        this.setConfirmPasswordError(this.confirmPassword !== this.password);
      },
    },
  };
</script>

<style lang="scss" scoped>
  .login-form {
    max-width: 400px;
  }
</style>

