<template>
<form class="container login-form" @submit.prevent="submit">
  <b-notification v-if="formError" type="is-danger" has-icon>
    {{ formError }}
  </b-notification>
  <h1 class="is-size-1 mb-25 mt-25">Reset Password</h1>

  <b-field label="Username">
    <b-input
      type="name"
      password-reveal
      placeholder="Username"
      required
      v-model="username">
    </b-input>
  </b-field>

  <b-field label="Password Reset PIN">
    <b-input
      type="password"
      password-reveal
      placeholder="Password Reset PIN"
      required
      v-model="resetPIN">
    </b-input>
  </b-field>

  <b-field label="New Password">
    <b-input
      type="password"
      password-reveal
      placeholder="New Password"
      required
      v-model="newPassword">
    </b-input>
  </b-field>

  <b-field label="Confirm New Password">
    <b-input
      type="password"
      password-reveal
      placeholder="Confirm New Password"
      required
      v-model="confirmNewPassword">
    </b-input>
  </b-field>

  <div>
    <button class="button is-primary mt-20" :class="{ 'is-loading': buttonLoading }">Reset Password</button>
  </div>
</form>
</template>

<script>
  import { changePassword } from '../../../api/user';

  export default {
    data() {
      return {
        username: '',
        resetPIN: '',
        newPassword: '',
        confirmNewPassword: '',
        buttonLoading: false,
        confirmPasswordError: false,
        confirmPasswordMessage: null,
        formError: null,
      };
    },
    mounted() {
      if (this.$route.params.pin) {
        this.resetPIN = this.$route.params.pin;
      }
    },
    methods: {
      submit() {
        this.buttonLoading = true;
        this.formError = null;

        const vm = this;

        changePassword(this.username, this.resetPIN, this.newPassword)
          .then((response) => {
            if (!response.ok) {
              response.json().then((data) => {
                vm.formError = data.message;
              });
              return;
            }

            this.$router.push('/');
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
