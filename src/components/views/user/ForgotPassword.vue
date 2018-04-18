<template>
<form class="container login-form" @submit.prevent="submit">
  <b-notification v-if="formError" type="is-danger" has-icon>
    {{ formError }}
  </b-notification>
  <h1 class="is-size-1 mb-25 mt-25">Reset Password</h1>

  <b-field label="Username">
    <b-input
      type="name"
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

  <div>
    <button class="button is-primary mt-20" :class="{ 'is-loading': buttonLoading }">Reset Password</button>
  </div>
</form>
</template>

<script>
  import { forgotPassword } from '../../../api/user';

  export default {
    data() {
      return {
        username: '',
        recoveryEmail: '',
        buttonLoading: false,
        confirmPasswordError: false,
        confirmPasswordMessage: null,
        formError: null,
      };
    },
    methods: {
      submit() {
        this.buttonLoading = true;
        this.formError = null;

        const vm = this;

        forgotPassword(this.username, this.recoveryEmail)
          .then((response) => {
            if (!response.ok) {
              response.json().then((data) => {
                vm.formError = data.message;
              });
              return;
            }

            this.$router.push('/user/changePassword');
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
