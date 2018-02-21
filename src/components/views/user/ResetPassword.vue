<template>
<form class="container login-form" @submit.prevent="submit">
  <b-notification v-if="formError" type="is-danger" has-icon>
    {{ formError }}
  </b-notification>
  <h1 class="is-size-1 mb-25 mt-25">Reset Password</h1>

  <b-field label="Current Password">
    <b-input
      type="password"
      password-reveal
      placeholder="Current Password"
      required
      v-model="oldPassword">
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
  import { resetPassword } from '../../../api/user';

  export default {
    data() {
      return {
        oldPassword: '',
        newPassword: '',
        confirmNewPassword: '',
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

        resetPassword(this.oldPassword, this.newPassword)
          .then((response) => {
            if (!response.ok) {
              response.json().then((data) => {
                vm.formError = data.message;
              });
              return;
            }

            this.$router.push('/user/profile');
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
